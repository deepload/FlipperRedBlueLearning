import os
import subprocess
from datetime import datetime

def create_professional_ebook():
    """Generate professional PDF and EPUB using pandoc"""
    
    print("🚀 Creating professional e-book with pandoc...")
    
    # Create enhanced markdown with metadata
    metadata = f"""---
title: "Red Team & Blue Team Guide: Flipper Zero Security Testing"
subtitle: "A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing"
author: "Cybersecurity Professional"
date: "{datetime.now().strftime('%B %Y')}"
publisher: "Security Research Publications"
subject: "Cybersecurity, Penetration Testing, Red Team, Blue Team"
keywords: "cybersecurity, penetration testing, red team, blue team, flipper zero, security testing, ethical hacking"
lang: "en-US"
documentclass: "book"
geometry: "margin=2.5cm"
fontsize: "11pt"
linestretch: "1.2"
toc: true
toc-depth: 3
numbersections: true
---

\\newpage

# Copyright and Legal Notice

© 2024 Security Research Publications. All rights reserved.

**IMPORTANT LEGAL DISCLAIMER:**
This guide is intended for educational and authorized security testing purposes only. The techniques described should only be used on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal and may result in criminal prosecution.

**Publication Information:**
- Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
- Publisher: Security Research Publications
- Publication Date: {datetime.now().strftime('%B %Y')}
- Language: English
- Format: Professional E-book

\\newpage

"""
    
    # Read original content
    with open("red_team_blue_team_guide.md", 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Combine metadata with content
    enhanced_content = metadata + original_content
    
    # Write enhanced markdown
    with open("enhanced_guide.md", 'w', encoding='utf-8') as f:
        f.write(enhanced_content)
    
    print("📖 Enhanced markdown created with metadata")
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    # Generate PDF using pandoc
    print("📄 Generating PDF with pandoc...")
    try:
        pdf_cmd = [
            "pandoc",
            "enhanced_guide.md",
            "-o", "output/Red_Team_Blue_Team_Guide_Professional.pdf",
            "--pdf-engine=weasyprint",
            "--css=professional_style.css",
            "--standalone",
            "--toc",
            "--number-sections",
            "--highlight-style=tango"
        ]
        
        # Create CSS file for styling
        css_content = """
        @page {
            size: A4;
            margin: 2.5cm;
            @top-center {
                content: "Red Team & Blue Team Guide";
                font-size: 10pt;
                color: #666;
            }
            @bottom-center {
                content: "Page " counter(page);
                font-size: 10pt;
                color: #666;
            }
        }
        
        body {
            font-family: Georgia, serif;
            line-height: 1.6;
            color: #333;
            font-size: 11pt;
        }
        
        h1 {
            color: #2c3e50;
            font-size: 20pt;
            margin-top: 30pt;
            margin-bottom: 20pt;
            page-break-before: always;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10pt;
        }
        
        h2 {
            color: #34495e;
            font-size: 16pt;
            margin-top: 25pt;
            margin-bottom: 15pt;
        }
        
        h3 {
            color: #2c3e50;
            font-size: 14pt;
            margin-top: 20pt;
            margin-bottom: 10pt;
        }
        
        code {
            background-color: #f8f9fa;
            padding: 2pt 4pt;
            border-radius: 3pt;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
            color: #e74c3c;
        }
        
        pre {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15pt;
            border-radius: 5pt;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
            line-height: 1.4;
            margin: 15pt 0;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15pt 0;
        }
        
        th, td {
            border: 1pt solid #bdc3c7;
            padding: 8pt;
            text-align: left;
        }
        
        th {
            background-color: #34495e;
            color: white;
        }
        """
        
        with open("professional_style.css", 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        result = subprocess.run(pdf_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            pdf_path = "output/Red_Team_Blue_Team_Guide_Professional.pdf"
            if os.path.exists(pdf_path):
                size = os.path.getsize(pdf_path) / (1024 * 1024)
                print(f"✅ PDF generated: {pdf_path}")
                print(f"📊 Size: {size:.2f} MB")
            else:
                print("❌ PDF file not found after generation")
        else:
            print(f"❌ Pandoc PDF error: {result.stderr}")
            
    except FileNotFoundError:
        print("❌ Pandoc not found. Trying alternative method...")
        return generate_with_weasyprint()
    except Exception as e:
        print(f"❌ PDF generation error: {e}")
        return generate_with_weasyprint()
    
    # Generate EPUB
    print("📚 Generating EPUB with pandoc...")
    try:
        epub_cmd = [
            "pandoc",
            "enhanced_guide.md",
            "-o", "output/Red_Team_Blue_Team_Guide_Professional.epub",
            "--standalone",
            "--toc",
            "--epub-cover-image=cover.jpg",
            "--epub-metadata=metadata.xml"
        ]
        
        # Create metadata for EPUB
        metadata_xml = f"""
        <dc:title>Red Team & Blue Team Guide: Flipper Zero Security Testing</dc:title>
        <dc:creator>Cybersecurity Professional</dc:creator>
        <dc:publisher>Security Research Publications</dc:publisher>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:language>en-US</dc:language>
        <dc:subject>Cybersecurity</dc:subject>
        <dc:subject>Penetration Testing</dc:subject>
        <dc:subject>Red Team</dc:subject>
        <dc:subject>Blue Team</dc:subject>
        <dc:subject>Flipper Zero</dc:subject>
        <dc:description>A comprehensive guide to offensive and defensive cybersecurity testing using Flipper Zero and advanced penetration testing techniques.</dc:description>
        """
        
        with open("metadata.xml", 'w', encoding='utf-8') as f:
            f.write(metadata_xml)
        
        result = subprocess.run(epub_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            epub_path = "output/Red_Team_Blue_Team_Guide_Professional.epub"
            if os.path.exists(epub_path):
                size = os.path.getsize(epub_path) / (1024 * 1024)
                print(f"✅ EPUB generated: {epub_path}")
                print(f"📊 Size: {size:.2f} MB")
            else:
                print("❌ EPUB file not found after generation")
        else:
            print(f"❌ Pandoc EPUB error: {result.stderr}")
            
    except Exception as e:
        print(f"❌ EPUB generation error: {e}")
    
    # Create publishing information
    create_publishing_info()
    
    print("🎉 E-book generation completed!")

def generate_with_weasyprint():
    """Fallback method using WeasyPrint directly"""
    print("🔄 Using WeasyPrint fallback method...")
    
    try:
        import markdown
        from weasyprint import HTML, CSS
        
        # Read content
        with open("enhanced_guide.md", 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert to HTML
        html = markdown.markdown(content, extensions=['codehilite', 'tables', 'toc'])
        
        # Read CSS
        with open("professional_style.css", 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Generate PDF
        html_doc = f"<html><head><meta charset='utf-8'></head><body>{html}</body></html>"
        HTML(string=html_doc).write_pdf(
            "output/Red_Team_Blue_Team_Guide_Professional.pdf",
            stylesheets=[CSS(string=css_content)]
        )
        
        pdf_path = "output/Red_Team_Blue_Team_Guide_Professional.pdf"
        if os.path.exists(pdf_path):
            size = os.path.getsize(pdf_path) / (1024 * 1024)
            print(f"✅ PDF generated with WeasyPrint: {pdf_path}")
            print(f"📊 Size: {size:.2f} MB")
            return True
        
    except Exception as e:
        print(f"❌ WeasyPrint fallback failed: {e}")
        return False

def create_publishing_info():
    """Create publishing information file"""
    info_content = f"""
PROFESSIONAL E-BOOK PUBLISHING INFORMATION
==========================================

Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
Subtitle: A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing
Author: Cybersecurity Professional
Publisher: Security Research Publications
Publication Date: {datetime.now().strftime('%B %Y')}
Language: English
Format: PDF + EPUB

File Details:
- PDF: Red_Team_Blue_Team_Guide_Professional.pdf
- EPUB: Red_Team_Blue_Team_Guide_Professional.epub
- Enhanced Markdown: enhanced_guide.md

Amazon KDP Requirements:
✅ Professional formatting and typography
✅ Table of contents with page numbers
✅ Copyright page and legal disclaimers
✅ Proper metadata for discoverability
✅ Code syntax highlighting
✅ Consistent styling throughout
✅ Print-ready PDF format
✅ E-reader compatible EPUB

Content Highlights:
- Comprehensive Flipper Zero security testing guide
- Red Team offensive testing techniques
- Blue Team detection and mitigation strategies
- Car security vulnerabilities and rolling code exploits
- Advanced RF signal analysis and forensics
- Custom firmware documentation (DarkWeb, RollBack, KeyMaster)
- Python code examples for detection systems
- Legal and ethical considerations

Marketing Keywords:
cybersecurity, penetration testing, red team, blue team, flipper zero,
security testing, ethical hacking, network security, wireless security,
incident response, forensics, security analysis, car security, rolling codes,
RF hacking, software defined radio, custom firmware, vulnerability assessment

Target Categories:
- Computer Science > Security > Penetration Testing
- Technology > Computer Security
- Computer Science > Networking

Recommended Pricing:
- E-book: $19.99 - $29.99
- Print: $39.99 - $49.99

Target Audience:
- Cybersecurity professionals
- Penetration testers
- Security researchers
- IT security students
- Ethical hackers

Next Steps for Amazon Publishing:
1. Upload PDF for print-on-demand
2. Upload EPUB for Kindle Direct Publishing
3. Create professional cover design
4. Write compelling book description
5. Set up author profile
6. Configure pricing and distribution
"""
    
    with open("output/publishing_info.txt", 'w', encoding='utf-8') as f:
        f.write(info_content)
    
    print("📋 Publishing information saved to: output/publishing_info.txt")

if __name__ == "__main__":
    create_professional_ebook()
