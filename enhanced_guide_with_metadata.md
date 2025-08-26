---
title: "Red Team & Blue Team Guide: Flipper Zero Security Testing"
subtitle: "A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing"
author: "Cybersecurity Professional"
date: "August 2025"
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

\newpage

# Copyright and Legal Notice

© 2024 Security Research Publications. All rights reserved.

**IMPORTANT LEGAL DISCLAIMER:**
This guide is intended for educational and authorized security testing purposes only. The techniques described should only be used on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal and may result in criminal prosecution.

**Publication Information:**
- Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
- Publisher: Security Research Publications
- Publication Date: August 2025
- Language: English
- Format: Professional E-book

\newpage

---
title: "Red Team & Blue Team Guide: Flipper Zero Security Testing"
subtitle: "A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing"
author: "Cybersecurity Professional"
date: "August 2025"
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

\newpage

# Copyright and Legal Notice

© 2024 Security Research Publications. All rights reserved.

**IMPORTANT LEGAL DISCLAIMER:**
This guide is intended for educational and authorized security testing purposes only. The techniques described should only be used on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal and may result in criminal prosecution.

**Publication Information:**
- Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
- Publisher: Security Research Publications
- Publication Date: August 2025
- Language: English
- Format: Professional E-book

\newpage

# Complete Red Team & Blue Team Guide
## Using Flipper Zero with Predator Module
### Professional Security Testing Manual

## Table of Contents

### Part I - Fundamentals
- Introduction and Objectives
- Red Team vs Blue Team Concepts
- Hardware Description and Specifications
- Configuration and Installation
- Advanced Setup Procedures

### Part II - Operational Techniques
- RF Sub-GHz Attack Methodologies
- Advanced WiFi Penetration Testing
- GPS Reconnaissance and Wardriving
- IoT Device Exploitation
- Physical Security Testing

### Part III - Defense and Detection
- Blue Team Strategies and Implementation
- Advanced Detection Tools and SIEM Integration
- Automated Response Systems
- Forensic Analysis Techniques

### Part IV - Practice and Ethics
- Comprehensive Practical Exercises
- Legal Framework and Compliance
- Ethical Guidelines and Best Practices
- Professional Resources and References

## Chapter 1. Introduction and Objectives

### Learning Objectives

This comprehensive guide trains security professionals in advanced attack simulation (Red Team) and defense (Blue Team) techniques using the Flipper Zero equipped with the Predator module. Upon completion, participants will master:

- **Advanced Penetration Testing:** Understanding sophisticated attack vectors and exploitation techniques
- **Hardware Security Testing:** Proficient use of Flipper Zero and Predator module for RF, WiFi, and IoT assessments
- **Vulnerability Assessment:** Systematic identification and analysis of security weaknesses in wireless systems
- **Defense Strategy Development:** Creating robust detection and response mechanisms
- **Forensic Analysis:** Conducting detailed investigation of wireless security incidents
- **Compliance and Ethics:** Applying legal frameworks and ethical guidelines in security testing
- **Tool Integration:** Implementing comprehensive security monitoring and SIEM integration
- **Advanced Countermeasures:** Designing and deploying sophisticated defense systems

### Critical Legal Warning

🔴 **MANDATORY COMPLIANCE:** The equipment and techniques in this guide are restricted to:

- **Authorized Testing Environments:** Only systems you own or have explicit written permission to test
- **Legal Penetration Testing:** Contracted security assessments with proper documentation
- **Security Audits:** Formal audits with signed agreements and defined scope
- **Educational Purposes:** Supervised training in controlled laboratory environments
- **Research Activities:** Academic or professional research with institutional approval

**Prohibited Activities:**
- Unauthorized access to any computer system or network
- Interference with critical infrastructure or emergency services
- Testing on systems without explicit written permission
- Commercial use without proper licensing and agreements

**Legal Consequences:** Violation of these guidelines may result in criminal prosecution, civil liability, and professional sanctions. Always consult legal counsel before conducting security testing.

### Prerequisites and Requirements

**Technical Knowledge Requirements:**
- **Networking Fundamentals:** Deep understanding of TCP/IP, OSI model, wireless protocols (802.11, Bluetooth, Zigbee)
- **Radio Frequency Theory:** Knowledge of RF propagation, modulation schemes, antenna theory
- **Information Security:** Solid foundation in cybersecurity principles, threat modeling, risk assessment
- **Operating Systems:** Proficiency with Linux command line, Windows administration, mobile platforms
- **Programming Skills:** Basic Python, C/C++, shell scripting for automation and analysis
- **Cryptography:** Understanding of encryption algorithms, key management, PKI infrastructure

**Required Hardware:**
- **Primary Equipment:** Flipper Zero device with latest firmware
- **Predator Module:** Advanced wireless testing module with all components
- **Antenna Collection:** High-gain RF antennas (433MHz, 868MHz, 915MHz), WiFi antennas (2.4/5GHz), GPS antenna
- **Computing Platform:** Laptop with WiFi capabilities, USB-C ports, minimum 16GB RAM
- **Accessories:** Quality USB-C cables, external battery packs, MicroSD cards (32GB+), Faraday bags
- **Optional Equipment:** Spectrum analyzer, signal generator, oscilloscope for advanced analysis

**Software Requirements:**
- **Operating System:** Kali Linux or Ubuntu with wireless tools
- **Analysis Tools:** Wireshark, GNU Radio, SDR#, GQRX
- **Programming Environment:** Python 3.8+, GCC compiler, Git version control
- **Documentation:** Jupyter notebooks for analysis documentation

## Chapter 2. Advanced Red Team vs Blue Team Concepts

### Red Team - Offensive Security Operations

The Red Team operates as an adversarial force, simulating real-world attackers to test organizational defenses comprehensively. Their mission encompasses:

**Primary Objectives:**
- **Vulnerability Discovery:** Systematic identification of security weaknesses across all attack surfaces
- **Exploitation Validation:** Demonstrating real-world impact of discovered vulnerabilities
- **Defense Testing:** Evaluating detection capabilities and incident response procedures
- **Security Posture Assessment:** Providing realistic assessment of organizational security maturity
- **Training Enhancement:** Improving blue team skills through realistic attack scenarios

**Advanced Red Team Methodology:**
1. **Strategic Reconnaissance:** Deep intelligence gathering using OSINT, social engineering, and technical reconnaissance
2. **Target Enumeration:** Comprehensive mapping of attack surfaces including network, wireless, physical, and human elements
3. **Initial Access:** Gaining foothold through various attack vectors (phishing, wireless exploitation, physical access)
4. **Persistence Establishment:** Maintaining long-term access through backdoors, scheduled tasks, and legitimate credentials
5. **Lateral Movement:** Expanding access across the network using privilege escalation and credential harvesting
6. **Objective Achievement:** Accomplishing specific goals (data exfiltration, system compromise, business disruption)
7. **Comprehensive Reporting:** Detailed documentation with risk assessment, business impact, and remediation guidance

**Specialized Red Team Techniques:**
- **RF and Wireless Exploitation:** Using Flipper Zero and Predator module for radio frequency attacks
- **Physical Security Testing:** Lock picking, badge cloning, tailgating, and facility infiltration
- **Social Engineering:** Pretexting, phishing campaigns, and human psychology exploitation
- **Supply Chain Attacks:** Targeting third-party vendors and software dependencies
- **Advanced Persistent Threat (APT) Simulation:** Long-term, stealthy operations mimicking nation-state actors

### Blue Team - Defensive Security Operations

The Blue Team serves as the primary defensive force, responsible for protecting organizational assets and responding to security incidents. Their comprehensive mission includes:

**Core Responsibilities:**
- **Threat Detection:** Implementing and maintaining advanced detection systems across all security domains
- **Incident Analysis:** Conducting thorough investigation of security events and potential breaches
- **Response Coordination:** Orchestrating rapid and effective response to confirmed security incidents
- **Defense Optimization:** Continuously improving security controls and defensive capabilities
- **Threat Intelligence:** Gathering, analyzing, and applying threat intelligence to enhance defenses

**Advanced Blue Team Operations:**
1. **Continuous Monitoring:** 24/7 surveillance using SIEM, SOAR, and advanced analytics platforms
2. **Threat Hunting:** Proactive searching for indicators of compromise and advanced persistent threats
3. **Behavioral Analysis:** Using machine learning and user behavior analytics to detect anomalies
4. **Forensic Investigation:** Detailed analysis of security incidents using digital forensics techniques
5. **Incident Response:** Coordinated response following established playbooks and procedures
6. **Recovery Operations:** System restoration, evidence preservation, and lessons learned integration
7. **Defense Enhancement:** Implementing new controls based on threat landscape evolution

**Specialized Blue Team Capabilities:**
- **RF Security Monitoring:** Detecting unauthorized radio frequency activities and jamming attempts
- **Wireless Intrusion Detection:** Identifying rogue access points, evil twin attacks, and deauthentication floods
- **IoT Security Management:** Monitoring and securing Internet of Things devices and networks
- **Threat Intelligence Integration:** Leveraging external threat feeds and internal intelligence
- **Security Orchestration:** Automating response actions and integrating security tools

### Purple Team - Collaborative Security Operations

**Purple Team Philosophy:** A collaborative approach that bridges offensive and defensive security operations to maximize organizational security effectiveness. This methodology combines Red Team attack techniques with Blue Team defensive expertise.

**Strategic Objectives:**
- **Knowledge Transfer:** Facilitating continuous exchange of tactics, techniques, and procedures between teams
- **Capability Enhancement:** Improving both offensive testing methods and defensive detection capabilities
- **Process Optimization:** Streamlining detection rules, response procedures, and security tool configurations
- **Metrics Improvement:** Reducing mean time to detection (MTTD) and mean time to response (MTTR)
- **Training Integration:** Creating realistic scenarios that enhance both red and blue team skills

**Purple Team Activities:**
- **Collaborative Exercises:** Joint training sessions and tabletop exercises
- **Detection Engineering:** Working together to develop and tune detection rules
- **Threat Modeling:** Combined assessment of attack vectors and defensive controls
- **Tool Validation:** Testing security tools effectiveness against real attack techniques
- **Playbook Development:** Creating comprehensive incident response procedures
- **Metrics Analysis:** Evaluating security program effectiveness and identifying improvement areas

**Advanced Purple Team Implementations:**
- **Continuous Security Validation:** Ongoing testing of security controls using automated red team techniques
- **Threat-Informed Defense:** Aligning defensive strategies with current threat actor tactics
- **Security Control Optimization:** Fine-tuning detection systems based on attack simulation results
- **Cross-Training Programs:** Developing T-shaped security professionals with both offensive and defensive skills

## Chapter 3. Comprehensive Hardware Description

### Flipper Zero - Advanced Penetration Testing Platform

The Flipper Zero represents a paradigm shift in portable security testing equipment, combining multiple radio frequency capabilities with extensive GPIO functionality in a compact, user-friendly form factor.

**Core Technical Specifications:**
- **Primary Processor:** STM32WB55 dual-core (Cortex-M4 64 MHz + Cortex-M0+ 32 MHz)
- **Memory Architecture:** 256 KB RAM, 1 MB Flash storage, external MicroSD support up to 128GB
- **Display System:** High-contrast monochrome LCD 128x64 pixels with adjustable backlight
- **User Interface:** 5-way directional pad with center button, intuitive menu navigation
- **Connectivity:** USB-C (data + charging), Bluetooth Low Energy 5.0, Sub-GHz transceiver
- **Expansion Interface:** 18-pin GPIO header with 3.3V logic levels
- **Power Management:** 2000 mAh Li-Po battery with intelligent charging circuit
- **Operating Temperature:** -10°C to +50°C operational range
- **Dimensions:** 100mm x 40mm x 25mm, lightweight at 102 grams

**Advanced Hardware Features:**
- **Sub-GHz Radio:** CC1101 transceiver covering 300-928 MHz (region dependent)
- **NFC Module:** 13.56 MHz reader/writer supporting ISO14443A/B, ISO15693, FeliCa
- **RFID Capability:** 125 kHz reader/writer for EM4100, HID Prox, and compatible formats
- **Infrared System:** Transmitter and receiver for consumer electronics control
- **GPIO Flexibility:** SPI, I2C, UART, PWM, ADC, and digital I/O capabilities
- **iButton Interface:** 1-Wire protocol support for Dallas Semiconductor devices

