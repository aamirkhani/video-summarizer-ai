#!/usr/bin/env python3
"""
VideoSense AI - Artwork Generation for Landing Page
Creates visual assets using text-to-image generation concepts
"""

import os
import json
from datetime import datetime

def create_artwork_prompts():
    """Generate detailed prompts for creating VideoSense AI artwork"""
    
    artwork_prompts = {
        "hero_banner": {
            "title": "Hero Banner - AI Video Processing",
            "prompt": "A futuristic, sleek illustration showing AI analyzing video content. Split-screen design with original video on left showing a business meeting, and AI-processed summary on right with glowing neural network patterns. Modern gradient background in blues and purples. Clean, professional, tech-forward aesthetic. High-resolution, web-ready banner format.",
            "dimensions": "1920x600",
            "style": "Modern tech illustration, gradient backgrounds, clean lines"
        },
        
        "ai_brain_processing": {
            "title": "AI Brain Processing Videos",
            "prompt": "Abstract digital brain made of interconnected nodes and flowing data streams, processing video frames. Holographic video thumbnails floating around the brain. Bright cyan and purple neon colors against dark background. Futuristic, high-tech visualization of AI video analysis. Particle effects and glowing connections.",
            "dimensions": "800x600",
            "style": "Cyberpunk, neon colors, abstract tech art"
        },
        
        "video_timeline_ai": {
            "title": "AI Video Timeline Analysis",
            "prompt": "Elegant visualization of video timeline with AI-identified key moments highlighted as glowing points. Waveform audio visualization below with word-level timestamps. Clean, modern interface design with subtle animations. Professional blue and white color scheme. Technical but accessible design.",
            "dimensions": "1200x400",
            "style": "Clean UI design, data visualization, professional"
        },
        
        "synchronized_playback": {
            "title": "Synchronized Video Playback",
            "prompt": "Two video players side by side showing synchronized playback - original video on left, AI summary on right. Connecting lines and sync indicators between them. Modern media player interface with play controls. Sleek, professional design with subtle shadows and gradients.",
            "dimensions": "1000x600",
            "style": "Modern UI design, media players, professional interface"
        },
        
        "ai_assistant_collaboration": {
            "title": "Human-AI Collaboration",
            "prompt": "Artistic representation of human creativity collaborating with AI. Human silhouette on left with creative thought bubbles, AI robot/assistant on right with code and algorithms. Meeting in the middle with shared video content creation. Warm colors for human side, cool tech colors for AI side.",
            "dimensions": "800x600",
            "style": "Conceptual art, human-AI collaboration, warm and cool color contrast"
        },
        
        "feature_icons": {
            "title": "Feature Icons Set",
            "prompt": "Set of modern, minimalist icons representing: 1) Lightning bolt for speed, 2) Target/bullseye for precision, 3) Globe for multi-language, 4) Shield for enterprise security, 5) Magic wand for AI processing, 6) Video play button with AI sparkles. Consistent style, gradient colors, professional look.",
            "dimensions": "400x400 each",
            "style": "Icon design, minimalist, gradient colors, consistent style"
        },
        
        "background_pattern": {
            "title": "Subtle Background Pattern",
            "prompt": "Subtle, elegant background pattern with video-related elements. Faint video frame outlines, play buttons, and AI circuit patterns. Very light opacity, won't interfere with text. Professional blue and gray tones. Seamless, tileable pattern for web backgrounds.",
            "dimensions": "500x500",
            "style": "Subtle pattern, low opacity, professional, seamless"
        },
        
        "success_illustration": {
            "title": "Success/Results Illustration",
            "prompt": "Celebratory illustration showing successful video processing. Original long video transforming into compact summary with sparkles and success indicators. Charts showing time savings and compression ratios. Positive, achievement-focused design with green success colors and gold accents.",
            "dimensions": "600x400",
            "style": "Success illustration, positive colors, achievement theme"
        }
    }
    
    return artwork_prompts

