import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Javed AI Master Tool", page_icon="⚡", layout="wide")

# Automatically load API Key from Streamlit Secrets
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        api_connected = True
    else:
        api_connected = False
except Exception:
    api_connected = False

st.markdown("""
    <div style="background: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
        <div style="background: #eab308; color: #000; font-weight: bold; font-size: 24px; width: 50px; height: 50px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">J</div>
        <div>
            <h2 style="margin:0; color:#0284c7; font-size:22px;">JAVED AI MASTER TOOL</h2>
            <p style="margin:2px 0 0 0; color:#64748b; font-size:13px;">🟢 Gemini Secrets Connected Edition</p>
        </div>
    </div>
""", unsafe_allow_html=True)

if not api_connected:
    st.error("⚠️ براہ کرم Streamlit Settings -> Secrets میں اپنی GEMINI_API_KEY درج کریں!")
else:
    st.success("✅ Gemini API Key successfully connected from Secrets!")

# Session state initialization
if 'active_module' not in st.session_state:
    st.session_state.active_module = "HD Fiverr Image AI"

st.markdown("### 📌 SPECIALIZED MODULES")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎧 Fiverr Requirements"): st.session_state.active_module = "Fiverr Requirements"
    if st.button("📦 3D & Gaming Engine"): st.session_state.active_module = "3D & Gaming Engine"
with col2:
    if st.button("</> Web Design & Full App"): st.session_state.active_module = "Web Design & Full App"
    if st.button("🖼️ HD Fiverr Image AI"): st.session_state.active_module = "HD Fiverr Image AI"
with col3:
    if st.button("🐍 Python & AI Automations"): st.session_state.active_module = "Python & AI Automations"
    if st.button("🎬 360° Video & GIF AI"): st.session_state.active_module = "360° Video & GIF AI"

st.info(f"🎯 فعال ماڈیول: **{st.session_state.active_module}**")

user_input = st.text_area("PASTE PROMPT FROM GEMINI / CLIENT REQUIREMENTS:", placeholder="یہاں اپنی ریکوائرمنٹ لکھیں...", height=120)

if st.button("⚡ GENERATE MASTER DELIVERABLE"):
    if not api_connected:
        st.error("پہلے Secrets میں کی درج کریں!")
    elif not user_input:
        st.warning("براہ کرم کوئی پرامپٹ درج کریں۔")
    else:
        with st.spinner("🚀 جمنائی اے آئی پروسیس کر رہا ہے..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Act as an expert AI Master Developer. Module: {st.session_state.active_module}. User Request: {user_input}. Provide professional output/code.")
                
                tab_res, tab_prev = st.tabs(["</> Generated Code / Result", "👁️ Live Web Preview"])
                with tab_res:
                    st.write(response.text)
                with tab_prev:
                    if "html" in response.text.lower() or st.session_state.active_module == "Web Design & Full App":
                        st.components.v1.html(response.text, height=300, scrolling=True)
                    else:
                        st.info("👁️ رزلٹ پہلے ٹیب میں دستیاب ہے۔")
            except Exception as e:
                st.error(f"❌ خرابی پیش آئی: {e}")
