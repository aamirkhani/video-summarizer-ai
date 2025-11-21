#!/usr/bin/env python3
"""
Video Information Display
Shows information about video files
"""

import sys
import os
from moviepy.editor import VideoFileClip

def show_video_info(video_path: str):
    """Display information about a video file"""
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return
    
    print(f"=== Video Information: {video_path} ===")
    
    try:
        # Load video
        video = VideoFileClip(video_path)
        
        # Get video properties
        duration = video.duration
        fps = video.fps
        size = video.size
        
        print(f"Duration: {duration:.2f} seconds ({duration/60:.2f} minutes)")
        print(f"Frame rate: {fps:.2f} FPS")
        print(f"Resolution: {size[0]}x{size[1]} pixels")
        print(f"File size: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
        
        # Check if audio exists
        if video.audio is not None:
            print("Audio: Present")
        else:
            print("Audio: Not present")
        
        video.close()
        
        print(f"\n✅ Video file is valid and ready to play!")
        print(f"You can play this video using any video player like VLC, Windows Media Player, etc.")
        
    except Exception as e:
        print(f"Error reading video: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python video_info.py <video_path>")
        sys.exit(1)
    
    video_path = sys.argv[1]
    show_video_info(video_path)
