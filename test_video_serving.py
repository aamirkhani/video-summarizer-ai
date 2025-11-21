#!/usr/bin/env python3
"""
Test Video Serving
Check if sample videos can be served properly
"""

import os
import requests
import time

def test_video_files():
    """Test if video files exist and are accessible"""
    print("🎬 Testing Video File Accessibility")
    print("=" * 50)
    
    sample_videos = [
        'business_meeting_01',
        'documentary_01', 
        'podcast_01',
        'interview_01',
        'university_lecture_01',
        'training_session_01'
    ]
    
    print("\n📁 Checking file existence:")
    for video_id in sample_videos:
        summary_path = f"samples/summaries/{video_id}_summary.mp4"
        if os.path.exists(summary_path):
            size_mb = os.path.getsize(summary_path) / (1024 * 1024)
            print(f"   ✅ {video_id}: {size_mb:.2f} MB")
        else:
            print(f"   ❌ {video_id}: File not found")
    
    return sample_videos

def test_flask_routes():
    """Test Flask video serving routes"""
    print("\n🌐 Testing Flask Routes:")
    print("   Note: Start the Flask app first with 'python app.py'")
    
    sample_videos = ['business_meeting_01', 'documentary_01', 'podcast_01']
    
    for video_id in sample_videos:
        url = f"http://localhost:6010/serve_sample/{video_id}/summary"
        print(f"   Testing: {url}")
        
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                content_length = response.headers.get('content-length', 'Unknown')
                print(f"   ✅ {video_id}: Status {response.status_code}, Size: {content_length} bytes")
            else:
                print(f"   ❌ {video_id}: Status {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"   ⚠️  {video_id}: Flask app not running")
        except Exception as e:
            print(f"   ❌ {video_id}: Error - {e}")

def create_fallback_solution():
    """Create a fallback solution for video loading issues"""
    print("\n🛠️ FALLBACK SOLUTION:")
    print("=" * 25)
    
    fallback_html = '''
<!-- Fallback: Static video thumbnails with links -->
<div class="video-tiles-container mb-4">
    <div class="row">
        <div class="col-lg-4 col-md-6 mb-3">
            <div class="video-tile-static" onclick="window.open('/sample_preview/business_meeting_01')">
                <div class="static-preview">
                    <div class="preview-placeholder">
                        <i class="fas fa-play-circle fa-3x text-primary"></i>
                        <h6>Business Meeting</h6>
                        <small>10:56 → 0:16 (37x faster)</small>
                    </div>
                </div>
                <div class="tile-footer">
                    <span class="badge bg-primary">Business</span>
                    <span class="compression-badge">37x compression</span>
                </div>
            </div>
        </div>
        <!-- More static tiles... -->
    </div>
</div>
'''
    
    with open('fallback_video_tiles.html', 'w') as f:
        f.write(fallback_html)
    
    print("   📄 Created fallback_video_tiles.html")
    print("   💡 Use this if video streaming fails")

def diagnose_issues():
    """Diagnose common video loading issues"""
    print("\n🔍 COMMON ISSUES & SOLUTIONS:")
    print("=" * 35)
    
    print("\n❌ Issue 1: Spinning wheels (loading forever)")
    print("   Cause: Video files not accessible via Flask route")
    print("   Solution: Check Flask app is running and routes work")
    
    print("\n❌ Issue 2: Videos not playing")
    print("   Cause: Browser security restrictions on autoplay")
    print("   Solution: User must interact with page first")
    
    print("\n❌ Issue 3: CORS errors")
    print("   Cause: Cross-origin resource sharing issues")
    print("   Solution: Add CORS headers to Flask app")
    
    print("\n❌ Issue 4: Video format not supported")
    print("   Cause: Browser doesn't support MP4 codec")
    print("   Solution: Add multiple video formats")
    
    print("\n✅ QUICK FIXES:")
    print("   1. Restart Flask app: python app.py")
    print("   2. Check browser console for errors")
    print("   3. Try different browser")
    print("   4. Use fallback static tiles")

def main():
    """Main function"""
    print("🎬 VideoSense AI - Video Serving Diagnostics")
    print("=" * 60)
    
    # Test file existence
    sample_videos = test_video_files()
    
    # Test Flask routes (if app is running)
    test_flask_routes()
    
    # Create fallback solution
    create_fallback_solution()
    
    # Diagnose common issues
    diagnose_issues()
    
    print("\n" + "=" * 60)
    print("🚀 NEXT STEPS:")
    print("   1. Start Flask app: python app.py")
    print("   2. Visit: http://localhost:6010")
    print("   3. Check browser console for errors")
    print("   4. If videos still don't load, use fallback solution")

if __name__ == "__main__":
    main()
