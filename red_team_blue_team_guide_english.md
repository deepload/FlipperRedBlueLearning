# 📖 Complete Red Team & Blue Team, Flipper Zero and Predator module Guide
## 🐬 Using Flipper Zero with 🦅 Predator Module
### 📝 Created by [deep]load && NicolocccoAI
### 🤝 Special acknowledgment to the collaborative efforts and expertise
### 🏆 Featuring Methodologies from Legendary Cybersecurity Experts

```
🔥 ADVANCED CYBERSECURITY TRAINING 🔥
═══════════════════════════════════════
🛡️  Red Team Offensive Operations    🛡️
🔍  Blue Team Defense Strategies     🔍
🎯  Hands-on Practical Scenarios     🎯
═══════════════════════════════════════
```

## 📋 Table of Contents

```
┌─────────────────────────────────────────────────────────┐
│                    📚 COURSE STRUCTURE                  │
└─────────────────────────────────────────────────────────┘
```

### 🏗️ Part I - Fundamentals
- 🎯 Introduction and Objectives
- ⚔️ Red Team vs Blue Team Concepts  
- 🔧 Hardware Description
- ⚙️ Configuration and Installation

### ⚡ Part II - Operational Techniques
- 📡 RF Sub-GHz Attacks
- 📶 WiFi Attacks
- 🛰️ GPS Reconnaissance and Wardriving
- 🎮 Practical Scenarios

### 🛡️ Part III - Defense & Detection
- 🔵 Blue Team Strategies
- 🔍 Detection Tools
- 🚫 Countermeasures

### 📖 Part IV - Practice & Ethics
- 💪 Practical Exercises
- ⚖️ Legal and Ethical Aspects
- 📚 Resources and References

```
🎖️ CERTIFICATION LEVELS:
├── 🥉 Bronze: Basic Operations
├── 🥈 Silver: Advanced Techniques  
└── 🥇 Gold: Expert Mastery
```

## 📖 Chapter 1. Introduction and Objectives

```
🎯 MISSION BRIEFING 🎯
════════════════════
🔴 Red Team: Attack & Exploit
🔵 Blue Team: Defend & Detect
🟣 Purple Team: Collaborate & Improve
════════════════════
```

#### 🎯 Learning Objectives