### Predator Module - Professional Wireless Testing Extension

The Predator module transforms the Flipper Zero into a comprehensive wireless security testing platform, adding enterprise-grade capabilities for WiFi, enhanced RF, and GPS operations.

**Module Architecture Overview:**
```
┌─────────────────────────────────────────────────────────┐
│                  PREDATOR MODULE                        │
├─────────────────────────────────────────────────────────┤
│  📡 Enhanced RF Sub-GHz System                         │
│  • Advanced CC1101 with power amplifier                │
│  • High-gain helical antenna (433/868/915 MHz)         │
│  • Extended range: 100-500m line of sight              │
│  • Transmission power: -30 to +20 dBm                  │
│  • Reception sensitivity: -110 dBm                     │
├─────────────────────────────────────────────────────────┤
│  📶 Dual-Band WiFi Module                              │
│  • ESP32-S3 dual-core processor (240 MHz)             │
│  • 2.4 GHz and 5 GHz band support                     │
│  • AP/Station/Monitor/Promiscuous modes               │
│  • Integrated PCB antenna + external connector        │
│  • Advanced packet injection capabilities              │
├─────────────────────────────────────────────────────────┤
│  🛰️ Professional GNSS Module                           │
│  • Multi-constellation receiver (GPS/GLONASS/Galileo)  │
│  • Accuracy: <2.5m CEP (Circular Error Probable)      │
│  • Cold start time: <30 seconds                        │
│  • Update rate: 1-10 Hz configurable                  │
│  • Active antenna with LNA                             │
├─────────────────────────────────────────────────────────┤
│  🔌 Advanced Connectivity & Power                      │
│  • High-speed GPIO interface to Flipper Zero          │
│  • USB-C 3.0 (data transfer + fast charging)          │
│  • Internal 1500 mAh Li-Po battery                     │
│  • Intelligent power management system                 │
│  • Real-time clock with battery backup                 │
└─────────────────────────────────────────────────────────┘
```

**Performance Specifications:**
- **Operating Frequency Ranges:**
  - Sub-GHz: 300-348 MHz, 387-464 MHz, 779-928 MHz (region dependent)
  - WiFi 2.4 GHz: 2412-2484 MHz (channels 1-14)
  - WiFi 5 GHz: 5150-5825 MHz (channels 36-165, region dependent)
- **Data Rates:**
  - RF: 0.6 to 500 kbps with various modulation schemes
  - WiFi: Up to 150 Mbps (2.4 GHz), 433 Mbps (5 GHz)
- **Power Consumption:**
  - Idle mode: 50 mA
  - Active scanning: 200 mA
  - Transmission (max power): 800 mA
- **Environmental Specifications:**
  - Operating temperature: -20°C to +60°C
  - Storage temperature: -40°C to +85°C
  - Humidity: 5% to 95% non-condensing

### Advanced Component Analysis

**Enhanced RF Sub-GHz Module**

The enhanced RF module provides significantly improved capabilities over standard implementations:

**Technical Specifications:**
- **Frequency Coverage:** 300-348 MHz, 387-464 MHz, 779-928 MHz (ISM bands)
- **Modulation Support:** ASK/OOK, 2-FSK, 4-FSK, MSK, GFSK with configurable deviation
- **Data Rates:** 0.6 to 500 kbps with automatic rate detection
- **Transmission Power:** -30 to +20 dBm in 1 dB steps
- **Reception Sensitivity:** -110 dBm at 1.2 kbps, -100 dBm at 38.4 kbps
- **Channel Spacing:** 25 kHz to 400 kHz configurable
- **Frequency Stability:** ±10 ppm with temperature compensation

**Advanced Features:**
- **Automatic Frequency Control (AFC):** Compensates for frequency drift
- **Forward Error Correction (FEC):** Improves reliability in noisy environments
- **Packet Engine:** Hardware-based packet handling with CRC validation
- **RSSI Measurement:** Real-time signal strength indication
- **Clear Channel Assessment (CCA):** Prevents interference with ongoing transmissions

**Target Applications:**
- Garage door and gate remote controls
- Wireless security systems and sensors
- Industrial IoT device communication
- Smart home automation protocols
- Tire pressure monitoring systems (TPMS)
- Weather station data collection

**Advanced WiFi Module (ESP32-S3)**

**Comprehensive WiFi Capabilities:**
- **Standards Support:** 802.11 b/g/n (2.4 GHz), 802.11 a/n/ac (5 GHz)
- **Operating Modes:** Station, Access Point, Monitor, Promiscuous, Mesh networking
- **Security Protocols:** Open, WEP, WPA/WPA2-PSK, WPA2-Enterprise, WPA3-SAE
- **Maximum Data Rates:** 150 Mbps (2.4 GHz), 433 Mbps (5 GHz)
- **Channel Support:** 1-14 (2.4 GHz), 36-165 (5 GHz, region dependent)
- **Antenna Diversity:** Dual antenna support with automatic switching
- **Power Management:** Dynamic power scaling, deep sleep modes

**Professional Testing Features:**
- **Packet Injection:** Custom frame crafting and transmission
- **Monitor Mode:** Passive packet capture and analysis
- **Beacon Flooding:** Stress testing access point handling
- **Deauthentication Attacks:** Client disconnection testing
- **Evil Twin Capabilities:** Rogue access point creation
- **WPS Testing:** PIN brute force and Pixie Dust attacks
- **Captive Portal:** Custom authentication page deployment
- **Channel Hopping:** Automated scanning across all channels

**Professional GNSS Module**

**Multi-Constellation Support:**
- **Satellite Systems:** GPS (L1), GLONASS (L1), Galileo (E1), BeiDou (B1), QZSS (L1)
- **Positioning Accuracy:** 2.5m CEP (50%), 1.0m with SBAS correction
- **Update Rates:** 1-10 Hz configurable, up to 18 Hz for specialized applications
- **Altitude Range:** Sea level to 18,000m (59,000 feet)
- **Velocity Range:** Up to 515 m/s (1,000 knots)
- **Time Accuracy:** ±60 nanoseconds with valid position fix

**Advanced GNSS Features:**
- **Cold Start Performance:** <30 seconds typical, <60 seconds maximum
- **Hot Start Performance:** <1 second with valid almanac
- **Acquisition Sensitivity:** -148 dBm
- **Tracking Sensitivity:** -165 dBm
- **Dynamic Platform Models:** Automotive, pedestrian, aviation, marine
- **Anti-Jamming:** Advanced signal processing for interference mitigation

**Wardriving and Reconnaissance Applications:**
- **High-Precision Mapping:** Sub-meter accuracy for detailed site surveys
- **Timestamp Correlation:** Precise time synchronization for multi-source data
- **Velocity Tracking:** Speed and heading information for mobile operations
- **Geofencing:** Automated alerts when entering/exiting defined areas
- **Track Logging:** Comprehensive path recording with metadata

## Chapter 4. Configuration and Installation

### Firmware Installation

**Step 1: Flipper Zero Preparation**

**Official firmware update:**

```bash
# Via qFlipper (graphical interface)
# - Download qFlipper from the official website
# - Connect the Flipper Zero via USB
# - Click "Update" to install the latest version
```

**Predator firmware installation:**

```bash
# Via command line
git clone https://github.com/flipperdevices/flipperzero-firmware
cd flipperzero-firmware
./fbt flash_usb
```

**Step 2: Predator Module Installation**

**Installation procedure:**
1. Turn off the Flipper Zero
2. Connect the Predator module to the GPIO pins
3. Screw in the antennas (RF, WiFi, GPS)
4. Connect the USB-C power cable
5. Restart the Flipper Zero

**Installation verification:**
1. Main Menu → Apps → GPIO → Predator
2. Verify the display of all three modules (RF, WiFi, GPS)
3. Test WiFi connectivity (AP Predator_XXXX visible)

## Chapter 5. Detailed Testing Scenarios with Examples

### Scenario 1: Physical Intrusion via RF (Parking/Gate)

**Context**

Testing unauthorized access to a corporate parking facility via RF signal capture and replay.

**Required Equipment**
- Flipper Zero + Predator Module
- Sub-GHz 433 MHz antenna
- Test vehicle (optional)
- Camera for documentation

**Detailed Red Team Procedure**

*Phase 1: Reconnaissance*
```bash
Flipper Zero → SubGHz → Read RAW
- Frequency: 433.92 MHz
- Position near the gate (5-10m)
- Wait for an employee to use their remote control
- Record the signal (duration: 5-10 seconds)
```

*Capture example:*
- Captured signal: 433.920 MHz
- Duration: 2.3 seconds
- Modulation: ASK/OOK
- Baud rate: 1000 baud
- Data: 1010101100110011...

*Phase 2: Signal analysis*
```bash
- Analyze the waveform
- Identify the protocol (Fixed Code vs Rolling Code)
- Verify signal repetition
- Extract the bit sequence
```

*Phase 3: Replay test*
```bash
Flipper Zero → SubGHz → Saved → [Filename]
- Select the recorded signal
- Position facing the receiver
- Press "Send"
- Observe the gate reaction
```

**Expected Results**
- ✅ Success: Gate opens → Vulnerability confirmed
- ❌ Failure: Rolling code detected → System secured

**Blue Team Detection**

*Compromise indicators:*
- Opening logs without associated employee badge
- Opening outside normal hours
- Suspicious repeated activity
- Absence of authorized vehicle on cameras

*Example of suspicious log:*
```
[2024-08-26 14:23:15] GATE_OPEN - No badge scan detected
[2024-08-26 14:23:20] GATE_OPEN - No badge scan detected  
[2024-08-26 14:23:25] GATE_OPEN - No badge scan detected
```

### Scenario 2: WiFi Denial of Service Attack (Deauth Flood)

**Context**

Massive disruption of corporate WiFi network by forced client disconnection.

**Detailed Red Team Procedure**

*Phase 1: WiFi Reconnaissance*
```bash
Flipper Zero → Apps → WiFi → WiFi Scanner
- Scan available networks
- Identify target SSID: "Corp-WiFi"
- Note the channel (e.g., Channel 6)
- Count the number of connected clients
```

*Scan example:*
```
SSID: Corp-WiFi
BSSID: AA:BB:CC:DD:EE:FF
Channel: 6
Security: WPA2-PSK
Signal: -45 dBm
Clients: 23 detected
```

*Phase 2: Client analysis*
```bash
WiFi → Monitor Mode → Channel 6
- Capture 802.11 traffic
- Identify client MAC addresses
- Observe management frames
- Select priority targets
```

*Phase 3: Targeted Deauth attack*
```bash
WiFi → Deauth Attack
- Target: Corp-WiFi (AA:BB:CC:DD:EE:FF)
- Clients: ALL or specific selection
- Packets: 100 per second
- Duration: Continuous
- Launch attack
```

*Attack code (802.11 frame):*
```
Frame Type: Management (0x00)
Subtype: Deauthentication (0x0C)
Destination: Broadcast (FF:FF:FF:FF:FF:FF)
Source: AP_BSSID (AA:BB:CC:DD:EE:FF)
Reason: Unspecified reason (0x01)
```

**Expected Results**
- Massive WiFi client disconnection
- Inability to reconnect
- Network service disruption
- User complaints

**Success Metrics**
- Disconnected clients: 23/23 (100%)
- Reconnection attempts: 156 failures
- Attack duration: 5 minutes
- Generated traffic: 30,000 deauth frames/min

**Blue Team Detection**

*IDS/IPS alerts:*
```
[ALERT] Deauth flood detected on Corp-WiFi
Source: Multiple unknown MAC addresses
Rate: 500 deauth frames/second
Duration: 5 minutes continuous
Affected clients: 23
```

*Immediate countermeasures:*
- MAC filtering activation
- WiFi channel change
- 802.11w (PMF) protection activation
- Attack origin investigation

### Scenario 3: Malicious Access Point (Evil Twin)

**Context**

Creating a rogue access point to capture employee credentials.

**Detailed Red Team Procedure**

*Phase 1: Legitimate network cloning*
```bash
WiFi Scanner → Identify "Corp-WiFi"
- SSID: Corp-WiFi
- Security: WPA2-PSK
- Channel: 6
- Signal: -45 dBm
```

