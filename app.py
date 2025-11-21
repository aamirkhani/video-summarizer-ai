#!/usr/bin/env python3
"""
VideoSense AI - Flask Web Application
Revolutionary AI-powered video summarization platform
"""

from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import uuid
import json
from datetime import datetime
import threading
from video_summarizer_simple import VideoSummarizer
from video_info import show_video_info
import tempfile
import shutil

app = Flask(__name__)
app.secret_key = 'videosense-ai-secret-key-2024'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm', 'm4v'}

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)
os.makedirs('templates', exist_ok=True)

# Global storage for processing status
processing_status = {}
completed_summaries = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_video_info(video_path):
    """Get video information"""
    try:
        from moviepy.editor import VideoFileClip
        video = VideoFileClip(video_path)
        info = {
            'duration': round(video.duration, 2),
            'fps': video.fps,
            'size': video.size,
            'file_size': os.path.getsize(video_path)
        }
        video.close()
        return info
    except Exception as e:
        return {'error': str(e)}

def process_video_async(job_id, input_path, output_path, summary_type='auto', target_length='2_minutes'):
    """Process video in background thread"""
    try:
        processing_status[job_id] = {
            'status': 'processing',
            'progress': 0,
            'stage': 'Initializing AI models...',
            'start_time': datetime.now().isoformat()
        }
        
        # Initialize summarizer
        summarizer = VideoSummarizer()
        processing_status[job_id]['progress'] = 20
        processing_status[job_id]['stage'] = 'Extracting audio and generating timestamps...'
        
        # Process video
        result = summarizer.process_video(input_path, output_path)
        
        processing_status[job_id]['progress'] = 100
        processing_status[job_id]['status'] = 'completed'
        processing_status[job_id]['stage'] = 'Summary video created successfully!'
        
        # Store completed summary info
        completed_summaries[job_id] = {
            'input_file': os.path.basename(input_path),
            'output_file': os.path.basename(output_path),
            'result': result,
            'completion_time': datetime.now().isoformat(),
            'summary_type': summary_type,
            'target_length': target_length
        }
        
    except Exception as e:
        processing_status[job_id] = {
            'status': 'error',
            'error': str(e),
            'stage': f'Error: {str(e)}'
        }

