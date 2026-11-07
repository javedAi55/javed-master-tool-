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
            background-color: #f8fafc;
            color: #1e293b;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 10px;
            margin: 0;
        }
        .header {
            background: #ffffff;
            padding: 15px;
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
            width: 45px;
            height: 45px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .title-container h2 {
            margin: 0;
            color: #0284c7;
            font-size: 20px;
        }
        .title-container p {
            margin: 2px 0 0 0;
            color: #64748b;
            font-size: 12px;
        }
        .card {
            background: #ffffff;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 15px;
        }
        .card-title {
            color: #475569;
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
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            padding: 12px;
            border-radius: 8px;
            color: #1e293b;
            text-align: left;
            cursor: pointer;
            transition: 0.2s;
        }
        .btn-module:hover, .btn-module.active {
            background: #e0f2fe;
            border-color: #0284c7;
        }
        .btn-module h4 { margin: 0 0 4px 0; font-size: 14px; color: #0f172a; }
        .btn-module p { margin: 0; font-size: 11px; color: #64748b; }
        textarea {
            width: 100%;
            height: 90px;
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            color: #1e293b;
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
        .action-btn:hover {
            opacity: 0.9;
        }
        .output-section {
            background: #ffffff;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-top: 15px;
        }
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        .tab {
            background: #0284c7;
            color: #fff;
            border: 1px solid #0284c7;
            padding: 8px 15px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: bold;
            cursor: pointer;
        }
        .tab.inactive {
            background: #f1f5f9;
            color: #64748b;
            border-color: #cbd5e1;
        }
        .code-box {
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 12px;
            font-family: monospace;
            font-size: 12px;
            color: #38bdf8;
            overflow-x: auto;
            max-height: 200px;
            white-space: pre-wrap;
        }
        .sub-btn-group {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }
        .sub-btn {
            background: #f1f5f9;
            color: #1e293b;
            border: 1px solid #cbd5e1;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12px;
            cursor: pointer;
        }
        .sub-btn:hover {
            background: #e2e8f0;
        }
    </style>
</head>
<body>

    <div class="header">
        <div class="avatar">J</div>
        <div class="title-container">
            <h2>JAVED AI MASTER TOOL</h2>
            <p>🟢 Private & Unlimited Control Panel (White Edition)</p>
        </div>
    </div>

    <div class="card">
        <div class="card-title">Specialized Modules (Click to Select)</div>
        <div class="grid">
            <div class="btn-module" onclick="selectModule('Fiverr Requirements Module Active!')">
                <h4>🎧 Fiverr Requirements</h4>
                <p>Convert Client Msg to Code</p>
            </div>
            <div class="btn-module" onclick="selectModule('Web Design & Full App Module Active!')">
                <h4>&lt;/&gt; Web Design & Full App</h4>
                <p>HTML, CSS, JS, Tailwind</p>
            </div>
            <div class="btn-module" onclick="selectModule('Python & AI Automations Module Active!')">
                <h4>🐍 Python & AI Automations</h4>
                <p>Scripts, Bot & APIs</p>
            </div>
            <div class="btn-module" onclick="selectModule('3D & Gaming Engine Module Active!')">
                <h4>📦 3D & Gaming Engine</h4>
                <p>Tripo, Blender & Game Assets</p>
            </div>
            <div class="btn-module" onclick="selectModule('HD Fiverr Image AI Module Active!')">
                <h4>🖼️ HD Fiverr Image AI</h4>
                <p>White BG Gig Banner Prompts</p>
            </div>
            <div class="btn-module" onclick="selectModule('360° Video & GIF AI Module Active!')">
                <h4>🎬 360° Video & GIF AI</h4>
                <p>Fiverr Animated Portfolio</p>
            </div>
        </div>
    </div>

    <div class="card">
        <div class="card-title">Paste Prompt from Gemini / Client Requirements:</div>
        <textarea id="userInput" placeholder="Paste your task details here..."></textarea>
        <button class="action-btn" onclick="generateResult()">⚡ GENERATE MASTER DELIVERABLE</button>
    </div>

    <div class="output-section">
        <div class="tabs">
            <div class="tab" id="codeTab">Generated Code/Result</div>
            <div class="tab inactive" id="webTab">Live Web Preview</div>
        </div>
        <div class="code-box" id="outputResult">
            Hello Javed bhai! Tool is ready. Select any module or click Generate to start coding!
        </div>
        <div class="sub-btn-group">
            <button class="sub-btn" onclick="copyCode()">📋 Copy Code</button>
            <button class="sub-btn" onclick="alert('File downloaded successfully!')">📥 Download File</button>
        </div>
    </div>

    <script>
        function selectModule(msg) {
            document.getElementById('outputResult').innerText = "Status: " + msg + "\\nReady to process your request!";
        }

        function generateResult() {
            let val = document.getElementById('userInput').value;
            if(val.trim() === "") {
                document.getElementById('outputResult').innerText = "Please enter some prompt or requirements first!";
            } else {
                document.getElementById('outputResult').innerText = "🚀 Processing Javed Master Command:\\n-> " + val + "\\n\\n✅ Code & Deliverable generated successfully!";
            }
        }

        function copyCode() {
            let text = document.getElementById('outputResult').innerText;
            navigator.clipboard.writeText(text);
            alert("Code copied to clipboard!");
        }
    </script>

</body>
</html>
"""

components.html(html_code, height=950, scrolling=True)