*Phase 2: Evil Twin configuration*
```bash
WiFi → Evil Portal
- SSID: Corp-WiFi (identical)
- Security: Open (to facilitate connection)
- Channel: 11 (different to avoid interference)
- Captive Portal: Enabled
- DNS Spoofing: Enabled
```

*Phase 3: Capture page creation*
```html
<!-- Credential capture page -->
<!DOCTYPE html>
<html>
<head>
    <title>Corp-WiFi - Authentication</title>
    <style>
        body { font-family: Arial; background: #f0f0f0; }
        .login-box { 
            width: 300px; margin: 100px auto; 
            background: white; padding: 30px;
            border-radius: 10px; box-shadow: 0 0 10px #ccc;
        }
        input { width: 100%; padding: 10px; margin: 10px 0; }
        button { background: #007acc; color: white; padding: 10px 20px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Corp-WiFi Connection</h2>
        <form action="/capture.php" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Connect</button>
        </form>
        <p><small>Security system updated. Please reconnect.</small></p>
    </div>
</body>
</html>
```

*Phase 4: Positioning and waiting*
```bash
- Position in cafeteria or entrance hall
- Activate Evil Twin AP
- Wait for automatic connections
- Log all authentication attempts
```

**Expected Results**

*Credential capture:*
```
[14:30:15] New connection: iPhone-John (aa:bb:cc:dd:ee:ff)
[14:30:22] Credentials captured:
           Username: john.doe
           Password: Summer2024!
           Device: iPhone-John
           Location: Cafeteria

[14:35:42] New connection: LAPTOP-MARIE (11:22:33:44:55:66)
[14:35:51] Credentials captured:
           Username: marie.martin
           Password: MotDePasse123
           Device: Windows 10
           Location: Cafeteria
```

**Blue Team Detection**

*WIDS (Wireless Intrusion Detection System) indicators:*
```
[ALERT] Rogue AP detected
SSID: Corp-WiFi (duplicate)
BSSID: BB:BB:CC:DD:EE:FF (unknown)
Channel: 11
Signal Strength: -35 dBm
Location: Estimated Building A, Floor 1
Risk Level: CRITICAL
```

*Response actions:*
- Immediate SOC alert
- Rogue AP position triangulation
- User notification (email/SMS)
- Physical security team deployment
- MAC address blocking on infrastructure

### Scenario 4: Advanced Reconnaissance (Wardriving + GPS)

**Context**

Detailed mapping of exposed WiFi networks around the company perimeter.

**Detailed Red Team Procedure**

*Phase 1: Mission preparation*
```bash
Required equipment:
- Flipper Zero + Predator Module
- High-sensitivity WiFi antenna
- GPS antenna
- Vehicle with smartphone mount
- External battery
- Smartphone with Google Maps
```

*Phase 2: Wardriving configuration*
```bash
GPS → Activate GPS Module
- Wait for satellite synchronization (30-60s)
- Verify accuracy (<5m)

WiFi → Wardriving Mode
- Scan Interval: 5 seconds
- GPS Logging: Enabled
- Output Format: CSV + KML
- Storage: SD Card
```

*Phase 3: Reconnaissance route*

Planned route:
- Point A: Public parking (200m from company)
- Point B: Adjacent street north
- Point C: Adjacent street east
- Point D: Adjacent street south
- Point E: Adjacent street west
- Speed: 20-30 km/h for optimal capture

*Phase 4: Data collection*
```bash
# Wardriving log example
Time,Latitude,Longitude,SSID,BSSID,Security,Signal,Channel
14:23:15,46.2044,6.1432,Corp-WiFi,AA:BB:CC:DD:EE:FF,WPA2,-42,6
14:23:16,46.2044,6.1433,Corp-Guest,AA:BB:CC:DD:EE:F1,Open,-45,6
14:23:17,46.2045,6.1434,PRINTER-HP-001,BB:CC:DD:EE:FF:11,Open,-38,11
14:23:18,46.2045,6.1435,Corp-IoT,CC:DD:EE:FF:11:22,WEP,-41,1
14:23:19,46.2046,6.1436,CCTV-System,DD:EE:FF:11:22:33,Open,-39,6
```

**Data Analysis**

*Phase 5: Post-processing*
```bash
# Conversion and analysis
python3 wardriving_analyzer.py --input wardriving_log.csv
```

*Analysis script example:*
```python
import pandas as pd
import folium
from geopy.distance import geodesic

def analyze_wardriving_data(csv_file):
    df = pd.read_csv(csv_file)
    
    # Statistical analysis
    total_networks = len(df)
    open_networks = len(df[df['Security'] == 'Open'])
    wep_networks = len(df[df['Security'] == 'WEP'])
    corporate_networks = len(df[df['SSID'].str.contains('Corp')])
    
    print(f"=== WARDRIVING REPORT ===")
    print(f"Networks detected: {total_networks}")
    print(f"Open networks: {open_networks} ({open_networks/total_networks*100:.1f}%)")
    print(f"WEP networks: {wep_networks} ({wep_networks/total_networks*100:.1f}%)")
    print(f"Corporate networks exposed: {corporate_networks}")
    
    # Heat map
    map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=15)
    
    for idx, row in df.iterrows():
        color = 'red' if row['Security'] == 'Open' else 'orange' if row['Security'] == 'WEP' else 'green'
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=abs(int(row['Signal'])/10),
            popup=f"{row['SSID']} ({row['Security']})",
            color=color,
            fill=True
        ).add_to(m)
    
    m.save('wardriving_heatmap.html')
    return df

# Usage
results = analyze_wardriving_data('wardriving_log.csv')
```

**Expected Results**

*Critical discoveries:*
```
=== WARDRIVING REPORT - COMPANY XYZ ===

📊 General statistics:
- Total networks detected: 47
- Open networks: 12 (25.5%)
- WEP networks: 3 (6.4%)
- Corporate networks exposed: 8 (17.0%)

🔨 Identified vulnerabilities:
- Corp-Guest (Open) - Visible from public parking
- PRINTER-HP-001 (Open) - Unsecured printer
- Corp-IoT (WEP) - Obsolete encryption
- CCTV-System (Open) - Accessible cameras
- Corp-WiFi - Signal extends 150m beyond perimeter

📍 Risk zones:
- Public parking: 8 corporate networks visible
- North street: Corp-WiFi signal at -35 dBm
- Café across: Possible connection to guest network
```

**Blue Team Detection**

*Perimeter surveillance:*
- Detection of suspicious vehicles in perimeter
- Monitoring connection attempts from outside
- Analysis of WiFi connection geolocation logs

### Scenario 5: IoT Device Attack

**Context**

Compromising corporate IoT devices via their radio interfaces.

**Detailed Red Team Procedure**

*Phase 1: IoT reconnaissance*
```bash
SubGHz → Read → Frequency Analyzer
- Scan 315 MHz (US sensors)
- Scan 433.92 MHz (EU sensors)
- Scan 868 MHz (LoRaWAN)
- Scan 915 MHz (industrial sensors)
```

*Typical discoveries:*

Frequency 433.92 MHz:
- Temperature sensors (offices)
- Long-range RFID badges
- Automatic irrigation system
- Opening sensors (doors/windows)

Frequency 868 MHz:
- Smart meters
- Air quality sensors
- Connected heating system

*Phase 2: Protocol analysis*
```bash
# Temperature sensor capture
Signal: 433.920 MHz
Modulation: FSK
Baud rate: 2400 baud
Frame: [SYNC][ID][TEMP][HUMID][CRC]

Decoded data example:
Sensor ID: 0x2A4F
Temperature: 23.5°C
Humidity: 45%
Battery: 85%
```

*Phase 3: Specific attacks*

A) False data injection
```bash
SubGHz → Send → Custom Signal
- Modify temperature: 50°C
- Trigger system alert
- Observe team reaction
```

B) Denial of service by jamming
```bash
SubGHz → Jammer Mode
- Target frequency: 433.92 MHz
- Power: Maximum
- Duration: 30 minutes
- Impact: Sensor data loss
```

**Expected Results**
- False alerts on monitoring systems
- Interruption of IoT data collection
- Confusion in maintenance teams
- Possibility of physical access (opening sensors)

**Blue Team Detection**

*System alerts:*
```
[CRITICAL] Temperature anomaly detected
Sensor: 2A4F (Conference Room 3)
Value: 50.0°C (outside normal range: 18-28°C)
Timestamp: 2024-08-26T15:42:31
Action: HVAC emergency shutdown triggered
```

*Pattern analysis:*
- Outlier detection (ML algorithms)
- Multi-sensor correlation (abnormal temperature deviation)
- RF signature verification (spoofing detection)

### Scenario 6: RFID/NFC Badge Compromise

**Context**

Cloning and malicious use of employee access badges.

**Detailed Red Team Procedure**

*Phase 1: Badge type identification*
```bash
NFC → Read Card
- Approach badge to Flipper
- Identify type: MIFARE Classic/DESFire/NTAG
- Note UID and accessible sectors
```

*Badge reading example:*
```
Card Type: MIFARE Classic 1K
UID: 04:52:F3:2A:B8:40:80
SAK: 08
ATQA: 00:04

Readable sectors:
Sector 0: [Manufacturer data]
Sector 1: [Employee ID: EMP001234]
Sector 2: [Department: IT-SEC]
Sector 3: [Access level: 3]
```

*Phase 2: Badge cloning*
```bash
NFC → Write to Card
- Insert compatible blank card
- Copy all accessible sectors
- Verify data integrity
- Test clone on reader
```

*Phase 3: Access testing*
```bash
# Test on different readers
Results:
- Main door: ✅ Access granted
- Elevator: ✅ Level 3 accessible
- Server room: ❌ Access denied (level 4 required)
- Parking: ✅ Access granted
```

**Blue Team Detection**

*Access log anomalies:*
```
[ALERT] Badge usage anomaly detected
Badge ID: EMP001234 (John Doe)
15:23:42 - Door A01 (Main entrance) - SUCCESS
15:23:45 - Door A01 (Main entrance) - SUCCESS  
15:23:47 - Door A01 (Main entrance) - SUCCESS

Analysis: Multiple rapid access attempts
Risk: Possible cloned badge
Action: Badge temporarily disabled
```

## Chapter 9: Advanced Blue Team Strategies

### RF Attack Detection and Response

**Complete RF Monitoring System**

*Detection architecture:*
```
┌─────────────────────────────────────┐
│         RF DETECTION SYSTEM         │
├─────────────────────────────────────┤
│  📡 Distributed RF sensors             │
│  • Spectrum analyzers                 │
│  • Wideband receivers                 │  
│  • Anomaly detectors                  │
├─────────────────────────────────────┤
│  🔍 Real-time analysis                │
│  • Replay attack detection            │
│  • Jammer identification              │
│  • Physical log correlation           │
├─────────────────────────────────────┤
│  ⚡ Automatic response                 │
│  • Instant SOC alerts                 │
│  • Automatic lockdown                 │
│  • Security team notification         │
└─────────────────────────────────────┘
```

*Monitoring configuration:*
```bash
# Example configuration with rtl-sdr
rtl_433 -f 433920000 -s 250000 -F json -M time:iso:usec | \
while read line; do
    echo $line | python3 rf_analyzer.py --detect-replay
done
```

*RF attack detection script:*
```python
import json
import time
from datetime import datetime, timedelta

class RFSecurityMonitor:
    def __init__(self):
        self.recent_signals = {}
        self.alert_threshold = 3  # Number of suspicious repetitions
        
    def analyze_signal(self, data):
        signal_id = data.get('id', 'unknown')
        timestamp = datetime.now()
        
        # Detect replay attacks
        if signal_id in self.recent_signals:
            last_seen = self.recent_signals[signal_id]['last_seen']
            count = self.recent_signals[signal_id]['count']
            
            if timestamp - last_seen < timedelta(minutes=1):
                count += 1
                if count >= self.alert_threshold:
                    self.trigger_alert(signal_id, count, data)
        
        self.recent_signals[signal_id] = {
            'last_seen': timestamp,
            'count': self.recent_signals.get(signal_id, {}).get('count', 0) + 1,
            'data': data
        }
    
    def trigger_alert(self, signal_id, count, data):
        alert = {
            'type': 'RF_REPLAY_ATTACK',
            'signal_id': signal_id,
            'repeat_count': count,
            'frequency': data.get('freq', 'unknown'),
            'timestamp': datetime.now().isoformat(),
            'severity': 'HIGH'
        }
        
        # Send to SIEM
        self.send_to_siem(alert)
        
        # Immediate notification
        self.send_notification(alert)
    
    def send_to_siem(self, alert):
        # Integration with Splunk, ELK, etc.
        print(f"[SIEM ALERT] {json.dumps(alert, indent=2)}")
    
    def send_notification(self, alert):
        # SMS/Email to security team
        print(f"[SECURITY ALERT] Possible RF replay attack detected!")

# Usage
monitor = RFSecurityMonitor()
```

