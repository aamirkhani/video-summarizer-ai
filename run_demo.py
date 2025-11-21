#!/usr/bin/env python3
"""
VideoSense AI - Complete Demo Runner
Demonstrates the full web application with sample gallery
"""

import subprocess
import time
import webbrowser
import os
import sys

def check_samples():
    """Check if sample videos are available"""
    samples_dir = "samples/summaries"
    if not os.path.exists(samples_dir):
        print("❌ Sample videos not found!")
        print("Run 'python download_samples.py' first to generate sample videos.")
        return False
    
    sample_files = [f for f in os.listdir(samples_dir) if f.endswith('_summary.mp4')]
    print(f"✅ Found {len(sample_files)} sample videos")
    return len(sample_files) > 0

def start_flask_app():
    """Start the Flask web application"""
    print("🚀 Starting VideoSense AI Web Application...")
    print("🌐 Server will be available at: http://localhost:6010")
    print("📱 Features available:")
    print("   • Sample Gallery with 12 processed videos")
    print("   • Upload and process your own videos")
    print("   • Download AI-generated summaries")
    print("   • REST API for integration")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        # Start Flask app
        subprocess.run([sys.executable, "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 VideoSense AI server stopped")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    """Main demo function"""
    print("🎬 VideoSense AI - Complete Demo")
    print("=" * 50)
    
    # Check if samples exist
    if not check_samples():
        print("\n🔧 To generate sample videos, run:")
        print("   python download_samples.py")
        print("\n⚡ To start with just upload functionality:")
        print("   python app.py")
        return
    
    print("\n🎯 Demo includes:")
    print("   ✅ 12 Pre-processed sample videos")
    print("   ✅ Interactive sample gallery")
    print("   ✅ Upload and process new videos")
    print("   ✅ Real-time processing status")
    print("   ✅ Download generated summaries")
    print("   ✅ REST API endpoints")
    
    print("\n🌟 Sample Categories:")
    print("   • Business (5 videos): Meetings, training, demos")
    print("   • Education (5 videos): Lectures, tutorials, documentaries")
    print("   • Entertainment (2 videos): Podcasts, interviews")
    
    print("\n" + "=" * 50)
    
    # Start the web application
    start_flask_app()

if __name__ == "__main__":
    main()
