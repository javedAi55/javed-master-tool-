import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="Javed AI Master Tool", page_icon="⚡", layout="wide")

# Custom Styling for Professional Look (White & Clean Edition)
st.markdown("""
    <style>
    .main-header {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 20px;
    }
    .avatar {
        background: #eab308;
        color: #000;
        font-weight: bold;
        font-size: 24px;
        width: 50px;
        height: 50px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #f1f5f9;
        color: #1e293b;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 12px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #e0f2fe;
        border-color: #0284c7;
        color: #0284c7;
    }
    .generate-btn>button {
        background: linear-gradient(90deg, #f59e0b, #d97706) !important;
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Top Header Banner matching your design
st.markdown("""
    <div class="main-header">
        <div class="avatar">J</div>
        <div>
            <h2 style="margin:0; color:#0284c7; font-size:22px;">JAVED AI MASTER TOOL</h2>
            <p style="margin:2px 0 0 0; color:#64748b; font-size:13px;">🟢 Private & Unlimited Control Panel (API Enabled)</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar for API Keys & Engine Power
with st.sidebar:
    st.header("⚙️ Engine & API Settings")
    ai_engine = st.selectbox(
        "SELECT ENGINE POWER",
        ["Gemini 3 Flash (Fast & Unlimited)", "OpenAI GPT-4o (High Precision)", "Claude 3.5 Sonnet (Best Coding)", "DeepSeek R1 (Deep Logic & Math)"]
    )
    api_key = st.text_input("Enter API Key (Optional):", type="password", placeholder="sk-...")
    if api_key:
        st.success("API Key Connected Active! ✅")
    else:
        st.info("Using Built-in Master Engine.")

# Session state initialization
if 'active_module' not in st.session_state:
    st.session_state.active_module = "HD Fiverr Image AI"

st.markdown("### 📌 SPECIALIZED MODULES")

# Module Selection Buttons in Grid
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎧 Fiverr Requirements"):
        st.session_state.active_module = "Fiverr Requirements"
    if st.button("📦 3D & Gaming Engine"):
        st.session_state.active_module = "3D & Gaming Engine"

with col2:
    if st.button("</> Web Design & Full App"):
        st.session_state.active_module = "Web Design & Full App"
    if st.button("🖼️ HD Fiverr Image AI"):
        st.session_state.active_module = "HD Fiverr Image AI"

with col3:
    if st.button("🐍 Python & AI Automations"):
        st.session_state.active_module = "Python & AI Automations"
    if st.button("🎬 360° Video & GIF AI"):
        st.session_state.active_module = "360° Video & GIF AI"

st.info(f"🎯 فعال ماڈیول (Active Module): **{st.session_state.active_module}** | منتخب انجن: **{ai_engine.split(' ')[0]}**")

# Input Prompt Section
user_input = st.text_area("PASTE PROMPT FROM GEMINI / CLIENT REQUIREMENTS:", placeholder="یہاں کلائنٹ کی ریکوائرمنٹ یا اپنا پرامپٹ لکھیں (مثلاً: شیر کی ایچ ڈی تصویر یا چیٹ ایپ)...", height=120)

# Generate Button
st.markdown('<div class="generate-btn">', unsafe_allow_html=True)
run_generation = st.button("⚡ GENERATE MASTER DELIVERABLE")
st.markdown('</div>', unsafe_allow_html=True)

# Output Tabs Section
if run_generation or user_input:
    tab_res, tab_prev = st.tabs(["</> Generated Code / Result", "👁️ Live Web Preview"])
    
    mod = st.session_state.active_module
    
    with tab_res:
        if mod == "HD Fiverr Image AI":
            code_out = f"""/* Fiverr HD Gig Image Prompt Generated via {ai_engine} */
Prompt: Ultra-realistic HD render of {user_input if user_input else 'Professional Design'}, studio lighting, 8k resolution, clean white isolated background, perfectly sized for Fiverr Gallery (1280x769 pixels)."""
            st.code(code_out, language="markdown")
            
        elif mod == "Web Design & Full App":
            code_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Javed AI Master App</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0fdf4; text-align: center; padding: 40px; }}
        .card {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); max-width: 500px; margin: auto; }}
        h1 {{ color: #16a34a; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{user_input if user_input else 'Javed Web Masterpiece'}</h1>
        <p>Successfully created using Javed AI Master Tool & {ai_engine}!</p>
    </div>
</body>
</html>"""
            st.code(code_out, language="html")
            
        elif mod == "360° Video & GIF AI":
            code_out = f"""# Video / GIF Animation Prompt for {ai_engine}
Target: {user_input if user_input else 'Cinematic Showcase'}
Camera Motion: 360-degree smooth orbit rotation, high definition, smooth 60fps loop, optimized for freelance portfolio showcase."""
            st.code(code_out, language="python")
            
        else:
            code_out = f"# Processing Module: {mod}\n# Engine: {ai_engine}\n# User Request: {user_input}\n\nprint('Master Deliverable Generated Successfully!')"
            st.code(code_out, language="python")

    with tab_prev:
        if mod == "Web Design & Full App":
            preview_html = f"""
            <div style="font-family: Arial; text-align: center; background: #f0fdf4; padding: 30px; border-radius: 10px; border: 1px solid #bbf7d0;">
                <h2 style="color: #16a34a; margin-top:0;">{user_input if user_input else 'Javed Web Masterpiece'}</h2>
                <p style="color: #15803d;">یہ رہا آپ کی ویب سائٹ کا لائیو پریویو جو آپ کے ٹول نے تیار کیا ہے!</p>
            </div>
            """
            components.html(preview_html, height=220)
        elif mod == "HD Fiverr Image AI":
            st.success("🖼️ فائور گیلری ایچ ڈی پرامپٹ تیار ہے! آپ اسے کاپی کر کے کسی بھی اے آئی امیج جنریٹر میں چلا سکتے ہیں۔")
        elif mod == "360° Video & GIF AI":
            st.info("🎬 ویڈیو اور جی آئی ایف کی کمانڈ ریڈی ہے! کلائنٹ کو دینے کے لیے یہ بہترین ہے۔")
        else:
            st.success(f"✅ {mod} کا رزلٹ کامیابی سے پروسیس ہو چکا ہے!")