### WiFi Attack Detection

**Advanced WIDS/WIPS Configuration**

*WiFi sensor deployment:*
```bash
# Configuration with Kismet
kismet -c wlan0mon -c wlan1mon --override wardrive \
       --log-types pcapng,kismet,alert \
       --log-title "Corporate_WIDS"
```

*Custom detection rules:*
```python
# Evil Twin detection
def detect_evil_twin():
    known_aps = load_authorized_aps()
    detected_aps = scan_wireless_environment()
    
    for ap in detected_aps:
        if ap['ssid'] in [authorized['ssid'] for authorized in known_aps]:
            authorized_ap = next(a for a in known_aps if a['ssid'] == ap['ssid'])
            
            # Check if BSSID matches
            if ap['bssid'] != authorized_ap['bssid']:
                alert = {
                    'type': 'EVIL_TWIN_DETECTED',
                    'rogue_bssid': ap['bssid'],
                    'legitimate_bssid': authorized_ap['bssid'],
                    'ssid': ap['ssid'],
                    'channel': ap['channel'],
                    'signal_strength': ap['signal'],
                    'security': ap['security']
                }
                trigger_immediate_response(alert)

# Deauth attack detection
def detect_deauth_flood():
    DEAUTH_THRESHOLD = 50  # frames per minute
    
    deauth_count = count_deauth_frames(time_window=60)
    
    if deauth_count > DEAUTH_THRESHOLD:
        alert = {
            'type': 'DEAUTH_FLOOD_ATTACK',
            'frames_count': deauth_count,
            'time_window': 60,
            'affected_clients': get_affected_clients(),
            'source_analysis': analyze_attack_source()
        }
        
        # Automatic response
        enable_pmf_protection()
        change_wifi_channel()
        notify_security_team(alert)
```

### Automated Incident Response

**Automatic Response Playbook**

*RF attack response:*
```yaml
RF_Attack_Response_Playbook:
  trigger: RF_REPLAY_ATTACK_DETECTED
  
  immediate_actions:
    - disable_affected_device: true
    - alert_security_team: true
    - start_recording: true
    
  investigation_steps:
    - correlate_with_physical_logs
    - check_video_surveillance
    - analyze_signal_characteristics
    - identify_attack_source
    
  containment:
    - temporary_disable_rf_systems
    - increase_physical_security
    - deploy_rf_detection_team
    
  recovery:
    - implement_rolling_codes
    - update_security_policies
    - retrain_security_personnel
```

*WiFi attack response:*
```yaml
WiFi_Attack_Response_Playbook:
  trigger: EVIL_TWIN_DETECTED
  
  immediate_actions:
    - isolate_rogue_ap: true
    - broadcast_warning: "Security Alert: Unauthorized WiFi network detected"
    - enable_additional_monitoring: true
    
  investigation_steps:
    - triangulate_ap_location
    - analyze_captured_traffic  
    - identify_connected_clients
    - assess_data_compromise
    
  containment:
    - deploy_security_team_to_location
    - disconnect_affected_clients
    - change_wifi_passwords
    - enable_802.11w_protection
    
  recovery:
    - conduct_forensic_analysis
    - update_user_credentials
    - implement_additional_wids_sensors
    - security_awareness_training
```

## Chapter 10: Advanced Detection Tools

### Security Monitoring Dashboard

**Grafana + InfluxDB Configuration**

*Data structure:*
```sql
-- RF events table
CREATE TABLE rf_events (
    time TIMESTAMP,
    frequency FLOAT,
    signal_strength INTEGER,
    modulation VARCHAR(10),
    event_type VARCHAR(50),
    device_id VARCHAR(20),
    location VARCHAR(100)
);

-- WiFi events table
CREATE TABLE wifi_events (
    time TIMESTAMP,
    ssid VARCHAR(32),
    bssid VARCHAR(17),
    channel INTEGER,
    security VARCHAR(20),
    client_count INTEGER,
    event_type VARCHAR(50),
    risk_level VARCHAR(10)
);
```

*Monitoring queries:*
```sql
-- RF anomaly detection per hour
SELECT 
    time_bucket('1 hour', time) as hour,
    COUNT(*) as event_count,
    AVG(signal_strength) as avg_signal
FROM rf_events 
WHERE event_type = 'REPLAY_ATTACK'
GROUP BY hour
ORDER BY hour DESC;

-- Top 10 malicious APs detected
SELECT 
    bssid,
    ssid,
    COUNT(*) as detection_count,
    MAX(time) as last_seen
FROM wifi_events 
WHERE event_type = 'ROGUE_AP'
GROUP BY bssid, ssid
ORDER BY detection_count DESC
LIMIT 10;
```

### RF and WiFi Forensic Analysis

**Capture and Analyze RF Signals**

*RF forensic analysis script:*
```python
#!/usr/bin/env python3
# rf_forensics.py - RF forensic analysis tool

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pandas as pd
from datetime import datetime

class RFForensicAnalyzer:
    def __init__(self, capture_file):
        self.data = self.load_capture(capture_file)
        self.metadata = self.extract_metadata()
        self.signatures = self.load_attack_signatures()
    
    def load_capture(self, file_path):
        # Load data from RF capture file
        print(f"Loading RF capture from {file_path}")
        # Format: [timestamp, frequency, signal_strength, raw_data]
        return pd.read_csv(file_path)
    
    def extract_metadata(self):
        # Extract important metadata
        return {
            'start_time': self.data['timestamp'].min(),
            'end_time': self.data['timestamp'].max(),
            'duration_sec': (pd.to_datetime(self.data['timestamp'].max()) - 
                            pd.to_datetime(self.data['timestamp'].min())).total_seconds(),
            'frequency_range': [self.data['frequency'].min(), self.data['frequency'].max()],
            'signal_strength_range': [self.data['signal_strength'].min(), 
                                     self.data['signal_strength'].max()]
        }
    
    def load_attack_signatures(self):
        # Known attack signatures
        return {
            'replay_attack': {
                'pattern': 'repeated_identical_signals',
                'threshold': 3,
                'timeframe_sec': 60
            },
            'jamming': {
                'pattern': 'continuous_high_power',
                'threshold_dbm': -30,
                'duration_sec': 10
            },
            'spoofing': {
                'pattern': 'modified_device_id',
                'indicators': ['altered_checksum', 'invalid_sequence']
            }
        }
    
    def detect_attacks(self):
        results = {
            'potential_attacks': [],
            'anomalies': [],
            'timeline': {}
        }
        
        # Replay attack detection
        signal_groups = self.data.groupby('raw_data')
        for signal_data, group in signal_groups:
            if len(group) >= self.signatures['replay_attack']['threshold']:
                # Check temporal criteria
                timestamps = pd.to_datetime(group['timestamp'])
                if (timestamps.max() - timestamps.min()).total_seconds() <= \
                   self.signatures['replay_attack']['timeframe_sec']:
                    results['potential_attacks'].append({
                        'type': 'replay_attack',
                        'confidence': 'high',
                        'signal_data': signal_data[:20] + '...',  # Truncated for readability
                        'occurrences': len(group),
                        'timestamps': group['timestamp'].tolist(),
                    })
        
        # Jamming detection
        high_power_signals = self.data[self.data['signal_strength'] >= 
                                     self.signatures['jamming']['threshold_dbm']]
        
        if len(high_power_signals) > 0:
            # Group by continuous periods
            high_power_signals['timestamp'] = pd.to_datetime(high_power_signals['timestamp'])
            high_power_signals = high_power_signals.sort_values('timestamp')
            
            # Identify continuous periods of strong signal
            time_diffs = high_power_signals['timestamp'].diff().dt.total_seconds()
            new_group = time_diffs.isna() | (time_diffs > 1)  # New group if gap > 1s
            groups = new_group.cumsum()
            
            for group_id, group in high_power_signals.groupby(groups):
                duration = (group['timestamp'].max() - 
                           group['timestamp'].min()).total_seconds()
                
                if duration >= self.signatures['jamming']['threshold_dbm']:
                    results['potential_attacks'].append({
                        'type': 'jamming',
                        'confidence': 'medium',
                        'frequency': group['frequency'].mean(),
                        'avg_power': group['signal_strength'].mean(),
                        'duration_sec': duration,
                        'start_time': group['timestamp'].min(),
                        'end_time': group['timestamp'].max()
                    })
        
        return results
    
    def generate_report(self, output_file):
        attack_results = self.detect_attacks()
        
        with open(output_file, 'w') as f:
            f.write("===== RF FORENSIC ANALYSIS REPORT =====\n")
            f.write(f"Analysis date: {datetime.now()}\n\n")
            
            f.write("=== CAPTURE METADATA ===\n")
            for key, value in self.metadata.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\n=== POTENTIAL ATTACKS DETECTED ===\n")
            if len(attack_results['potential_attacks']) == 0:
                f.write("No attacks detected.\n")
            else:
                for i, attack in enumerate(attack_results['potential_attacks'], 1):
                    f.write(f"\nAttack #{i}:\n")
                    f.write(f"  Type: {attack['type']}\n")
                    f.write(f"  Confidence: {attack['confidence']}\n")
                    for key, value in attack.items():
                        if key not in ['type', 'confidence']:
                            f.write(f"  {key}: {value}\n")
            
            f.write("\n=== RECOMMENDATIONS ===\n")
            if any(a['type'] == 'replay_attack' for a in attack_results['potential_attacks']):
                f.write("- Implement rolling codes for all RF devices\n")
                f.write("- Add encryption for sensitive transmissions\n")
            
            if any(a['type'] == 'jamming' for a in attack_results['potential_attacks']):
                f.write("- Install RF jamming detectors\n")
                f.write("- Consider wired alternatives for critical systems\n")

# Usage
if __name__ == "__main__":
    analyzer = RFForensicAnalyzer("rf_capture_20240825.csv")
    analyzer.generate_report("rf_forensic_report.txt")
    print("Analysis completed and report generated.")
```

**WiFi Forensic Analysis**

*PCAP analysis with Wireshark:*
```bash
# Deauth attack extraction
tshark -r capture.pcap -Y "wlan.fc.type_subtype==0x000c" -T fields \
       -e frame.time_epoch -e wlan.sa -e wlan.da -e radiotap.dbm_antsignal

# Statistical analysis
tshark -r capture.pcap -q -z io,stat,30,"COUNT(wlan.fc.type_subtype==0x000c)"

# Suspicious AP information extraction
tshark -r capture.pcap -T fields -e wlan.bssid -e wlan.ssid \
       -e wlan.fc.type_subtype -e radiotap.channel.freq -Y "wlan.fc.type_subtype==8" | sort | uniq
```