@app.route('/')
def index():
    """Main dashboard"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and start processing"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        # Generate unique job ID
        job_id = str(uuid.uuid4())
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{filename}"
        input_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(input_path)
        
        # Generate output path
        output_filename = f"summary_{timestamp}_{job_id[:8]}.mp4"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        # Get form data
        summary_type = request.form.get('summary_type', 'auto')
        target_length = request.form.get('target_length', '2_minutes')
        
        # Start background processing
        thread = threading.Thread(
            target=process_video_async,
            args=(job_id, input_path, output_path, summary_type, target_length)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'job_id': job_id,
            'message': 'Video uploaded successfully. Processing started.',
            'filename': filename
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/status/<job_id>')
def get_status(job_id):
    """Get processing status"""
    if job_id in processing_status:
        return jsonify(processing_status[job_id])
    elif job_id in completed_summaries:
        return jsonify({
            'status': 'completed',
            'progress': 100,
            'stage': 'Summary ready for download!'
        })
    else:
        return jsonify({'error': 'Job not found'}), 404

@app.route('/result/<job_id>')
def get_result(job_id):
    """Get processing result"""
    if job_id in completed_summaries:
        return jsonify(completed_summaries[job_id])
    else:
        return jsonify({'error': 'Result not found'}), 404

@app.route('/download/<job_id>')
def download_summary(job_id):
    """Download summary video"""
    if job_id in completed_summaries:
        summary_info = completed_summaries[job_id]
        output_file = summary_info['output_file']
        output_path = os.path.join(OUTPUT_FOLDER, output_file)
        
        if os.path.exists(output_path):
            return send_file(output_path, as_attachment=True, download_name=f"summary_{output_file}")
        else:
            return jsonify({'error': 'File not found'}), 404
    else:
        return jsonify({'error': 'Summary not found'}), 404

@app.route('/library')
def library():
    """Show library of processed videos"""
    return render_template('library.html', summaries=completed_summaries)

@app.route('/api/v1/summarize', methods=['POST'])
def api_summarize():
    """API endpoint for video summarization"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if 'video_url' not in data:
            return jsonify({'error': 'video_url is required'}), 400
        
        # Generate job ID
        job_id = str(uuid.uuid4())
        
        # For now, return mock response since we'd need to implement URL downloading
        return jsonify({
            'job_id': job_id,
            'status': 'accepted',
            'message': 'Video processing started',
            'estimated_completion': '2-5 minutes',
            'webhook_url': f'/api/v1/status/{job_id}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/v1/status/<job_id>')
def api_status(job_id):
    """API endpoint for status checking"""
    return get_status(job_id)

@app.route('/samples')
def samples():
    """Show sample videos gallery"""
    # Load samples index
    samples_index_path = 'samples/samples_index.json'
    if os.path.exists(samples_index_path):
        with open(samples_index_path, 'r') as f:
            samples_data = json.load(f)
    else:
        samples_data = {'samples': [], 'categories': {}}
    
    return render_template('samples.html', samples_data=samples_data)

@app.route('/samples/download/<sample_id>')
def download_sample(sample_id):
    """Download a sample summary video"""
    sample_file = f"samples/summaries/{sample_id}_summary.mp4"
    
    if os.path.exists(sample_file):
        return send_file(sample_file, as_attachment=True, download_name=f"{sample_id}_summary.mp4")
    else:
        return jsonify({'error': 'Sample not found'}), 404

@app.route('/sample_info/<sample_id>')
def sample_info(sample_id):
    """Get detailed information about a sample"""
    metadata_file = f"samples/summaries/{sample_id}_metadata.json"
    
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        return jsonify(metadata)
    else:
        return jsonify({'error': 'Sample metadata not found'}), 404

@app.route('/preview/<job_id>')
def preview_video(job_id):
    """Show video preview page with side-by-side comparison"""
    if job_id in completed_summaries:
        summary_info = completed_summaries[job_id]
        result = summary_info['result']
        
        # Get video file paths
        original_path = result['input_video']
        summary_path = result['output_video']
        
        # Get video information
        original_info = get_video_info(original_path)
        summary_info_data = get_video_info(summary_path)
        
        # Calculate compression ratio
        if 'duration' in original_info and 'duration' in summary_info_data:
            compression_ratio = f"{original_info['duration'] / summary_info_data['duration']:.1f}x"
        else:
            compression_ratio = "N/A"
        
        return render_template('video_preview.html',
            job_id=job_id,
            original_video_url=f'/serve_video/{job_id}/original',
            summary_video_url=f'/serve_video/{job_id}/summary',
            original_download_url=f'/download_original/{job_id}',
            summary_download_url=f'/download/{job_id}',
            original_duration=f"{original_info.get('duration', 0)/60:.1f} min" if 'duration' in original_info else "N/A",
            summary_duration=f"{summary_info_data.get('duration', 0):.1f} sec" if 'duration' in summary_info_data else "N/A",
            original_size=f"{original_info.get('file_size', 0)/(1024*1024):.1f} MB" if 'file_size' in original_info else "N/A",
            summary_size=f"{summary_info_data.get('file_size', 0)/(1024*1024):.1f} MB" if 'file_size' in summary_info_data else "N/A",
            original_resolution=f"{original_info['size'][0]}x{original_info['size'][1]}" if 'size' in original_info else "N/A",
            compression_ratio=compression_ratio,
            segments=result['summary_segments']
        )
    else:
        return jsonify({'error': 'Video not found'}), 404

@app.route('/serve_video/<job_id>/<video_type>')
def serve_video(job_id, video_type):
    """Serve video files for streaming"""
    if job_id in completed_summaries:
        summary_info = completed_summaries[job_id]
        result = summary_info['result']
        
        if video_type == 'original':
            video_path = result['input_video']
        elif video_type == 'summary':
            video_path = result['output_video']
        else:
            return jsonify({'error': 'Invalid video type'}), 400
        
        if os.path.exists(video_path):
            return send_file(video_path, mimetype='video/mp4')
        else:
            return jsonify({'error': 'Video file not found'}), 404
    else:
        return jsonify({'error': 'Job not found'}), 404

@app.route('/download_original/<job_id>')
def download_original(job_id):
    """Download original video"""
    if job_id in completed_summaries:
        summary_info = completed_summaries[job_id]
        result = summary_info['result']
        original_path = result['input_video']
        
        if os.path.exists(original_path):
            return send_file(original_path, as_attachment=True, download_name=f"original_{job_id}.mp4")
        else:
            return jsonify({'error': 'Original video not found'}), 404
    else:
        return jsonify({'error': 'Job not found'}), 404

@app.route('/sample_preview/<sample_id>')
def sample_preview(sample_id):
    """Show sample video preview"""
    metadata_file = f"samples/summaries/{sample_id}_metadata.json"
    
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        
        result = metadata['processing_result']
        original_path = result['input_video']
        summary_path = result['output_video']
        
        # Get video information
        original_info = get_video_info(original_path)
        summary_info = get_video_info(summary_path)
        
        # Calculate compression ratio
        if 'duration' in original_info and 'duration' in summary_info:
            compression_ratio = f"{original_info['duration'] / summary_info['duration']:.1f}x"
        else:
            compression_ratio = "N/A"
        
        return render_template('video_preview.html',
            job_id=sample_id,
            original_video_url=f'/serve_sample/{sample_id}/original',
            summary_video_url=f'/serve_sample/{sample_id}/summary',
            original_download_url=f'/download_sample_original/{sample_id}',
            summary_download_url=f'/samples/download/{sample_id}',
            original_duration=f"{original_info.get('duration', 0)/60:.1f} min" if 'duration' in original_info else "N/A",
            summary_duration=f"{summary_info.get('duration', 0):.1f} sec" if 'duration' in summary_info else "N/A",
            original_size=f"{original_info.get('file_size', 0)/(1024*1024):.1f} MB" if 'file_size' in original_info else "N/A",
            summary_size=f"{summary_info.get('file_size', 0)/(1024*1024):.1f} MB" if 'file_size' in summary_info else "N/A",
            original_resolution=f"{original_info['size'][0]}x{original_info['size'][1]}" if 'size' in original_info else "N/A",
            compression_ratio=compression_ratio,
            segments=result['summary_segments']
        )
    else:
        return jsonify({'error': 'Sample not found'}), 404

@app.route('/serve_sample/<sample_id>/<video_type>')
def serve_sample_video(sample_id, video_type):
    """Serve sample video files for streaming"""
    if video_type == 'original':
        video_path = f"samples/originals/{sample_id}.mp4"
    elif video_type == 'summary':
        video_path = f"samples/summaries/{sample_id}_summary.mp4"
    else:
        return jsonify({'error': 'Invalid video type'}), 400
    
    if os.path.exists(video_path):
        return send_file(video_path, mimetype='video/mp4')
    else:
        return jsonify({'error': 'Video file not found'}), 404

@app.route('/download_sample_original/<sample_id>')
def download_sample_original(sample_id):
    """Download original sample video"""
    original_path = f"samples/originals/{sample_id}.mp4"
    
    if os.path.exists(original_path):
        return send_file(original_path, as_attachment=True, download_name=f"original_{sample_id}.mp4")
    else:
        return jsonify({'error': 'Original sample video not found'}), 404

if __name__ == '__main__':
    print("🎬 Starting VideoSense AI Platform...")
    print("🌐 Access the application at: http://localhost:6010")
    print("📚 API Documentation available at: http://localhost:6010/api/docs")
    app.run(host='0.0.0.0', port=6010, debug=True)
