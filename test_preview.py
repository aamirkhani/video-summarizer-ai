#!/usr/bin/env python3
"""
Test Video Preview Functionality
Creates a test video processing job and demonstrates the preview feature
"""

import os
import json
import uuid
from datetime import datetime
from video_summarizer_simple import VideoSummarizer

def create_test_preview():
    """Create a test video processing result for preview demonstration"""
    
    # Use an existing sample video
    test_video = "test_video.mp4"
    if not os.path.exists(test_video):
        print("❌ Test video not found. Please ensure test_video.mp4 exists.")
        return None
    
    print("🎬 Creating test preview with existing video...")
    
    # Generate a test job ID
    job_id = str(uuid.uuid4())
    
    # Create output path
    output_path = f"output/test_preview_{job_id[:8]}.mp4"
    
    try:
        # Process the video
        summarizer = VideoSummarizer()
        result = summarizer.process_video(test_video, output_path)
        
        # Create mock completed summary entry
        from app import completed_summaries
        completed_summaries[job_id] = {
            'input_file': os.path.basename(test_video),
            'output_file': os.path.basename(output_path),
            'result': result,
            'completion_time': datetime.now().isoformat(),
            'summary_type': 'auto',
            'target_length': '2_minutes'
        }
        
        print(f"✅ Test preview created successfully!")
        print(f"📹 Job ID: {job_id}")
        print(f"🔗 Preview URL: http://localhost:6010/preview/{job_id}")
        print(f"📁 Original: {result['input_video']}")
        print(f"📁 Summary: {result['output_video']}")
        
        return job_id
        
    except Exception as e:
        print(f"❌ Error creating test preview: {e}")
        return None

def show_preview_features():
    """Display information about preview features"""
    print("\n🎯 Video Preview Features:")
    print("=" * 50)
    print("✅ Side-by-side video comparison")
    print("✅ Synchronized playback controls")
    print("✅ Real-time video streaming")
    print("✅ Download both original and summary")
    print("✅ Interactive segment navigation")
    print("✅ Compression ratio analysis")
    print("✅ Video statistics display")
    print("✅ Responsive design for all devices")
    
    print("\n🎮 Interactive Controls:")
    print("• Play Both - Synchronized playback")
    print("• Pause Both - Stop both videos")
    print("• Reset Both - Return to beginning")
    print("• Seek to Segment - Jump to specific moments")
    print("• Download Options - Get original or summary")
    
    print("\n📊 Analytics Displayed:")
    print("• Original vs Summary duration")
    print("• File size comparison")
    print("• Compression ratio")
    print("• Video resolution")
    print("• Segment importance scores")
    print("• AI reasoning for each segment")

def main():
    """Main function"""
    print("🎬 VideoSense AI - Preview Feature Demo")
    print("=" * 50)
    
    show_preview_features()
    
    # Check if we should create a test preview
    response = input("\n🤔 Create a test preview? (y/n): ").lower().strip()
    
    if response == 'y':
        job_id = create_test_preview()
        if job_id:
            print(f"\n🚀 Start the Flask app and visit:")
            print(f"   http://localhost:6010/preview/{job_id}")
            print(f"\n💡 Or try sample previews:")
            print(f"   http://localhost:6010/sample_preview/business_meeting_01")
            print(f"   http://localhost:6010/sample_preview/documentary_01")
            print(f"   http://localhost:6010/sample_preview/podcast_01")
    else:
        print("\n💡 Sample previews available:")
        print("   http://localhost:6010/sample_preview/business_meeting_01")
        print("   http://localhost:6010/sample_preview/documentary_01")
        print("   http://localhost:6010/sample_preview/podcast_01")
    
    print(f"\n🌐 Start the web app with: python app.py")

if __name__ == "__main__":
    main()