*Beacon frame analysis script:*
```python
import pyshark
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime, timedelta

# Load capture
cap = pyshark.FileCapture('evil_twin_capture.pcap', display_filter='wlan.fc.type_subtype == 0x08')

# Beacon extraction
beacon_frames = []
for packet in cap:
    try:
        beacon_frames.append({
            'timestamp': float(packet.frame_info.time_epoch),
            'bssid': packet.wlan.bssid,
            'ssid': packet.wlan.ssid if hasattr(packet.wlan, 'ssid') else '[Hidden]',
            'channel': int(packet.wlan_radio.channel),
            'signal_strength': int(packet.wlan_radio.signal_dbm) if hasattr(packet.wlan_radio, 'signal_dbm') else None
        })
    except AttributeError:
        continue

cap.close()

# Data analysis
df = pd.DataFrame(beacon_frames)

# Detect duplicated SSIDs with different BSSIDs
ssid_groups = df.groupby('ssid')
duplicated_ssids = []

for ssid, group in ssid_groups:
    if len(group['bssid'].unique()) > 1 and ssid != '[Hidden]':
        duplicated_ssids.append({
            'ssid': ssid,
            'bssid_count': len(group['bssid'].unique()),
            'bssids': group['bssid'].unique().tolist(),
            'channels': group['channel'].unique().tolist(),
            'signal_strengths': group.groupby('bssid')['signal_strength'].mean().to_dict()
        })

# Display results
print(f"\n=== WIFI FORENSIC ANALYSIS REPORT ===\n")
print(f"Analysis date: {datetime.now()}\n")
print(f"Total beacon frames analyzed: {len(beacon_frames)}")
print(f"Unique access points detected: {len(df['bssid'].unique())}\n")

print("=== EVIL TWIN DETECTION ===\n")
if len(duplicated_ssids) == 0:
    print("No Evil Twin detected.")
else:
    print(f"{len(duplicated_ssids)} potentially duplicated SSIDs detected:\n")
    for i, ap in enumerate(duplicated_ssids, 1):
        print(f"#{i} SSID: {ap['ssid']}")
        print(f"  Number of BSSIDs: {ap['bssid_count']}")
        print("  Detected BSSIDs:")
        for j, bssid in enumerate(ap['bssids']):
            signal = ap['signal_strengths'].get(bssid, 'N/A')
            print(f"    {j+1}. {bssid} (Signal: {signal} dBm)")
        print(f"  Channels used: {', '.join(map(str, ap['channels']))}\n")

# Analysis-based recommendations
print("=== RECOMMENDATIONS ===\n")
if len(duplicated_ssids) > 0:
    print("1. Verify authenticity of the following access points:")
    for ap in duplicated_ssids:
        print(f"   - {ap['ssid']} (BSSIDs: {', '.join(ap['bssids'][:2])}...)")
    print("\n2. Implement Evil Twin detection system")
    print("3. Inform users about unsecured network risks")
    print("4. Implement 802.1X authentication for enterprise networks")
else:
    print("No immediate action required. Continue regular monitoring.")
```

## Chapter 11: Advanced Technical Countermeasures

### RF Device Security Hardening

**RF Defense Systems**

*Rolling code implementation:*
```c
// KeeLoq implementation example for doors/barriers
#include <KeeLoq.h>

// Manufacturer and device secret keys
uint64_t manufacturerKey = 0x5CAEDF21A3B4C908;
int deviceSerialNumber = 0x00012345;
uint64_t deviceKey;

// Generate unique key for each device
void initializeDevice() {
  deviceKey = KeeLoq::deriveKey(manufacturerKey, deviceSerialNumber);
  
  // Initial parameters
  uint32_t counter = 0;    // Synchronized counter
  uint32_t seed = random(0xFFFFFFFF);  // Random seed
  
  printf("Device initialized: SNR=%08X\n", deviceSerialNumber);
}

// Code generation for transmission
uint32_t generateRollingCode() {
  static uint32_t counter = 0;
  counter++;
  
  // Merge counter with device ID
  uint32_t plaintext = (deviceSerialNumber & 0xFFFF) | (counter << 16);
  
  // Code encryption
  uint32_t encrypted = KeeLoq::encrypt(plaintext, deviceKey);
  
  printf("Generated code: %08X (counter=%u)\n", encrypted, counter);
  return encrypted;
}

// Received code verification
bool validateRollingCode(uint32_t receivedCode) {
  // Code decryption
  uint32_t decrypted = KeeLoq::decrypt(receivedCode, deviceKey);
  
  // Component extraction
  uint16_t receivedSerialNumber = decrypted & 0xFFFF;
  uint16_t receivedCounter = decrypted >> 16;
  
  // Verify serial number
  if (receivedSerialNumber != (deviceSerialNumber & 0xFFFF)) {
    printf("Invalid serial number\n");
    return false;
  }
  
  // Verify counter (with tolerance window)
  static uint32_t lastCounter = 0;
  if (receivedCounter <= lastCounter) {
    printf("Replay attack detected! Counter=%u, Last=%u\n", 
           receivedCounter, lastCounter);
    return false;
  }
  
  // Valid code, update counter
  lastCounter = receivedCounter;
  printf("Valid code. New counter=%u\n", lastCounter);
  return true;
}
```

*RF jamming detection:*
```c
#include <RFDetection.h>
#include <Alert.h>
#include <MovingAverage.h>

RFDetector detector(433.92); // MHz
MovingAverage avgNoise(60);  // 60-second average
Alert securityAlert;

void setup() {
  Serial.begin(115200);
  detector.begin();
  securityAlert.begin();
  
  // Initial calibration
  Serial.println("Calibrating RF noise level...");
  delay(1000);
  
  // Measure ambient noise for 30 seconds
  unsigned long startTime = millis();
  while (millis() - startTime < 30000) {
    float currentNoise = detector.measureNoiseLevel();
    avgNoise.add(currentNoise);
    delay(500);
  }
  
  float baselineNoise = avgNoise.getAverage();
  float threshold = baselineNoise + 15.0; // +15dB above ambient noise
  
  detector.setJammingThreshold(threshold);
  Serial.print("Calibration complete. Baseline level: ");
  Serial.print(baselineNoise);
  Serial.print(" dBm, Alert threshold: ");
  Serial.print(threshold);
  Serial.println(" dBm");
}

void loop() {
  // Measure current RF level
  float currentLevel = detector.measureSignalLevel();
  float currentNoise = detector.measureNoiseLevel();
  
  // Update noise moving average
  avgNoise.add(currentNoise);
  
  // Check if jamming detected
  if (detector.isJammingDetected()) {
    // Immediate alert
    Serial.print("ALERT! RF jamming detected! Level: ");
    Serial.print(currentLevel);
    Serial.print(" dBm, Threshold: ");
    Serial.print(detector.getJammingThreshold());
    Serial.println(" dBm");
    
    securityAlert.trigger("RF_JAMMING", 
                         "RF jamming detected on " + String(detector.getFrequency()) + " MHz");
    
    // Automatic actions
    activateBackupSystems();
    notifySecurityPersonnel();
    
    // Wait before resetting alert
    delay(10000);
    securityAlert.reset();
  } else {
    // Normal monitoring
    Serial.print("RF level: ");
    Serial.print(currentLevel);
    Serial.print(" dBm, Average noise: ");
    Serial.print(avgNoise.getAverage());
    Serial.println(" dBm");
  }
  
  // Dynamically adapt detection threshold
  float dynamicThreshold = avgNoise.getAverage() + 15.0;
  detector.setJammingThreshold(dynamicThreshold);
  
  delay(1000);
}

void activateBackupSystems() {
  // Activate backup systems
  Serial.println("Activating backup systems...");
}

void notifySecurityPersonnel() {
  // Notify security personnel
  Serial.println("Notification sent to security team");
}
```

### Advanced WiFi Security

**Enterprise WiFi Security Configuration**

*802.1X with RADIUS configuration:*
```bash
# /etc/hostapd/hostapd.conf
interface=wlan0
driver=nl80211
ssid=CompanySecureWiFi
hw_mode=g
channel=6
ieee8021x=1
auth_algs=1
wpa=2
wpa_key_mgmt=WPA-EAP
wpa_pairwise=CCMP
rsn_pairwise=CCMP

# RADIUS configuration
auth_server_addr=10.0.0.10
auth_server_port=1812
auth_server_shared_secret=your_secret_key_here

# Management Frame Protection
wmm_enabled=1
wmm_ac_bk_cwmin=4
wmm_ac_bk_cwmax=10
wmm_ac_bk_aifs=7
wmm_ac_bk_txop_limit=0
wmm_ac_be_aifs=3
wmm_ac_be_cwmin=4
wmm_ac_be_cwmax=10
wmm_ac_be_txop_limit=0
wmm_ac_vi_aifs=2
wmm_ac_vi_cwmin=3
wmm_ac_vi_cwmax=4
wmm_ac_vi_txop_limit=94
wmm_ac_vo_aifs=2
wmm_ac_vo_cwmin=2
wmm_ac_vo_cwmax=3
wmm_ac_vo_txop_limit=47

# Enable 802.11w (Management Frame Protection)
wme_enabled=1
ieee80211w=2
group_mgmt_cipher=AES-128-CMAC
```

*Deauthentication detection script:*
```python
#!/usr/bin/env python3
# deauth_detector.py - Deauthentication attack detector

import pyshark
import datetime
import smtplib
from collections import defaultdict
from email.mime.text import MIMEText

class DeauthDetector:
    def __init__(self):
        self.deauth_threshold = 20  # Number of deauth frames per second
        self.monitoring_interface = "wlan0mon"
        self.time_window = 5  # Time window in seconds
        self.deauth_counter = defaultdict(list)
        self.authorized_aps = self._load_authorized_aps()
        
    def _load_authorized_aps(self):
        # Load authorized access points list
        authorized = {}
        with open("authorized_aps.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    authorized[parts[0]] = {'ssid': parts[1], 'channel': parts[2] if len(parts) > 2 else None}
        return authorized
    
    def _alert(self, message):
        print(f"[ALERT] {message}")
        
        # Send email alert
        try:
            msg = MIMEText(message)
            msg['Subject'] = "[SECURITY ALERT] WiFi Deauth Attack Detected"
            msg['From'] = "security_system@example.com"
            msg['To'] = "security_team@example.com"
            
            smtp = smtplib.SMTP('smtp.example.com')
            smtp.sendmail("security_system@example.com", 
                         ["security_team@example.com"], 
                         msg.as_string())
            smtp.quit()
        except Exception as e:
            print(f"Failed to send email alert: {e}")
    
    def _clean_old_entries(self, current_time):
        # Clean entries older than time_window
        for mac, timestamps in list(self.deauth_counter.items()):
            self.deauth_counter[mac] = [ts for ts in timestamps 
                                    if (current_time - ts).total_seconds() < self.time_window]
            if not self.deauth_counter[mac]:
                del self.deauth_counter[mac]
    
    def start_monitoring(self):
        print(f"Starting deauth detection on {self.monitoring_interface}...")
        
        # Real-time capture
        capture = pyshark.LiveCapture(interface=self.monitoring_interface,
                                     display_filter='wlan.fc.type_subtype == 0x000c')
        
        try:
            for packet in capture.sniff_continuously():
                self._process_packet(packet)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
    
    def _process_packet(self, packet):
        try:
            # Extract packet information
            timestamp = datetime.datetime.now()
            if hasattr(packet.wlan, 'sa') and hasattr(packet.wlan, 'bssid'):
                sender = packet.wlan.sa
                bssid = packet.wlan.bssid
                
                # Check if it's an authorized AP
                is_authorized = bssid in self.authorized_aps
                
                # Add timestamp
                self.deauth_counter[sender].append(timestamp)
                
                # Clean old entries
                self._clean_old_entries(timestamp)
                
                # Check if threshold exceeded
                if len(self.deauth_counter[sender]) >= self.deauth_threshold:
                    alert_msg = f"Possible deauth attack detected!\n"
                    alert_msg += f"Sender MAC: {sender}\n"
                    alert_msg += f"BSSID: {bssid}\n"
                    alert_msg += f"Count: {len(self.deauth_counter[sender])} frames in {self.time_window}s\n"
                    alert_msg += f"Time: {timestamp}\n"
                    
                    if is_authorized:
                        alert_msg += f"WARNING: Attack targets an authorized AP!\n"
                        alert_msg += f"SSID: {self.authorized_aps[bssid]['ssid']}\n"
                    
                    self._alert(alert_msg)
                    
                    # Reset counter to avoid burst alerts
                    self.deauth_counter[sender] = []
            
        except Exception as e:
            print(f"Error processing packet: {e}")

# Usage
if __name__ == "__main__":
    detector = DeauthDetector()
    detector.start_monitoring()
```

**Dynamic WiFi Security System**

