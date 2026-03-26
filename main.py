from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="DevOps Assignment")


TERMINAL_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Assignment — Prashasst Dongre</title>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #0a0a0f;
            font-family: 'Fira Code', monospace;
            overflow: hidden;
        }

        /* Animated grid background */
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(0, 255, 136, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 136, 0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            animation: gridMove 20s linear infinite;
        }

        @keyframes gridMove {
            0% { transform: translate(0, 0); }
            100% { transform: translate(40px, 40px); }
        }

        .container {
            position: relative;
            z-index: 1;
            width: 90%;
            max-width: 780px;
        }

        /* Terminal window */
        .terminal {
            background: #0d1117;
            border-radius: 12px;
            border: 1px solid #21262d;
            box-shadow:
                0 0 40px rgba(0, 255, 136, 0.08),
                0 20px 60px rgba(0, 0, 0, 0.5);
            overflow: hidden;
            animation: fadeUp 0.8s ease-out;
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(30px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        /* Title bar */
        .title-bar {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 12px 16px;
            background: #161b22;
            border-bottom: 1px solid #21262d;
        }

        .dot { width: 12px; height: 12px; border-radius: 50%; }
        .dot.red   { background: #ff5f56; }
        .dot.yel   { background: #ffbd2e; }
        .dot.grn   { background: #27c93f; }

        .title-bar span {
            flex: 1;
            text-align: center;
            color: #484f58;
            font-size: 13px;
        }

        /* Terminal body */
        .body {
            padding: 24px;
            color: #c9d1d9;
            font-size: 14px;
            line-height: 1.9;
        }

        .prompt {
            color: #00ff88;
            text-shadow: 0 0 8px rgba(0, 255, 136, 0.4);
        }

        .comment { color: #484f58; }

        .cmd {
            color: #58a6ff;
        }

        .flag { color: #d2a8ff; }
        .string { color: #a5d6ff; }
        .highlight {
            color: #00ff88;
            font-weight: 600;
            text-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
        }
        .warn { color: #ffbd2e; }
        .info { color: #58a6ff; }

        .line {
            opacity: 0;
            animation: typeLine 0.4s ease forwards;
        }

        .line:nth-child(1)  { animation-delay: 0.2s; }
        .line:nth-child(2)  { animation-delay: 0.5s; }
        .line:nth-child(3)  { animation-delay: 0.8s; }
        .line:nth-child(4)  { animation-delay: 1.0s; }
        .line:nth-child(5)  { animation-delay: 1.3s; }
        .line:nth-child(6)  { animation-delay: 1.5s; }
        .line:nth-child(7)  { animation-delay: 1.7s; }
        .line:nth-child(8)  { animation-delay: 1.9s; }
        .line:nth-child(9)  { animation-delay: 2.1s; }
        .line:nth-child(10) { animation-delay: 2.3s; }
        .line:nth-child(11) { animation-delay: 2.5s; }
        .line:nth-child(12) { animation-delay: 2.7s; }
        .line:nth-child(13) { animation-delay: 2.9s; }
        .line:nth-child(14) { animation-delay: 3.1s; }
        .line:nth-child(15) { animation-delay: 3.3s; }
        .line:nth-child(16) { animation-delay: 3.5s; }
        .line:nth-child(17) { animation-delay: 3.7s; }

        @keyframes typeLine {
            from { opacity: 0; transform: translateX(-8px); }
            to   { opacity: 1; transform: translateX(0); }
        }

        /* Blinking cursor on last line */
        .cursor::after {
            content: '█';
            color: #00ff88;
            animation: blink 1s step-end infinite;
        }

        @keyframes blink {
            50% { opacity: 0; }
        }

        .separator {
            border: none;
            border-top: 1px dashed #21262d;
            margin: 8px 0;
        }

        /* Floating badge */
        .badge {
            margin-top: 16px;
            text-align: center;
            color: #484f58;
            font-size: 12px;
            animation: fadeUp 0.8s ease-out 3.8s both;
        }
        .badge a {
            color: #58a6ff;
            text-decoration: none;
        }

        /* Glowing orbs */
        .orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.12;
            pointer-events: none;
        }
        .orb-1 { width: 300px; height: 300px; background: #00ff88; top: -80px;  left: -60px; }
        .orb-2 { width: 250px; height: 250px; background: #58a6ff; bottom: -60px; right: -40px; }
    </style>
</head>
<body>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>

    <div class="container">
        <div class="terminal">
            <div class="title-bar">
                <div class="dot red"></div>
                <div class="dot yel"></div>
                <div class="dot grn"></div>
                <span>devops-assignment — bash</span>
            </div>
            <div class="body">
                <div class="line"><span class="comment"># ──────────────────────────────────────────</span></div>
                <div class="line"><span class="comment">#  DevOps Assignment Submission</span></div>
                <div class="line"><span class="comment"># ──────────────────────────────────────────</span></div>
                <div class="line">&nbsp;</div>

                <div class="line"><span class="prompt">$ </span><span class="cmd">echo</span> <span class="string">"Submitted by"</span></div>
                <div class="line"><span class="highlight">→ Prashasst Dongre</span></div>
                <div class="line">&nbsp;</div>

                <div class="line"><span class="prompt">$ </span><span class="cmd">cat</span> <span class="flag">/etc/student.conf</span></div>
                <div class="line"><span class="warn">ENROLLMENT</span>=<span class="string">"0201AI221053"</span></div>
                <div class="line"><span class="warn">SEMESTER</span>=<span class="string">"8th Sem"</span></div>
                <div class="line"><span class="warn">BRANCH</span>=<span class="string">"Artificial Intelligence and Data Science"</span></div>
                <div class="line">&nbsp;</div>

                <div class="line"><hr class="separator"></div>

                <div class="line"><span class="prompt">$ </span><span class="cmd">docker</span> <span class="flag">run</span> <span class="string">--rm devops-assignment</span></div>
                <div class="line"><span class="info">[✓]</span> FastAPI server running on port <span class="highlight">8000</span></div>
                <div class="line"><span class="info">[✓]</span> All tests passed</div>
                <div class="line"><span class="info">[✓]</span> CI/CD pipeline <span class="highlight">active</span></div>
                <div class="line cursor"><span class="prompt">$ </span></div>
            </div>
        </div>
        <div class="badge">
            Powered by <a href="https://fastapi.tiangolo.com" target="_blank">FastAPI</a> ·
            Containerized with <a href="https://docker.com" target="_blank">Docker</a> ·
            CI/CD via <a href="https://github.com/features/actions" target="_blank">GitHub Actions</a>
        </div>
    </div>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the terminal-style landing page."""
    return TERMINAL_HTML


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}
