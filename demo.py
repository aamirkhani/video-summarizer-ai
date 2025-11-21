#!/usr/bin/env python3
"""
AI Video Summarizer Demo
Demonstrates the complete functionality of the video summarizer
"""

import os
from video_summarizer_simple import VideoSummarizer
from video_info import show_video_info

def run_demo():
    """Run a complete demonstration of the video summarizer"""
    print("🎬 AI Video Summarizer Demo")
    print("=" * 50)
    
    # Check if we have a test video
    test_video = "test_video.mp4"
    if not os.path.exists(test_video):
        print("❌ No test video found. Please run the main script first to download a test video.")
        return
    
    print("📹 Original Video Information:")
    show_video_info(test_video)
    print()
    
    # Initialize summarizer
    print("🤖 Initializing AI Video Summarizer...")
    summarizer = VideoSummarizer()
    print()
    
    # Process video
    output_path = "output/demo_summary.mp4"
    print("⚡ Processing video...")
    
    try:
        result = summarizer.process_video(test_video, output_path)
        
        print("\n✅ Processing Complete!")
        print("=" * 50)
        
        # Show results
        print(f"📊 Summary Statistics:")
        print(f"   • Original duration: {596.47:.1f} seconds")
        print(f"   • Summary duration: ~{sum(seg['end_time'] - seg['start_time'] for seg in result['summary_segments']):.1f} seconds")
        print(f"   • Compression ratio: {596.47 / sum(seg['end_time'] - seg['start_time'] for seg in result['summary_segments']):.1f}x")
        print(f"   • Number of segments: {len(result['summary_segments'])}")
        
        print(f"\n📝 Selected Segments:")
        for i, segment in enumerate(result['summary_segments']):
            duration = segment['end_time'] - segment['start_time']
            print(f"   {i+1}. {segment['topic'].title()}")
            print(f"      Time: {segment['start_time']:.1f}s - {segment['end_time']:.1f}s ({duration:.1f}s)")
            print(f"      Importance: {segment['importance']}/10")
            print(f"      Reason: {segment['reason']}")
            print()
        
        print("📹 Summary Video Information:")
        show_video_info(output_path)
        
        print("\n🎉 Demo Complete!")
        print(f"Your summary video is ready: {output_path}")
        print("You can play it with any video player!")
        
    except Exception as e:
        print(f"❌ Error during processing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_demo()
