#!/usr/bin/env python3
"""
Sample Video Downloader and Processor
Downloads 20 sample videos and generates summaries using our AI summarizer
"""

import os
import requests
import json
from datetime import datetime
from video_summarizer_simple import VideoSummarizer
import time

# Create directories
os.makedirs("samples", exist_ok=True)
os.makedirs("samples/originals", exist_ok=True)
os.makedirs("samples/summaries", exist_ok=True)

# Sample video sources with metadata
SAMPLE_VIDEOS = [
    # Business & Professional
    {
        "id": "business_meeting_01",
        "title": "Team Strategy Meeting",
        "category": "Business",
        "description": "Corporate team discussing quarterly goals and strategies",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
        "expected_duration": "596s",
        "tags": ["meeting", "strategy", "business"]
    },
    {
        "id": "training_session_01",
        "title": "Employee Training Session",
        "category": "Business",
        "description": "HR training on workplace safety and procedures",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
        "expected_duration": "654s",
        "tags": ["training", "hr", "safety"]
    },
    {
        "id": "product_demo_01",
        "title": "Software Product Demo",
        "category": "Business",
        "description": "Live demonstration of new software features",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
        "expected_duration": "15s",
        "tags": ["demo", "software", "features"]
    },
    {
        "id": "webinar_01",
        "title": "Marketing Webinar",
        "category": "Business",
        "description": "Digital marketing strategies for 2024",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
        "expected_duration": "15s",
        "tags": ["webinar", "marketing", "digital"]
    },
    {
        "id": "standup_meeting_01",
        "title": "Daily Standup Meeting",
        "category": "Business",
        "description": "Agile team daily standup and progress updates",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
        "expected_duration": "60s",
        "tags": ["standup", "agile", "team"]
    },
    
    # Educational Content
    {
        "id": "university_lecture_01",
        "title": "Computer Science Lecture",
        "category": "Education",
        "description": "Introduction to machine learning algorithms",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4",
        "expected_duration": "15s",
        "tags": ["lecture", "computer-science", "ml"]
    },
    {
        "id": "tutorial_01",
        "title": "Python Programming Tutorial",
        "category": "Education",
        "description": "Step-by-step Python programming for beginners",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4",
        "expected_duration": "15s",
        "tags": ["tutorial", "python", "programming"]
    },
    {
        "id": "documentary_01",
        "title": "Climate Change Documentary",
        "category": "Education",
        "description": "Scientific analysis of global climate patterns",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
        "expected_duration": "888s",
        "tags": ["documentary", "climate", "science"]
    },
    {
        "id": "language_lesson_01",
        "title": "Spanish Language Lesson",
        "category": "Education",
        "description": "Basic Spanish conversation and grammar",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4",
        "expected_duration": "30s",
        "tags": ["language", "spanish", "lesson"]
    },
    {
        "id": "science_experiment_01",
        "title": "Chemistry Lab Experiment",
        "category": "Education",
        "description": "Acid-base reaction demonstration and analysis",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
        "expected_duration": "734s",
        "tags": ["science", "chemistry", "experiment"]
    },
    
    # Entertainment & Media
    {
        "id": "podcast_01",
        "title": "Tech Podcast Episode",
        "category": "Entertainment",
        "description": "Discussion about latest technology trends",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/VolkswagenGTIReview.mp4",
        "expected_duration": "20s",
        "tags": ["podcast", "technology", "trends"]
    },
    {
        "id": "interview_01",
        "title": "CEO Interview",
        "category": "Entertainment",
        "description": "Startup CEO discusses company vision and growth",
        "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4",
        "expected_duration": "57s",
        "tags": ["interview", "ceo", "startup"]
    },
    {
        "id": "cooking_show_01",
        "title": "Italian Cooking Show",
        "category": "Entertainment",
        "description": "Traditional pasta making techniques",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_360x240_1mb.mp4",
        "expected_duration": "30s",
        "tags": ["cooking", "italian", "pasta"]
    },
    {
        "id": "travel_vlog_01",
        "title": "Tokyo Travel Vlog",
        "category": "Entertainment",
        "description": "Exploring Tokyo's hidden gems and local culture",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_640x360_1mb.mp4",
        "expected_duration": "30s",
        "tags": ["travel", "tokyo", "culture"]
    },
    {
        "id": "gaming_stream_01",
        "title": "Gaming Live Stream",
        "category": "Entertainment",
        "description": "Professional esports gameplay and commentary",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_720x480_1mb.mp4",
        "expected_duration": "30s",
        "tags": ["gaming", "esports", "stream"]
    },
    
    # News & Information
    {
        "id": "news_broadcast_01",
        "title": "Evening News Broadcast",
        "category": "News",
        "description": "Daily news covering politics, economy, and weather",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4",
        "expected_duration": "30s",
        "tags": ["news", "politics", "economy"]
    },
    {
        "id": "tech_review_01",
        "title": "Smartphone Review",
        "category": "News",
        "description": "Comprehensive review of latest smartphone features",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1920x1080_1mb.mp4",
        "expected_duration": "30s",
        "tags": ["review", "smartphone", "technology"]
    },
    {
        "id": "panel_discussion_01",
        "title": "Economic Panel Discussion",
        "category": "News",
        "description": "Experts discuss current economic trends and forecasts",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_2mb.mp4",
        "expected_duration": "60s",
        "tags": ["panel", "economics", "discussion"]
    },
    {
        "id": "weather_report_01",
        "title": "Weather Forecast",
        "category": "News",
        "description": "Weekly weather forecast with detailed analysis",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_640x360_2mb.mp4",
        "expected_duration": "60s",
        "tags": ["weather", "forecast", "meteorology"]
    },
    {
        "id": "financial_analysis_01",
        "title": "Stock Market Analysis",
        "category": "News",
        "description": "Daily stock market trends and investment insights",
        "url": "https://sample-videos.com/zip/10/mp4/SampleVideo_1920x1080_2mb.mp4",
        "expected_duration": "60s",
        "tags": ["finance", "stocks", "investment"]
    }
]

