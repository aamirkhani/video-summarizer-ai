#!/usr/bin/env python3
"""
Video Summarization Architecture and Data Flow Diagram Generator
Creates visual diagrams showing the core video summarization pipeline
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_architecture_diagram():
    """Create system architecture diagram for video summarization"""
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'AI Video Summarization Architecture', 
            fontsize=18, fontweight='bold', ha='center')
    
    # Color scheme
    colors = {
        'input': '#E3F2FD',
        'processing': '#FFF3E0', 
        'ai': '#E8F5E8',
        'output': '#FCE4EC',
        'storage': '#F3E5F5'
    }
    
    # Input Layer
    input_box = FancyBboxPatch((0.5, 8), 2, 0.8, 
                               boxstyle="round,pad=0.1", 
                               facecolor=colors['input'], 
                               edgecolor='black', linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.5, 8.4, 'Input Video\n(.mp4, .avi, .mov)', 
            ha='center', va='center', fontweight='bold')
    
    # Core Processing Components
    
    # 1. VideoSummarizer Class
    summarizer_box = FancyBboxPatch((0.5, 6.5), 9, 1, 
                                    boxstyle="round,pad=0.1", 
                                    facecolor=colors['processing'], 
                                    edgecolor='black', linewidth=2)
    ax.add_patch(summarizer_box)
    ax.text(5, 7, 'VideoSummarizer Class', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    
    # 2. Audio Processing Module
    audio_box = FancyBboxPatch((0.5, 5), 2.5, 1, 
                               boxstyle="round,pad=0.1", 
                               facecolor=colors['ai'], 
                               edgecolor='black', linewidth=2)
    ax.add_patch(audio_box)
    ax.text(1.75, 5.5, 'Whisper AI\nAudio Processing', 
            ha='center', va='center', fontweight='bold')
    
    # 3. LLM Analysis Module
    llm_box = FancyBboxPatch((3.5, 5), 2.5, 1, 
                             boxstyle="round,pad=0.1", 
                             facecolor=colors['ai'], 
                             edgecolor='black', linewidth=2)
    ax.add_patch(llm_box)
    ax.text(4.75, 5.5, 'OpenAI GPT\nContent Analysis', 
            ha='center', va='center', fontweight='bold')
    
    # 4. Video Assembly Module
    assembly_box = FancyBboxPatch((6.5, 5), 2.5, 1, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=colors['processing'], 
                                  edgecolor='black', linewidth=2)
    ax.add_patch(assembly_box)
    ax.text(7.75, 5.5, 'MoviePy\nVideo Assembly', 
            ha='center', va='center', fontweight='bold')
    
    # Supporting Libraries
    
    # Whisper Model
    whisper_box = FancyBboxPatch((0.5, 3.5), 2.5, 0.8, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=colors['storage'], 
                                 edgecolor='gray', linewidth=1)
    ax.add_patch(whisper_box)
    ax.text(1.75, 3.9, 'Whisper Base Model\n(Speech Recognition)', 
            ha='center', va='center', fontsize=10)
    
    # OpenAI Client
    openai_box = FancyBboxPatch((3.5, 3.5), 2.5, 0.8, 
                                boxstyle="round,pad=0.05", 
                                facecolor=colors['storage'], 
                                edgecolor='gray', linewidth=1)
    ax.add_patch(openai_box)
    ax.text(4.75, 3.9, 'OpenAI API Client\n(GPT-3.5-turbo)', 
            ha='center', va='center', fontsize=10)
    
    # MoviePy Engine
    moviepy_box = FancyBboxPatch((6.5, 3.5), 2.5, 0.8, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=colors['storage'], 
                                 edgecolor='gray', linewidth=1)
    ax.add_patch(moviepy_box)
    ax.text(7.75, 3.9, 'MoviePy Engine\n(Video Processing)', 
            ha='center', va='center', fontsize=10)
    
    # Fallback System
    fallback_box = FancyBboxPatch((3.5, 2), 2.5, 0.8, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor='#FFEBEE', 
                                  edgecolor='red', linewidth=1, linestyle='--')
    ax.add_patch(fallback_box)
    ax.text(4.75, 2.4, 'Fallback System\n(Heuristic Analysis)', 
            ha='center', va='center', fontsize=10, style='italic')
    
    # Output
    output_box = FancyBboxPatch((7, 0.5), 2.5, 0.8, 
                                boxstyle="round,pad=0.1", 
                                facecolor=colors['output'], 
                                edgecolor='black', linewidth=2)
    ax.add_patch(output_box)
    ax.text(8.25, 0.9, 'Summary Video\n+ Metadata', 
            ha='center', va='center', fontweight='bold')
    
    # Arrows showing data flow
    arrows = [
        # Input to VideoSummarizer
        ((1.5, 8), (5, 6.5)),
        # VideoSummarizer to modules
        ((2.5, 6.5), (1.75, 6)),
        ((5, 6.5), (4.75, 6)),
        ((7.5, 6.5), (7.75, 6)),
        # Modules to libraries
        ((1.75, 5), (1.75, 4.3)),
        ((4.75, 5), (4.75, 4.3)),
        ((7.75, 5), (7.75, 4.3)),
        # Fallback connection
        ((4.75, 3.5), (4.75, 2.8)),
        # To output
        ((7.75, 5), (8.25, 1.3))
    ]
    
    for start, end in arrows:
        arrow = ConnectionPatch(start, end, "data", "data",
                               arrowstyle="->", shrinkA=5, shrinkB=5,
                               mutation_scale=20, fc="black", lw=2)
        ax.add_patch(arrow)
    
    # Add component labels
    ax.text(0.2, 7, '1', fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="circle", facecolor='white'))
    ax.text(0.2, 5.5, '2', fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="circle", facecolor='white'))
    ax.text(3.2, 5.5, '3', fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="circle", facecolor='white'))
    ax.text(6.2, 5.5, '4', fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="circle", facecolor='white'))
    ax.text(9.7, 0.9, '5', fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="circle", facecolor='white'))
    
    plt.tight_layout()
    plt.savefig('video_summarization_architecture.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_data_flow_diagram():
    """Create detailed data flow diagram for video summarization"""
    
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(6, 11.5, 'Video Summarization Data Flow', 
            fontsize=18, fontweight='bold', ha='center')
    
    # Color scheme for data types
    data_colors = {
        'video': '#E3F2FD',
        'audio': '#FFF3E0',
        'text': '#E8F5E8',
        'analysis': '#FCE4EC',
        'segments': '#F3E5F5'
    }
    
    # Stage 1: Input Processing
    ax.text(1, 10.5, 'Stage 1: Audio Extraction', 
            fontsize=14, fontweight='bold')
    
    # Input video
    video_input = FancyBboxPatch((0.5, 9.5), 2, 0.6, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=data_colors['video'], 
                                 edgecolor='black')
    ax.add_patch(video_input)
    ax.text(1.5, 9.8, 'Input Video\n(MP4/AVI/MOV)', ha='center', va='center', fontsize=10)
    
    # Whisper processing
    whisper_proc = FancyBboxPatch((3.5, 9.5), 2.5, 0.6, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor=data_colors['audio'], 
                                  edgecolor='black')
    ax.add_patch(whisper_proc)
    ax.text(4.75, 9.8, 'Whisper AI Processing\n(Speech → Text + Timestamps)', 
            ha='center', va='center', fontsize=10)
    
    # Transcript output
    transcript_out = FancyBboxPatch((7, 9.5), 2.5, 0.6, 
                                    boxstyle="round,pad=0.05", 
                                    facecolor=data_colors['text'], 
                                    edgecolor='black')
    ax.add_patch(transcript_out)
    ax.text(8.25, 9.8, 'Word-Level Transcript\n+ Timing Data', 
            ha='center', va='center', fontsize=10)
    
    # Stage 2: Content Analysis
    ax.text(1, 8.5, 'Stage 2: LLM Analysis', 
            fontsize=14, fontweight='bold')
    
    # Transcript data structure
    transcript_data = FancyBboxPatch((0.5, 7.5), 3, 0.8, 
                                     boxstyle="round,pad=0.05", 
                                     facecolor=data_colors['text'], 
                                     edgecolor='black')
    ax.add_patch(transcript_data)
    ax.text(2, 7.9, 'Structured Transcript Data:\n• Full text\n• Word timestamps\n• Segments', 
            ha='center', va='center', fontsize=9)
    
    # LLM processing
    llm_proc = FancyBboxPatch((4.5, 7.5), 3, 0.8, 
                              boxstyle="round,pad=0.05", 
                              facecolor=data_colors['analysis'], 
                              edgecolor='black')
    ax.add_patch(llm_proc)
    ax.text(6, 7.9, 'GPT-3.5 Analysis:\n• Content importance\n• Topic identification\n• Segment selection', 
            ha='center', va='center', fontsize=9)
    
    # Analysis output
    analysis_out = FancyBboxPatch((8.5, 7.5), 3, 0.8, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor=data_colors['segments'], 
                                  edgecolor='black')
    ax.add_patch(analysis_out)
    ax.text(10, 7.9, 'Summary Segments:\n• Start/end times\n• Importance scores\n• Topic labels', 
            ha='center', va='center', fontsize=9)
    
    # Stage 3: Video Assembly
    ax.text(1, 6.5, 'Stage 3: Video Assembly', 
            fontsize=14, fontweight='bold')
    
    # Segment extraction
    extraction = FancyBboxPatch((0.5, 5.5), 2.5, 0.8, 
                                boxstyle="round,pad=0.05", 
                                facecolor=data_colors['video'], 
                                edgecolor='black')
    ax.add_patch(extraction)
    ax.text(1.75, 5.9, 'Segment Extraction:\n• Precise timing\n• Quality preservation', 
            ha='center', va='center', fontsize=9)
    
    # Concatenation
    concat = FancyBboxPatch((3.5, 5.5), 2.5, 0.8, 
                            boxstyle="round,pad=0.05", 
                            facecolor=data_colors['video'], 
                            edgecolor='black')
    ax.add_patch(concat)
    ax.text(4.75, 5.9, 'Video Concatenation:\n• Seamless transitions\n• Audio sync', 
            ha='center', va='center', fontsize=9)
    
    # Final output
    final_output = FancyBboxPatch((6.5, 5.5), 2.5, 0.8, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor=data_colors['video'], 
                                  edgecolor='black')
    ax.add_patch(final_output)
    ax.text(7.75, 5.9, 'Summary Video:\n• H.264/AAC encoding\n• Metadata included', 
            ha='center', va='center', fontsize=9)
    
    # Data format examples
    ax.text(1, 4.5, 'Data Formats & Examples', 
            fontsize=14, fontweight='bold')
    
    # Example boxes
    examples = [
        (0.5, 3.5, 'Transcript Format:\n{\n  "word": "hello",\n  "start": 1.2,\n  "end": 1.8,\n  "confidence": 0.95\n}'),
        (3.5, 3.5, 'LLM Prompt:\n"Analyze transcript and\nidentify 3-5 key segments\nfor summary video..."'),
        (6.5, 3.5, 'Segment Output:\n{\n  "start_time": 15.2,\n  "end_time": 45.8,\n  "importance": 9,\n  "topic": "introduction"\n}'),
        (9.5, 3.5, 'Video Metadata:\n{\n  "duration": 120.5,\n  "segments": 4,\n  "compression": "8.5x"\n}')
    ]
    
    for x, y, text in examples:
        example_box = FancyBboxPatch((x, y), 2.5, 1.2, 
                                     boxstyle="round,pad=0.05", 
                                     facecolor='#F5F5F5', 
                                     edgecolor='gray')
        ax.add_patch(example_box)
        ax.text(x + 1.25, y + 0.6, text, ha='center', va='center', 
                fontsize=8, fontfamily='monospace')
    
    # Fallback path
    ax.text(1, 2.5, 'Fallback Processing (No API Key)', 
            fontsize=12, fontweight='bold', color='red')
    
    fallback_box = FancyBboxPatch((0.5, 1.5), 11, 0.6, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor='#FFEBEE', 
                                  edgecolor='red', linestyle='--')
    ax.add_patch(fallback_box)
    ax.text(6, 1.8, 'Heuristic Analysis: First segment (intro) + Middle segment (content) + Last segment (conclusion)', 
            ha='center', va='center', fontsize=10, style='italic')
    
    # Flow arrows
    flow_arrows = [
        # Stage 1 flow
        ((2.5, 9.8), (3.5, 9.8)),
        ((6, 9.8), (7, 9.8)),
        # Stage 2 flow  
        ((8.25, 9.5), (2, 8.3)),
        ((3.5, 7.9), (4.5, 7.9)),
        ((7.5, 7.9), (8.5, 7.9)),
        # Stage 3 flow
        ((10, 7.5), (1.75, 6.3)),
        ((3, 5.9), (3.5, 5.9)),
        ((6, 5.9), (6.5, 5.9)),
        # Fallback path
        ((2, 7.5), (6, 2.1))
    ]
    
    for start, end in flow_arrows:
        arrow = ConnectionPatch(start, end, "data", "data",
                               arrowstyle="->", shrinkA=3, shrinkB=3,
                               mutation_scale=15, fc="blue", lw=1.5)
        ax.add_patch(arrow)
    
    # Processing time indicators
    time_labels = [
        (1.5, 10.2, '~30s'),
        (6, 8.2, '~60s'),
        (4.75, 6.2, '~90s')
    ]
    
    for x, y, time in time_labels:
        ax.text(x, y, time, fontsize=10, fontweight='bold', 
                bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('video_summarization_dataflow.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Generate both architecture and data flow diagrams"""
    print("Generating Video Summarization Architecture Diagram...")
    create_architecture_diagram()
    
    print("Generating Video Summarization Data Flow Diagram...")
    create_data_flow_diagram()
    
    print("Diagrams saved as:")
    print("- video_summarization_architecture.png")
    print("- video_summarization_dataflow.png")

if __name__ == "__main__":
    main()
