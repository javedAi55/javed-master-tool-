import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Javed AI Master Tool", page_icon="⚡", layout="wide")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Javed AI Master Tool</title>
    <style>
        body {
            background-color: #0b0f19;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 10px;
            margin: 0;
        }
        .header {
            background: #141b2d;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #1e293b;
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
            width: 45px;
            height: 45px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .title-container h2 {
            margin: 0;
            color: #38bdf8;
            font-size: 20px;
        }
        .title-container p {
            margin: 2px 0 0 0;
            color: #94a3b8;
            font-size: 12px;
        }
        .card {
            background: #141b2d;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #1e293b;
            margin-bottom: 15px;
        }
        .card-title {
            color: #94a3b8;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
        }
        .btn-module {
            background: #1e293b;
            border: 1px solid #334155;
            padding: 12px;
            border-radius: 8px;
            color: #fff;
            text-align: left;
            cursor: pointer;
        }
        .btn-module:hover {
            border-color: #eab308;
        }
        .btn-module h4 { margin: 0 0 4px 0; font-size: 14px; color: #f8fafc; }
        .btn-module p { margin: 0; font-size: 11px; color: #64748b; }
        textarea {
            width: 100%;
            height: 90px;
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 8px;
            color: #fff;
            padding: 10px;
            box-sizing: border-box;
            font-size: 13px;
        }
        .action-btn {
            background: linear-gradient(90deg, #f59e0b, #d97706);
            color: #000;
            font-weight: bold;
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 8px;
            font-size: 15px;
            cursor: pointer;
            margin-top: 10px;
        }
        /* Result & Output Box Styles */
        .output-section {
            background: #141b2d;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #1e293b;
            margin-top: 15px;
        }
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        .tab {
            background: #1e293b;
            color: #f59e0b;
            border: 1px solid #f59e0b;
            padding: 8px 15px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: bold;
            cursor: pointer;
        }
        .tab.inactive {
            background: #0f172a;
            color: #94a3b8;
            border-color: #334155;
        }
        .code-box {
            background: #090d16;
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 12px;
            font-family: monospace;
            font-size: 12px;
            color: #38bdf8;
            overflow-x: auto;
            max-height: 200px;
        }
        .sub-btn-group {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }
        .sub-btn {
            background: #1e293b;
            color: #fff;
            border: 1px solid #334155;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div class="header">
        <div class="avatar">J</div>
        <div class="title-container">
            <h2>JAVED AI MASTER TOOL</h2>
            <p>🟢 Private & Unlimited Control Panel</p>
        </div>
    </div>

    <div class="card">
        <div class="card-title">Specialized Modules</div>
        <div class="grid">
            <div class="btn-module">
                <h4>🎧 Fiverr Requirements</h4>
                <p>Convert Client Msg to Code</p>
            </div>
            <div class="btn-module">
                <h4>&lt;/&gt; Web Design & Full App</h4>
                <p>HTML, CSS, JS, Tailwind</p>
            </div>
            <div class="btn-module">
                <h4>🐍 Python & AI Automations</h4>
                <p>Scripts, Bot & APIs</p>
            </div>
            <div class="btn-module">
                <h4>📦 3D & Gaming Engine</h4>
                <p>Tripo, Blender & Game Assets</p>
            </div>
            <div class="btn-module">
                <h4>🖼️ HD Fiverr Image AI</h4>
                <p>White BG Gig Banner Prompts</p>
            </div>
            <div class="btn-module">
                <h4>🎬 360° Video & GIF AI</h4>
                <p>Fiverr Animated Portfolio</p>
            </div>
        </div>
    </div>

    <div class="card">
        <div class="card-title">Paste Prompt from Gemini / Client Requirements:</div>
        <textarea placeholder="Paste your task details here..."></textarea>
        <button class="action-btn">⚡ GENERATE MASTER DELIVERABLE</button>
    </div>

    <div class="output-section">
        <div class="tabs">
            <div class="tab">&lt;/&gt; Generated Code/Result</div>
            <div class="tab inactive">👁️ Live Web Preview</div>
        </div>
        <div class="code-box">
            Hello! I am **Javed's Ultimate AI Master Tool**.<br>
            Ready to generate Web Apps, Python Scripts, 3D Assets, and Fiverr HD Banners!
        </div>
        <div class="sub-btn-group">
            <button class="sub-btn">📋 Copy Code</button>
            <button class="sub-btn">📥 Download File</button>
        </div>
    </div>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