def generate_css_artwork():
    """Generate CSS-based artwork and visual elements"""
    
    css_artwork = """
/* VideoSense AI - Custom Artwork CSS */

/* Animated Background Gradient */
.hero-gradient {
    background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* AI Processing Animation */
.ai-processing-dots {
    display: inline-block;
    position: relative;
}

.ai-processing-dots::after {
    content: '';
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: #667eea;
    animation: aiDots 1.5s infinite;
}

@keyframes aiDots {
    0%, 20% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.5); opacity: 0.7; }
    100% { transform: scale(1); opacity: 1; }
}

/* Video Frame Animation */
.video-frame-effect {
    position: relative;
    overflow: hidden;
}

.video-frame-effect::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    animation: scanLine 3s infinite;
}

@keyframes scanLine {
    0% { left: -100%; }
    100% { left: 100%; }
}

/* Neural Network Pattern */
.neural-network-bg {
    background-image: 
        radial-gradient(circle at 20% 20%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 60%, rgba(240, 147, 251, 0.1) 0%, transparent 50%);
    background-size: 300px 300px, 400px 400px, 200px 200px;
    animation: networkFloat 20s ease-in-out infinite;
}

@keyframes networkFloat {
    0%, 100% { background-position: 0% 0%, 100% 100%, 50% 50%; }
    50% { background-position: 100% 100%, 0% 0%, 0% 100%; }
}

/* Glowing Elements */
.glow-effect {
    box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
    animation: pulseGlow 2s ease-in-out infinite alternate;
}

@keyframes pulseGlow {
    from { box-shadow: 0 0 20px rgba(102, 126, 234, 0.3); }
    to { box-shadow: 0 0 30px rgba(102, 126, 234, 0.6); }
}

/* Data Stream Effect */
.data-stream {
    position: relative;
    overflow: hidden;
}

.data-stream::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: repeating-linear-gradient(
        90deg,
        transparent,
        transparent 10px,
        rgba(102, 126, 234, 0.1) 10px,
        rgba(102, 126, 234, 0.1) 20px
    );
    animation: dataFlow 2s linear infinite;
}

@keyframes dataFlow {
    0% { transform: translateX(-20px); }
    100% { transform: translateX(20px); }
}

/* Success Sparkle Effect */
.success-sparkle {
    position: relative;
}

.success-sparkle::before,
.success-sparkle::after {
    content: '✨';
    position: absolute;
    font-size: 1.2rem;
    animation: sparkle 2s ease-in-out infinite;
}

.success-sparkle::before {
    top: -10px;
    right: -10px;
    animation-delay: 0s;
}

.success-sparkle::after {
    bottom: -10px;
    left: -10px;
    animation-delay: 1s;
}

@keyframes sparkle {
    0%, 100% { opacity: 0; transform: scale(0.5); }
    50% { opacity: 1; transform: scale(1); }
}
"""
    
    return css_artwork

def create_svg_illustrations():
    """Generate SVG illustrations for the website"""
    
    svg_illustrations = {
        "ai_brain_icon": """
<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="brainGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
        </linearGradient>
    </defs>
    <path d="M50 10 C70 10, 85 25, 85 45 C85 65, 70 80, 50 80 C30 80, 15 65, 15 45 C15 25, 30 10, 50 10 Z" 
          fill="url(#brainGradient)" opacity="0.8"/>
    <circle cx="35" cy="35" r="3" fill="#fff" opacity="0.9"/>
    <circle cx="50" cy="30" r="2" fill="#fff" opacity="0.7"/>
    <circle cx="65" cy="40" r="3" fill="#fff" opacity="0.9"/>
    <circle cx="40" cy="55" r="2" fill="#fff" opacity="0.6"/>
    <circle cx="60" cy="60" r="3" fill="#fff" opacity="0.8"/>
    <line x1="35" y1="35" x2="50" y2="30" stroke="#fff" stroke-width="1" opacity="0.5"/>
    <line x1="50" y1="30" x2="65" y2="40" stroke="#fff" stroke-width="1" opacity="0.5"/>
    <line x1="35" y1="35" x2="40" y2="55" stroke="#fff" stroke-width="1" opacity="0.5"/>
    <line x1="65" y1="40" x2="60" y2="60" stroke="#fff" stroke-width="1" opacity="0.5"/>
</svg>
        """,
        
        "video_processing_icon": """
<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="videoGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f093fb;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#f5576c;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="10" y="20" width="35" height="25" rx="3" fill="url(#videoGradient)" opacity="0.8"/>
    <rect x="55" y="20" width="35" height="25" rx="3" fill="url(#videoGradient)" opacity="0.6"/>
    <polygon points="22,30 22,38 30,34" fill="#fff"/>
    <polygon points="67,30 67,38 75,34" fill="#fff"/>
    <path d="M45 32 L55 32" stroke="#667eea" stroke-width="2" marker-end="url(#arrowhead)"/>
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="#667eea"/>
        </marker>
    </defs>
    <text x="50" y="70" text-anchor="middle" font-family="Arial" font-size="12" fill="#667eea">AI Processing</text>
</svg>
        """,
        
        "sync_icon": """
<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="syncGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#28a745;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#20c997;stop-opacity:1" />
        </linearGradient>
    </defs>
    <circle cx="30" cy="50" r="20" fill="none" stroke="url(#syncGradient)" stroke-width="3"/>
    <circle cx="70" cy="50" r="20" fill="none" stroke="url(#syncGradient)" stroke-width="3"/>
    <path d="M50 35 Q50 25, 60 35" fill="none" stroke="url(#syncGradient)" stroke-width="2"/>
    <path d="M50 65 Q50 75, 40 65" fill="none" stroke="url(#syncGradient)" stroke-width="2"/>
    <circle cx="30" cy="50" r="3" fill="#28a745"/>
    <circle cx="70" cy="50" r="3" fill="#28a745"/>
</svg>
        """
    }
    
    return svg_illustrations

