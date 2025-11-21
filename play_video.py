#!/usr/bin/env python3
"""
Simple video player using OpenCV
"""

import cv2
import sys
import os

def play_video(video_path: str):
    """Play video using OpenCV"""
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return
    
    print(f"Playing video: {video_path}")
    print("Press 'q' to quit, 'space' to pause/resume")
    
    # Open video
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = int(1000 / fps) if fps > 0 else 33  # milliseconds
    
    paused = False
    
    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                print("End of video")
                break
        
        # Display frame
        cv2.imshow('Video Player', frame)
        
        # Handle key presses
        key = cv2.waitKey(frame_delay if not paused else 0) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord(' '):  # Space bar
            paused = not paused
            print("Paused" if paused else "Resumed")
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python play_video.py <video_path>")
        sys.exit(1)
    
    video_path = sys.argv[1]
    play_video(video_path)
