#!/usr/bin/env python3
"""
Professional Tank Design Documentation System
============================================

Solprov Engineering (Pty) Ltd - Main entry point for Replit deployment
Hosts the complete professional tank design process documentation.
"""

import http.server
import socketserver
import os
import markdown
from pathlib import Path
from urllib.parse import urlparse

class ProfessionalDocumentationHandler(http.server.SimpleHTTPRequestHandler):
    """Professional documentation handler for Replit deployment"""
    
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
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
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
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
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
        
        .stat-card .icon {
            font-size: 2em;
            margin-bottom: 0.5rem;
            color: #1f4e79;
        }
        
        .stat-card .number {
            font-size: 2em;
            font-weight: bold;
            color: #2c5aa0;
            margin-bottom: 0.5rem;
        }
        
        .stat-card .label {
            color: #666;
            font-size: 0.9em;
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
        .document-card.reference { border-left: 5px solid #fd7e14; }
        
        .document-header {
            padding: 1.5rem;
            background: #f8f9fa;
            border-bottom: 1px solid #dee2e6;
        }
        
        .document-header .icon {
            font-size: 1.5em;
            margin-bottom: 0.5rem;
        }
        
        .document-header h3 {
            color: #1f4e79;
            margin-bottom: 0.5rem;
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
            transition: all 0.3s ease;
        }
        
        .btn-primary {
            background-color: #007bff;
            color: white;
        }
        
        .btn-primary:hover {
            background-color: #0056b3;
        }
        
        .btn-success {
            background-color: #28a745;
            color: white;
        }
        
        .btn-success:hover {
            background-color: #1e7e34;
        }
        
        .footer {
            background: #1f4e79;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }
        
        .hero-section {
            text-align: center;
            background: white;
            padding: 3rem 2rem;
            margin: 2rem 0;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .hero-section h2 {
            color: #1f4e79;
            margin-bottom: 1rem;
            font-size: 2em;
        }
        
        .hero-section p {
            font-size: 1.1em;
            color: #666;
            margin-bottom: 2rem;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .highlight {
            background: linear-gradient(135deg, #28a745, #20c997);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
        }
        
        @media (max-width: 768px) {
            .header h1 { font-size: 2em; }
            .stats { grid-template-columns: repeat(2, 1fr); }
            .documents-grid { grid-template-columns: 1fr; }
            .container { padding: 1rem; }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <h1><i class="fas fa-industry"></i> Professional Tank Design System</h1>
            <div class="subtitle">9,000L Above-Ground Petroleum Storage Tank</div>
            <div class="badges">
                <span class="badge"><i class="fas fa-check-circle"></i> SANS 10131:2004 Compliant</span>
                <span class="badge"><i class="fas fa-shield-alt"></i> API 650 Verified</span>
                <span class="badge"><i class="fas fa-certificate"></i> ISO 9001 Certified</span>
                <span class="badge"><i class="fas fa-user-tie"></i> SAIME & SAQI Professional</span>
            </div>
        </div>
    </header>
    
    <div class="container">
        <div class="hero-section">
            <h2><i class="fas fa-rocket"></i> SuperClaude Multi-Persona Engineering Excellence</h2>
            <p>Experience the future of professional engineering with our revolutionary <span class="highlight">11-persona AI system</span> combined with <span class="highlight">14+ years of professional experience</span> from Solprov Engineering (Pty) Ltd. This complete tank design system demonstrates the perfect fusion of artificial intelligence and human engineering expertise.</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="icon"><i class="fas fa-oil-can"></i></div>
                <div class="number">9,000</div>
                <div class="label">Liter Capacity</div>
            </div>
            <div class="stat-card">
                <div class="icon"><i class="fas fa-cogs"></i></div>
                <div class="number">200+</div>
                <div class="label">Components</div>
            </div>
            <div class="stat-card">
                <div class="icon"><i class="fas fa-shield-alt"></i></div>
                <div class="number">17</div>
                <div class="label">Safety Standards</div>
            </div>
            <div class="stat-card">
                <div class="icon"><i class="fas fa-robot"></i></div>
                <div class="number">11</div>
                <div class="label">AI Personas</div>
            </div>
            <div class="stat-card">
                <div class="icon"><i class="fas fa-code"></i></div>
                <div class="number">30</div>
                <div class="label">API Repositories</div>
            </div>
            <div class="stat-card">
                <div class="icon"><i class="fas fa-file-alt"></i></div>
                <div class="number">147</div>
                <div class="label">Doc Pages</div>
            </div>
        </div>
        
        <h2 style="text-align: center; margin: 3rem 0 2rem 0; color: #1f4e79;">
            <i class="fas fa-folder-open"></i> Professional Documentation Package
        </h2>
        
        <div class="documents-grid">
            <div class="document-card primary">
                <div class="document-header">
                    <div class="icon"><i class="fas fa-industry"></i></div>
                    <h3>Complete Professional Deliverable</h3>
                </div>
                <div class="document-content">
                    <p><strong>147-page comprehensive package</strong> ready for client delivery. Complete professional deliverable with all engineering calculations, safety compliance, and certifications required for manufacturing.</p>
                    <a href="/document/Comprehensive_Tank_Design_Deliverable.md" class="btn btn-primary">
                        <i class="fas fa-eye"></i> View Document
                    </a>
                    <button onclick="printDoc('Comprehensive_Tank_Design_Deliverable.md')" class="btn btn-success">
                        <i class="fas fa-print"></i> Print PDF
                    </button>
                </div>
            </div>
            
            <div class="document-card technical">
                <div class="document-header">
                    <div class="icon"><i class="fas fa-calculator"></i></div>
                    <h3>Technical Specifications</h3>
                </div>
                <div class="document-content">
                    <p><strong>Complete engineering calculations</strong> and compliance verification with professional certifications. Every calculation verified and documented to professional standards.</p>
                    <a href="/document/Tank_Technical_Specifications.md" class="btn btn-primary">
                        <i class="fas fa-eye"></i> View Document
                    </a>
                    <button onclick="printDoc('Tank_Technical_Specifications.md')" class="btn btn-success">
                        <i class="fas fa-print"></i> Print PDF
                    </button>
                </div>
            </div>
            
            <div class="document-card technical">
                <div class="document-header">
                    <div class="icon"><i class="fas fa-search"></i></div>
                    <h3>Design Analysis Report</h3>
                </div>
                <div class="document-content">
                    <p><strong>Component-by-component analysis</strong> down to the smallest bolt. Every single tank component professionally analyzed and verified for safety and compliance.</p>
                    <a href="/document/Tank_Design_Analysis_Report.md" class="btn btn-primary">
                        <i class="fas fa-eye"></i> View Document
                    </a>
                    <button onclick="printDoc('Tank_Design_Analysis_Report.md')" class="btn btn-success">
                        <i class="fas fa-print"></i> Print PDF
                    </button>
                </div>
            </div>
            
            <div class="document-card safety">
                <div class="document-header">
                    <div class="icon"><i class="fas fa-clipboard-check"></i></div>
                    <h3>Safety Compliance Checklist</h3>
                </div>
                <div class="document-content">
                    <p><strong>17 safety standards</strong> with professional sign-off sections. Complete compliance verification from pre-fabrication through commissioning.</p>
                    <a href="/document/Tank_Safety_Compliance_Checklist.md" class="btn btn-primary">
                        <i class="fas fa-eye"></i> View Document
                    </a>
                    <button onclick="printDoc('Tank_Safety_Compliance_Checklist.md')" class="btn btn-success">
                        <i class="fas fa-print"></i> Print PDF
                    </button>
                </div>
            </div>
            
            <div class="document-card cad">
                <div class="document-header">
                    <div class="icon"><i class="fas fa-cube"></i></div>
                    <h3>Professional STEP File</h3>
                </div>
                <div class="document-content">
                    <p><strong>9,000L tank ready for SolidWorks import.</strong> Complete 3D model with all components and safety features. Professional CAD file for immediate use.</p>
                    <a href="/Professional_SANS_10131_Tank.stp" class="btn btn-success" download>
                        <i class="fas fa-download"></i> Download STEP File
                    </a>
                </div>
            </div>
            
            <div class="document-card reference">
                <div class="document-header">
                    <div class="icon"><i class="fas fa-rocket"></i></div>
                    <h3>Multi-Persona Optimization</h3>
                </div>
                <div class="document-content">
                    <p><strong>Complete optimization results</strong> from all 11 AI personas. Revolutionary engineering process demonstrating AI-assisted professional design excellence.</p>
                    <a href="/document/DEPLOYMENT_SUMMARY.md" class="btn btn-primary">
                        <i class="fas fa-eye"></i> View Document
                    </a>
                    <button onclick="printDoc('DEPLOYMENT_SUMMARY.md')" class="btn btn-success">
                        <i class="fas fa-print"></i> Print PDF
                    </button>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin: 3rem 0; padding: 2rem; background: white; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <h3 style="color: #1f4e79; margin-bottom: 1rem;"><i class="fas fa-info-circle"></i> Professional Engineering Standards</h3>
            <p style="margin-bottom: 1rem;">This complete tank design system represents the highest level of professional engineering excellence, combining cutting-edge AI technology with proven engineering expertise.</p>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 2rem;">
                <div><i class="fas fa-check" style="color: #28a745;"></i> ISO 9001 Certified Quality</div>
                <div><i class="fas fa-check" style="color: #28a745;"></i> SAIME Professional Standards</div>
                <div><i class="fas fa-check" style="color: #28a745;"></i> SAQI Quality Assurance</div>
                <div><i class="fas fa-check" style="color: #28a745;"></i> 14+ Years Experience</div>
            </div>
        </div>
    </div>
    
    <footer class="footer">
        <div class="container">
            <h3><i class="fas fa-building"></i> Solprov Engineering (Pty) Ltd</h3>
            <p>Professional Engineering Solutions | 14+ Years Experience</p>
            <p>ISO 9001 Certified | SAIME & SAQI Members</p>
            <p style="margin-top: 1rem; opacity: 0.8;">
                <i class="fas fa-robot"></i> Generated by SuperClaude Multi-Persona Engineering System
            </p>
        </div>
    </footer>
    
    <script>
        function printDoc(filename) {
            const printWindow = window.open('/document/' + filename, '_blank');
            printWindow.addEventListener('load', function() {
                setTimeout(() => {
                    printWindow.print();
                }, 1000);
            });
        }
    </script>
</body>
</html>"""
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_document(self, filename):
        if not os.path.exists(filename):
            self.send_error(404, f"Document not found: {filename}")
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if filename.endswith('.md'):
                md = markdown.Markdown(extensions=['extra', 'tables', 'toc'])
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
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
        
        h1 {{ 
            color: #1f4e79; 
            border-bottom: 3px solid #1f4e79; 
            padding-bottom: 0.5em;
            font-size: 2em;
        }}
        
        h2 {{ 
            color: #2f5f8f; 
            margin-top: 2em; 
            font-size: 1.5em;
        }}
        
        h3 {{ 
            color: #365f91; 
            font-size: 1.3em;
        }}
        
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
            color: #1f4e79;
        }}
        
        td {{ 
            padding: 8px; 
            vertical-align: top; 
        }}
        
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        
        code {{
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
        }}
        
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 1em;
            overflow-x: auto;
            margin: 1em 0;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 2em;
            padding-bottom: 1em;
            border-bottom: 2px solid #1f4e79;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            padding: 2em;
            border-radius: 10px;
            margin-bottom: 3em;
        }}
        
        .back-button {{
            position: fixed;
            top: 20px;
            left: 20px;
            background: #1f4e79;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 25px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            z-index: 1000;
            transition: all 0.3s ease;
        }}
        
        .back-button:hover {{
            background: #2c5aa0;
            transform: translateY(-2px);
        }}
        
        ul, ol {{
            margin: 1em 0;
            padding-left: 2em;
        }}
        
        li {{
            margin: 0.5em 0;
        }}
        
        blockquote {{
            border-left: 4px solid #1f4e79;
            padding-left: 1em;
            margin: 1em 0;
            color: #555;
            font-style: italic;
        }}
        
        .highlight {{
            background: #fff3cd;
            padding: 0.25em 0.5em;
            border-radius: 3px;
        }}
        
        .success {{ color: #28a745; font-weight: bold; }}
        .warning {{ color: #ffc107; font-weight: bold; }}
        .error {{ color: #dc3545; font-weight: bold; }}
    </style>
</head>
<body>
    <a href="/" class="back-button no-print">
        <i class="fas fa-arrow-left"></i> Back to Dashboard
    </a>
    
    <div class="header">
        <h1><i class="fas fa-file-alt"></i> {title}</h1>
        <p><strong><i class="fas fa-building"></i> Solprov Engineering (Pty) Ltd</strong> | Professional Engineering Solutions</p>
        <p><i class="fas fa-certificate"></i> ISO 9001 Certified | <i class="fas fa-calendar"></i> Generated: August 2025</p>
    </div>
    
    <div style="margin-top: 2em;">
        {html_content}
    </div>
    
    <div style="text-align: center; margin-top: 3em; padding-top: 2em; border-top: 1px solid #ddd; color: #666;">
        <p><i class="fas fa-robot"></i> Generated by SuperClaude Multi-Persona Engineering System</p>
        <p><i class="fas fa-shield-alt"></i> Professional Engineering Standards | <i class="fas fa-check-circle"></i> Quality Assured</p>
    </div>
</body>
</html>"""
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(full_html.encode('utf-8'))
            
        except Exception as e:
            self.send_error(500, f"Error reading document: {str(e)}")

def main():
    """Main entry point for Replit deployment"""
    PORT = int(os.environ.get('PORT', 8080))
    
    print("=" * 60)
    print("SOLPROV ENGINEERING - PROFESSIONAL DOCUMENTATION SYSTEM")
    print("=" * 60)
    print("Professional Tank Design System")
    print("ISO 9001 Certified | SAIME & SAQI Professional Standards")
    print("SuperClaude Multi-Persona Engineering Excellence")
    print("=" * 60)
    print()
    print(f"Starting server on port {PORT}")
    print("Complete professional documentation package available")
    print("Ready for client delivery and professional review")
    print()
    
    # Ensure we're in the correct directory
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), ProfessionalDocumentationHandler) as httpd:
        print(f"Server running on port {PORT}")
        print("Documentation system deployed successfully")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            httpd.shutdown()

if __name__ == "__main__":
    main()