def save_artwork_assets():
    """Save all artwork assets to files"""
    
    # Create static directories
    os.makedirs("static/css", exist_ok=True)
    os.makedirs("static/images", exist_ok=True)
    os.makedirs("static/svg", exist_ok=True)
    
    # Save artwork prompts for reference
    prompts = create_artwork_prompts()
    with open("static/artwork_prompts.json", "w") as f:
        json.dump(prompts, f, indent=2)
    
    # Save CSS artwork
    css_content = generate_css_artwork()
    with open("static/css/artwork.css", "w") as f:
        f.write(css_content)
    
    # Save SVG illustrations
    svg_illustrations = create_svg_illustrations()
    for name, svg_content in svg_illustrations.items():
        with open(f"static/svg/{name}.svg", "w") as f:
            f.write(svg_content)
    
    print("✅ Artwork assets saved successfully!")
    return prompts, css_content, svg_illustrations

def generate_artwork_integration():
    """Generate code to integrate artwork into the website"""
    
    integration_code = """
<!-- Add to base.html head section -->
<link href="{{ url_for('static', filename='css/artwork.css') }}" rel="stylesheet">

<!-- Hero Section with Animated Background -->
<div class="hero-gradient neural-network-bg">
    <div class="container py-5">
        <div class="row align-items-center">
            <div class="col-md-6">
                <h1 class="display-4 fw-bold text-white mb-4">
                    <span class="glow-effect">VideoSense AI</span>
                </h1>
                <p class="lead text-white mb-4">
                    Transform hours of video into minutes of insights with 
                    <span class="ai-processing-dots">AI-powered precision</span>
                </p>
            </div>
            <div class="col-md-6 text-center">
                <div class="video-frame-effect">
                    <img src="{{ url_for('static', filename='svg/ai_brain_icon.svg') }}" 
                         alt="AI Brain" class="img-fluid" style="max-width: 200px;">
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Feature Cards with SVG Icons -->
<div class="row">
    <div class="col-md-4 text-center mb-4">
        <div class="feature-icon glow-effect">
            <img src="{{ url_for('static', filename='svg/video_processing_icon.svg') }}" 
                 alt="Video Processing" style="width: 60px; height: 60px;">
        </div>
        <h5>AI Processing</h5>
        <p class="text-muted">Advanced video analysis with neural networks</p>
    </div>
    <div class="col-md-4 text-center mb-4">
        <div class="feature-icon success-sparkle">
            <img src="{{ url_for('static', filename='svg/sync_icon.svg') }}" 
                 alt="Synchronized Playback" style="width: 60px; height: 60px;">
        </div>
        <h5>Synchronized Playback</h5>
        <p class="text-muted">Side-by-side comparison with perfect timing</p>
    </div>
</div>

<!-- Data Stream Background for Processing Section -->
<div class="data-stream">
    <div class="container py-5">
        <!-- Processing content here -->
    </div>
</div>
"""
    
    return integration_code

def main():
    """Main function to generate all artwork"""
    print("🎨 VideoSense AI - Artwork Generation")
    print("=" * 50)
    
    # Generate and save all artwork assets
    prompts, css, svg = save_artwork_assets()
    
    # Generate integration code
    integration = generate_artwork_integration()
    
    with open("static/integration_guide.html", "w") as f:
        f.write(integration)
    
    print(f"\n📊 ARTWORK GENERATED:")
    print(f"   • {len(prompts)} Text-to-Image Prompts")
    print(f"   • {len(css.split('@keyframes'))-1} CSS Animations")
    print(f"   • {len(svg)} SVG Illustrations")
    print(f"   • Integration guide created")
    
    print(f"\n🎨 ARTWORK TYPES CREATED:")
    for key, prompt in prompts.items():
        print(f"   • {prompt['title']}")
    
    print(f"\n📁 FILES CREATED:")
    print(f"   • static/artwork_prompts.json - Text-to-image prompts")
    print(f"   • static/css/artwork.css - CSS animations and effects")
    print(f"   • static/svg/ - SVG illustrations")
    print(f"   • static/integration_guide.html - Integration examples")
    
    print(f"\n🌟 FEATURES INCLUDED:")
    print(f"   • Animated gradient backgrounds")
    print(f"   • AI processing animations")
    print(f"   • Neural network patterns")
    print(f"   • Glowing effects and sparkles")
    print(f"   • Data stream visualizations")
    print(f"   • Professional SVG icons")
    
    print(f"\n🎯 NEXT STEPS:")
    print(f"   1. Use the prompts in static/artwork_prompts.json with AI image generators")
    print(f"   2. Add the CSS file to your base template")
    print(f"   3. Use the SVG illustrations in your HTML")
    print(f"   4. Follow the integration guide for implementation")
    
    print(f"\n✨ Your VideoSense AI website will look amazing!")

if __name__ == "__main__":
    main()
