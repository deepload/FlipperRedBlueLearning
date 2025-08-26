# 📖 Red Team & Blue Team Guide - EPUB Generation Project

## 🎯 Project Overview

This project contains a comprehensive cybersecurity training guide covering Red Team and Blue Team operations using Flipper Zero with Predator module. The guide includes practical scenarios, detection strategies, and hands-on examples for security professionals.

### 📝 Credits
- **Created by**: Team [deep]load and NicoLoccco
- **Special acknowledgment**: Collaborative efforts and expertise
- **Featuring**: Methodologies from Legendary Cybersecurity Experts

## 📁 Project Structure

```
C:\Projects\Flipper\
├── red_team_blue_team_guide_english.md    # Main guide (English-only version)
├── simple_epub_generator.py               # Simple EPUB generator (recommended)
├── enhanced_epub_generator.py             # Advanced EPUB generator with chapters
├── professional_epub_generator.py         # Professional formatting generator
├── visual_epub_generator.py               # Visual generator with ASCII-to-image conversion
├── epub/                                  # Output directory for generated EPUBs
│   ├── Red_Team_Blue_Team_Guide_Professional.epub
│   └── images/                            # Generated diagram images
├── __pycache__/                          # Python cache files
└── README.md                             # This file
```

## 🚀 How to Generate EPUB from the Guide

### Method 1: Simple EPUB Generator (Recommended)

The `simple_epub_generator.py` is the most reliable option for basic EPUB generation:

```bash
cd C:\Projects\Flipper
python simple_epub_generator.py
```

**Features:**
- ✅ Fast generation
- ✅ Professional styling
- ✅ Chapter-based structure
- ✅ Clean formatting
- ⚠️ Currently has line break formatting issues in code blocks

### Method 2: Enhanced EPUB Generator

For more advanced features with better chapter management:

```bash
cd C:\Projects\Flipper
python enhanced_epub_generator.py
```

**Features:**
- ✅ Advanced chapter splitting
- ✅ Table of contents generation
- ✅ Professional metadata
- ✅ Amazon KDP compliance
- ❌ Requires `markdown` library dependency

### Method 3: Professional EPUB Generator

For professional publishing with advanced formatting:

```bash
cd C:\Projects\Flipper
python professional_epub_generator.py
```

**Features:**
- ✅ Professional typography
- ✅ Enhanced code highlighting
- ✅ Styled expert quotes
- ✅ Mobile-friendly design
- ❌ Requires `markdown` library dependency

### Method 4: Visual EPUB Generator

For converting ASCII diagrams to images:

```bash
cd C:\Projects\Flipper
python visual_epub_generator.py
```

**Features:**
- ✅ ASCII art to image conversion
- ✅ Professional diagram rendering
- ✅ Visual enhancements
- ❌ Requires `PIL` (Pillow) library dependency

## 📋 Prerequisites

### Required Files
- `red_team_blue_team_guide_english.md` - Main source file

### Python Dependencies

**For Simple Generator (No dependencies required):**
- Python 3.6+ with standard libraries only

**For Advanced Generators:**
```bash
pip install markdown
pip install Pillow  # Only for visual generator
```

## 🔧 Generated Output

All generators create EPUB files in the `epub/` directory:

- **File Format**: `.epub` (standard e-book format)
- **Compatibility**: Compatible with most e-readers (Kindle, Apple Books, Adobe Digital Editions)
- **Size**: Typically 0.02-0.5 MB depending on generator and content
- **Structure**: Professional chapter-based organization

## 📚 Content Overview

The guide covers:

### 🏗️ Part I - Fundamentals
- Introduction and Objectives
- Red Team vs Blue Team Concepts  
- Hardware Description (Flipper Zero + Predator Module)
- Configuration and Installation

### ⚡ Part II - Operational Techniques
- RF Sub-GHz Attacks
- WiFi Attacks
- GPS Reconnaissance and Wardriving
- Practical Scenarios

### 🛡️ Part III - Defense & Detection
- Blue Team Strategies
- Detection Tools
- Countermeasures

### 📖 Part IV - Practice & Ethics
- Practical Exercises
- Legal and Ethical Aspects
- Resources and References

## 🎖️ Certification Levels
- 🥉 **Bronze**: Basic Operations
- 🥈 **Silver**: Advanced Techniques  
- 🥇 **Gold**: Expert Mastery

## ⚠️ Legal Notice

**CRITICAL**: This guide is for authorized educational and testing purposes only. All techniques must be used in compliance with applicable laws and with proper written authorization.

## 🐛 Known Issues

### Current Issues (as of 2025-01-27):
1. **Line Break Formatting**: Legal warning section in code blocks may display without proper line breaks
2. **Generator Execution**: Some generators may have execution issues on certain systems
3. **Dependencies**: Advanced generators require additional Python packages

### Workarounds:
- Use `simple_epub_generator.py` for most reliable results
- Manually verify EPUB output in e-reader before distribution
- Check Python environment and dependencies if generators fail

## 🔄 Troubleshooting

### Generator Not Running:
```bash
# Check Python version
python --version

# Verify file exists
dir red_team_blue_team_guide_english.md

# Run with explicit path
python C:\Projects\Flipper\simple_epub_generator.py
```

### Missing Dependencies:
```bash
# Install required packages
pip install markdown Pillow

# Or use simple generator (no dependencies)
python simple_epub_generator.py
```

### EPUB Validation:
- Use online EPUB validators to check file integrity
- Test in multiple e-readers for compatibility
- Verify all chapters and formatting appear correctly

## 📞 Support

For issues or improvements:
1. Check the generated EPUB in your preferred e-reader
2. Verify all source files are present and readable
3. Ensure Python environment is properly configured
4. Review error messages for specific dependency issues

## 🔮 Future Improvements

- [ ] Fix line break formatting in code blocks
- [ ] Add batch processing for multiple files
- [ ] Implement EPUB validation
- [ ] Add cover image generation
- [ ] Improve error handling and logging
- [ ] Add configuration file support

---

**Last Updated**: January 27, 2025  
**Version**: 1.0  
**Authors**: Team [deep]load and NicoLoccco