![Training Path](https://via.placeholder.com/600x200/FF6B6B/FFFFFF?text=🎓+CYBERSECURITY+TRAINING+PATH+🎓)

This guide aims to train students in modern attack simulation (Red Team) and defense (Blue Team) techniques using the Flipper Zero equipped with the Predator module. Upon completion of this training, participants will be able to:
- Understand fundamental penetration testing principles
- Master the use of Flipper Zero and Predator module
- Identify vulnerabilities in RF, WiFi, and IoT systems
- Develop effective detection and defense strategies
- Apply ethical and legal best practices

#### ⚠️ Legal Warning

```
🚨 CRITICAL LEGAL NOTICE 🚨
═══════════════════════════
⚖️  AUTHORIZED USE ONLY  ⚖️
🔒  ETHICAL HACKING ONLY  🔒
📋  WRITTEN CONSENT REQ.  📋
═══════════════════════════
```

{{ ... }}
═══════════════════════════
🔴 **IMPORTANT:** The use of equipment and techniques presented in this guide must be strictly limited to:
- Authorized testing environments
- Legal penetration testing missions
- Security audits with written agreement
- Supervised educational exercises

Any malicious or unauthorized use is prohibited and may be subject to criminal penalties.

#### 🎓 Prerequisites

```
📚 KNOWLEDGE REQUIREMENTS
═════════════════════════
🧠 Technical Foundation
💻 Practical Experience  
🔧 Hardware Familiarity
═════════════════════════
```

**🧠 Technical Knowledge:**
- Basic networking concepts (TCP/IP, WiFi)
- Understanding of radio protocols (RF)
- Information security fundamentals
- Linux usage (recommended)

**🔧 Required Equipment:**

```
📦 HARDWARE CHECKLIST
═════════════════════
🐬 Flipper Zero Device
🦅 Predator Module
📡 RF Antenna (433MHz)
📶 WiFi Antenna (2.4GHz)
🛰️ GPS Antenna
💻 Laptop (Linux preferred)
🔌 USB-C Cables
🔋 External Battery Pack
📱 Smartphone (optional)
═════════════════════
```

![Hardware Setup](https://via.placeholder.com/800x300/4ECDC4/FFFFFF?text=🔧+FLIPPER+ZERO+%2B+PREDATOR+SETUP+🔧)

## ⚔️ Chapter 2. Fundamental Red Team vs Blue Team Concepts

```
⚔️  CYBER WARFARE TEAMS  ⚔️
═══════════════════════════
🔴 RED TEAM    vs    🔵 BLUE TEAM
   Attackers           Defenders
   Offensive           Defensive
   Exploit             Protect
═══════════════════════════
```

![Red vs Blue](https://via.placeholder.com/700x250/FF4757/FFFFFF?text=🔴+RED+TEAM+vs+🔵+BLUE+TEAM)

#### 🔴 Red Team - Offensive Team

```
🎯 RED TEAM MISSION
═══════════════════
🔍 Reconnaissance
🎪 Social Engineering
💥 Exploitation
🏃 Persistence
📊 Reporting
═══════════════════
```

The Red Team simulates a real adversary with the objective to:
- Identify vulnerabilities
- Exploit security flaws
- Test detection and response
- Improve overall security posture

**Red Team Methodology:**
- Reconnaissance - Information gathering
- Enumeration - Target identification
- Exploitation - Vulnerability utilization
- Post-Exploitation - Access maintenance
- Reporting - Results documentation

#### 🔵 Blue Team - Defensive Team

```
🛡️ BLUE TEAM MISSION
════════════════════
👁️ Monitor Systems
🔍 Detect Threats
⚡ Respond Quickly
🔧 Improve Defenses
📈 Learn & Adapt
════════════════════
```

The Blue Team defends the infrastructure with the mission to:
- Detect intrusions
- Analyze incidents
- Respond to threats
- Improve defenses

**Blue Team Activities:**
- Monitoring - Continuous surveillance
- Analysis - Log and alert analysis
- Investigation - Incident investigation
- Response - Threat response
- Improvement - Defense enhancement

#### 🟣 Purple Team - Collaboration

```
🤝 PURPLE TEAM SYNERGY
══════════════════════
🔴 + 🔵 = 🟣
Red + Blue = Purple
══════════════════════
💡 Knowledge Sharing
🔄 Continuous Improvement
📊 Real-time Feedback
🎯 Enhanced Security
══════════════════════
```

![Purple Team](https://via.placeholder.com/600x200/9B59B6/FFFFFF?text=🟣+PURPLE+TEAM+COLLABORATION+🟣)

**🟣 Purple Team Concept:** Collaborative approach where Red Team and Blue Team work together to:
- Share knowledge
- Improve attack and defense techniques
- Optimize detection processes
- Reduce incident response time

## 🔧 Chapter 3. Detailed Hardware Description

```
🔬 HARDWARE LABORATORY 🔬
═════════════════════════
🐬 Flipper Zero Analysis
🦅 Predator Module Deep Dive
📡 Antenna Specifications
🔌 Connectivity Options
═════════════════════════
```

![Hardware Overview](https://via.placeholder.com/800x400/3742FA/FFFFFF?text=🐬+FLIPPER+ZERO+HARDWARE+OVERVIEW+🐬)

#### 🐬 Flipper Zero - Overview

```
🎮 FLIPPER ZERO SPECS
════════════════════
🧠 STM32WB55 (64MHz)
💾 256KB RAM + 1MB Flash
📺 128x64 LCD Display
🎛️ 5-Way Navigation
🔋 2000mAh Battery
🔌 USB-C + Bluetooth
📡 Sub-GHz + NFC + IR
════════════════════
```

The Flipper Zero is a versatile physical and radio penetration testing tool. Main features:

**Technical Specifications:**
- Processor: STM32WB55 (Cortex-M4 64 MHz)
- Memory: 256 KB RAM, 1 MB Flash
- Display: Monochrome LCD 128x64
- Interface: 5 directional buttons
- Connectivity: USB-C, Bluetooth, Sub-GHz
- GPIO: 18 pins for extensions
- Power: 2000 mAh battery

#### 🦅 Predator Module - Detailed Specifications

![Predator Module](https://via.placeholder.com/700x300/E74C3C/FFFFFF?text=🦅+PREDATOR+MODULE+ARCHITECTURE+🦅)

**🏗️ Module Architecture:**
```
╔═════════════════════════════════════╗
║          🦅 PREDATOR MODULE          ║
╠═════════════════════════════════════╣
║  📡 RF Sub-GHz (433 MHz)           ║
║  • 🔧 CC1101 Transceiver            ║
║  • 📶 Helical antenna               ║
║  • 📏 Range: 100-500m               ║
║  • ⚡ Power: +10 dBm max            ║
╠═════════════════════════════════════╣
║  📶 WiFi Module (2.4 GHz)          ║
║  • 🧠 ESP32-S2 Microcontroller      ║
║  • 🔗 AP/Station Interface          ║
║  • 📡 Integrated PCB antenna        ║
║  • 🚀 Up to 150 Mbps throughput    ║
╠═════════════════════════════════════╣
║  🛰️ GPS Module (Multi-GNSS)         ║
║  • 🌍 GPS, GLONASS, Galileo        ║
║  • 🎯 Accuracy: <3m CEP             ║
║  • ⏱️ Time to Fix: <30s             ║
║  • 📊 Update rate: 1-10 Hz          ║
╠═════════════════════════════════════╣
║  🔌 Connectivity & Power            ║
║  • 🔗 Flipper Zero GPIO             ║
║  • 🔌 USB-C (data + charging)       ║
║  • 🔋 Internal battery 1500 mAh     ║
║  • ⚡ 5V/3.3V power rails           ║
╚═════════════════════════════════════╝
```

```
🎨 VISUAL INDICATOR LEGEND
═════════════════════════
🟢 Active/Connected
🟡 Standby/Scanning  
🔴 Error/Disconnected
🔵 Data Transfer
⚪ Idle/Off
═════════════════════════
```

#### 🔧 Components and Features

```
🔬 TECHNICAL DEEP DIVE 🔬
════════════════════════
📡 RF Analysis
📶 WiFi Capabilities  
🛰️ GPS Performance
🔋 Power Management
════════════════════════
```

**📡 RF Sub-GHz Module**

```
📊 RF SPECIFICATIONS
═══════════════════
🎛️ Frequency: 300-928 MHz
📶 Modulations: ASK, FSK, MSK, GFSK
⚡ TX Power: +10 dBm max
🎯 Sensitivity: -110 dBm
📏 Range: 100-500m (LOS)
🔧 Protocols: 100+ supported
═══════════════════
```

- Supported frequencies: 300-928 MHz
- Modulations: ASK, FSK, MSK, GFSK
- Transmission power: +10 dBm max
- Sensitivity: -110 dBm
- Applications: Remote controls, IoT sensors, alarms

**📶 WiFi ESP32-S2 Module**

![WiFi Module](https://via.placeholder.com/600x200/2ECC71/FFFFFF?text=📶+ESP32-S2+WIFI+MODULE+📶)

**🌐 WiFi Capabilities:**

```
📡 WIFI SPECIFICATIONS
═════════════════════
📋 Standards: 802.11 b/g/n
🔧 Modes: STA/AP/Monitor
🔒 Security: WEP/WPA/WPA2/WPA3
🚀 Speed: Up to 150 Mbps
📊 Channels: 1-14 (2.4 GHz)
🎯 Range: 100m (open space)
═════════════════════
```
- Standards: 802.11 b/g/n
- Modes: Station, Access Point, Monitor
- Security: WEP, WPA/WPA2-PSK, WPA2-Enterprise
- Throughput: Up to 150 Mbps
- Channels: 1-14 (2.4 GHz)

**🛰️ GPS Module**

![GPS Module](https://via.placeholder.com/600x200/F39C12/FFFFFF?text=🛰️+MULTI-GNSS+RECEIVER+🛰️)

**🌍 Location Characteristics:**

```
🛰️ GNSS SPECIFICATIONS
══════════════════════
🌍 Constellations: GPS, GLONASS, Galileo, BeiDou
🎯 Accuracy: 2.5m CEP (50%)
⚡ Update Rate: 1-10 Hz
🏔️ Altitude: Up to 18,000m
🏃 Speed: Up to 515 m/s
⏱️ Cold Start: <30s
🔋 Power: <25mA active
══════════════════════
```
- Constellations: GPS, GLONASS, Galileo, BeiDou
- Accuracy: 2.5m CEP (50%)
- Update frequency: 1-10 Hz
- Altitude: Up to 18,000m
- Speed: Up to 515 m/s

## ⚙️ Chapter 4. Configuration and Installation

```
🔧 SETUP LABORATORY 🔧
═══════════════════════
🚀 Firmware Updates
📦 Module Assembly
🔗 Connectivity Tests
✅ System Verification
═══════════════════════
```

![Setup Process](https://via.placeholder.com/800x250/8E44AD/FFFFFF?text=⚙️+INSTALLATION+%26+CONFIGURATION+⚙️)

#### 🚀 Firmware Installation

```
📋 INSTALLATION CHECKLIST
════════════════════════
☐ Download qFlipper
☐ Update Flipper firmware
☐ Install Predator firmware
☐ Test all modules
☐ Verify connectivity
════════════════════════
```

**🔧 Step 1: Flipper Zero Preparation**

```
🐬 FLIPPER ZERO UPDATE PROCESS
═════════════════════════════
1️⃣ Download qFlipper
2️⃣ Connect via USB-C
3️⃣ Check current version
4️⃣ Install latest firmware
5️⃣ Verify installation
═════════════════════════════
```

**📱 Official firmware update:**

```bash
# 🖥️ Via qFlipper (graphical interface)
# Step-by-step process:
1. Download qFlipper from: https://flipperzero.one/update
2. Connect Flipper Zero via USB-C cable
3. Launch qFlipper application
4. Click "Update" button
5. Wait for completion (5-10 minutes)
6. Verify version: Settings → About

# ✅ Expected result:
# Firmware: 0.xx.x (latest)
# Build date: [current]
# Target: f7
```

**🦅 Predator firmware installation:**

```bash
# 💻 Via command line (advanced users)
git clone https://github.com/flipperdevices/flipperzero-firmware
cd flipperzero-firmware

# 🔧 Build and flash
./fbt flash_usb

# 📊 Monitor progress
tail -f build.log

# ✅ Verification commands
./fbt cli
> version
> storage info
```

```
⚠️ TROUBLESHOOTING TIPS
══════════════════════
🔴 USB not detected:
   → Try different cable
   → Check USB drivers
   → Use different port

🟡 Update failed:
   → Restart Flipper
   → Clear cache
   → Manual recovery mode

🟢 Success indicators:
   → Green LED solid
   → Boot animation
   → Main menu accessible
══════════════════════
```

**🔧 Step 2: Predator Module Assembly**

```
🦅 PREDATOR ASSEMBLY GUIDE
═════════════════════════
     [Flipper Zero]
          |
    [GPIO Connection]
          |
    [Predator Module]
     /     |     \
[RF Ant] [WiFi] [GPS]
═════════════════════════
```

**📋 Assembly procedure:**

```
🔧 STEP-BY-STEP ASSEMBLY
═══════════════════════
1️⃣ Power OFF Flipper Zero
   → Hold BACK button (3 sec)
   → Confirm shutdown

2️⃣ Connect Predator Module
   → Align GPIO pins carefully
   → Press firmly until seated
   → Check alignment indicators

3️⃣ Install Antennas
   📡 RF Antenna (433MHz)
      → Screw clockwise (hand tight)
   📶 WiFi Antenna (2.4GHz)
      → Attach to SMA connector
   🛰️ GPS Antenna
      → Connect to GPS port

4️⃣ Power Connections
   🔌 USB-C to Predator module
   🔋 Verify battery levels

5️⃣ System Restart
   ⚡ Power ON Flipper Zero
   ⏱️ Wait for boot sequence
═══════════════════════
```

**✅ Installation verification:**

```
🔍 VERIFICATION CHECKLIST
════════════════════════
📱 Navigation Path:
   Main Menu → Apps → GPIO → Predator

📊 Module Status Check:
   ✅ RF Module: 🟢 Active
   ✅ WiFi Module: 🟢 Connected
   ✅ GPS Module: 🟡 Searching

🌐 WiFi Test:
   → Scan for "Predator_XXXX" AP
   → Signal strength: -30 to -50 dBm
   → Connection successful

🛰️ GPS Test:
   → Satellite count: 4+ visible
   → Fix status: 3D Fix acquired
   → Accuracy: <5m
════════════════════════
```

![Assembly Diagram](https://via.placeholder.com/700x400/E67E22/FFFFFF?text=🔧+PREDATOR+MODULE+ASSEMBLY+🔧)

## 🎮 Chapter 5. Detailed Testing Scenarios with Examples

```
🎯 PRACTICAL SCENARIOS 🎯
════════════════════════
🔴 Red Team Operations
🔵 Blue Team Responses
📊 Real-world Examples
🏆 Success Metrics
════════════════════════
```

![Scenarios Overview](https://via.placeholder.com/900x300/2C3E50/FFFFFF?text=🎮+HANDS-ON+PRACTICAL+SCENARIOS+🎮)

#### 🔴 Scenario 1: Physical Intrusion via RF (Parking/Gate)

```
🚗 SCENARIO BRIEFING
══════════════════
🎯 Target: Corporate parking gate
🔧 Method: RF signal replay
⏱️ Duration: 30 minutes
🎖️ Difficulty: ⭐⭐⭐
══════════════════
```

![RF Attack Flow](https://via.placeholder.com/800x200/E74C3C/FFFFFF?text=📡+RF+SIGNAL+CAPTURE+%26+REPLAY+📡)

**🎯 Context**

```
📋 MISSION PARAMETERS
═══════════════════
🏢 Target: Corporate facility
🚗 Asset: Parking gate system
🔍 Objective: Test access controls
⚖️ Authorization: Written consent
📅 Window: Business hours only
═══════════════════
```

Testing unauthorized access to corporate parking via RF signal capture and replay.

**🎭 Attack Scenario:**
- **Threat Actor:** External attacker
- **Motivation:** Physical access to facility
- **Skill Level:** Intermediate
- **Resources:** Consumer-grade equipment

**🎒 Required Equipment**

```
📦 MISSION EQUIPMENT
══════════════════
🐬 Flipper Zero device
🦅 Predator Module
📡 Sub-GHz antenna (433MHz)
🚗 Test vehicle (optional)
📷 Documentation camera
📱 Smartphone (timing)
🎧 Earpiece (communication)
📝 Field notebook
══════════════════
```

![Equipment Setup](https://via.placeholder.com/600x250/34495E/FFFFFF?text=🎒+RF+ATTACK+EQUIPMENT+🎒)

**Detailed Red Team Procedure**

*🔍 Phase 1: Reconnaissance*

```
🕵️ RECONNAISSANCE PHASE
═════════════════════
📍 Position: 5-10m from gate
⏱️ Duration: 15-30 minutes
👥 Targets: Employee vehicles
📊 Success: 3+ signal captures
═════════════════════
```

```bash
# 📡 Signal Capture Procedure
Flipper Zero → SubGHz → Read RAW

# ⚙️ Configuration:
Frequency: 433.92 MHz
Sample Rate: 2 MSPS
Gain: Auto
Modulation: Auto-detect

# 📍 Positioning:
→ Distance: 5-10m from receiver
→ Line of sight: Clear
→ Concealment: Behind vehicle/pillar
→ Escape route: Planned

# ⏱️ Timing:
→ Peak hours: 8-9 AM, 5-6 PM
→ Capture window: 5-10 seconds
→ Multiple samples: 3-5 different remotes

# 📊 Recording:
→ Auto-save: Enabled
→ Filename: Gate_YYYYMMDD_HHMMSS
→ Metadata: Time, weather, distance
```

```
🎯 CAPTURE TARGETS
════════════════
🚗 Employee vehicles
🚚 Delivery trucks  
🚐 Service vehicles
👮 Security patrols
🏃 Pedestrian remotes
════════════════
```

*📊 Capture example:*

```
📡 SIGNAL ANALYSIS REPORT
═══════════════════════
🎛️ Frequency: 433.920 MHz
⏱️ Duration: 2.3 seconds
📶 Modulation: ASK/OOK
⚡ Baud Rate: 1000 baud
📊 Signal Strength: -45 dBm
🔢 Raw Data: 1010101100110011...
🔍 Pattern: Fixed code detected
✅ Quality: Excellent (SNR: 25dB)
═══════════════════════
```

```
📈 WAVEFORM VISUALIZATION
════════════════════════
     ┌─┐   ┌─┐ ┌───┐
─────┘ └───┘ └─┘   └────
|<-- Preamble -->|<-Data->

🔍 Analysis:
• Preamble: 12 bits sync
• Data: 24 bits payload  
• Encoding: Manchester
• Repeat: 3x transmission
════════════════════════
```

*🔬 Phase 2: Signal Analysis*

```
🧪 ANALYSIS LABORATORY
════════════════════
📊 Waveform Analysis
🔍 Protocol Detection
🔢 Data Extraction
🔒 Security Assessment
════════════════════
```

```bash
# 🔬 Deep Signal Analysis

# 📊 Waveform Processing:
→ Import captured signal
→ Apply noise filtering
→ Normalize amplitude
→ Identify bit boundaries

# 🔍 Protocol Identification:
if (signal.has_rolling_code()):
    print("🔒 Rolling Code Detected - SECURE")
    security_level = "HIGH"
else:
    print("🔓 Fixed Code Detected - VULNERABLE")
    security_level = "LOW"

# 🔢 Data Extraction:
bits = extract_manchester_data(signal)
device_id = bits[0:20]  # Device identifier
command = bits[20:24]   # Command (open/close)
checksum = bits[24:28]  # Error detection

# 📋 Security Assessment:
print(f"Device ID: {device_id}")
print(f"Command: {command}")
print(f"Security: {security_level}")
print(f"Replay Risk: {'HIGH' if security_level == 'LOW' else 'LOW'}")
```

```
🔒 SECURITY ANALYSIS
══════════════════
✅ Fixed Code System:
   → Vulnerable to replay
   → No encryption
   → Predictable pattern

❌ Rolling Code System:
   → Replay resistant
   → Encrypted payload
   → Counter mechanism
══════════════════
```

*🚀 Phase 3: Replay Attack*

```
⚡ ATTACK EXECUTION
═════════════════
🎯 Target: Gate receiver
📡 Signal: Captured remote
⏱️ Timing: Off-peak hours
👁️ Observation: Gate response
═════════════════
```

```bash
# 🚀 Replay Attack Procedure
Flipper Zero → SubGHz → Saved → [Gate_20240826_143022]

# ⚙️ Attack Configuration:
→ Select captured signal file
→ Verify signal integrity
→ Set transmission power: MAX
→ Configure repeat count: 3x

# 📍 Positioning:
→ Distance: 2-5m from receiver
→ Antenna orientation: Optimal
→ Clear line of sight
→ Minimize interference

# 🚀 Execution:
1. Press "Send" button
2. Observe gate mechanism
3. Document response time
4. Record success/failure
5. Clear evidence

# 📊 Success Metrics:
→ Gate opens: ✅ VULNERABLE
→ Gate ignores: ❌ PROTECTED
→ Partial response: ⚠️ INVESTIGATE
```

```
⏱️ ATTACK TIMELINE
════════════════
T+0s:  Signal transmission starts
T+1s:  Gate receiver processes
T+2s:  Motor activation (if vulnerable)
T+3s:  Gate movement begins
T+8s:  Gate fully open
T+30s: Auto-close timer starts
════════════════
```

**📊 Expected Results**

```
🎯 ATTACK OUTCOMES
════════════════
✅ SUCCESS SCENARIO:
   → Gate opens immediately
   → No authentication required
   → Fixed code vulnerability
   → Physical access gained
   → Critical security flaw

❌ FAILURE SCENARIO:
   → Gate remains closed
   → Rolling code protection
   → Signal ignored/rejected
   → Modern security system
   → Adequate protection

⚠️ PARTIAL SUCCESS:
   → Delayed response
   → Multiple attempts needed
   → Weak implementation
   → Upgrade recommended
════════════════
```

```
📈 VULNERABILITY MATRIX
═════════════════════
Fixed Code:     🔴 CRITICAL
Weak Rolling:   🟡 MEDIUM
Strong Rolling: 🟢 LOW
Encrypted:      🟢 MINIMAL
═════════════════════
```

![Attack Results](https://via.placeholder.com/700x200/27AE60/FFFFFF?text=📊+ATTACK+SUCCESS+METRICS+📊)

**🔵 Blue Team Detection**

```
🛡️ DEFENSIVE MONITORING
═════════════════════
📊 Log Analysis
📹 Video Correlation
🚨 Anomaly Detection
⚡ Incident Response
═════════════════════
```

![Blue Team Response](https://via.placeholder.com/700x250/3498DB/FFFFFF?text=🔵+BLUE+TEAM+DETECTION+%26+RESPONSE+🔵)

*🚨 Compromise Indicators:*

```
🔍 DETECTION SIGNATURES
═════════════════════
🚪 Gate Activity:
   → Opening without badge scan
   → Multiple rapid activations
   → Off-hours access attempts
   → Unusual timing patterns

📹 Video Analysis:
   → No authorized vehicle
   → Suspicious individuals
   → Loitering near gate
   → Electronic devices visible

📊 Pattern Analysis:
   → Frequency anomalies
   → Signal strength variations
   → Timing correlations
   → Behavioral deviations
═════════════════════
```

*📋 Detection Technologies:*

```
🔧 MONITORING TOOLS
═════════════════
📡 RF Spectrum Analyzer
   → Continuous monitoring
   → Anomaly detection
   → Signal fingerprinting

📹 Video Analytics
   → Motion detection
   → License plate recognition
   → Facial recognition

📊 SIEM Integration
   → Log correlation
   → Threat intelligence
   → Automated alerting
═════════════════
```

*📋 Suspicious Log Example:*

```
🚨 SECURITY INCIDENT LOG
══════════════════════
[2024-08-26 14:23:15] 🚪 GATE_OPEN
   └─ ❌ No badge scan detected
   └─ 📹 No vehicle on camera
   └─ 📡 RF signal: 433.92MHz
   └─ ⚠️ ANOMALY SCORE: 85/100

[2024-08-26 14:23:20] 🚪 GATE_OPEN  
   └─ ❌ No badge scan detected
   └─ 📹 Same location, no vehicle
   └─ 📡 Identical RF signature
   └─ 🚨 ALERT TRIGGERED

[2024-08-26 14:23:25] 🚪 GATE_OPEN
   └─ ❌ No badge scan detected
   └─ 📹 Suspicious individual
   └─ 📡 Replay attack pattern
   └─ 🔴 INCIDENT ESCALATED
══════════════════════
```

```
⚡ AUTOMATED RESPONSE
══════════════════
🚨 Immediate Actions:
   → Security team notified
   → Gate temporarily disabled
   → Camera focus on area
   → RF jamming activated

📞 Escalation Chain:
   → SOC Analyst (T+0min)
   → Security Manager (T+5min)
   → Physical Security (T+10min)
   → Law Enforcement (T+30min)
══════════════════
```

#### 🔴 Scenario 2: WiFi Denial of Service Attack (Deauth Flood)

**Context**

Massive disruption of corporate WiFi network by forced client disconnection.

**Detailed Red Team Procedure**

*Phase 1: WiFi reconnaissance*
```bash
Flipper Zero → Apps → WiFi → WiFi Scanner
- Scan available networks
- Identify target SSID: "Corp-WiFi"
- Note channel (ex: Channel 6)
- Count connected clients
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
- Clients disconnected: 23/23 (100%)
- Reconnection attempts: 156 failures
- Attack duration: 5 minutes
- Traffic generated: 30,000 deauth frames/min

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
- Attack source investigation

#### 🔴 Scenario 3: Malicious Access Point (Evil Twin)

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
           Password: Password123
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
- Physical security team dispatch
- MAC address blocking on infrastructure

#### 🔴 Scenario 4: Advanced Reconnaissance (Wardriving + GPS)

**Context**

Detailed mapping of exposed WiFi networks around the company perimeter.

**Detailed Red Team Procedure**

*Phase 1: Mission preparation*
```bash
Required equipment:
- Flipper Zero + Predator Module
- High sensitivity WiFi antenna
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
- Point B: North adjacent street
- Point C: East adjacent street  
- Point D: South adjacent street
- Point E: West adjacent street
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
    print(f"Exposed corporate networks: {corporate_networks}")
    
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
- Exposed corporate networks: 8 (17.0%)

🔨 Identified vulnerabilities:
- Corp-Guest (Open) - Visible from public parking
- PRINTER-HP-001 (Open) - Unsecured printer
- Corp-IoT (WEP) - Obsolete encryption
- CCTV-System (Open) - Accessible cameras
- Corp-WiFi - Signal extends 150m beyond perimeter

📍 Risk zones:
- Public parking: 8 corporate networks visible
- North street: Corp-WiFi signal at -35 dBm
- Café across street: Guest network connection possible
```

**Blue Team Detection**

*Perimeter surveillance:*
- Detection of suspicious vehicles in perimeter
- Monitoring connection attempts from outside
- Analysis of WiFi connection geolocation logs

#### 🔴 Scenario 5: IoT Device Attack

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
- Automatic sprinkler system
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
- IoT data collection interruption
- Maintenance team confusion
- Possible physical access (opening sensors)

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

#### 🔴 Scenario 6: RFID/NFC Badge Compromise

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

#### 🔑️ RF Attack Detection and Response

**Complete RF Monitoring System**

*Detection architecture:*
```
┌─────────────────────────────────────┐
│         RF DETECTION SYSTEM         │
├─────────────────────────────────────┤
│  📡 Distributed RF sensors         │
│  • Spectrum analyzers              │
│  • Wideband receivers              │  
│  • Anomaly detectors               │
├─────────────────────────────────────┤
│  🔍 Real-time analysis             │
│  • Replay attack detection         │
│  • Jammer identification           │
│  • Physical log correlation        │
├─────────────────────────────────────┤
│  ⚡ Automatic response              │
│  • Instant SOC alerts              │
│  • Automatic lockdown              │
│  • Security team notification      │
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

#### 🔑️ WiFi Attack Detection

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
        
        trigger_immediate_response(alert)
```

## Chapter 10: Legal and Ethical Considerations

#### ⚖️ Legal Framework

**Authorization Requirements**
- Written permission from system owners
- Clear scope definition
- Time-limited testing windows
- Emergency contact procedures
- Data handling agreements

**Compliance Standards**
- ISO 27001 security management
- NIST Cybersecurity Framework
- GDPR data protection requirements
- Industry-specific regulations

#### 🛡️ Ethical Guidelines

**Professional Conduct**
- Minimize system disruption
- Protect confidential information
- Report vulnerabilities responsibly
- Maintain professional integrity
- Continuous education and training

**Best Practices**
- Document all testing activities
- Use least privilege principles
- Implement proper data destruction
- Maintain chain of custody
- Regular security awareness training

---

*This guide was designed for educational and security training purposes. All described techniques must be used only within a legal and ethical framework, with appropriate authorizations.*

© 2024 - Red Team & Blue Team Guide - v1.0
