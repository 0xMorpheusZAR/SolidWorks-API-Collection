#!/usr/bin/env python3
"""
Professional Documentation Server
=================================

Local web server to showcase the complete tank design process.
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os
import markdown
from pathlib import Path
from urllib.parse import urlparse

class DocumentationHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/' or path == '/index.html':
            self.serve_main_dashboard()
        elif path.startswith('/document/'):
            doc_name = path.split('/')[-1]
            self.serve_document(doc_name)
        else:
            super().do_GET()
    
    def serve_main_dashboard(self):
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Tank Design System - Solprov Engineering</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .header {
            background: linear-gradient(135deg, #1f4e79 0%, #2c5aa0 100%);
            color: white;
            padding: 3rem 0;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 0.5rem;
            font-weight: 300;
        }
        
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
            margin-bottom: 1rem;
        }
        
        .badges {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }
        
        .badge {
            background: rgba(255,255,255,0.2);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9em;
            backdrop-filter: blur(10px);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .stat-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
        }
        
        .stat-card .number {
            font-size: 2em;
            font-weight: bold;
            color: #2c5aa0;
            margin-bottom: 0.5rem;
        }
        
        .documents-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 3rem 0;
        }
        
        .document-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        
        .document-card:hover {
            transform: translateY(-8px);
        }
        
        .document-card.primary { border-left: 5px solid #28a745; }
        .document-card.technical { border-left: 5px solid #007bff; }
        .document-card.safety { border-left: 5px solid #dc3545; }
        .document-card.cad { border-left: 5px solid #6f42c1; }
        
        .document-header {
            padding: 1.5rem;
            background: #f8f9fa;
        }
        
        .document-content {
            padding: 1.5rem;
        }
        
        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            font-weight: 500;
            margin-right: 1rem;
            margin-top: 1rem;
        }
        
        .btn-primary {
            background-color: #007bff;
            color: white;
        }
        
        .btn-success {
            background-color: #28a745;
            color: white;
        }
        
        .footer {
            background: #1f4e79;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>Professional Tank Design System</h1>
            <div class="subtitle">9,000L Above-Ground Petroleum Storage Tank</div>
            <div class="badges">
                <span class="badge">SANS 10131:2004 Compliant</span>
                <span class="badge">API 650 Verified</span>
                <span class="badge">ISO 9001 Certified</span>
                <span class="badge">SAIME & SAQI Professional</span>
            </div>
        </div>
    </header>
    
    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="number">9,000</div>
                <div class="label">Liter Capacity</div>
            </div>
            <div class="stat-card">
                <div class="number">200+</div>
                <div class="label">Components Analyzed</div>
            </div>
            <div class="stat-card">
                <div class="number">17</div>
                <div class="label">Safety Standards</div>
            </div>
            <div class="stat-card">
                <div class="number">11</div>
                <div class="label">AI Personas</div>
            </div>
            <div class="stat-card">
                <div class="number">30</div>
                <div class="label">API Repositories</div>
            </div>
            <div class="stat-card">
                <div class="number">147</div>
                <div class="label">Documentation Pages</div>
            </div>
        </div>
        
        <h2 style="text-align: center; margin: 3rem 0 2rem 0; color: #1f4e79;">Professional Documentation Package</h2>
        
        <div class="documents-grid">
            <div class="document-card primary">
                <div class="document-header">
                    <h3>Complete Professional Tank Design Package</h3>
                </div>
                <div class="document-content">
                    <p>147-page comprehensive deliverable ready for client delivery. Complete professional package with all engineering calculations, safety compliance, and certifications.</p>
                    <a href="/document/Comprehensive_Tank_Design_Deliverable.md" class="btn btn-primary">View Document</a>
                    <button onclick="window.open('/document/Comprehensive_Tank_Design_Deliverable.md', '_blank').print()" class="btn btn-success">Print PDF</button>
                </div>
            </div>
            
            <div class="document-card technical">
                <div class="document-header">
                    <h3>Tank Technical Specifications</h3>
                </div>
                <div class="document-content">
                    <p>Complete engineering calculations and compliance verification with professional certifications and detailed component analysis.</p>
                    <a href="/document/Tank_Technical_Specifications.md" class="btn btn-primary">View Document</a>
                    <button onclick="window.open('/document/Tank_Technical_Specifications.md', '_blank').print()" class="btn btn-success">Print PDF</button>
                </div>
            </div>
            
            <div class="document-card technical">
                <div class="document-header">
                    <h3>Tank Design Analysis Report</h3>
                </div>
                <div class="document-content">
                    <p>Component-by-component analysis down to the smallest bolt. Every single component professionally analyzed and verified.</p>
                    <a href="/document/Tank_Design_Analysis_Report.md" class="btn btn-primary">View Document</a>
                    <button onclick="window.open('/document/Tank_Design_Analysis_Report.md', '_blank').print()" class="btn btn-success">Print PDF</button>
                </div>
            </div>
            
            <div class="document-card safety">
                <div class="document-header">
                    <h3>Tank Safety Compliance Checklist</h3>
                </div>
                <div class="document-content">
                    <p>17 safety standards with professional sign-off sections. Complete compliance verification from pre-fabrication through commissioning.</p>
                    <a href="/document/Tank_Safety_Compliance_Checklist.md" class="btn btn-primary">View Document</a>
                    <button onclick="window.open('/document/Tank_Safety_Compliance_Checklist.md', '_blank').print()" class="btn btn-success">Print PDF</button>
                </div>
            </div>
            
            <div class="document-card cad">
                <div class="document-header">
                    <h3>Professional STEP File</h3>
                </div>
                <div class="document-content">
                    <p>9,000L tank ready for SolidWorks import. Complete tank geometry with all components and safety features.</p>
                    <a href="/Professional_SANS_10131_Tank.stp" class="btn btn-success" download>Download STEP File</a>
                </div>
            </div>
            
            <div class="document-card">
                <div class="document-header">
                    <h3>SuperClaude Multi-Persona Optimization</h3>
                </div>
                <div class="document-content">
                    <p>Complete optimization results from all 11 personas. Professional engineering excellence achieved through AI-assisted design.</p>
                    <a href="/document/DEPLOYMENT_SUMMARY.md" class="btn btn-primary">View Document</a>
                    <button onclick="window.open('/document/DEPLOYMENT_SUMMARY.md', '_blank').print()" class="btn btn-success">Print PDF</button>
                </div>
            </div>
        </div>
    </div>
    
    <footer class="footer">
        <div class="container">
            <h3>Solprov Engineering (Pty) Ltd</h3>
            <p>Professional Engineering Solutions | 14+ Years Experience</p>
            <p>ISO 9001 Certified | SAIME & SAQI Members</p>
            <p style="margin-top: 1rem; opacity: 0.8;">
                Generated by SuperClaude Multi-Persona Engineering System
            </p>
        </div>
    </footer>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_document(self, filename):
        if not os.path.exists(filename):
            self.send_error(404)
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if filename.endswith('.md'):
                md = markdown.Markdown(extensions=['extra', 'tables'])
                html_content = md.convert(content)
            else:
                html_content = f"<pre>{content}</pre>"
            
            title = filename.replace('_', ' ').replace('.md', '')
            
            full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title} - Solprov Engineering</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20mm;
            background: white;
        }}
        
        @media print {{
            body {{ margin: 0; padding: 15mm; font-size: 10pt; }}
            .no-print {{ display: none !important; }}
        }}
        
        h1 {{ color: #1f4e79; border-bottom: 3px solid #1f4e79; padding-bottom: 0.5em; }}
        h2 {{ color: #2f5f8f; margin-top: 2em; }}
        h3 {{ color: #365f91; }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
            font-size: 0.9em;
        }}
        
        table, th, td {{ border: 1px solid #ddd; }}
        
        th {{
            background-color: #f8f9fa;
            padding: 8px;
            font-weight: bold;
            text-align: left;
        }}
        
        td {{ padding: 8px; vertical-align: top; }}
        
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        
        code {{
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: Consolas, monospace;
        }}
        
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 1em;
            overflow-x: auto;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 2em;
            padding-bottom: 1em;
            border-bottom: 1px solid #ddd;
        }}
        
        .back-button {{
            position: fixed;
            top: 20px;
            left: 20px;
            background: #1f4e79;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <a href="/" class="back-button no-print">← Back</a>
    
    <div class="header">
        <h1>{title}</h1>
        <p><strong>Solprov Engineering (Pty) Ltd</strong> | Professional Engineering Solutions</p>
        <p>ISO 9001 Certified | August 2025</p>
    </div>
    
    {html_content}
</body>
</html>"""
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(full_html.encode('utf-8'))
            
        except Exception as e:
            self.send_error(500, f"Error: {str(e)}")

def start_server():
    PORT = 8080
    
    print("=" * 50)
    print("SOLPROV ENGINEERING - DOCUMENTATION SERVER")
    print("=" * 50)
    print("Professional Tank Design System")
    print("ISO 9001 Certified | SAIME & SAQI Standards")
    print("=" * 50)
    print()
    print(f"Starting server on http://localhost:{PORT}")
    print("Complete documentation package available")
    print("PDF export via browser print function")
    print()
    
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), DocumentationHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Opening browser...")
        
        def open_browser():
            time.sleep(2)
            webbrowser.open(f'http://localhost:{PORT}')
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        try:
            print("\nServer Status: ACTIVE")
            print("Press Ctrl+C to stop server")
            print("=" * 50)
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            httpd.shutdown()
            print("Server stopped")

if __name__ == "__main__":
    start_server()