def download_video(video_info, max_retries=3):
    """Download a video with retry logic"""
    video_id = video_info['id']
    url = video_info['url']
    filename = f"samples/originals/{video_id}.mp4"
    
    if os.path.exists(filename):
        print(f"✅ {video_id} already exists, skipping download")
        return filename
    
    print(f"📥 Downloading {video_info['title']} ({video_id})...")
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            file_size = os.path.getsize(filename)
            print(f"✅ Downloaded {video_id}: {file_size / (1024*1024):.2f} MB")
            return filename
            
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed for {video_id}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                print(f"❌ Failed to download {video_id} after {max_retries} attempts")
                return None

def process_video_sample(video_info, input_path):
    """Process a video and generate summary"""
    video_id = video_info['id']
    output_path = f"samples/summaries/{video_id}_summary.mp4"
    
    if os.path.exists(output_path):
        print(f"✅ Summary for {video_id} already exists, skipping processing")
        return output_path
    
    print(f"🤖 Processing {video_info['title']} with AI...")
    
    try:
        # Initialize summarizer
        summarizer = VideoSummarizer()
        
        # Process video
        result = summarizer.process_video(input_path, output_path)
        
        # Save metadata
        metadata = {
            **video_info,
            'processing_result': result,
            'processed_at': datetime.now().isoformat(),
            'original_file': input_path,
            'summary_file': output_path
        }
        
        metadata_path = f"samples/summaries/{video_id}_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2, default=str)
        
        print(f"✅ Processed {video_id} successfully")
        return output_path
        
    except Exception as e:
        print(f"❌ Failed to process {video_id}: {e}")
        return None

def generate_sample_index():
    """Generate an index of all processed samples"""
    samples_index = {
        'generated_at': datetime.now().isoformat(),
        'total_samples': len(SAMPLE_VIDEOS),
        'categories': {},
        'samples': []
    }
    
    # Count by category
    for video in SAMPLE_VIDEOS:
        category = video['category']
        if category not in samples_index['categories']:
            samples_index['categories'][category] = 0
        samples_index['categories'][category] += 1
    
    # Process each sample
    for video_info in SAMPLE_VIDEOS:
        video_id = video_info['id']
        metadata_path = f"samples/summaries/{video_id}_metadata.json"
        
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            samples_index['samples'].append(metadata)
        else:
            # Add basic info even if not processed
            samples_index['samples'].append({
                **video_info,
                'status': 'not_processed'
            })
    
    # Save index
    with open('samples/samples_index.json', 'w') as f:
        json.dump(samples_index, f, indent=2, default=str)
    
    print(f"📊 Generated samples index with {len(samples_index['samples'])} entries")
    return samples_index

def main():
    """Main function to download and process all sample videos"""
    print("🎬 VideoSense AI - Sample Video Generator")
    print("=" * 50)
    
    successful_downloads = 0
    successful_processing = 0
    
    # Download and process each video
    for i, video_info in enumerate(SAMPLE_VIDEOS, 1):
        print(f"\n📹 Processing sample {i}/{len(SAMPLE_VIDEOS)}: {video_info['title']}")
        
        # Download video
        input_path = download_video(video_info)
        if input_path:
            successful_downloads += 1
            
            # Process video
            output_path = process_video_sample(video_info, input_path)
            if output_path:
                successful_processing += 1
        
        # Small delay between processing
        time.sleep(1)
    
    # Generate index
    samples_index = generate_sample_index()
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 PROCESSING SUMMARY")
    print("=" * 50)
    print(f"✅ Successfully downloaded: {successful_downloads}/{len(SAMPLE_VIDEOS)} videos")
    print(f"✅ Successfully processed: {successful_processing}/{len(SAMPLE_VIDEOS)} videos")
    print(f"📁 Original videos: samples/originals/")
    print(f"📁 Summary videos: samples/summaries/")
    print(f"📄 Index file: samples/samples_index.json")
    
    # Show category breakdown
    print(f"\n📊 Categories:")
    for category, count in samples_index['categories'].items():
        print(f"   • {category}: {count} videos")
    
    print(f"\n🎉 Sample generation complete!")
    print(f"You can now use these samples in your web application.")

if __name__ == "__main__":
    main()
