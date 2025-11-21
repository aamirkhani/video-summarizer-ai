#!/usr/bin/env python3
"""
AI Video Summarizer
Extracts key segments from videos using speech analysis and LLM summarization
"""

import os
import json
import requests
import whisper_timestamped as whisper
from moviepy.editor import VideoFileClip, concatenate_videoclips
from openai import OpenAI
from dotenv import load_dotenv
import tempfile
from typing import List, Dict, Tuple

# Load environment variables
load_dotenv()

class VideoSummarizer:
    def __init__(self, openai_api_key: str = None):
        """Initialize the video summarizer with OpenAI API key"""
        self.openai_api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
        if not self.openai_api_key:
            print("Warning: No OpenAI API key provided. Using mock LLM responses.")
            self.client = None
        else:
            try:
                self.client = OpenAI(api_key=self.openai_api_key)
            except Exception as e:
                print(f"Warning: Failed to initialize OpenAI client: {e}")
                print("Using mock LLM responses.")
                self.client = None
        
        # Load Whisper model
        print("Loading Whisper model...")
        self.whisper_model = whisper.load_model("base")
        print("Whisper model loaded successfully!")
    
    def extract_audio_with_timestamps(self, video_path: str) -> Dict:
        """Extract audio and generate word-level timestamps using Whisper"""
        print(f"Extracting audio and generating timestamps from {video_path}...")
        
        # Use whisper-timestamped to get word-level timestamps
        result = whisper.transcribe(self.whisper_model, video_path, language="en")
        
        # Format the result for our use
        formatted_transcript = []
        for segment in result['segments']:
            for word_info in segment.get('words', []):
                formatted_transcript.append({
                    'word': word_info['text'].strip(),
                    'start': word_info['start'],
                    'end': word_info['end'],
                    'confidence': word_info.get('confidence', 1.0)
                })
        
        return {
            'full_text': result['text'],
            'transcript': formatted_transcript,
            'segments': result['segments']
        }
    
    def analyze_with_llm(self, transcript_data: Dict) -> List[Dict]:
        """Use LLM to identify important segments for summarization"""
        full_text = transcript_data['full_text']
        segments = transcript_data['segments']
        
        # Create a prompt for the LLM
        prompt = f"""
        Analyze this video transcript and identify the most important segments for creating a summary video.
        
        Full transcript: {full_text}
        
        Segment information with timestamps:
        {json.dumps([{'text': seg['text'], 'start': seg['start'], 'end': seg['end']} for seg in segments], indent=2)}
        
        Please identify 3-5 key segments that would make a good summary video. For each segment, provide:
        1. start_time: exact start time in seconds
        2. end_time: exact end time in seconds  
        3. importance: score from 1-10
        4. topic: brief description of what this segment covers
        5. reason: why this segment is important
        
        Respond in JSON format like this:
        {{
            "summary_segments": [
                {{
                    "start_time": 0.0,
                    "end_time": 15.5,
                    "importance": 9,
                    "topic": "introduction",
                    "reason": "Sets up the main topic"
                }}
            ]
        }}
        """
        
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert video editor who identifies the most important segments for creating summary videos."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                
                # Parse the JSON response
                response_text = response.choices[0].message.content
                # Extract JSON from the response (in case there's extra text)
                start_idx = response_text.find('{')
                end_idx = response_text.rfind('}') + 1
                json_str = response_text[start_idx:end_idx]
                
                return json.loads(json_str)['summary_segments']
            
            except Exception as e:
                print(f"Error calling OpenAI API: {e}")
                print("Falling back to mock response...")
        
        # Mock response if no API key or API fails
        return self._generate_mock_summary(segments)
    
    def _generate_mock_summary(self, segments: List[Dict]) -> List[Dict]:
        """Generate a mock summary when LLM is not available"""
        print("Using mock LLM analysis...")
        
        # Simple heuristic: take first segment, middle segment, and last segment
        summary_segments = []
        
        if len(segments) >= 1:
            summary_segments.append({
                "start_time": segments[0]['start'],
                "end_time": min(segments[0]['end'], segments[0]['start'] + 10),
                "importance": 9,
                "topic": "introduction",
                "reason": "Opening segment"
            })
        
        if len(segments) >= 3:
            mid_idx = len(segments) // 2
            summary_segments.append({
                "start_time": segments[mid_idx]['start'],
                "end_time": min(segments[mid_idx]['end'], segments[mid_idx]['start'] + 10),
                "importance": 8,
                "topic": "main_content",
                "reason": "Middle segment with key content"
            })
        
        if len(segments) >= 2:
            summary_segments.append({
                "start_time": max(0, segments[-1]['end'] - 10),
                "end_time": segments[-1]['end'],
                "importance": 7,
                "topic": "conclusion",
                "reason": "Closing segment"
            })
        
        return summary_segments
    
    def create_summary_video(self, video_path: str, summary_segments: List[Dict], output_path: str):
        """Create a summary video by extracting and concatenating segments"""
        print(f"Creating summary video from {len(summary_segments)} segments...")
        
        # Load the original video
        video = VideoFileClip(video_path)
        
        # Extract clips for each summary segment
        clips = []
        for i, segment in enumerate(summary_segments):
            start_time = segment['start_time']
            end_time = segment['end_time']
            
            print(f"Extracting segment {i+1}: {start_time:.1f}s - {end_time:.1f}s ({segment['topic']})")
            
            # Extract the clip
            clip = video.subclip(start_time, end_time)
            clips.append(clip)
        
        # Concatenate all clips
        print("Concatenating clips...")
        final_video = concatenate_videoclips(clips, method="compose")
        
        # Write the final video
        print(f"Writing summary video to {output_path}...")
        final_video.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        # Clean up
        video.close()
        final_video.close()
        for clip in clips:
            clip.close()
        
        print(f"Summary video created successfully: {output_path}")
    
    def process_video(self, input_path: str, output_path: str) -> Dict:
        """Complete pipeline: analyze video and create summary"""
        print(f"Processing video: {input_path}")
        
        # Step 1: Extract audio and timestamps
        transcript_data = self.extract_audio_with_timestamps(input_path)
        
        # Step 2: Analyze with LLM
        summary_segments = self.analyze_with_llm(transcript_data)
        
        # Step 3: Create summary video
        self.create_summary_video(input_path, summary_segments, output_path)
        
        return {
            'input_video': input_path,
            'output_video': output_path,
            'transcript': transcript_data,
            'summary_segments': summary_segments
        }

