"""
CreatorOS AI Master Tool for Freelance Digital Creators
Single-file production-ready Streamlit Application
Modules:
  1. Fiverr Client SOW & Proposal Architect
  2. Full Web Studio (HTML/CSS/JS) with Sandbox Live Preview
  3. 3D & Gaming Asset Director (Prompts, PBR Specs & Blender bpy Scripts)
  4. Freelance Python Automation Lab
  5. 360° Panoramic & Turntable Video/GIF Engine
"""

import streamlit as st
import streamlit.components.v1 as components
import requests
import json
import os
import re

# ==========================================
# PAGE CONFIGURATION & CLEAN WHITE UI THEME
# ==========================================
st.set_page_config(
    page_title="CreatorOS | AI Master Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_WHITE_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #1e293b;
    }

    /* Main Background & Clean Whitespace */
    .stApp {
        background-color: #fafbfc;
    }

    /* Top Bar Header Area */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.02);
    }
    
    /* Studio Cards */
    .card {
        background-color: #ffffff;
        border: 1px solid #e8ecf1;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
    }

    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .card-subtitle {
        font-size: 0.88rem;
        color: #64748b;
        margin-bottom: 16px;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 10px 22px;
        font-weight: 600;
        font-size: 0.92rem;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.12);
        width: 100%;
    }
    .stButton>button:hover {
        background: #334155;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
        color: #ffffff;
    }

    /* Input & Textarea Elements */
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea, 
    .stSelectbox>div>div {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        color: #0f172a !important;
        font-size: 0.92rem !important;
    }
    .stTextInput>div>div>input:focus, 
    .stTextArea>div>div>textarea:focus {
        border-color: #0f172a !important;
        box-shadow: 0 0 0 1px #0f172a !important;
    }

    /* Badges & Indicators */
    .badge {
        display: inline-block;
        padding: 4px 10px;
        background-color: #f1f5f9;
        border: 1px solid #e2e8f0;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .badge-primary {
        background-color: #eff6ff;
        border-color: #dbeafe;
        color: #1d4ed8;
    }

    /* Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: 600;
        color: #64748b;
    }
    .stTabs [aria-selected="true"] {
        background-color: #f8fafc;
        color: #0f172a;
    }
</style>
"""
st.markdown(CUSTOM_WHITE_CSS, unsafe_allow_html=True)


# ==========================================
# GEMINI API CLIENT (DIRECT REST INTERFACE)
# ==========================================
def call_gemini(api_key: str, model: str, prompt: str, system_prompt: str = "", temperature: float = 0.7) -> str:
    """Direct, robust Gemini API caller using standard HTTP requests without SDK mismatch issues."""
    if not api_key:
        return "⚠️ Error: Please provide a Gemini API Key in the sidebar to run this module."

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key.strip()}"
    headers = {"Content-Type": "application/json"}
    
    contents = []
    if system_prompt:
        contents.append({
            "role": "user",
            "parts": [{"text": f"[SYSTEM INSTRUCTION]:\n{system_prompt}\n\n[USER REQUEST]:\n{prompt}"}]
        })
    else:
        contents.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })

    payload = {
        "contents": contents,
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": 4096,
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        data = response.json()
        
        if response.status_code != 200:
            error_msg = data.get("error", {}).get("message", "Unknown API error occurred.")
            return f"❌ Gemini API Error ({response.status_code}): {error_msg}"
        
        candidates = data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts:
                return parts[0].get("text", "")
        return "⚠️ Received an empty response from Gemini API."
    except requests.exceptions.Timeout:
        return "❌ Request timed out. Please try again with a smaller prompt."
    except requests.exceptions.RequestException as e:
        return f"❌ Connection Error: {str(e)}"


def extract_html_code(raw_text: str) -> str:
    """Extracts raw HTML/CSS/JS code from Markdown code fences if present."""
    html_match = re.search(r"```html\s*(.*?)\s*```", raw_text, re.DOTALL | re.IGNORECASE)
    if html_match:
        return html_match.group(1).strip()
    generic_match = re.search(r"```\s*(.*?)\s*```", raw_text, re.DOTALL)
    if generic_match and "<!DOCTYPE" in generic_match.group(1).upper() or "<html" in generic_match.group(1).lower():
        return generic_match.group(1).strip()
    return raw_text.strip()


# ==========================================
# SIDEBAR CONTROLS
# ==========================================
with st.sidebar:
    st.markdown("""
        <div style="padding: 10px 0 20px 0;">
            <div class="badge badge-primary">Freelance Studio v2.4</div>
            <h2 style="margin: 6px 0 0 0; font-size: 1.5rem; font-weight: 800; color: #0f172a;">CreatorOS</h2>
            <p style="font-size: 0.85rem; color: #64748b; margin-top: 4px;">Advanced AI Toolkit for Digital Creators</p>
        </div>
    """, unsafe_allow_html=True)

    # API Configuration
    st.markdown("### 🔑 API Configuration")
    env_key = os.environ.get("GEMINI_API_KEY", "")
    api_key_input = st.text_input(
        "Gemini API Key",
        value=env_key,
        type="password",
        placeholder="AIzaSy...",
        help="Paste your Gemini API key from Google AI Studio. It can also be loaded automatically via GEMINI_API_KEY environment variable."
    )

    model_selected = st.selectbox(
        "Active Model",
        options=["gemini-1.5-flash", "gemini-2.0-flash", "gemini-2.5-pro"],
        index=0,
        help="Flash is optimized for high-speed generation; Pro is recommended for complex code & long proposals."
    )

    st.markdown("---")
    st.markdown("### 🧭 Workspace Modules")
    selected_module = st.radio(
        "Navigation",
        options=[
            "📁 Fiverr Client & Proposal Suite",
            "🌐 Web Design Studio (Live Preview)",
            "🎮 3D & Gaming Asset Director",
            "⚡ Python Automation Lab",
            "🔄 360° Video & Looping GIF Studio"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
        <div style="font-size: 0.78rem; color: #94a3b8; line-height: 1.4;">
            💡 <b>Pro Tip:</b> For HTML prototypes, click 'Render Live Sandbox' to inspect interactive elements directly.
        </div>
    """, unsafe_allow_html=True)


# =========================================================
# MODULE 1: FIVERR CLIENT & PROPOSAL ARCHITECT
# =========================================================
if selected_module == "📁 Fiverr Client & Proposal Suite":
    st.markdown("""
        <div class="card">
            <div class="card-title">📁 Fiverr Requirements Analyzer & Scope Architect</div>
            <div class="card-subtitle">Transform messy client messages into crystal-clear Deliverables, Milestone Contracts, SOW breakdowns, and winning custom offer pitches.</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("#### 📥 Client Input")
        client_raw_text = st.textarea(
            "Raw Client Message or Project Brief",
            height=200,
            placeholder="e.g. 'Hey, I need a modern landing page for my fitness brand with animations and a calculator, but I only have 4 days and $250. Also need it connected to Mailchimp...'"
        )

        niche = st.selectbox(
            "Gig Category",
            ["Full-Stack Web & Landing Pages", "3D Modeling & Game Assets", "Python Automation & Scraping", "Video Editing / Motion Graphics / VFX", "Digital Brand Identity"]
        )

        col_b1, col_b2 = st.columns(2)
        with col_b1:
            pricing_tier = st.selectbox("Pricing Strategy", ["Premium ($$$ High-ticket)", "Competitive Standard", "Aggressive Win (Entry Tier)"])
        with col_b2:
            delivery_timeline = st.text_input("Target Turnaround", value="3 Days")

        analyze_btn = st.button("🚀 Generate Proposal & SOW Architecture")

    with col2:
        st.markdown("#### 📋 Structured Proposal Output")
        if analyze_btn:
            if not client_raw_text.strip():
                st.warning("Please provide client messages or brief details first.")
            else:
                with st.spinner("Analyzing scope creep, drafting milestones, and formatting proposal..."):
                    sys_prompt = (
                        "You are a top-rated Fiverr Pro and Upwork Expert Freelance Agency Consultant. "
                        "Given an unstructured client brief, generate: "
                        "1. Scope of Work (SOW) Deliverables (Categorized & bulleted).\n"
                        "2. Ambiguity & Scope-Creep Warnings (Flag what's missing, risks, or unrealistic).\n"
                        "3. Clarifying Questions (3-5 targeted questions that establish elite authority).\n"
                        "4. Recommended 3-Tier Milestone Breakdown (Basic, Standard, Premium).\n"
                        "5. A high-converting, friendly, conversion-optimized Fiverr Custom Offer Message (ready to copy-paste)."
                    )
                    prompt = f"""
                    Client Category: {niche}
                    Pricing Strategy: {pricing_tier}
                    Target Delivery: {delivery_timeline}
                    
                    Raw Client Message / Brief:
                    {client_raw_text}
                    """
                    response = call_gemini(api_key_input, model_selected, prompt, sys_prompt, temperature=0.6)
                    st.markdown(response)
                    st.download_button("💾 Download SOW Document (.md)", response, file_name="fiverr_sow_proposal.md")
        else:
            st.info("Fill out client brief parameters on the left and click Generate.")


# =========================================================
# MODULE 2: WEB DESIGN STUDIO (HTML/CSS/JS + LIVE PREVIEW)
# =========================================================
elif selected_module == "🌐 Web Design Studio (Live Preview)":
    st.markdown("""
        <div class="card">
            <div class="card-title">🌐 Full-Stack HTML/CSS/JS Studio & Live Sandbox</div>
            <div class="card-subtitle">Generate responsive, production-ready single-file websites with embedded interactive JavaScript and preview them immediately.</div>
        </div>
    """, unsafe_allow_html=True)

    col_input, col_view = st.columns([1, 1], gap="large")

    with col_input:
        site_brief = st.text_area(
            "Website Concept & Deliverables",
            height=140,
            placeholder="e.g. Modern dark/light toggle SaaS landing page for an AI audio enhancer with interactive pricing slider, hero with floating badge, and feature comparison grid."
        )

        col_w1, col_w2 = st.columns(2)
        with col_w1:
            design_aesthetic = st.selectbox(
                "Visual Style",
                ["Ultra-Clean Modern White / Minimalist", "SaaS Tech Slate & Indigo", "Luxury Monochromatic / High-End", "Vibrant Cyberpunk / Neon Glassmorphism"]
            )
        with col_w2:
            interactive_features = st.multiselect(
                "Interactive Elements",
                ["Filterable Gallery", "Interactive Pricing Calculator", "Testimonial Carousel", "Dark/Light Toggle", "Modal Popups", "Animated SVG Shapes"],
                default=["Interactive Pricing Calculator"]
            )

        generate_web_btn = st.button("⚡ Generate Complete Web Code")

    # Session State for Code Storage
    if "web_code" not in st.session_state:
        st.session_state.web_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CreatorOS Preview</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #ffffff;
            color: #0f172a;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 85vh;
            margin: 0;
            text-align: center;
        }
        .box {
            padding: 40px;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            max-width: 480px;
        }
        h1 { font-size: 1.5rem; margin-bottom: 8px; }
        p { color: #64748b; font-size: 0.95rem; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Sandbox Preview Window</h1>
        <p>Configure your site requirements on the left panel and click 'Generate Complete Web Code' to view your live interactive prototype here.</p>
    </div>
</body>
</html>"""

    if generate_web_btn:
        if not site_brief.strip():
            st.warning("Please provide a website concept description.")
        else:
            with st.spinner("Writing HTML5, CSS3, and JavaScript..."):
                sys_prompt = (
                    "You are a World-Class Frontend Engineer and UI/UX Designer. "
                    "Generate a single-file, self-contained, responsive, clean HTML page containing all styles within `<style>` and all interactive logic within `<script>`. "
                    "Include modern semantic tags, accessible responsive layouts (Flexbox/CSS Grid), modern typography, and smooth transitions. "
                    "Do NOT use external broken CDN dependencies for core layouts. Return ONLY the complete HTML code block inside ```html ... ```."
                )
                prompt = f"""
                Site Purpose: {site_brief}
                Design Theme: {design_aesthetic}
                Required Interactive Features: {', '.join(interactive_features)}
                Requirements:
                - Self-contained single file (HTML + embedded CSS + embedded Vanilla JS).
                - Responsive on mobile & desktop.
                - Beautiful typography, soft shadows, rounded corners, modern button states.
                - Complete real copy (no placeholder lorem ipsum).
                """
                raw_res = call_gemini(api_key_input, model_selected, prompt, sys_prompt, temperature=0.7)
                extracted_code = extract_html_code(raw_res)
                st.session_state.web_code = extracted_code

    with col_view:
        tab_preview, tab_code = st.tabs(["🖥️ Live Interactive Sandbox", "📝 Source Code"])
        
        with tab_preview:
            st.markdown('<div class="badge badge-primary" style="margin-bottom: 8px;">Sandbox View (100% Isolated iframe)</div>', unsafe_allow_html=True)
            components.html(st.session_state.web_code, height=520, scrolling=True)

        with tab_code:
            st.text_area("HTML / CSS / JS Code", value=st.session_state.web_code, height=450)
            st.download_button(
                "⬇️ Download index.html",
                st.session_state.web_code,
                file_name="index.html",
                mime="text/html"
            )


# =========================================================
# MODULE 3: 3D & GAMING ASSET DIRECTOR
# =========================================================
elif selected_module == "🎮 3D & Gaming Asset Director":
    st.markdown("""
        <div class="card">
            <div class="card-title">🎮 3D Asset, PBR Map & Blender Automation Director</div>
            <div class="card-subtitle">Generate hyper-detailed generative 3D prompts (Meshy, Trellis, Midjourney Turntables), PBR channel specs, and executable Blender Python (`bpy`) setup scripts.</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        asset_concept = st.text_input("Asset Concept", placeholder="e.g. Cyberpunk Relic Container with holographic glyphs")
        
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            target_engine = st.selectbox("Target Pipeline", ["Unreal Engine 5 (Nanite/Lumen)", "Unity URP/HDRP", "Blender Studio Cycles", "Web/Three.js (GLTF/GLB)"])
            poly_budget = st.selectbox("Poly Budget & Topology", ["Low-Poly Game Asset (<5k tris)", "Mid-Poly Subdivision Ready (15k-30k tris)", "High-Poly Cinematic Sculpt"])
        with col_g2:
            art_style = st.selectbox("Art Style", ["Hyper-Realistic PBR Photoreal", "Stylized Overwatch/Fortnite Hand-Painted", "Sci-Fi Hard Surface Industrial", "Dark Fantasy Souls-like"])
            texture_res = st.selectbox("Texture Resolution", ["4K (Cinematic)", "2K (Standard Game)", "1K (Mobile/Web Optimized)"])

        include_blender_script = st.checkbox("Generate Blender Python (`bpy`) automation script for base geometry and turntable cameras", value=True)
        gen_3d_btn = st.button("🚀 Architect 3D Production Blueprint")

    with col2:
        st.markdown("#### 📦 Generated 3D Technical Specs")
        if gen_3d_btn:
            if not asset_concept.strip():
                st.warning("Please provide an asset concept.")
            else:
                with st.spinner("Generating 3D prompts, PBR configurations, and Blender automation code..."):
                    sys_prompt = (
                        "You are a Lead 3D Technical Artist & Game Art Director. "
                        "When given a 3D asset concept, provide: "
                        "1. AI 3D Generation Prompts for Meshy AI / Trellis / Midjourney 3D Turntable (isolated white background, orthographic multi-angle tags).\n"
                        "2. PBR Material & Texture Map Blueprint (Albedo/BaseColor, Normal (OpenGL/DirectX), Roughness, Metallic, Ambient Occlusion, Emission parameters).\n"
                        "3. Complete Topology & UV Mapping Guidance.\n"
                        "4. If requested, a fully functional Blender Python (`bpy`) script that creates a procedural base mesh or turntable studio lighting setup."
                    )
                    prompt = f"""
                    Asset: {asset_concept}
                    Target Engine: {target_engine}
                    Poly Budget: {poly_budget}
                    Art Direction: {art_style}
                    Texture Resolution: {texture_res}
                    Generate Blender Python Script: {include_blender_script}
                    """
                    response = call_gemini(api_key_input, model_selected, prompt, sys_prompt, temperature=0.6)
                    st.markdown(response)
                    st.download_button("💾 Save 3D Asset Spec (.md)", response, file_name=f"{asset_concept[:15].lower().replace(' ', '_')}_spec.md")
        else:
            st.info("Define your 3D asset parameters to generate production blueprints and Blender code.")


# =========================================================
# MODULE 4: PYTHON AUTOMATION LAB
# =========================================================
elif selected_module == "⚡ Python Automation Lab":
    st.markdown("""
        <div class="card">
            <div class="card-title">⚡ Freelance Python Automation & Script Lab</div>
            <div class="card-subtitle">Generate robust, error-handled Python scripts for clients: scrapers, bulk media processors, API connectors, CSV/Excel pipelines, and bot utilities.</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        auto_title = st.text_input("Task Name", placeholder="e.g. Scrape real estate listings to clean Excel sheets")
        auto_description = st.text_area(
            "Detailed Requirements & Edge Cases",
            height=140,
            placeholder="e.g. Scrape listing title, price, address from a target URL, clean numerical prices, handle rate limiting with randomized delay, export to formatted Excel with timestamped filenames."
        )

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            script_framework = st.selectbox(
                "Primary Library Focus",
                ["BeautifulSoup4 / Requests", "Playwright / Headless Browser", "Pandas / OpenPyXL Data Pipeline", "Pillow / OpenCV Media Batcher", "FastAPI / Lightweight Webhook API"]
            )
        with col_p2:
            code_quality = st.selectbox(
                "Code Rigor",
                ["Production Grade (Logging, CLI Args, Type Hints, Try/Except)", "Concise Utility Script"]
            )

        gen_code_btn = st.button("⚡ Build Complete Automation Script")

    with col2:
        st.markdown("#### 🐍 Production Python Code")
        if gen_code_btn:
            if not auto_description.strip():
                st.warning("Please describe the automation requirements.")
            else:
                with st.spinner("Writing robust Python automation code..."):
                    sys_prompt = (
                        "You are a Senior Python Automation Engineer. "
                        "Write clean, modular, highly readable, production-grade Python scripts with comprehensive docstrings, type hinting, "
                        "proper exception handling, logging, and defensive error checks. "
                        "Include a requirements.txt block and explicit CLI execution instructions."
                    )
                    prompt = f"""
                    Automation Task: {auto_title}
                    Specific Requirements: {auto_description}
                    Preferred Framework: {script_framework}
                    Target Grade: {code_quality}
                    """
                    response = call_gemini(api_key_input, model_selected, prompt, sys_prompt, temperature=0.4)
                    st.markdown(response)
                    st.download_button("💾 Download Python Script (.py)", response, file_name="automation_tool.py")
        else:
            st.info("Input automation requirements on the left to generate clean Python scripts.")


# =========================================================
# MODULE 5: 360° VIDEO & LOOPING GIF GENERATOR
# =========================================================
elif selected_module == "🔄 360° Video & Looping GIF Studio":
    st.markdown("""
        <div class="card">
            <div class="card-title">🔄 360° Panoramic & Turntable Looping GIF Engine</div>
            <div class="card-subtitle">Generate prompt matrices for VR 360° equirectangular panoramas, flawless turntable looping GIFs, and cinematic camera trajectory prompts for Runway Gen-3, Luma Dream Machine, and Sora.</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        scene_concept = st.text_area(
            "Subject or Panoramic Environment",
            height=120,
            placeholder="e.g. Isometric floating futuristic Japanese bonsai garden, water droplets suspended, morning mist, 360 degree smooth rotation."
        )

        col_v1, col_v2 = st.columns(2)
        with col_v1:
            gen_type = st.selectbox(
                "Format Type",
                [
                    "360° Seamless Equirectangular VR Panorama (2:1)",
                    "3D Asset 360° Turntable (Isolated Looping GIF)",
                    "Cinematic Camera Orbit (Runway / Luma / Sora)",
                    "Infinite Seamless Ambient Cinemagraph Loop"
                ]
            )
            camera_motion = st.selectbox(
                "Camera Trajectory",
                ["360° Continuous Yaw Orbit", "Static Equirectangular 360° Sphere", "Slow Spiral Crane In", "Dolly Zoom (Vertigo Effect)"]
            )
        with col_v2:
            target_ai = st.selectbox(
                "Target AI Video/Image Model",
                ["Midjourney v6 / SDXL (360 Panorama Mode)", "Runway Gen-3 Alpha", "Luma Dream Machine", "OpenAI Sora / Kling AI"]
            )
            lighting_mood = st.selectbox(
                "Lighting & Color Grading",
                ["Studio Softbox Pure Rim Lighting", "Golden Hour Cinematic Haze", "Cyberpunk Volumetric Neon", "Moody Moody Rembrandt Studio"]
            )

        gen_video_btn = st.button("🎥 Generate Prompt Matrix & FFmpeg Loop Commands")

    with col2:
        st.markdown("#### 🎬 Prompt Matrix & Loop Engineering")
        if gen_video_btn:
            if not scene_concept.strip():
                st.warning("Please describe the scene or subject.")
            else:
                with st.spinner("Engineering 360° prompts, trajectory matrices, and loop commands..."):
                    sys_prompt = (
                        "You are an Elite Generative AI Video & 360/VR Technical Specialist. "
                        "When given a concept, output: "
                        "1. Exact Positive Master Prompt tailored for the target engine (including camera aspect ratio, lens millimeter, shutter angle, motion descriptors).\n"
                        "2. Negative Prompt (crucial to prevent seam tearing in 360° panoramas or stuttering in looping turntables).\n"
                        "3. Motion Setting Parameters (Motion strength, camera motion speed values).\n"
                        "4. FFmpeg Command snippet to convert generated MP4 video outputs into an ultra-smooth, lightweight looping GIF or WebP."
                    )
                    prompt = f"""
                    Scene Concept: {scene_concept}
                    Format: {gen_type}
                    Target AI Tool: {target_ai}
                    Camera Motion: {camera_motion}
                    Lighting Mood: {lighting_mood}
                    """
                    response = call_gemini(api_key_input, model_selected, prompt, sys_prompt, temperature=0.7)
                    st.markdown(response)
                    st.download_button("💾 Download Video Prompt Spec (.txt)", response, file_name="video_360_prompt_recipe.txt")
        else:
            st.info("Select motion, format, and environment parameters on the left to generate video/GIF blueprints.")


# ==========================================
# FOOTER
# ==========================================
st.markdown("""
    <div style="margin-top: 50px; padding: 20px 0; border-top: 1px solid #e2e8f0; text-align: center; color: #94a3b8; font-size: 0.85rem;">
        CreatorOS Studio • Built for Freelancers, Technical Artists & Developers • Native Streamlit Architecture
    </div>
""", unsafe_allow_html=True)
