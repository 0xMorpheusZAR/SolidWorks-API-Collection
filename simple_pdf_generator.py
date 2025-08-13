#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple PDF Documentation Generator
=================================

Creates PDF documentation from Markdown files.
"""

import os
import sys
from pathlib import Path

def markdown_to_pdf(markdown_file, output_pdf, title=None):
    """Convert markdown file to professional PDF"""
    try:
        import markdown
        from weasyprint import HTML, CSS
        
        print(f"Converting {markdown_file} to PDF...")
        
        # Read markdown content
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert markdown to HTML
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
        html_content = md.convert(markdown_content)
        
        # Professional CSS styling
        css_styling = CSS(string='''
        @page {
            size: A4;
            margin: 2.5cm;
            @top-center {
                content: "Solprov Engineering (Pty) Ltd - Professional Documentation";
                font-family: Arial, sans-serif;
                font-size: 10pt;
                color: #666;
            }
            @bottom-center {
                content: "Page " counter(page);
                font-family: Arial, sans-serif;
                font-size: 10pt;
                color: #666;
            }
        }
        
        body {
            font-family: Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
        }
        
        h1 { color: #1f4e79; font-size: 24pt; margin-bottom: 1em; }
        h2 { color: #2f5f8f; font-size: 16pt; margin-top: 1.5em; }
        h3 { color: #365f91; font-size: 14pt; margin-top: 1.2em; }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        
        table, th, td {
            border: 1px solid #ddd;
        }
        
        th {
            background-color: #f8f9fa;
            padding: 10px 8px;
            font-weight: bold;
        }
        
        td {
            padding: 8px;
        }
        
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            font-family: 'Courier New', monospace;
        }
        
        pre {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            padding: 10px;
            margin: 1em 0;
        }
        ''')
        
        # Create complete HTML document
        html_document = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>{title or "Professional Documentation"}</title>
        </head>
        <body>
            <div style="text-align: center; color: #1f4e79; margin-bottom: 2em;">
                <h1>{title or "Professional Documentation"}</h1>
                <p><strong>Solprov Engineering (Pty) Ltd</strong><br>
                Professional Engineering Solutions<br>
                ISO 9001 Certified | August 2025</p>
            </div>
            {html_content}
        </body>
        </html>
        '''
        
        # Generate PDF
        html_doc = HTML(string=html_document)
        html_doc.write_pdf(output_pdf, stylesheets=[css_styling])
        
        print(f"Success: Created {output_pdf}")
        return True
        
    except Exception as e:
        print(f"Error converting {markdown_file}: {e}")
        return False

def main():
    print("=" * 50)
    print("PDF Documentation Generator")
    print("=" * 50)
    
    # Document mapping
    documents = [
        ('Comprehensive_Tank_Design_Deliverable.md', 'Complete_Professional_Tank_Design_Package.pdf', 'Complete Professional Tank Design Package'),
        ('Tank_Technical_Specifications.md', 'Tank_Technical_Specifications.pdf', 'Tank Technical Specifications'),
        ('Tank_Design_Analysis_Report.md', 'Tank_Design_Analysis_Report.pdf', 'Tank Design Analysis Report'),
        ('Tank_Safety_Compliance_Checklist.md', 'Tank_Safety_Compliance_Checklist.pdf', 'Tank Safety Compliance Checklist'),
        ('README.md', 'SolidWorks_API_Collection_Overview.pdf', 'SolidWorks API Collection Overview'),
        ('DEPLOYMENT_SUMMARY.md', 'SuperClaude_Deployment_Summary.pdf', 'SuperClaude Multi-Persona Optimization Summary')
    ]
    
    # Create PDFs directory
    pdf_dir = Path('Professional_PDF_Documentation')
    pdf_dir.mkdir(exist_ok=True)
    
    successful = 0
    total = len(documents)
    
    for markdown_file, pdf_filename, title in documents:
        if os.path.exists(markdown_file):
            output_path = pdf_dir / pdf_filename
            if markdown_to_pdf(markdown_file, str(output_path), title):
                successful += 1
        else:
            print(f"File not found: {markdown_file}")
    
    print(f"\nConversion Summary: {successful}/{total} files converted successfully")
    print(f"PDF files created in: {pdf_dir.absolute()}")
    
    return successful == total

if __name__ == "__main__":
    success = main()
    if success:
        print("\nPDF documentation package ready!")
    else:
        print("\nSome PDFs could not be created.")