def download_test_video(url: str, filename: str) -> str:
    """Download a test video from URL"""
    print(f"Downloading test video: {filename}")
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print(f"Downloaded: {filename}")
    return filename

def main():
    """Main function to run the video summarizer"""
    print("=== AI Video Summarizer ===")
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    # Check if test video exists, if not try to download
    test_video_path = "test_video.mp4"
    
    if not os.path.exists(test_video_path):
        # Try to download test video
        test_video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        
        try:
            download_test_video(test_video_url, test_video_path)
        except Exception as e:
            print(f"Failed to download test video: {e}")
            print("Please provide your own video file as 'test_video.mp4'")
            return
    else:
        print(f"Using existing test video: {test_video_path}")
    
    # Initialize the summarizer
    summarizer = VideoSummarizer()
    
    # Process the video
    output_path = "output/summary_video.mp4"
    
    try:
        result = summarizer.process_video(test_video_path, output_path)
        
        print("\n=== Processing Complete ===")
        print(f"Original video: {result['input_video']}")
        print(f"Summary video: {result['output_video']}")
        print(f"Number of segments in summary: {len(result['summary_segments'])}")
        
        # Print segment details
        print("\nSummary segments:")
        for i, segment in enumerate(result['summary_segments']):
            print(f"  {i+1}. {segment['start_time']:.1f}s - {segment['end_time']:.1f}s: {segment['topic']} (importance: {segment['importance']})")
        
        return result
        
    except Exception as e:
        print(f"Error processing video: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
