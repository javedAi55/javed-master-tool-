import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Javed AI Master Tool", page_icon="⚡", layout="wide")

# Custom Styling
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

# Top Header Banner
st.markdown("""
    <div class="main-header">
        <div class="avatar">J</div>
        <div>
            <h2 style="margin:0; color:#0284c7; font-size:22px;">JAVED AI MASTER TOOL</h2>
            <p style="margin:2px 0 0 0; color:#64748b; font-size:13px;">🟢 Gemini API Live Connected Edition</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar for API Key
with st.sidebar:
    st.header("⚙️ API & Engine Settings")
    user_api_key = st.text_input("Enter Gemini API Key:", type="password", placeholder="AIzaSy...")
    
    if user_api_key:
        genai.configure(api_key=user_api_key)
        st.success("API Key Active & Connected! ✅")
    else:
        st.warning("براہ کرم اپنی Gemini API Key یہاں درج کریں تاکہ ٹول لائیو کام کر سکے۔")

# Session state initialization
if 'active_module' not in st.session_state:
    st.session_state.active_module = "HD Fiverr Image AI"

st.markdown("### 📌 SPECIALIZED MODULES")

# Module Selection Buttons
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

st.info(f"🎯 فعال ماڈیول: **{st.session_state.active_module}**")

# Input Prompt Section
user_input = st.text_area("PASTE PROMPT FROM GEMINI / CLIENT REQUIREMENTS:", placeholder="یہاں اپنا حکم یا ریکوائرمنٹ لکھیں (مثلاً: شیر کی تصویر کا پرامپٹ بنائیں یا لاگ ان پیج کا کوڈ لکھیں)...", height=120)

# Generate Button
st.markdown('<div class="generate-btn">', unsafe_allow_html=True)
run_generation = st.button("⚡ GENERATE MASTER DELIVERABLE")
st.markdown('</div>', unsafe_allow_html=True)

# Output Execution with Gemini API
if run_generation:
    if not user_api_key:
        st.error("⚠️ پہلے سائیڈ بار میں اپنی Gemini API Key درج کریں!")
    elif not user_input:
        st.warning("⚠️ براہ کرم اوپر کوئی پرامپٹ یا تفصیل درج کریں۔")
    else:
        with st.spinner("🚀 جمنائی اے آئی (Gemini AI) پروسیس کر رہا ہے..."):
            try:
                # Call Gemini Model
                model = genai.GenerativeModel('gemini-1.5-flash')
                full_prompt = f"Act as an expert AI Master Developer. Module: {st.session_state.active_module}. User Request: {user_input}. Provide professional output/code/prompt accordingly."
                response = model.generate_content(full_prompt)
                
                tab_res, tab_prev = st.tabs(["</> Generated Code / Result", "👁️ Live Web Preview"])
                
                with tab_res:
                    st.write(response.text)
                    
                with tab_prev:
                    if "html" in response.text.lower() or st.session_state.active_module == "Web Design & Full App":
                        st.components.v1.html(response.text, height=300, scrolling=True)
                    else:
                        st.info("👁️ یہ ماڈیول رزلٹ اور کوڈ کے لیے آپٹمائزڈ ہے۔ آپ پہلا ٹیب دیکھ سکتے ہیں۔")
            except Exception as e:
                st.error(f"❌ خرابی پیش آئی: {e}")