*Dynamic WIDS/WIPS configuration:*
```yaml
# config.yml - Dynamic WIDS/WIPS System

system:
  name: "Enterprise-WIDS"
  version: 1.0
  mode: "active"  # passive or active
  interfaces:
    - wlan0mon
    - wlan1mon

monitoring:
  scan_interval: 60  # seconds
  channels:
    - 1
    - 6
    - 11
    - 36
    - 40
  dwell_time: 5  # seconds per channel

detection:
  rogue_ap:
    enabled: true
    ssid_whitelist:
      - "CompanyWiFi"
      - "CompanyWiFi-Guest"
      - "CompanyWiFi-IoT"
    alert_threshold: "high"
    auto_response: "locate"
  
  evil_twin:
    enabled: true
    check_beacon_fingerprint: true
    check_probe_response: true
    alert_threshold: "critical"
    auto_response: "notify_block"
  
  deauth_attack:
    enabled: true
    frames_threshold: 20
    time_window: 5  # seconds
    alert_threshold: "critical"
    auto_response: "notify_jam_attacker"
  
  karma_attack:
    enabled: true
    probe_request_honeypot: true
    honeypot_ssids:
      - "Free-Airport-WiFi"
      - "PublicWiFi"
      - "CoffeeShop"
    alert_threshold: "high"
    auto_response: "notify_log"

notification:
  email:
    enabled: true
    smtp_server: "smtp.company.com"
    port: 587
    use_tls: true
    username: "wids-alerts@company.com"
    recipients:
      - "security-team@company.com"
      - "it-oncall@company.com"
  
  siem:
    enabled: true
    type: "syslog"
    server: "10.0.0.50"
    port: 514
    protocol: "tcp"
    facility: "local0"
    severity_mapping:
      critical: "emerg"
      high: "alert"
      medium: "warning"
      low: "info"

response:
  active_defense:
    enabled: true
    deauth_rogue: true
    channel_switch: true
    notify_clients: true
  
  evidence_collection:
    enabled: true
    pcap_storage: "/var/log/wids/captures/"
    retention_days: 30
    auto_analyze: true
```

## Chapter 12: Ethics and Legal Compliance

### Legal Framework and Authorizations

Before conducting any Red Team operations using the Flipper Zero and Predator module, it is imperative to obtain the necessary legal authorizations. Here are the crucial elements to consider:

1. **Written Authorization** - Obtain an official mandate signed by the management of the targeted organization that precisely describes:
   - Scope of tests (buildings, systems, networks)
   - Duration of operations
   - Authorized and prohibited techniques
   - Emergency procedure in case of problems

2. **Regulatory Compliance** - Verify the legality of actions according to:
   - National legislation on computer intrusions
   - Radio communications regulations
   - Personal data protection laws
   - Specific sector regulations (finance, health, etc.)

3. **Non-prosecution Clause** - Legal document protecting pentesters against potential legal action if actions remain within the defined framework.
### Ethical Boundaries and Safety

The use of Flipper Zero with Predator module for Red Team operations must respect strict ethical limits:

1. **Proportionality** - Use only the techniques necessary to demonstrate vulnerability without causing excessive damage.

2. **Confidentiality** - Protect all sensitive data obtained during tests and destroy it after authorized use.

3. **Non-disruption** - Avoid any action that may interrupt critical services or endanger people.

4. **Prohibited techniques**:
   - Use of RF jamming in sensitive areas (hospitals, airports, emergency services)
   - Interception of personal data unrelated to the test
   - Prolonged denial of service on essential infrastructures
   - Exploitation of vulnerabilities to access data outside the defined perimeter

5. **Documentation and transparency** - Precisely document all actions taken and share them only with authorized persons.

### Authorization Document Template

```
                    RED TEAM PENETRATION TEST AUTHORIZATION

Date: [DATE]
Reference: [REFERENCE/ID]

1. PARTIES

Client ("the Organization"):
[ORGANIZATION NAME]
[COMPLETE ADDRESS]
Represented by: [FIRST NAME, LAST NAME], [POSITION]

Provider ("the Red Team"):
[COMPANY OR TEAM NAME]
[COMPLETE ADDRESS]
Represented by: [FIRST NAME, LAST NAME], [POSITION]

2. PURPOSE

The Organization authorizes the Red Team to perform penetration tests, including social engineering techniques, physical access, and technical vulnerability exploitation, to evaluate its security level.

3. SCOPE

Physical sites included:
- [BUILDING A, ADDRESS]
- [BUILDING B, ADDRESS]

Systems and networks included:
- WiFi networks: [SSID LIST]
- RF systems: [SYSTEMS LIST, DOORS, BARRIERS]
- Other devices: [SPECIFY]

4. AUTHORIZATION PERIOD

Start date: [DD/MM/YYYY], [TIME]
End date: [DD/MM/YYYY], [TIME]

5. AUTHORIZED TECHNIQUES

- [X] RF signal capture and replay
- [X] WiFi network attacks
- [X] Badge cloning
- [X] Active reconnaissance
- [ ] RF jamming
- [ ] Denial of service

6. EMERGENCY CONTACTS

Organization side:
[NAME], [POSITION], [24/7 PHONE], [EMAIL]

Red Team side:
[NAME], [POSITION], [24/7 PHONE], [EMAIL]

7. NON-PROSECUTION CLAUSE

The Organization commits not to legally prosecute the Red Team for actions conducted strictly within the scope and techniques authorized in this document.

8. SIGNATURES

________________________           ________________________
For the Organization                For the Red Team

[NAME, DATE]                       [NAME, DATE]
```

## Chapter 13: Conclusion

### Integration into a Global Security Strategy

The use of Flipper Zero with the Predator module in Red Team/Blue Team exercises represents one element of a broader security strategy. This approach should be integrated into:

1. **Comprehensive security program** - Supplement with code audits, vulnerability testing, architecture reviews, etc.

2. **Continuous training** - Use exercise results to improve IT team training and raise user awareness.

3. **Process improvement** - Regularly revise security and incident management procedures based on identified vulnerabilities.

4. **Technology watch** - Stay informed about new attack and defense techniques in the RF and WiFi domains.

5. **Purple Team approach** - Foster collaboration between Red Team and Blue Team to maximize learning and defense effectiveness.

### Summary of Acquired Skills

**Red Team Skills:**
- Advanced configuration of Flipper Zero and Predator module
- Execution of sophisticated RF attacks
- Implementation of targeted WiFi attacks
- Analysis and exploitation of wireless protocols
- Non-intrusive reconnaissance techniques

**Blue Team Skills:**
- Real-time detection of RF and WiFi attacks
- Configuration of robust defense systems
- Forensic analysis of wireless incidents
- Deployment of effective countermeasures
- Integration of alerts into SOC

**Cross-functional Skills:**
- Structured testing methodology
- RF/WiFi risk assessment
- Vulnerability documentation
- Technical communication between teams
- Knowledge of legal and ethical framework

## Appendix: Additional Resources

### Documentation and Manuals

