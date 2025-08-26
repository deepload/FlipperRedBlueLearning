#!/usr/bin/env python3
"""
Simple PDF Generator for Red Team & Blue Team Guide
"""

import os
import markdown
from weasyprint import HTML, CSS
from datetime import datetime

def generate_professional_pdf():
    """Generate a professional PDF from the markdown guide"""
    
    print("🚀 Starting PDF generation...")
    
    # Read the markdown file
    input_file = "red_team_blue_team_guide.md"
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("📖 Processing markdown content...")
    
    # Add professional title page
    title_page = f"""
# Red Team & Blue Team Guide
## Flipper Zero Security Testing & Car Security Exploits

**A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing**

*Publication Date: {datetime.now().strftime('%B %Y')}*

---

## Copyright and Legal Notice

© 2024 Security Research Publications. All rights reserved.

**IMPORTANT LEGAL DISCLAIMER:**
This guide is intended for educational and authorized security testing purposes only. The techniques described should only be used on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal and may result in criminal prosecution.

---

"""
    
    # Combine title page with content
    full_content = title_page + content
    
    # Convert markdown to HTML
    print("🔄 Converting to HTML...")
    html_content = markdown.markdown(
        full_content,
        extensions=['codehilite', 'tables', 'toc', 'fenced_code', 'extra']
    )
    
    # Professional CSS styling
    css_styles = """
    @page {
        size: A4;
        margin: 2cm;
        @top-center {
            content: "Red Team & Blue Team Guide - Flipper Zero Security Testing";
            font-size: 9pt;
            color: #666;
        }
        @bottom-center {
            content: "Page " counter(page);
            font-size: 9pt;
            color: #666;
        }
    }
    
    body {
        font-family: 'Georgia', 'Times New Roman', serif;
        line-height: 1.6;
        color: #333;
        font-size: 11pt;
    }
    
    h1 {
        color: #2c3e50;
        font-size: 22pt;
        font-weight: bold;
        margin-top: 30pt;
        margin-bottom: 20pt;
        page-break-before: always;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10pt;
    }
    
    h2 {
        color: #34495e;
        font-size: 16pt;
        font-weight: bold;
        margin-top: 25pt;
        margin-bottom: 15pt;
        border-bottom: 1px solid #bdc3c7;
        padding-bottom: 5pt;
    }
    
    h3 {
        color: #2c3e50;
        font-size: 14pt;
        font-weight: bold;
        margin-top: 20pt;
        margin-bottom: 10pt;
    }
    
    h4 {
        color: #34495e;
        font-size: 12pt;
        font-weight: bold;
        margin-top: 15pt;
        margin-bottom: 8pt;
    }
    
    code {
        background-color: #f8f9fa;
        padding: 2pt 4pt;
        border-radius: 3pt;
        font-family: 'Courier New', monospace;
        font-size: 9pt;
        color: #e74c3c;
        border: 1px solid #e9ecef;
    }
    
    pre {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 15pt;
        border-radius: 5pt;
        font-family: 'Courier New', monospace;
        font-size: 9pt;
        line-height: 1.4;
        overflow-x: auto;
        margin: 15pt 0;
        border: 1px solid #34495e;
    }
    
    pre code {
        background: none;
        color: #ecf0f1;
        border: none;
        padding: 0;
    }
    
    blockquote {
        background-color: #f39c12;
        color: white;
        padding: 10pt 15pt;
        border-left: 5pt solid #e67e22;
        margin: 15pt 0;
        border-radius: 0 5pt 5pt 0;
        font-weight: bold;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15pt 0;
        font-size: 10pt;
    }
    
    th, td {
        border: 1pt solid #bdc3c7;
        padding: 8pt;
        text-align: left;
    }
    
    th {
        background-color: #34495e;
        color: white;
        font-weight: bold;
    }
    
    tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    
    strong {
        color: #2c3e50;
        font-weight: bold;
    }
    
    em {
        color: #7f8c8d;
        font-style: italic;
    }
    
    ul, ol {
        margin: 10pt 0;
        padding-left: 20pt;
    }
    
    li {
        margin: 5pt 0;
    }
    
    .highlight {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 3pt;
        padding: 10pt;
        margin: 10pt 0;
    }
    
    .warning {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 3pt;
        padding: 10pt;
        margin: 10pt 0;
        color: #721c24;
    }
    
    .info {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 3pt;
        padding: 10pt;
        margin: 10pt 0;
        color: #0c5460;
    }
    """
    
    # Create full HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Red Team & Blue Team Guide - Flipper Zero Security Testing</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    # Generate PDF
    print("📄 Generating PDF...")
    try:
        css = CSS(string=css_styles)
        pdf_path = "output/Red_Team_Blue_Team_Guide_Professional.pdf"
        HTML(string=full_html).write_pdf(pdf_path, stylesheets=[css])
        
        print(f"✅ PDF generated successfully: {pdf_path}")
        
        # Get file size
        file_size = os.path.getsize(pdf_path) / (1024 * 1024)  # MB
        print(f"📊 File size: {file_size:.2f} MB")
        
        return pdf_path
        
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return None

if __name__ == "__main__":
    generate_professional_pdf()