**Flipper Zero and Predator Module:**
- [Official Flipper Zero Documentation](https://docs.flipperzero.one/)
- [Predator Module Technical Guide](https://github.com/RogueMaster/flipperzero-firmware-wPlugins/)
- [Awesome Flipper Zero - Resource Collection](https://github.com/djsime1/awesome-flipperzero)

**RF Security:**
- "Software Defined Radio for Hackers" - Michael Ossmann
- "Practical Signal Processing and RF System Design" - B. Forouzan
- [RF Security Research Repository](https://github.com/mossmann/hackrf/wiki/Documentation)

**WiFi Security:**
- "Attacking and Defending WiFi Networks" - J. Wright
- [WiFi Security Testing Framework Guide](https://wifisecurityblog.com/)
- [Aircrack-ng Documentation](https://www.aircrack-ng.org/documentation.html)

### Complementary Tools

**RF Analysis:**
- [GQRX](https://gqrx.dk/) - Software Defined Radio Receiver
- [Universal Radio Hacker](https://github.com/jopohl/urh) - Radio protocol analysis
- [rtl_433](https://github.com/merbanan/rtl_433) - 433/868/915 MHz protocol decoder

**WiFi Security:**
- [Kismet](https://www.kismetwireless.net/) - Wireless network detection and WIDS
- [Wireshark](https://www.wireshark.org/) - Network protocol analyzer
- [Aircrack-ng Suite](https://www.aircrack-ng.org/) - WiFi security audit

**Forensics:**
- [PyShark](https://github.com/KimiNewt/pyshark) - Python wrapper for tshark
- [Scapy](https://scapy.net/) - Network packet manipulation
- [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) - Network forensic analyzer

---

*This guide was designed for educational and security training purposes. All described techniques must be used only within a legal and ethical framework, with appropriate authorizations.*

© 2024 - Guide Red Team & Blue Team - v1.0

## Chapter 14: Automotive Security

### Rolling Code Vulnerabilities

Modern vehicle security systems use rolling codes in their remote controls. This technology, designed to prevent simple signal copying, presents a major vulnerability when confronted with custom firmware on the Flipper Zero.

A major security concern has recently emerged regarding modern vehicle security. A custom firmware known as "DarkWeb" for the Flipper Zero allows bypassing rolling code security systems used in many modern cars, including:

- Chrysler
- Dodge
- Fiat
- Ford
- Hyundai
- Jeep
- Kia
- Mitsubishi
- Subaru

### Custom Firmwares and Vehicle Exploits

**It is important to understand that the claim "a Flipper Zero firmware can open all cars" is an oversimplification**. Several custom firmwares exist with different capabilities for exploiting automotive systems. Here are the main ones:

1. **DarkWeb Firmware** - Most specialized for automotive attacks
   - Current version: 3.5.8
   - Specialty: Analysis and cloning of rolling codes with a single sample
   - Vulnerable brands: Primarily American and Asian models with 433.92 MHz remotes
   - Main technique: Mathematical analysis of code generation algorithm
   - Limitation: Does not work on all vehicles (approximately 65-70% success rate on compatible models)
   - User interface: Specialized DarkWeb console with advanced hexadecimal display

2. **RollBack Firmware** - Specifically targeting desynchronization vulnerabilities
   - Current version: 2.8
   - Specialty: Forces the vehicle system to accept previously used codes
   - Vulnerable brands: Certain European and American models (2015-2020)
   - Main technique: Forced desynchronization attack
   - Limitation: Requires favorable RF conditions and proximity

3. **KeyMaster Firmware** (RogueMaster variant)
   - Current version: 4.2
   - Specialty: Extended library of proprietary automotive protocols
   - Main technique: Brute forcing limited combinations of certain systems
   - Interface: Advanced graphical with protocol browser
   - Effectiveness: Variable depending on model (30-50% on average)

4. **UniRF Pro**
   - Current version: 2.7
   - Specialty: Signal amplification and digital processing for longer-range captures
   - Main technique: Improving captured signal quality
   - Particularly effective for: Older vehicles with simpler systems

This vulnerability is particularly concerning because it requires **only a single capture** of a car key fob signal to compromise the entire vehicle security system.

### Exploit Mechanism

Unlike traditional attacks that require signal jamming and multiple captures, the DarkWeb exploit works with a single capture of a key fob button press. Two main methods are used:

1. **Sequence Reverse Engineering:** The firmware analyzes the single capture to determine the rolling code generation algorithm and predict subsequent codes.

2. **RollBack Attack:** The exploit uses a desynchronization technique to force the vehicle receiver to accept older codes, thus bypassing the rolling code protection.

Once exploited, this vulnerability allows the attacker to emulate all functions of the original key fob (unlock, lock, trunk, start).

**Important consequence:** Following the attack, the owner's original key fob becomes desynchronized and unusable until the system is reset.

#### 🔴 Procédure Red Team : Évaluation de la Vulnérabilité
### Red Team Procedure: Vulnerability Assessment

**Matériel nécessaire / Required Equipment:**
- Flipper Zero avec firmware DarkWeb
- Antenne Sub-GHz optimisée
- Ordinateur portable pour l'analyse

**Méthodologie de test (Red Team) :**

1. **Reconnaissance et préparation**
```bash
# Identification du véhicule cible et type de télécommande
- Noter la marque, modèle et année
- Observer la fréquence typique (433.92 MHz EU/315 MHz US)
- Rechercher des informations sur le type de chiffrement utilisé
- Préparer le Flipper Zero avec firmware DarkWeb v3.5+
- Assurer une batterie complètement chargée
- Préparer l'antenne Sub-GHz optimisée (>5dBi recommandé)
```

2. **Capture du signal - Méthode optimisée**
```bash
Flipper Zero → SubGHz → Read RAW
- Fréquence : 433.92 MHz (ou 315 MHz selon région)
- Taux d'échantillonnage : 4MHz (supérieur au standard)
- Mode d'amplitude : AM650 (optimisé pour télécommandes automobiles)
- Se positionner à une distance de 5-15m du véhicule
- Demander au propriétaire d'appuyer sur un bouton de sa télécommande
- Enregistrer le signal complet (un seul appui suffit)
- Enregistrer sous un nom de fichier descriptif (ex: "Jeep_Grand_Cherokee_2022_unlock.sub")
```

3. **Analyse et décodage**
```bash
# Vérification de la vulnérabilité
Flipper Zero → SubGHz → DarkWeb Menu → RollJam Analysis
- Charger le signal capturé
- Lancer l'analyse des codes tournants
- Vérifier la compatibilité avec les exploits connus
- Si compatible, extraire le protocole et les paramètres
- Identifier le fabricant de la puce de télécommande
- Générer une clé d'émulation unique
```

4. **Test d'émulation et vérification**
```bash
Flipper Zero → SubGHz → DarkWeb Menu → RollCode Emulate
- Sélectionner le signal analysé
- Choisir la fonction à émuler (Lock/Unlock/Trunk)
- Tester à distance croissante du véhicule ciblé (5m, 10m, 20m)
- Répéter l'opération 3 fois pour confirmer la fiabilité
- Vérifier les fonctions d'émulation supplémentaires (coffre, alarme, etc.)
- Tenter un cycle complet (verrouillage puis déverrouillage)
- Documenter chaque résultat avec vidéo
```

5. **Test de désynchronisation**
```bash
# Vérification de l'impact sur la télécommande d'origine
- Demander au propriétaire d'utiliser sa télécommande après l'attaque
- Noter le nombre d'essais avant que la télécommande originale fonctionne à nouveau
- Tester si l'émulation fonctionne encore après résynchronisation
- Documenter le comportement du système de sécurité du véhicule
```

**Procédure de vérification Blue Team :**

1. **Configuration du système de surveillance**
```bash
# Mise en place du moniteur RF indépendant
- Configurer un RTL-SDR avec GNU Radio
- Fréquence centrale : 433.92 MHz (ou 315 MHz selon région)
- Bande passante : 2MHz minimum
- Enregistrer l'activité RF pendant toute la durée du test
- Configurer l'analyse spectrale en temps réel
```

2. **Vérification de l'exploit**
```bash
# Méthodologie de validation Blue Team
- Observer l'activité RF pendant la capture Red Team
- Vérifier l'enregistrement et l'analyse du signal
- Confirmer que le signal capturé est de qualité suffisante
- Observer le comportement du véhicule lors de l'émulation
- Valider la désynchronisation de la télécommande originale
```

3. **Détection des marqueurs d'attaque**
```bash
# Identification des indicateurs d'exploitation
- Capturer l'empreinte RF spécifique de l'émulation DarkWeb
- Noter les différences avec l'émission légitime
- Identifier les marqueurs de manipulation du code tournant
- Mesurer les temps d'émission par rapport aux normes
- Détecter les anomalies dans la séquence de code
```

**Résultats documentés (Red Team & Blue Team) :**

- Succès/échec de l'exploitation pour chaque modèle testé
- Pourcentage de réussite sur plusieurs essais (min. 10 tests)
- Mesure de la distance maximale d'efficacité de l'exploitation
- Impact exact sur la télécommande originale (nombre d'appuis nécessaires pour résynchroniser)
- Délai avant résynchronisation automatique éventuelle
- Marqueurs RF spécifiques de l'attaque pour détection future
- Journalisation complète avec horodatage précis
- Preuve de concept vidéo (pour documentation interne uniquement)

#### 🔵 Stratégie Blue Team : Détection et Mitigation Avancée
### Blue Team Strategy: Advanced Detection and Mitigation

**Détection technique détaillée pour les exploits de firmware personnalisés :**

1. **Surveillance RF en temps réel** - Implémentation de systèmes de détection RF avancés :
   - **Matériel nécessaire :**
     - Récepteurs SDR (Software Defined Radio) comme HackRF, RTL-SDR ou YARD Stick One
     - Antennes directionnelles 433.92 MHz et 315 MHz
     - Logiciel d'analyse spectrale (GQRX, GNU Radio, Universal Radio Hacker)
   
   - **Configuration spécifique pour la détection des firmwares exploitant les télécommandes :**
   ```bash
   # Configuration du SDR pour détection DarkWeb
   rtl_433 -f 433.92M -H 60 -s 2M -R 0 -A -a
   
   # Détection des anomalies avec GNU Radio
   osmocom_fft -a hackrf -f 433.92M -s 8M --fft-rate=30 --peak-hold
   ```

2. **Signatures des exploits par firmware** - Marqueurs spécifiques à détecter :

   - **DarkWeb Firmware :**
     - Répétitions anormales du préambule (4-5 fois contre 2-3 normalement)
     - Durée d'émission plus longue (>300ms contre 150-200ms normalement)
     - Structure de signal modifiée (bits de redondance manquants)
     - Fréquence légèrement décalée (+/- 100kHz de la fréquence standard)

   - **RollBack Firmware :**
     - Impulsions de désynchronisation rapides avant le signal principal
     - Motifs de répétition non standard (4-7-4 contre 3-3-3 normalement)
     - Présence de blocs de données spécifiques "0xFE" dans l'en-tête

   - **KeyMaster/RogueMaster :**
     - Tentatives séquentielles multiples (brute force) à intervalles précis (400ms)
     - Signatures d'amplification non linéaire dans le signal
     - Transmission sur plusieurs canaux parallèles

3. **Détection par apprentissage automatique** - Implémentation de modèles d'IA pour identifier les signaux anormaux :
   ```bash
   # Installation des dépendances pour le système de détection par IA
   pip install tensorflow scipy numpy matplotlib scikit-learn
   
   # Exécution du modèle avec référence à la base de signatures légitimes
   python rf_anomaly_detector.py --source rtlsdr --freq 433.92e6 --model cnn_vehicle_model.h5
   ```

4. **Forensique RF pour analyse post-incident** - Configuration d'un système d'enregistrement permanent :
   ```bash
   # Enregistrement continu pour analyse forensique
   rtl_sdr -f 433.92e6 -s 2048k -g 40 - | sox -t raw -r 2048k -b 8 -e unsigned -c 1 - parking_monitoring.wav
   ```

**Surveillance des anomalies et détection physique :**

1. **Intégration à la vidéosurveillance** - Corrélation entre signaux RF et activité physique :
   - Système de détection pour les événements suivants :
   - Ouverture/fermeture du véhicule sans présence physique d'une personne avec clé
   - Tentatives multiples de déverrouillage dans un court laps de temps
   - Désynchronisation soudaine de télécommandes légitimes
   - Présence d'individus utilisant des dispositifs électroniques à proximité des véhicules

2. **Détection des anomalies du véhicule** - Pour les véhicules équipés de télématique :
   ```bash
   # Analyse des journaux OBD-II pour détecter les ouvertures anormales
   python obd2_analyzer.py --port /dev/ttyUSB0 --watch-pid 0x0102,0x0103 --alert-threshold 3
   ```

3. **Détection des dispositifs Flipper Zero actifs** :
   - Installation de Bluetooth Low Energy (BLE) scanners
   - Détection des signatures RF spécifiques des Flipper Zero actifs
   - Analyse de trafic pour identifier les signatures USB lors des connexions

   ```bash
   # Détection de Flipper Zero via Bluetooth
   sudo bluetoothctl scan on | grep -E "Flipper|DarkFlipper|FZero"
   
   # Surveillance USB pour les signatures Flipper
   sudo usbmon -i | grep -E "03eb:2ff[0-9]"
   ```

**Exemple de code pour la détection RF (Python) :**

```python
class RollingCodeMonitor:
    def __init__(self, freq=433.92e6):
        self.sdr = rtlsdr.RtlSdr()
        self.sdr.sample_rate = 2.4e6
        self.sdr.center_freq = freq
        self.sdr.gain = 'auto'
        self.baseline = self.establish_baseline()
    
    def establish_baseline(self):
        samples = self.sdr.read_samples(256*1024)
        return self.analyze_signal_features(samples)
    
    def analyze_signal_features(self, samples):
        # Extrait les caractéristiques du signal pour comparaison future
        power = np.mean(np.abs(samples)**2)
        psd = np.abs(np.fft.fft(samples))**2
        peak_freq = np.argmax(psd)
        return {'power': power, 'peak_freq': peak_freq, 'psd_shape': psd[:1024]}
    
    def detect_anomalies(self):
        current = self.sdr.read_samples(256*1024)
        features = self.analyze_signal_features(current)
        
        # Détecte les signatures spécifiques à DarkWeb
        if self.is_darkweb_signature(features):
            return "ALERTE: Signature DarkWeb détectée!"
            
        # Détecte les tentatives RollBack
        if self.is_rollback_attempt(current):
            return "ALERTE: Tentative d'attaque RollBack en cours!"
        
        return "Aucune anomalie détectée"
    
    def is_darkweb_signature(self, features):
        # Implémentation des règles de détection DarkWeb
        power_anomaly = features['power'] > self.baseline['power'] * 1.5
        freq_shift = abs(features['peak_freq'] - self.baseline['peak_freq']) > 20
        return power_anomaly and freq_shift
    
    def is_rollback_attempt(self, samples):
        # Détecte les impulsions rapides caractéristiques d'une attaque RollBack
        edges = np.diff(np.abs(samples) > np.mean(np.abs(samples)) * 1.5)
        edge_count = np.sum(edges > 0)
        timing = self.analyze_pulse_timing(edges)
        
        return edge_count > 30 and self.has_suspicious_pattern(timing)
    
    def has_suspicious_pattern(self, timing):
        # Vérifie les motifs de répétition suspects (4-7-4 pattern)
        pattern = [4, 7, 4]  # Motif caractéristique RollBack
        # Implémentation de l'algorithme de correspondance de motif
        return pattern_match_score(timing, pattern) > 0.8

# Utilisation
monitor = RollingCodeMonitor(freq=433.92e6)
while True:
    result = monitor.detect_anomalies()
    if "ALERTE" in result:
        send_notification(result)
    time.sleep(0.5)
```

**English :**

### Blue Team Strategy: Advanced Detection and Mitigation

**Technical detection details for custom firmware exploits:**

1. **Real-time RF monitoring** - Implementation of advanced RF detection systems:
   - **Required hardware:**
     - Software Defined Radio (SDR) receivers like HackRF, RTL-SDR or YARD Stick One
     - Directional antennas for 433.92 MHz and 315 MHz
     - Spectrum analysis software (GQRX, GNU Radio, Universal Radio Hacker)
   
   - **Specific configuration for detecting firmware exploiting key fobs:**
   ```bash
   # SDR configuration for DarkWeb detection
   rtl_433 -f 433.92M -H 60 -s 2M -R 0 -A -a
   
   # Anomaly detection with GNU Radio
   osmocom_fft -a hackrf -f 433.92M -s 8M --fft-rate=30 --peak-hold
   ```

2. **Firmware-specific exploit signatures** - Specific markers to detect:

   - **DarkWeb Firmware:**
     - Abnormal preamble repetitions (4-5 times vs 2-3 normally)
     - Longer emission duration (>300ms vs 150-200ms normally)
     - Modified signal structure (missing redundancy bits)
     - Slightly shifted frequency (+/- 100kHz from standard frequency)

   - **RollBack Firmware:**
     - Fast desynchronization pulses before the main signal
     - Non-standard repetition patterns (4-7-4 vs 3-3-3 normally)
     - Presence of specific "0xFE" data blocks in the header

   - **KeyMaster/RogueMaster:**
     - Multiple sequential attempts (brute force) at precise intervals (400ms)
     - Non-linear amplification signatures in the signal
     - Transmission on multiple parallel channels

3. **Machine learning detection** - Implementation of AI models to identify anomalous signals:
   ```bash
   # Installation of dependencies for AI detection system
   pip install tensorflow scipy numpy matplotlib scikit-learn
   
   # Running the model with reference to legitimate signature database
   python rf_anomaly_detector.py --source rtlsdr --freq 433.92e6 --model cnn_vehicle_model.h5
   ```

4. **RF forensics for post-incident analysis** - Configuration of a permanent recording system:
   ```bash
   # Continuous recording for forensic analysis
   rtl_sdr -f 433.92e6 -s 2048k -g 40 - | sox -t raw -r 2048k -b 8 -e unsigned -c 1 - parking_monitoring.wav
   ```

**Anomaly monitoring and physical detection:**

1. **Video surveillance integration** - Correlation between RF signals and physical activity:
   - Detection system for the following events:
   - Vehicle opening/closing without physical presence of a person with key
   - Multiple unlocking attempts in a short time period
   - Sudden desynchronization of legitimate key fobs
   - Presence of individuals using electronic devices near vehicles

2. **Vehicle anomaly detection** - For vehicles equipped with telematics:
   ```bash
   # OBD-II log analysis to detect abnormal openings
   python obd2_analyzer.py --port /dev/ttyUSB0 --watch-pid 0x0102,0x0103 --alert-threshold 3
   ```

3. **Detection of active Flipper Zero devices**:
   - Installation of Bluetooth Low Energy (BLE) scanners
   - Detection of RF signatures specific to active Flipper Zero
   - Traffic analysis to identify USB signatures during connections

   ```bash
   # Flipper Zero detection via Bluetooth
   sudo bluetoothctl scan on | grep -E "Flipper|DarkFlipper|FZero"
   
   # USB monitoring for Flipper signatures
   sudo usbmon -i | grep -E "03eb:2ff[0-9]"
   ```

**Example code for RF detection (Python):**

```python
class RollingCodeMonitor:
    def __init__(self, freq=433.92e6):
        self.sdr = rtlsdr.RtlSdr()
        self.sdr.sample_rate = 2.4e6
        self.sdr.center_freq = freq
        self.sdr.gain = 'auto'
        self.baseline = self.establish_baseline()
    
    def establish_baseline(self):
        samples = self.sdr.read_samples(256*1024)
        return self.analyze_signal_features(samples)
    
    def analyze_signal_features(self, samples):
        # Extract signal features for future comparison
        power = np.mean(np.abs(samples)**2)
        psd = np.abs(np.fft.fft(samples))**2
        peak_freq = np.argmax(psd)
        return {'power': power, 'peak_freq': peak_freq, 'psd_shape': psd[:1024]}
    
    def detect_anomalies(self):
        current = self.sdr.read_samples(256*1024)
        features = self.analyze_signal_features(current)
        
        # Detect DarkWeb-specific signatures
        if self.is_darkweb_signature(features):
            return "ALERT: DarkWeb signature detected!"
            
        # Detect RollBack attempts
        if self.is_rollback_attempt(current):
            return "ALERT: RollBack attack attempt in progress!"
        
        return "No anomaly detected"
    
    def is_darkweb_signature(self, features):
        # Implementation of DarkWeb detection rules
        power_anomaly = features['power'] > self.baseline['power'] * 1.5
        freq_shift = abs(features['peak_freq'] - self.baseline['peak_freq']) > 20
        return power_anomaly and freq_shift
    
    def is_rollback_attempt(self, samples):
        # Detect fast pulses characteristic of a RollBack attack
        edges = np.diff(np.abs(samples) > np.mean(np.abs(samples)) * 1.5)
        edge_count = np.sum(edges > 0)
        timing = self.analyze_pulse_timing(edges)
        
        return edge_count > 30 and self.has_suspicious_pattern(timing)
    
    def has_suspicious_pattern(self, timing):
        # Check for suspicious repetition patterns (4-7-4 pattern)
        pattern = [4, 7, 4]  # Characteristic RollBack pattern
        # Implementation of pattern matching algorithm
        return pattern_match_score(timing, pattern) > 0.8

# Usage
monitor = RollingCodeMonitor(freq=433.92e6)
while True:
    result = monitor.detect_anomalies()
    if "ALERT" in result:
        send_notification(result)
    time.sleep(0.5)
```

#### 🔵 Recommandations Blue Team pour la mitigation
### Blue Team Mitigation Recommendations

**Français :**

1. **Mise à jour des systèmes de sécurité** - Recommander des mises à niveau pour les systèmes vulnérables :
   - Conversion vers des systèmes à code dynamique à haute entropie
   - Migration vers des systèmes à authentification multifacteur (clé physique + code)
   - Implémentation de systèmes d'authentification biométrique complémentaires

2. **Zones sécurisées RF** - Établir des périmètres protégés :
   - Installation de cages de Faraday dans les zones sensibles de stationnement
   - Utilisation de brouilleurs RF ciblés légaux (dans le cadre réglementaire)
   - Déploiement de capteurs RF connectés au système d'alarme

3. **Formation et sensibilisation** - Former les équipes de sécurité et les utilisateurs :
   - Programmes de sensibilisation sur les risques liés aux télécommandes automobiles
   - Procédures d'alerte en cas de suspicion d'attaque
   - Méthodes de vérification de l'intégrité des systèmes d'accès

**English :**

1. **Security System Updates** - Recommend upgrades for vulnerable systems:
   - Conversion to high-entropy dynamic code systems
   - Migration to multi-factor authentication systems (physical key + code)
   - Implementation of complementary biometric authentication systems

2. **RF Secure Zones** - Establish protected perimeters:
   - Installation of Faraday cages in sensitive parking areas
   - Use of legal targeted RF jammers (within regulatory framework)
   - Deployment of RF sensors connected to the alarm system

3. **Training and Awareness** - Train security teams and users:
   - Awareness programs on risks related to automotive remote controls
   - Alert procedures in case of suspected attack
   - Methods for verifying the integrity of access systems

#### 🔵 Recommandations de sécurité supplémentaires
### Additional Security Recommendations

**Français :**

1. **Développement d'une base de données de signatures** - Créer un référentiel des signatures d'attaques :
   - Cataloguer les motifs de signaux par firmware malicieux
   - Partager les signatures entre les équipes de sécurité et constructeurs
   - Implémenter un système de mise à jour automatique des signatures

2. **Réponse aux incidents standardisée** - Établir des procédures :
   - Isolation immédiate des véhicules potentiellement compromis
   - Réinitialisation sécurisée des systèmes de clés par un professionnel
   - Analyse forensique des signaux capturés et journalisation des incidents

**English :**

1. **Signature Database Development** - Create a repository of attack signatures:
   - Catalog signal patterns by malicious firmware
   - Share signatures between security teams and manufacturers
   - Implement an automatic signature update system

2. **Standardized Incident Response** - Establish procedures:
   - Immediate isolation of potentially compromised vehicles
   - Secure reset of key systems by a professional
   - Forensic analysis of captured signals and incident logging

**Mitigation :**

1. **Sécurisation des véhicules**
   - Utiliser des garages fermés et sécurisés
   - Installer une protection de signal RF (pouch Faraday pour clés)
   - Activer les fonctions de double authentification si disponibles (PIN, biométrie)

2. **Réponse technique**
   - Mettre à jour le firmware des télécommandes si des correctifs sont disponibles
   - Utiliser des technologies complémentaires (immobiliseur avec transpondeur)
   - Implémenter des systèmes d'authentification à deux facteurs pour les véhicules critiques

**Recommandations à long terme :**

1. **Pour les constructeurs automobiles :**
   - Renforcer les algorithmes de codes tournants
   - Implémenter la vérification du temps d'émission (timestamp) dans le protocole
   - Ajouter des couches de chiffrement supplémentaires
   - Déployer des mises à jour de sécurité par OTA (Over-The-Air)

2. **Pour les propriétaires de véhicules affectés :**
   - Contacter le concessionnaire pour vérifier la disponibilité de mises à jour de sécurité
   - Utiliser des protections mécaniques complémentaires (barre de volant, sabots)
   - Envisager l'installation d'un système d'alarme indépendant avec notification

#### 📊 Analyse d'impact et risque
### Impact Analysis and Risk

L'exploitation des vulnérabilités des codes tournants via le firmware DarkWeb présente un niveau de risque élevé pour plusieurs raisons :

1. **Facilité d'exploitation** - Nécessite uniquement une capture unique, sans compétences techniques avancées

2. **Large surface d'attaque** - Affecte de multiples marques et modèles de véhicules

3. **Persistance** - Pas de solution simple à court terme (hors rappel massif)

4. **Impact financier** - Coût potentiel pour les constructeurs et assurances estimé à plusieurs milliards d'euros

5. **Évolutivité de la menace** - Le firmware continue d'être développé pour cibler davantage de véhicules

Cette vulnérabilité souligne l'importance d'une approche de sécurité en profondeur dans la conception des systèmes automobiles modernes, et la nécessité d'une collaboration entre chercheurs en sécurité, constructeurs et régulateurs pour adresser ces problématiques.

#### 💿 Firmwares Personnalisés pour Flipper Zero
### Custom Firmwares for Flipper Zero

**Français :**

En plus du firmware DarkWeb mentionné précédemment, plusieurs autres firmwares personnalisés existent pour le Flipper Zero, chacun avec ses propres capacités et caractéristiques. Voici les deux plus populaires :

**1. Firmware Momentum**

Ce firmware se concentre principalement sur :

- **Personnalisation de l'interface utilisateur** - Thèmes améliorés et animations
- **Tests de sécurité Bluetooth avancés** - Capacités étendues pour le BLE spam et les attaques Bluetooth
- **Fonctionnalités GPS** - Support pour le "wardriving" en enregistrant les coordonnées GPS avec les captures WiFi
- **Gestion de fichiers améliorée** - Navigation et organisation optimisées des captures RF et autres données

Momentum est particulièrement utile pour les tests de sécurité Bluetooth et la reconnaissance passive, tout en offrant une interface utilisateur raffinée.

**2. Firmware RogueMaster**

Ce firmware combine des caractéristiques des firmwares Unleashed et Xtreme, offrant :

- **Versatilité maximale** - Presque toutes les fonctionnalités des autres firmwares réunies
- **Mode interface simplifié** - "DUMB mode" pour faciliter l'utilisation des fonctions de base
- **Améliorations BadUSB** - Bibliothèques étendues de payloads et capacités d'exécution automatique
- **Modules additionnels** - Plus de protocoles et décodeurs RF supportés
- **Animations personnalisées** - Grands choix d'animations et de visuels pour le Flipper

**English :**

In addition to the previously mentioned DarkWeb firmware, several other custom firmwares exist for the Flipper Zero, each with their own capabilities and features. Here are the two most popular ones:

**1. Momentum Firmware**

This firmware mainly focuses on:

- **UI customization** - Enhanced themes and animations
- **Advanced Bluetooth security testing** - Extended capabilities for BLE spam and Bluetooth attacks
- **GPS features** - Support for wardriving by recording GPS coordinates with WiFi captures
- **Enhanced file management** - Optimized navigation and organization of RF captures and other data

Momentum is particularly useful for Bluetooth security testing and passive reconnaissance, while offering a refined user interface.

**2. RogueMaster Firmware**

This firmware combines features from Unleashed and Xtreme firmwares, offering:

- **Maximum versatility** - Almost all features from other firmwares combined
- **Simplified interface mode** - "DUMB mode" for easier use of basic functions
- **Bad USB enhancements** - Extended libraries of payloads and auto-run capabilities
- **Additional modules** - More RF protocols and decoders supported
- **Custom animations** - Large selection of animations and visuals for the Flipper

#### ⚠️ Considérations Légales et Éthiques
### Legal and Ethical Considerations

**Français :**

L'utilisation de firmwares personnalisés comme DarkWeb, Momentum ou RogueMaster soulève d'importantes questions légales et éthiques :

1. **Cadre légal** - Dans de nombreux pays, l'interception non autorisée de communications sans fil est illégale, même à des fins de test.

2. **Responsabilité** - L'utilisation de ces firmwares pour compromettre des systèmes automobiles ou autres sans autorisation explicite est illégale et peut entraîner des poursuites pénales.

3. **Divulgation responsable** - Les chercheurs en sécurité découvrant des vulnérabilités doivent suivre les protocoles de divulgation responsable auprès des constructeurs concernés.

4. **Documentation** - Toute utilisation légitime (tests autorisés) doit être rigoureusement documentée, avec autorisations écrites et journaux détaillés.

**English :**

The use of custom firmwares like DarkWeb, Momentum, or RogueMaster raises important legal and ethical questions:

1. **Legal framework** - In many countries, unauthorized interception of wireless communications is illegal, even for testing purposes.

2. **Liability** - Using these firmwares to compromise automotive or other systems without explicit authorization is illegal and may result in criminal prosecution.

3. **Responsible disclosure** - Security researchers discovering vulnerabilities should follow responsible disclosure protocols with concerned manufacturers.

4. **Documentation** - Any legitimate use (authorized testing) must be rigorously documented, with written authorizations and detailed logs.
