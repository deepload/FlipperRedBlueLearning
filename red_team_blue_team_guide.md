# 📖 Guide Complet Red Team & Blue Team
## Utilisation du Flipper Zero avec Module Predator
### Version Française / English Version
### Support de Cours Pratique

## 📋 Table des Matières / Table of Contents
### Partie I - Fondamentaux / Fundamentals
- Introduction et Objectifs
- Concepts Red Team vs Blue Team
- Description Matérielle
- Configuration et Installation

### Partie II - Techniques Opérationnelles / Operational Techniques
- Attaques RF Sub-GHz
- Attaques WiFi
- Reconnaissance GPS et Wardriving
- Scénarios Pratiques

### Partie III - Défense et Détection / Defense & Detection
- Stratégies Blue Team
- Outils de Détection
- Contre-mesures

### Partie IV - Pratique et Éthique / Practice & Ethics
- Exercices Pratiques
- Aspects Légaux et Éthiques
- Ressources et Références

## Chapitre 1. Introduction et Objectifs
### Introduction and Objectives

#### 🎯 Objectifs Pédagogiques / Learning Objectives

**Français :** Ce guide vise à former les étudiants aux techniques modernes de simulation d'attaque (Red Team) et de défense (Blue Team) en utilisant le Flipper Zero équipé du module Predator. À l'issue de cette formation, les participants seront capables de :
- Comprendre les principes fondamentaux des tests d'intrusion
- Maîtriser l'utilisation du Flipper Zero et du module Predator
- Identifier les vulnérabilités dans les systèmes RF, WiFi et IoT
- Développer des stratégies de détection et de défense efficaces
- Appliquer les bonnes pratiques éthiques et légales

**English :** This guide aims to train students in modern attack simulation (Red Team) and defense (Blue Team) techniques using the Flipper Zero equipped with the Predator module. Upon completion of this training, participants will be able to:
- Understand fundamental penetration testing principles
- Master the use of Flipper Zero and Predator module
- Identify vulnerabilities in RF, WiFi, and IoT systems
- Develop effective detection and defense strategies
- Apply ethical and legal best practices

#### ⚠️ Avertissement Légal / Legal Warning

🔴 **IMPORTANT - FRANÇAIS :** L'utilisation du matériel et des techniques présentées dans ce guide doit être strictement limitée à :
- Des environnements de test autorisés
- Des missions légales de tests d'intrusion
- Des audits de sécurité avec accord écrit
- Des exercices pédagogiques supervisés

Toute utilisation malveillante ou non autorisée est interdite et peut être sanctionnée pénalement.

🔴 **IMPORTANT - ENGLISH :** The use of equipment and techniques presented in this guide must be strictly limited to:
- Authorized testing environments
- Legal penetration testing missions
- Security audits with written agreement
- Supervised educational exercises

Any malicious or unauthorized use is prohibited and may be subject to criminal penalties.

#### 🎓 Prérequis / Prerequisites

**Connaissances Techniques :**
- Notions de base en réseaux (TCP/IP, WiFi)
- Compréhension des protocoles radio (RF)
- Bases de la sécurité informatique
- Utilisation de Linux (recommandé)

**Matériel Requis :**
- Flipper Zero
- Module Predator
- Antennes (RF, WiFi, GPS)
- Ordinateur portable avec WiFi
- Câbles de connexion

## Chapitre 2. Concepts Fondamentaux Red Team vs Blue Team
### Fundamental Red Team vs Blue Team Concepts

#### 🔴 Red Team - Équipe Offensive / Offensive Team

**Français :** L'équipe Red Team simule un adversaire réel avec pour objectif de :
- Identifier les vulnérabilités
- Exploiter les failles de sécurité
- Tester la détection et la réponse
- Améliorer la posture sécuritaire globale

**Méthodologie Red Team :**
- Reconnaissance - Collecte d'informations
- Énumération - Identification des cibles
- Exploitation - Utilisation des vulnérabilités
- Post-Exploitation - Maintien de l'accès
- Reporting - Documentation des résultats

**English :** The Red Team simulates a real adversary with the objective to:
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

#### 🔵 Blue Team - Équipe Défensive / Defensive Team

**Français :** L'équipe Blue Team défend l'infrastructure avec pour mission de :
- Détecter les intrusions
- Analyser les incidents
- Répondre aux menaces
- Améliorer les défenses

**Activités Blue Team :**
- Monitoring - Surveillance continue
- Analysis - Analyse des logs et alertes
- Investigation - Enquête sur les incidents
- Response - Réaction aux menaces
- Improvement - Amélioration des défenses

**English :** The Blue Team defends the infrastructure with the mission to:
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

#### 🟣 Purple Team - Collaboration / Collaboration

**Concept Purple Team :** Approche collaborative où Red Team et Blue Team travaillent ensemble pour :
- Partager les connaissances
- Améliorer les techniques d'attaque et de défense
- Optimiser les processus de détection
- Réduire le temps de réponse aux incidents

## Chapitre 3. Description Matérielle Détaillée
### Detailed Hardware Description

#### 🐬 Flipper Zero - Vue d'Ensemble / Overview

**Français :** Le Flipper Zero est un outil polyvalent de tests de pénétration physique et radio. Ses caractéristiques principales :

**Spécifications Techniques :**
- Processeur : STM32WB55 (Cortex-M4 64 MHz)
- Mémoire : 256 KB RAM, 1 MB Flash
- Écran : LCD monochrome 128x64
- Interface : 5 boutons directionnels
- Connectivité : USB-C, Bluetooth, Sub-GHz
- GPIO : 18 pins pour extensions
- Alimentation : Batterie 2000 mAh

**English :** The Flipper Zero is a versatile physical and radio penetration testing tool. Main features:

**Technical Specifications:**
- Processor: STM32WB55 (Cortex-M4 64 MHz)
- Memory: 256 KB RAM, 1 MB Flash
- Display: Monochrome LCD 128x64
- Interface: 5 directional buttons
- Connectivity: USB-C, Bluetooth, Sub-GHz
- GPIO: 18 pins for extensions
- Power: 2000 mAh battery

#### 📡 Module Predator - Spécifications Détaillées / Detailed Specifications

**Architecture du Module :**
```
┌─────────────────────────────────────┐
│           MODULE PREDATOR           │
├─────────────────────────────────────┤
│  📡 RF Sub-GHz (433 MHz)           │
│  • CC1101 Transceiver              │
│  • Antenne helicoidale             │
│  • Portée : 100-500m               │
├─────────────────────────────────────┤
│  📶 WiFi Module (2.4 GHz)          │
│  • ESP32-S2 Microcontroller        │
│  • Interface AP/Station            │
│  • Antenne PCB intégrée            │
├─────────────────────────────────────┤
│  🛰️ GPS Module                      │
│  • Récepteur GNSS                  │
│  • Précision : <3m                 │
│  • Time to Fix : <30s              │
├─────────────────────────────────────┤
│  🔌 Connectivité                    │
│  • GPIO Flipper Zero               │
│  • USB-C (données + charge)        │
│  • Batterie interne 1500 mAh       │
└─────────────────────────────────────┘
```

#### 🔧 Composants et Fonctionnalités / Components and Features

**Module RF Sub-GHz**

**Français :**
- Fréquences supportées : 300-928 MHz
- Modulations : ASK, FSK, MSK, GFSK
- Puissance de transmission : +10 dBm max
- Sensibilité : -110 dBm
- Applications : Télécommandes, capteurs IoT, alarmes

**English :**
- Supported frequencies: 300-928 MHz
- Modulations: ASK, FSK, MSK, GFSK
- Transmission power: +10 dBm max
- Sensitivity: -110 dBm
- Applications: Remote controls, IoT sensors, alarms

**Module WiFi ESP32-S2**

**Capacités WiFi :**
- Standards : 802.11 b/g/n
- Modes : Station, Access Point, Monitor
- Sécurité : WEP, WPA/WPA2-PSK, WPA2-Enterprise
- Débit : Jusqu'à 150 Mbps
- Canaux : 1-14 (2.4 GHz)

**Module GPS**

**Caractéristiques de localisation :**
- Constellations : GPS, GLONASS, Galileo, BeiDou
- Précision : 2.5m CEP (50%)
- Fréquence de mise à jour : 1-10 Hz
- Altitude : Jusqu'à 18,000m
- Vitesse : Jusqu'à 515 m/s

## Chapitre 4. Configuration et Installation
### Configuration and Installation

#### 🚀 Installation du Firmware / Firmware Installation

**Étape 1 : Préparation du Flipper Zero**

**Français :**
- Mise à jour du firmware officiel

```bash
# Via qFlipper (interface graphique)
- Télécharger qFlipper depuis le site officiel
- Connecter le Flipper Zero en USB
- Cliquer sur "Update" pour installer la dernière version
```

- Installation du firmware Predator

```bash
# Via ligne de commande
git clone https://github.com/flipperdevices/flipperzero-firmware
cd flipperzero-firmware
./fbt flash_usb
```

**Étape 2 : Montage du Module Predator**

**Procédure de montage :**
1. Éteindre le Flipper Zero
2. Connecter le module Predator sur les pins GPIO
3. Visser les antennes (RF, WiFi, GPS)
4. Connecter le câble d'alimentation USB-C
5. Redémarrer le Flipper Zero

**Vérification de l'installation :**
1. Menu principal → Apps → GPIO → Predator
2. Vérifier l'affichage des trois modules (RF, WiFi, GPS)
3. Tester la connectivité WiFi (AP Predator_XXXX visible)

## Chapitre 5. Scénarios de Test Détaillés avec Exemples
### Detailed Testing Scenarios with Examples

#### 🔴 Scénario 1 : Intrusion Physique via RF (Parking/Portail)
### Physical Intrusion via RF (Parking/Gate)

**Contexte / Context**

**Français :** Test d'accès non autorisé à un parking d'entreprise via capture et rejeu de signal RF. 

**English :** Testing unauthorized access to corporate parking via RF signal capture and replay.

**Matériel nécessaire / Required Equipment**
- Flipper Zero + Module Predator
- Antenne Sub-GHz 433 MHz
- Véhicule test (optionnel)
- Caméra pour documentation

**Procédure Red Team Détaillée / Detailed Red Team Procedure**

*Phase 1 : Reconnaissance*
```bash
Flipper Zero → SubGHz → Read RAW
- Fréquence : 433.92 MHz
- Se positionner près du portail (5-10m)
- Attendre qu'un employé utilise sa télécommande
- Enregistrer le signal (durée : 5-10 secondes)
```

*Exemple de capture :*
- Signal capturé : 433.920 MHz
- Durée : 2.3 secondes
- Modulation : ASK/OOK
- Débit : 1000 baud
- Données : 1010101100110011...

*Phase 2 : Analyse du signal*
```bash
- Analyser la forme d'onde
- Identifier le protocole (Fixed Code vs Rolling Code)
- Vérifier la répétition du signal
- Extraire la séquence de bits
```

*Phase 3 : Test de rejeu*
```bash
Flipper Zero → SubGHz → Saved → [Nom du fichier]
- Sélectionner le signal enregistré
- Se positionner face au récepteur
- Appuyer sur "Send" 
- Observer la réaction du portail
```

**Résultats Attendus / Expected Results**
- ✅ Succès : Portail s'ouvre → Vulnérabilité confirmée
- ❌ Échec : Rolling code détecté → Système sécurisé

**Détection Blue Team / Blue Team Detection**

*Indicateurs de compromission :*
- Log d'ouverture sans badge employé associé
- Ouverture hors horaires normales
- Activité répétée suspecte
- Absence de véhicule autorisé sur les caméras

*Exemple de log suspect :*
```
[2024-08-26 14:23:15] GATE_OPEN - No badge scan detected
[2024-08-26 14:23:20] GATE_OPEN - No badge scan detected  
[2024-08-26 14:23:25] GATE_OPEN - No badge scan detected
```

#### 🔴 Scénario 2 : Attaque de Déni de Service WiFi (Deauth Flood)
### WiFi Denial of Service Attack (Deauth Flood)

**Contexte / Context**

**Français :** Perturbation massive du réseau WiFi d'entreprise par déconnexion forcée des clients. 

**English :** Massive disruption of corporate WiFi network by forced client disconnection.

**Procédure Red Team Détaillée / Detailed Red Team Procedure**

*Phase 1 : Reconnaissance WiFi*
```bash
Flipper Zero → Apps → WiFi → WiFi Scanner
- Scan des réseaux disponibles
- Identifier le SSID cible : "Corp-WiFi"
- Noter le canal (ex: Channel 6)
- Compter le nombre de clients connectés
```

*Exemple de scan :*
```
SSID: Corp-WiFi
BSSID: AA:BB:CC:DD:EE:FF
Channel: 6
Security: WPA2-PSK
Signal: -45 dBm
Clients: 23 detected
```

*Phase 2 : Analyse des clients*
```bash
WiFi → Monitor Mode → Channel 6
- Capturer le trafic 802.11
- Identifier les adresses MAC des clients
- Observer les trames de gestion
- Sélectionner les cibles prioritaires
```

*Phase 3 : Attaque Deauth ciblée*
```bash
WiFi → Deauth Attack
- Target: Corp-WiFi (AA:BB:CC:DD:EE:FF)
- Clients: ALL ou sélection spécifique
- Packets: 100 par seconde
- Duration: Continu
- Lancer l'attaque
```

*Code de l'attaque (frame 802.11) :*
```
Frame Type: Management (0x00)
Subtype: Deauthentication (0x0C)
Destination: Broadcast (FF:FF:FF:FF:FF:FF)
Source: AP_BSSID (AA:BB:CC:DD:EE:FF)
Reason: Unspecified reason (0x01)
```

**Résultats Attendus / Expected Results**
- Déconnexion massive des clients WiFi
- Impossibilité de se reconnecter
- Perturbation des services réseau
- Plaintes utilisateurs

**Métriques de succès / Success Metrics**
- Clients déconnectés : 23/23 (100%)
- Tentatives de reconnexion : 156 échecs
- Durée de l'attaque : 5 minutes
- Trafic généré : 30,000 frames deauth/min

**Détection Blue Team / Blue Team Detection**

*Alertes IDS/IPS :*
```
[ALERT] Deauth flood detected on Corp-WiFi
Source: Multiple unknown MAC addresses
Rate: 500 deauth frames/second
Duration: 5 minutes continuous
Affected clients: 23
```

*Contre-mesures immédiates :*
- Activation du filtrage MAC
- Changement de canal WiFi
- Activation de la protection 802.11w (PMF)
- Investigation de l'origine de l'attaque

#### 🔴 Scénario 3 : Point d'Accès Malveillant (Evil Twin)
### Malicious Access Point (Evil Twin)

**Contexte / Context**

**Français :** Création d'un faux point d'accès pour capturer les identifiants des employés. 

**English :** Creating a rogue access point to capture employee credentials.

**Procédure Red Team Détaillée / Detailed Red Team Procedure**

*Phase 1 : Clonage du réseau légitime*
```bash
WiFi Scanner → Identifier "Corp-WiFi"
- SSID: Corp-WiFi
- Sécurité: WPA2-PSK
- Canal: 6
- Signal: -45 dBm
```

*Phase 2 : Configuration de l'Evil Twin*
```bash
WiFi → Evil Portal
- SSID: Corp-WiFi (identique)
- Security: Open (pour faciliter la connexion)
- Channel: 11 (différent pour éviter l'interférence)
- Captive Portal: Activé
- DNS Spoofing: Activé
```

*Phase 3 : Création de la page de capture*
```html
<!-- Page de capture d'identifiants -->
<!DOCTYPE html>
<html>
<head>
    <title>Corp-WiFi - Authentification</title>
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
        <h2>Connexion Corp-WiFi</h2>
        <form action="/capture.php" method="post">
            <input type="text" name="username" placeholder="Nom d'utilisateur" required>
            <input type="password" name="password" placeholder="Mot de passe" required>
            <button type="submit">Se connecter</button>
        </form>
        <p><small>Système de sécurité mis à jour. Veuillez vous reconnecter.</small></p>
    </div>
</body>
</html>
```

*Phase 4 : Positionnement et attente*
```bash
- Se positionner dans la cafétéria ou hall d'entrée
- Activer l'Evil Twin AP
- Attendre les connexions automatiques
- Logger toutes les tentatives d'authentification
```

**Résultats Attendus / Expected Results**

*Capture d'identifiants :*
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

**Détection Blue Team / Blue Team Detection**

*Indicateurs WIDS (Wireless Intrusion Detection System) :*
```
[ALERT] Rogue AP detected
SSID: Corp-WiFi (duplicate)
BSSID: BB:BB:CC:DD:EE:FF (unknown)
Channel: 11
Signal Strength: -35 dBm
Location: Estimated Building A, Floor 1
Risk Level: CRITICAL
```

*Actions de réponse :*
- Alerte immédiate au SOC
- Triangulation de la position du rogue AP
- Notification aux utilisateurs (email/SMS)
- Envoi d'une équipe de sécurité physique
- Blocage MAC address sur l'infrastructure

#### 🔴 Scénario 4 : Reconnaissance Avancée (Wardriving + GPS)
### Advanced Reconnaissance (Wardriving + GPS)

**Contexte / Context**

**Français :** Cartographie détaillée des réseaux WiFi exposés autour du périmètre de l'entreprise. 

**English :** Detailed mapping of exposed WiFi networks around the company perimeter.

**Procédure Red Team Détaillée / Detailed Red Team Procedure**

*Phase 1 : Préparation de la mission*
```bash
Matériel requis:
- Flipper Zero + Module Predator
- Antenne WiFi haute sensibilité
- Antenne GPS
- Véhicule avec support smartphone
- Batterie externe
- Smartphone avec Google Maps
```

*Phase 2 : Configuration du Wardriving*
```bash
GPS → Activate GPS Module
- Attendre la synchronisation satellite (30-60s)
- Vérifier la précision (<5m)

WiFi → Wardriving Mode
- Scan Interval: 5 secondes
- GPS Logging: Activé
- Output Format: CSV + KML
- Storage: SD Card
```

*Phase 3 : Parcours de reconnaissance*

Route planifiée:
- Point A: Parking public (200m de l'entreprise)
- Point B: Rue adjacente nord
- Point C: Rue adjacente est  
- Point D: Rue adjacente sud
- Point E: Rue adjacente ouest
- Vitesse: 20-30 km/h pour capture optimale

*Phase 4 : Collecte de données*
```bash
# Exemple de log wardriving
Time,Latitude,Longitude,SSID,BSSID,Security,Signal,Channel
14:23:15,46.2044,6.1432,Corp-WiFi,AA:BB:CC:DD:EE:FF,WPA2,-42,6
14:23:16,46.2044,6.1433,Corp-Guest,AA:BB:CC:DD:EE:F1,Open,-45,6
14:23:17,46.2045,6.1434,PRINTER-HP-001,BB:CC:DD:EE:FF:11,Open,-38,11
14:23:18,46.2045,6.1435,Corp-IoT,CC:DD:EE:FF:11:22,WEP,-41,1
14:23:19,46.2046,6.1436,CCTV-System,DD:EE:FF:11:22:33,Open,-39,6
```

**Analyse des Données / Data Analysis**

*Phase 5 : Post-traitement*
```bash
# Conversion et analyse
python3 wardriving_analyzer.py --input wardriving_log.csv
```

*Script d'analyse exemple :*
```python
import pandas as pd
import folium
from geopy.distance import geodesic

def analyze_wardriving_data(csv_file):
    df = pd.read_csv(csv_file)
    
    # Analyse statistique
    total_networks = len(df)
    open_networks = len(df[df['Security'] == 'Open'])
    wep_networks = len(df[df['Security'] == 'WEP'])
    corporate_networks = len(df[df['SSID'].str.contains('Corp')])
    
    print(f"=== RAPPORT WARDRIVING ===")
    print(f"Réseaux détectés: {total_networks}")
    print(f"Réseaux ouverts: {open_networks} ({open_networks/total_networks*100:.1f}%)")
    print(f"Réseaux WEP: {wep_networks} ({wep_networks/total_networks*100:.1f}%)")
    print(f"Réseaux corporate exposés: {corporate_networks}")
    
    # Carte de heat map
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

# Utilisation
results = analyze_wardriving_data('wardriving_log.csv')
```

**Résultats Attendus / Expected Results**

*Découvertes critiques :*
```
=== RAPPORT WARDRIVING - ENTREPRISE XYZ ===

📊 Statistiques générales:
- Total réseaux détectés: 47
- Réseaux ouverts: 12 (25.5%)
- Réseaux WEP: 3 (6.4%)
- Réseaux corporate exposés: 8 (17.0%)

🔨 Vulnérabilités identifiées:
- Corp-Guest (Open) - Visible depuis parking public
- PRINTER-HP-001 (Open) - Imprimante non sécurisée
- Corp-IoT (WEP) - Chiffrement obsolète
- CCTV-System (Open) - Caméras accessibles
- Corp-WiFi - Signal déborde de 150m hors périmètre

📍 Zones à risque:
- Parking public: 8 réseaux corporate visibles
- Rue nord: Signal Corp-WiFi à -35 dBm
- Café en face: Connexion possible au réseau invité
```

**Détection Blue Team / Blue Team Detection**

*Surveillance périmétrique :*
- Détection de véhicules suspects dans le périmètre
- Monitoring des tentatives de connexion depuis l'extérieur
- Analyse des logs de géolocalisation des connexions WiFi

#### 🔴 Scénario 5 : Attaque sur Objets Connectés (IoT)
### IoT Device Attack

**Contexte / Context**

**Français :** Compromission d'appareils IoT d'entreprise via leurs interfaces radio. 

**English :** Compromising corporate IoT devices via their radio interfaces.

**Procédure Red Team Détaillée / Detailed Red Team Procedure**

*Phase 1 : Reconnaissance IoT*
```bash
SubGHz → Read → Frequency Analyzer
- Scan 315 MHz (capteurs US)
- Scan 433.92 MHz (capteurs EU)
- Scan 868 MHz (LoRaWAN)
- Scan 915 MHz (capteurs industriels)
```

*Découvertes typiques :*

Fréquence 433.92 MHz:
- Capteurs de température (bureaux)
- Badges RFID longue portée
- Système d'arrosage automatique
- Capteurs d'ouverture (portes/fenêtres)

Fréquence 868 MHz:
- Compteurs intelligents
- Capteurs de qualité d'air
- Système de chauffage connecté

*Phase 2 : Analyse de protocole*
```bash
# Capture d'un capteur de température
Signal: 433.920 MHz
Modulation: FSK
Débit: 2400 baud
Trame: [SYNC][ID][TEMP][HUMID][CRC]

Exemple de données décodées:
ID Capteur: 0x2A4F
Température: 23.5°C
Humidité: 45%
Batterie: 85%
```

*Phase 3 : Attaques spécifiques*

A) Injection de données falsifiées
```bash
SubGHz → Send → Custom Signal
- Modifier la température: 50°C
- Déclencher une alerte système
- Observer la réaction des équipes
```

B) Déni de service par brouillage
```bash
SubGHz → Jammer Mode
- Fréquence cible: 433.92 MHz
- Puissance: Maximum
- Durée: 30 minutes
- Impact: Perte de données capteurs
```

**Résultats Attendus / Expected Results**
- Fausses alertes sur les systèmes de monitoring
- Interruption de la collecte de données IoT
- Confusion dans les équipes de maintenance
- Possibilité d'accès physique (capteurs d'ouverture)

**Détection Blue Team / Blue Team Detection**

*Alertes système :*
```
[CRITICAL] Temperature anomaly detected
Sensor: 2A4F (Conference Room 3)
Value: 50.0°C (outside normal range: 18-28°C)
Timestamp: 2024-08-26T15:42:31
Action: HVAC emergency shutdown triggered
```

*Analyse des modèles :*
- Détection de valeurs aberrantes (algorithmes ML)
- Corrélation multi-capteurs (écart de température anormal)
- Vérification des signatures RF (détection d'usurpation)

#### 🔴 Scénario 6 : Compromission de Badge RFID/NFC
### RFID/NFC Badge Compromise

**Contexte / Context**

**Français :** Clonage et utilisation malveillante de badges d'accès employé. 

**English :** Cloning and malicious use of employee access badges.

**Procédure Red Team Détaillée / Detailed Red Team Procedure**

*Phase 1 : Identification du type de badge*
```bash
NFC → Read Card
- Approcher le badge du Flipper
- Identifier le type: MIFARE Classic/DESFire/NTAG
- Noter l'UID et les secteurs accessibles
```

*Exemple de lecture badge :*
```
Card Type: MIFARE Classic 1K
UID: 04:52:F3:2A:B8:40:80
SAK: 08
ATQA: 00:04

Secteurs lisibles:
Secteur 0: [Données fabricant]
Secteur 1: [ID Employé: EMP001234]
Secteur 2: [Département: IT-SEC]
Secteur 3: [Niveau accès: 3]
```

*Phase 2 : Clonage du badge*
```bash
NFC → Write to Card
- Insérer une carte vierge compatible
- Copier tous les secteurs accessibles
- Vérifier l'intégrité des données
- Tester le clone sur un lecteur
```

*Phase 3 : Test d'accès*
```bash
# Test sur différents lecteurs
Résultats:
- Porte principale: ✅ Accès autorisé
- Ascenseur: ✅ Niveau 3 accessible
- Salle serveur: ❌ Accès refusé (niveau 4 requis)
- Parking: ✅ Accès autorisé
```

**Détection Blue Team / Blue Team Detection**

*Anomalies dans les logs d'accès :*
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

## Chapitre 9 : Stratégies Blue Team Avancées
### Advanced Blue Team Strategies

#### 🔑️ Détection et Réponse aux Attaques RF
### RF Attack Detection and Response

**Système de Monitoring RF Complet**

*Architecture de détection :*
```
┌─────────────────────────────────────┐
│         SYSTÈME DE DÉTECTION RF         │
├─────────────────────────────────────┤
│  📡 Capteurs RF distribués             │
│  • Analyseurs de spectre               │
│  • Récepteurs large bande              │  
│  • Détecteurs d'anomalies              │
├─────────────────────────────────────┤
│  🔍 Analyse en temps réel              │
│  • Détection de replay attacks         │
│  • Identification de brouilleurs       │
│  • Corrélation avec logs physiques     │
├─────────────────────────────────────┤
│  ⚡ Réponse automatique                │
│  • Alertes SOC instantanées            │
│  • Verrouillage automatique            │
│  • Notification équipes sécurité       │
└─────────────────────────────────────┘
```

*Configuration du monitoring :*
```bash
# Exemple de configuration avec rtl-sdr
rtl_433 -f 433920000 -s 250000 -F json -M time:iso:usec | \
while read line; do
    echo $line | python3 rf_analyzer.py --detect-replay
done
```

*Script de détection d'attaques RF :*
```python
import json
import time
from datetime import datetime, timedelta

class RFSecurityMonitor:
    def __init__(self):
        self.recent_signals = {}
        self.alert_threshold = 3  # Nombre de répétitions suspectes
        
    def analyze_signal(self, data):
        signal_id = data.get('id', 'unknown')
        timestamp = datetime.now()
        
        # Détecter les attaques par rejeu
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
        
        # Envoi vers le SIEM
        self.send_to_siem(alert)
        
        # Notification immédiate
        self.send_notification(alert)
    
    def send_to_siem(self, alert):
        # Intégration avec Splunk, ELK, etc.
        print(f"[SIEM ALERT] {json.dumps(alert, indent=2)}")
    
    def send_notification(self, alert):
        # SMS/Email vers l'équipe sécurité
        print(f"[SECURITY ALERT] Possible RF replay attack detected!")

# Utilisation
monitor = RFSecurityMonitor()
```

#### 🔑️ Détection d'Attaques WiFi
### WiFi Attack Detection

**Configuration WIDS/WIPS Avancée**

*Déploiement de capteurs WiFi :*
```bash
# Configuration avec Kismet
kismet -c wlan0mon -c wlan1mon --override wardrive \
       --log-types pcapng,kismet,alert \
       --log-title "Corporate_WIDS"
```

*Règles de détection personnalisées :*
```python
# Détection d'Evil Twin
def detect_evil_twin():
    known_aps = load_authorized_aps()
    detected_aps = scan_wireless_environment()
    
    for ap in detected_aps:
        if ap['ssid'] in [authorized['ssid'] for authorized in known_aps]:
            authorized_ap = next(a for a in known_aps if a['ssid'] == ap['ssid'])
            
            # Vérifier si le BSSID correspond
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

# Détection d'attaques Deauth
def detect_deauth_flood():
    DEAUTH_THRESHOLD = 50  # frames par minute
    
    deauth_count = count_deauth_frames(time_window=60)
    
    if deauth_count > DEAUTH_THRESHOLD:
        alert = {
            'type': 'DEAUTH_FLOOD_ATTACK',
            'frames_count': deauth_count,
            'time_window': 60,
            'affected_clients': get_affected_clients(),
            'source_analysis': analyze_attack_source()
        }
        
        # Réponse automatique
        enable_pmf_protection()
        change_wifi_channel()
        notify_security_team(alert)
```

#### 🔑️ Réponse Incidentielle Automatisée
### Automated Incident Response

**Playbook de Réponse Automatique**

*Réponse aux attaques RF :*
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

*Réponse aux attaques WiFi :*
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

## Chapitre 10 : Outils de Détection Avancés
### Advanced Detection Tools

#### 📊 Dashboard de Monitoring Sécurité
### Security Monitoring Dashboard

**Configuration Grafana + InfluxDB**

*Structure des données :*
```sql
-- Table des événements RF
CREATE TABLE rf_events (
    time TIMESTAMP,
    frequency FLOAT,
    signal_strength INTEGER,
    modulation VARCHAR(10),
    event_type VARCHAR(50),
    device_id VARCHAR(20),
    location VARCHAR(100)
);

-- Table des événements WiFi  
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

*Requêtes de monitoring :*
```sql
-- Détection d'anomalies RF par heure
SELECT 
    time_bucket('1 hour', time) as hour,
    COUNT(*) as event_count,
    AVG(signal_strength) as avg_signal
FROM rf_events 
WHERE event_type = 'REPLAY_ATTACK'
GROUP BY hour
ORDER BY hour DESC;

-- Top 10 des AP malveillants détectés
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

#### 🔍 Analyse Forensique RF et WiFi
### RF and WiFi Forensic Analysis

**Capturer et Analyser les Signaux RF**

*Script d'analyse forensique RF :*
```python
#!/usr/bin/env python3
# rf_forensics.py - Outil d'analyse forensique RF

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
        # Chargement des données depuis fichier capture RF
        print(f"Loading RF capture from {file_path}")
        # Format: [timestamp, frequency, signal_strength, raw_data]
        return pd.read_csv(file_path)
    
    def extract_metadata(self):
        # Extraire métadonnées importantes
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
        # Signatures d'attaques connues
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
        
        # Détection de replay attacks
        signal_groups = self.data.groupby('raw_data')
        for signal_data, group in signal_groups:
            if len(group) >= self.signatures['replay_attack']['threshold']:
                # Vérifier le critère temporel
                timestamps = pd.to_datetime(group['timestamp'])
                if (timestamps.max() - timestamps.min()).total_seconds() <= \
                   self.signatures['replay_attack']['timeframe_sec']:
                    results['potential_attacks'].append({
                        'type': 'replay_attack',
                        'confidence': 'high',
                        'signal_data': signal_data[:20] + '...',  # Tronqué pour lisibilité
                        'occurrences': len(group),
                        'timestamps': group['timestamp'].tolist(),
                    })
        
        # Détection de jamming
        high_power_signals = self.data[self.data['signal_strength'] >= 
                                     self.signatures['jamming']['threshold_dbm']]
        
        if len(high_power_signals) > 0:
            # Grouper par périodes continues
            high_power_signals['timestamp'] = pd.to_datetime(high_power_signals['timestamp'])
            high_power_signals = high_power_signals.sort_values('timestamp')
            
            # Identifier les périodes continues de signal fort
            time_diffs = high_power_signals['timestamp'].diff().dt.total_seconds()
            new_group = time_diffs.isna() | (time_diffs > 1)  # Nouvelle groupe si écart > 1s
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
            f.write("===== RAPPORT D'ANALYSE FORENSIQUE RF =====\n")
            f.write(f"Date d'analyse: {datetime.now()}\n\n")
            
            f.write("=== MÉTADONNÉES DE CAPTURE ===\n")
            for key, value in self.metadata.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\n=== ATTAQUES POTENTIELLES DÉTECTÉES ===\n")
            if len(attack_results['potential_attacks']) == 0:
                f.write("Aucune attaque détectée.\n")
            else:
                for i, attack in enumerate(attack_results['potential_attacks'], 1):
                    f.write(f"\nAttaque #{i}:\n")
                    f.write(f"  Type: {attack['type']}\n")
                    f.write(f"  Confiance: {attack['confidence']}\n")
                    for key, value in attack.items():
                        if key not in ['type', 'confidence']:
                            f.write(f"  {key}: {value}\n")
            
            f.write("\n=== RECOMMANDATIONS ===\n")
            if any(a['type'] == 'replay_attack' for a in attack_results['potential_attacks']):
                f.write("- Implementer des codes roulants pour tous les dispositifs RF\n")
                f.write("- Ajouter un chiffrement pour les transmissions sensibles\n")
            
            if any(a['type'] == 'jamming' for a in attack_results['potential_attacks']):
                f.write("- Installer des détecteurs de brouillage RF\n")
                f.write("- Considérer des alternatives filaires pour les systèmes critiques\n")

# Utilisation
if __name__ == "__main__":
    analyzer = RFForensicAnalyzer("rf_capture_20240825.csv")
    analyzer.generate_report("rf_forensic_report.txt")
    print("Analyse terminée et rapport généré.")
```

**Analyse Forensique WiFi**

*Analyse PCAP avec Wireshark :*
```bash
# Extraction des attaques deauth
tshark -r capture.pcap -Y "wlan.fc.type_subtype==0x000c" -T fields \
       -e frame.time_epoch -e wlan.sa -e wlan.da -e radiotap.dbm_antsignal

# Analyse statistique
tshark -r capture.pcap -q -z io,stat,30,"COUNT(wlan.fc.type_subtype==0x000c)"

# Extraction d'information des AP suspects
tshark -r capture.pcap -T fields -e wlan.bssid -e wlan.ssid \
       -e wlan.fc.type_subtype -e radiotap.channel.freq -Y "wlan.fc.type_subtype==8" | sort | uniq
```

*Script d'analyse de beacon frames :*
```python
import pyshark
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime, timedelta

# Charger la capture
cap = pyshark.FileCapture('evil_twin_capture.pcap', display_filter='wlan.fc.type_subtype == 0x08')

# Extraction des beacons
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

# Analyse des données
df = pd.DataFrame(beacon_frames)

# Détecter les SSID dupliqués avec BSSID différents
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

# Afficher les résultats
print(f"\n=== RAPPORT D'ANALYSE FORENSIQUE WIFI ===\n")
print(f"Date d'analyse: {datetime.now()}\n")
print(f"Total de beacon frames analysés: {len(beacon_frames)}")
print(f"Points d'accès uniques détectés: {len(df['bssid'].unique())}\n")

print("=== DÉTECTION D'EVIL TWIN ===\n")
if len(duplicated_ssids) == 0:
    print("Aucun Evil Twin détecté.")
else:
    print(f"{len(duplicated_ssids)} SSID potentiellement dupliqués détectés:\n")
    for i, ap in enumerate(duplicated_ssids, 1):
        print(f"#{i} SSID: {ap['ssid']}")
        print(f"  Nombre de BSSID: {ap['bssid_count']}")
        print("  BSSIDs détectés:")
        for j, bssid in enumerate(ap['bssids']):
            signal = ap['signal_strengths'].get(bssid, 'N/A')
            print(f"    {j+1}. {bssid} (Signal: {signal} dBm)")
        print(f"  Canaux utilisés: {', '.join(map(str, ap['channels']))}\n")

# Recommandations basées sur l'analyse
print("=== RECOMMANDATIONS ===\n")
if len(duplicated_ssids) > 0:
    print("1. Vérifier l'authenticité des points d'accès suivants:")
    for ap in duplicated_ssids:
        print(f"   - {ap['ssid']} (BSSIDs: {', '.join(ap['bssids'][:2])}...)")
    print("\n2. Mettre en place un système de détection d'Evil Twin")
    print("3. Informer les utilisateurs sur les risques des réseaux non sécurisés")
    print("4. Implémenter une authentification 802.1X pour les réseaux d'entreprise")
else:
    print("Aucune action immédiate requise. Continuer la surveillance régulière.")
```

## Chapitre 11 : Contre-mesures Techniques Avancées
### Advanced Technical Countermeasures

#### 🔒 Sécurisation des Dispositifs RF
### RF Device Security Hardening

**Systèmes de Défense RF**

*Implementation de codes roulants :*
```c
// Exemple d'implémentation KeeLoq pour portes/barrières
#include <KeeLoq.h>

// Clés secrètes du manufacturier et du dispositif
uint64_t manufacturerKey = 0x5CAEDF21A3B4C908;
int deviceSerialNumber = 0x00012345;
uint64_t deviceKey;

// Générer une clé unique pour chaque dispositif
void initializeDevice() {
  deviceKey = KeeLoq::deriveKey(manufacturerKey, deviceSerialNumber);
  
  // Paramètres initiaux
  uint32_t counter = 0;    // Compteur synchronisé
  uint32_t seed = random(0xFFFFFFFF);  // Graine aléatoire
  
  printf("Device initialized: SNR=%08X\n", deviceSerialNumber);
}

// Génération du code pour transmission
uint32_t generateRollingCode() {
  static uint32_t counter = 0;
  counter++;
  
  // Fusion du compteur avec l'ID du dispositif
  uint32_t plaintext = (deviceSerialNumber & 0xFFFF) | (counter << 16);
  
  // Chiffrement du code
  uint32_t encrypted = KeeLoq::encrypt(plaintext, deviceKey);
  
  printf("Generated code: %08X (counter=%u)\n", encrypted, counter);
  return encrypted;
}

// Vérification d'un code reçu
bool validateRollingCode(uint32_t receivedCode) {
  // Déchiffrement du code
  uint32_t decrypted = KeeLoq::decrypt(receivedCode, deviceKey);
  
  // Extraction des composants
  uint16_t receivedSerialNumber = decrypted & 0xFFFF;
  uint16_t receivedCounter = decrypted >> 16;
  
  // Vérifier le numéro de série
  if (receivedSerialNumber != (deviceSerialNumber & 0xFFFF)) {
    printf("Invalid serial number\n");
    return false;
  }
  
  // Vérifier le compteur (avec fenêtre de tolérance)
  static uint32_t lastCounter = 0;
  if (receivedCounter <= lastCounter) {
    printf("Replay attack detected! Counter=%u, Last=%u\n", 
           receivedCounter, lastCounter);
    return false;
  }
  
  // Code valide, mettre à jour le compteur
  lastCounter = receivedCounter;
  printf("Valid code. New counter=%u\n", lastCounter);
  return true;
}
```

*Détection de brouillage RF :*
```c
#include <RFDetection.h>
#include <Alert.h>
#include <MovingAverage.h>

RFDetector detector(433.92); // MHz
MovingAverage avgNoise(60);  // moyenne sur 60 secondes
Alert securityAlert;

void setup() {
  Serial.begin(115200);
  detector.begin();
  securityAlert.begin();
  
  // Calibration initiale
  Serial.println("Calibration du niveau de bruit RF...");
  delay(1000);
  
  // Mesurer le bruit ambiant pendant 30 secondes
  unsigned long startTime = millis();
  while (millis() - startTime < 30000) {
    float currentNoise = detector.measureNoiseLevel();
    avgNoise.add(currentNoise);
    delay(500);
  }
  
  float baselineNoise = avgNoise.getAverage();
  float threshold = baselineNoise + 15.0; // +15dB au-dessus du bruit ambiant
  
  detector.setJammingThreshold(threshold);
  Serial.print("Calibration terminée. Niveau de base: ");
  Serial.print(baselineNoise);
  Serial.print(" dBm, Seuil d'alerte: ");
  Serial.print(threshold);
  Serial.println(" dBm");
}

void loop() {
  // Mesurer le niveau RF actuel
  float currentLevel = detector.measureSignalLevel();
  float currentNoise = detector.measureNoiseLevel();
  
  // Mettre à jour la moyenne mobile du bruit
  avgNoise.add(currentNoise);
  
  // Vérifier si jamming détecté
  if (detector.isJammingDetected()) {
    // Alerte immédiate
    Serial.print("ALERTE! Brouillage RF détecté! Niveau: ");
    Serial.print(currentLevel);
    Serial.print(" dBm, Seuil: ");
    Serial.print(detector.getJammingThreshold());
    Serial.println(" dBm");
    
    securityAlert.trigger("RF_JAMMING", 
                         "Brouillage RF détecté sur " + String(detector.getFrequency()) + " MHz");
    
    // Actions automatiques
    activateBackupSystems();
    notifySecurityPersonnel();
    
    // Attendre avant de réinitialiser l'alerte
    delay(10000);
    securityAlert.reset();
  } else {
    // Surveillance normale
    Serial.print("Niveau RF: ");
    Serial.print(currentLevel);
    Serial.print(" dBm, Bruit moyen: ");
    Serial.print(avgNoise.getAverage());
    Serial.println(" dBm");
  }
  
  // Adapter dynamiquement le seuil de détection
  float dynamicThreshold = avgNoise.getAverage() + 15.0;
  detector.setJammingThreshold(dynamicThreshold);
  
  delay(1000);
}

void activateBackupSystems() {
  // Activer systèmes de secours
  Serial.println("Activation des systèmes de secours...");
}

void notifySecurityPersonnel() {
  // Notification du personnel de sécurité
  Serial.println("Notification envoyée à l'équipe de sécurité");
}
```

#### 🔒 Sécurisation WiFi Avancée
### Advanced WiFi Security

**Configuration de sécurité WiFi entreprise**

*Configuration 802.1X avec RADIUS :*
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

# Configuration RADIUS
auth_server_addr=10.0.0.10
auth_server_port=1812
auth_server_shared_secret=your_secret_key_here

# Protection Management Frame
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

# Activer 802.11w (Management Frame Protection)
wme_enabled=1
ieee80211w=2
group_mgmt_cipher=AES-128-CMAC
```

*Script de détection de désautorisation :*
```python
#!/usr/bin/env python3
# deauth_detector.py - Détecteur d'attaques de désautorisation

import pyshark
import datetime
import smtplib
from collections import defaultdict
from email.mime.text import MIMEText

class DeauthDetector:
    def __init__(self):
        self.deauth_threshold = 20  # Nombre de trames de désauth par seconde
        self.monitoring_interface = "wlan0mon"
        self.time_window = 5  # Fenêtre de temps en secondes
        self.deauth_counter = defaultdict(list)
        self.authorized_aps = self._load_authorized_aps()
        
    def _load_authorized_aps(self):
        # Charger la liste des points d'accès autorisés
        authorized = {}
        with open("authorized_aps.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    authorized[parts[0]] = {'ssid': parts[1], 'channel': parts[2] if len(parts) > 2 else None}
        return authorized
    
    def _alert(self, message):
        print(f"[ALERT] {message}")
        
        # Envoyer alerte par email
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
        # Nettoyer les entrées plus anciennes que time_window
        for mac, timestamps in list(self.deauth_counter.items()):
            self.deauth_counter[mac] = [ts for ts in timestamps 
                                    if (current_time - ts).total_seconds() < self.time_window]
            if not self.deauth_counter[mac]:
                del self.deauth_counter[mac]
    
    def start_monitoring(self):
        print(f"Starting deauth detection on {self.monitoring_interface}...")
        
        # Capture en temps réel
        capture = pyshark.LiveCapture(interface=self.monitoring_interface,
                                     display_filter='wlan.fc.type_subtype == 0x000c')
        
        try:
            for packet in capture.sniff_continuously():
                self._process_packet(packet)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
    
    def _process_packet(self, packet):
        try:
            # Extraire les informations du paquet
            timestamp = datetime.datetime.now()
            if hasattr(packet.wlan, 'sa') and hasattr(packet.wlan, 'bssid'):
                sender = packet.wlan.sa
                bssid = packet.wlan.bssid
                
                # Vérifier si c'est un AP autorisé
                is_authorized = bssid in self.authorized_aps
                
                # Ajouter l'horodatage
                self.deauth_counter[sender].append(timestamp)
                
                # Nettoyer les anciennes entrées
                self._clean_old_entries(timestamp)
                
                # Vérifier si seuil dépassé
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
                    
                    # Réinitialiser le compteur pour éviter des alertes en rafale
                    self.deauth_counter[sender] = []
            
        except Exception as e:
            print(f"Error processing packet: {e}")

# Utilisation
if __name__ == "__main__":
    detector = DeauthDetector()
    detector.start_monitoring()
```

**Système de sécurité WiFi dynamique**

*Configuration WIDS/WIPS dynamique :*
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

## Chapitre 12 : Éthique et Conformité Légale
### Ethics and Legal Compliance

#### 📜 Cadre Légal et Autorisations
### Legal Framework and Authorizations

**Français :**

Avant toute opération de Red Team utilisant le Flipper Zero et le module Predator, il est impératif d'obtenir les autorisations légales nécessaires. Voici les éléments cruciaux à considérer :

1. **Autorisation écrite** - Obtenir un mandat officiel signé par la direction de l'organisation ciblée qui décrit précisément :
   - Périmètre des tests (bâtiments, systèmes, réseaux)
   - Durée des opérations
   - Techniques autorisées et interdites
   - Procédure d'urgence en cas de problème

2. **Conformité réglementaire** - Vérifier la légalité des actions selon :
   - Législation nationale sur les intrusions informatiques
   - Réglementation des communications radio
   - Lois sur la protection des données personnelles
   - Réglementations sectorielles spécifiques (finance, santé, etc.)

3. **Clause de non-poursuite** - Document légal protégeant les pentesteurs contre d'éventuelles poursuites judiciaires si les actions restent dans le cadre défini.

**English :**

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

3. **Non-Prosecution Agreement** - Legal document protecting pentesters against potential legal proceedings if actions remain within the defined framework.

#### 🚨 Limites Éthiques et Sécurité
### Ethical Boundaries and Safety

**Français :**

L'utilisation du Flipper Zero avec module Predator pour des opérations de Red Team doit respecter des limites éthiques strictes :

1. **Proportionnalité** - N'utiliser que les techniques nécessaires pour démontrer la vulnérabilité sans causer de dommages excédentaires.

2. **Confidentialité** - Protéger toutes les données sensibles obtenues pendant les tests et les détruire après usage autorisé.

3. **Non-perturbation** - Éviter toute action pouvant interrompre des services critiques ou mettre en danger des personnes.

4. **Techniques interdites** :
   - Utilisation du brouillage RF dans des zones sensibles (hôpitaux, aéroports, services d'urgence)
   - Interception de données personnelles non liées au test
   - Déni de service prolongé sur des infrastructures essentielles
   - Exploitation de vulnérabilités pour accéder à des données hors du périmètre défini

5. **Documentation et transparence** - Documenter précisément toutes les actions effectuées et les partager uniquement avec les personnes autorisées.

**English :**

The use of Flipper Zero with the Predator module for Red Team operations must respect strict ethical boundaries:

1. **Proportionality** - Use only techniques necessary to demonstrate the vulnerability without causing excessive damage.

2. **Confidentiality** - Protect all sensitive data obtained during tests and destroy it after authorized use.

3. **Non-disruption** - Avoid any action that may interrupt critical services or endanger people.

4. **Prohibited techniques**:
   - Use of RF jamming in sensitive areas (hospitals, airports, emergency services)
   - Interception of personal data unrelated to the test
   - Prolonged denial of service on essential infrastructures
   - Exploitation of vulnerabilities to access data outside the defined perimeter

5. **Documentation and transparency** - Precisely document all actions taken and share them only with authorized persons.

#### 📝 Modèle de document d'autorisation
### Authorization Document Template

```
                    AUTORISATION DE TEST D'INTRUSION
                    RED TEAM PENETRATION TEST AUTHORIZATION

Date: [DATE]
Référence: [RÉFÉRENCE/ID]

1. PARTIES

Client ("l'Organisation"):
[NOM DE L'ORGANISATION]
[ADRESSE COMPLÈTE]
Représenté par: [NOM, PRÉNOM], [FONCTION]

Prestataire ("l'Équipe Red Team"):
[NOM DE LA SOCIÉTÉ OU ÉQUIPE]
[ADRESSE COMPLÈTE]
Représenté par: [NOM, PRÉNOM], [FONCTION]

2. OBJET

L'Organisation autorise l'Équipe Red Team à réaliser des tests d'intrusion, incluant des techniques d'ingénierie sociale, d'accès physique et d'exploitation de vulnérabilités techniques, afin d'évaluer son niveau de sécurité.

The Organization authorizes the Red Team to perform penetration tests, including social engineering techniques, physical access, and technical vulnerability exploitation, to evaluate its security level.

3. PÉRIMÈTRE / SCOPE

Sites physiques concernés / Physical sites included:
- [BÂTIMENT A, ADRESSE]
- [BÂTIMENT B, ADRESSE]

Systèmes et réseaux concernés / Systems and networks included:
- Réseaux WiFi: [LISTE DES SSID]
- Systèmes RF: [LISTE DES SYSTÈMES, PORTES, BARRIÈRES]
- Autres dispositifs: [PRÉCISER]

4. PÉRIODE D'AUTORISATION / AUTHORIZATION PERIOD

Date de début / Start date: [JJ/MM/AAAA], [HEURE]
Date de fin / End date: [JJ/MM/AAAA], [HEURE]

5. TECHNIQUES AUTORISÉES / AUTHORIZED TECHNIQUES

- [X] Capture et réutilisation de signaux RF / RF signal capture and replay
- [X] Attaques sur réseaux WiFi / WiFi network attacks
- [X] Clonage de badges / Badge cloning
- [X] Reconnaissance active / Active reconnaissance
- [ ] Brouillage RF / RF jamming
- [ ] Déni de service / Denial of service

6. CONTACTS D'URGENCE / EMERGENCY CONTACTS

Côté Organisation / Organization side:
[NOM], [FONCTION], [TÉLÉPHONE 24/7], [EMAIL]

Côté Équipe Red Team / Red Team side:
[NOM], [FONCTION], [TÉLÉPHONE 24/7], [EMAIL]

7. CLAUSE DE NON-POURSUITE / NON-PROSECUTION CLAUSE

L'Organisation s'engage à ne pas poursuivre juridiquement l'Équipe Red Team pour les actions menées dans le cadre strict du périmètre et des techniques autorisées dans ce document.

The Organization commits not to legally prosecute the Red Team for actions conducted strictly within the scope and techniques authorized in this document.

8. SIGNATURES

________________________           ________________________
Pour l'Organisation                 Pour l'Équipe Red Team
For the Organization                For the Red Team

[NOM, DATE]                        [NOM, DATE]
```

## Chapitre 13 : Conclusion
### Conclusion

#### 🌐 Intégration dans une Stratégie de Sécurité Globale
### Integration into a Global Security Strategy

**Français :**

L'utilisation du Flipper Zero avec le module Predator dans les exercices Red Team/Blue Team représente un élément d'une stratégie de sécurité plus large. Cette approche doit s'intégrer dans :

1. **Programme de sécurité complet** - Compléter avec des audits de code, tests de vulnérabilité, revues d'architecture, etc.

2. **Formation continue** - Utiliser les résultats des exercices pour améliorer la formation des équipes IT et sensibiliser les utilisateurs.

3. **Amélioration des processus** - Réviser régulièrement les procédures de sécurité et de gestion des incidents en fonction des failles identifiées.

4. **Veille technologique** - Rester informé des nouvelles techniques d'attaque et de défense dans le domaine RF et WiFi.

5. **Approche Purple Team** - Favoriser la collaboration entre Red Team et Blue Team pour maximiser l'apprentissage et l'efficacité des défenses.

**English :**

The use of Flipper Zero with the Predator module in Red Team/Blue Team exercises represents one element of a broader security strategy. This approach should be integrated into:

1. **Comprehensive security program** - Supplement with code audits, vulnerability testing, architecture reviews, etc.

2. **Continuous training** - Use exercise results to improve IT team training and raise user awareness.

3. **Process improvement** - Regularly revise security and incident management procedures based on identified vulnerabilities.

4. **Technology watch** - Stay informed about new attack and defense techniques in the RF and WiFi domains.

5. **Purple Team approach** - Foster collaboration between Red Team and Blue Team to maximize learning and defense effectiveness.

#### 💼 Synthèse des Compétences Acquises
### Summary of Acquired Skills

**Compétences Red Team :**
- Configuration avancée du Flipper Zero et du module Predator
- Exécution d'attaques RF sophistiquées
- Mise en place d'attaques WiFi ciblées
- Analyse et exploitation des protocoles sans fil
- Techniques de reconnaissance non-intrusive

**Compétences Blue Team :**
- Détection d'attaques RF et WiFi en temps réel
- Configuration de systèmes de défense robustes
- Analyse forensique des incidents sans fil
- Déploiement de contre-mesures efficaces
- Intégration des alertes dans un SOC

**Compétences Transversales :**
- Méthodologie de test structurée
- Évaluation des risques RF/WiFi
- Documentation des vulnérabilités
- Communication technique entre équipes
- Connaissance du cadre légal et éthique

## Annexe : Ressources Complémentaires
### Appendix: Additional Resources

#### 📚 Documentation et Manuels
### Documentation and Manuals

**Flipper Zero et Module Predator :**
- [Documentation officielle Flipper Zero](https://docs.flipperzero.one/)
- [Guide technique du module Predator](https://github.com/RogueMaster/flipperzero-firmware-wPlugins/)
- [Awesome Flipper Zero - Collection de ressources](https://github.com/djsime1/awesome-flipperzero)

**Sécurité RF :**
- "Software Defined Radio for Hackers" - Michael Ossmann
- "Practical Signal Processing and RF System Design" - B. Forouzan
- [RF Security Research Repository](https://github.com/mossmann/hackrf/wiki/Documentation)

**Sécurité WiFi :**
- "Attacking and Defending WiFi Networks" - J. Wright
- [WiFi Security Testing Framework Guide](https://wifisecurityblog.com/)
- [Aircrack-ng Documentation](https://www.aircrack-ng.org/documentation.html)

#### 💻 Outils Complémentaires
### Complementary Tools

**Analyse RF :**
- [GQRX](https://gqrx.dk/) - Récepteur Software Defined Radio
- [Universal Radio Hacker](https://github.com/jopohl/urh) - Analyse de protocoles radio
- [rtl_433](https://github.com/merbanan/rtl_433) - Décodeur de protocoles 433/868/915 MHz

**Sécurité WiFi :**
- [Kismet](https://www.kismetwireless.net/) - Détection de réseaux sans fil et WIDS
- [Wireshark](https://www.wireshark.org/) - Analyseur de protocoles réseau
- [Aircrack-ng Suite](https://www.aircrack-ng.org/) - Audit de sécurité WiFi

**Forensique :**
- [PyShark](https://github.com/KimiNewt/pyshark) - Wrapper Python pour tshark
- [Scapy](https://scapy.net/) - Manipulation de paquets réseau
- [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) - Analyseur forensique réseau

---

*Ce guide a été conçu à des fins éducatives et de formation sécurité. Toutes les techniques décrites doivent être utilisées uniquement dans un cadre légal et éthique, avec les autorisations appropriées.*

*This guide was designed for educational and security training purposes. All described techniques must be used only within a legal and ethical framework, with appropriate authorizations.*

© 2024 - Guide Red Team & Blue Team - v1.0

## Chapitre 14 : Sécurité Automobile#### 🔴 Vulnérabilités des codes tournants (Rolling Code)
### Rolling Code Vulnerabilities

Les systèmes de sécurité des véhicules modernes utilisent des codes tournants (rolling code) dans leurs télécommandes. Cette technologie, censée empêcher la copie simple des signaux, présente une vulnérabilité majeure lorsqu'elle est confrontée à un firmware personnalisé sur le Flipper Zero.

Une préoccupation de sécurité majeure a récemment émergé concernant la sécurité des véhicules modernes. Un firmware personnalisé connu sous le nom de "DarkWeb" pour le Flipper Zero permet de contourner les systèmes de sécurité à code tournant utilisés dans de nombreuses voitures modernes, notamment :

- Chrysler
- Dodge
- Fiat
- Ford
- Hyundai
- Jeep
- Kia
- Mitsubishi
- Subaru

### Firmwares personnalisés et exploits pour véhicules
### Custom Firmwares and Vehicle Exploits

**Il est important de comprendre que l'affirmation selon laquelle "un firmware Flipper Zero peut ouvrir toutes les voitures" est une simplification excessive**. Plusieurs firmwares personnalisés existent avec différentes capacités d'exploitation des systèmes automobiles. En voici les principaux :

1. **DarkWeb Firmware** - Le plus spécialisé pour les attaques automobiles
   - Version actuelle : 3.5.8
   - Spécialité : Analyse et clonage des codes tournants avec un seul échantillon
   - Marques vulnérables : Principalement des modèles américains et asiatiques avec télécommandes 433.92 MHz
   - Technique principale : Analyse mathématique de l'algorithme de génération de codes
   - Limitation : Ne fonctionne pas sur tous les véhicules (environ 65-70% de taux de succès sur les modèles compatibles)
   - Interface utilisateur : Console DarkWeb spécialisée avec affichage hexadécimal avancé

2. **RollBack Firmware** - Ciblant spécifiquement les vulnérabilités de désynchronisation
   - Version actuelle : 2.8
   - Spécialité : Force le système du véhicule à accepter des codes précédemment utilisés
   - Marques vulnérables : Certains modèles européens et américains (2015-2020)
   - Technique principale : Attaque par désynchronisation forcée
   - Limitation : Nécessite des conditions RF favorables et proximité

3. **KeyMaster Firmware** (variante de RogueMaster)
   - Version actuelle : 4.2
   - Spécialité : Bibliothèque étendue de protocoles propriétaires automobiles
   - Technique principale : Brute force des combinaisons limitées de certains systèmes
   - Interface : Graphique avancée avec navigateur de protocoles
   - Efficacité : Variable selon le modèle (30-50% en moyenne)

4. **UniRF Pro**
   - Version actuelle : 2.7
   - Spécialité : Amplification de signal et traitement numérique pour capturer à plus grande distance
   - Technique principale : Amélioration de la qualité du signal capturé
   - Particulièrement efficace pour : Les véhicules plus anciens avec systèmes plus simples

Cette vulnérabilité est particulièrement préoccupante car elle ne nécessite **qu'une seule capture** d'un signal de télécommande de voiture pour compromettre l'ensemble du système de sécurité du véhicule.

**English :**

{{ ... }}
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

**It's important to understand that the claim "a Flipper Zero firmware can open all cars" is an oversimplification**. Several custom firmwares exist with varying capabilities for exploiting automotive systems. Here are the main ones:

1. **DarkWeb Firmware** - Most specialized for automotive attacks
   - Current version: 3.5.8
   - Specialty: Analyzing and cloning rolling codes with a single sample
   - Vulnerable brands: Primarily American and Asian models with 433.92 MHz remotes
   - Main technique: Mathematical analysis of the code generation algorithm
   - Limitation: Doesn't work on all vehicles (approximately 65-70% success rate on compatible models)
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
- Subaru

This vulnerability is particularly concerning because it requires **only a single capture** of a car key fob signal to compromise the entire vehicle security system.

#### 🔓 Mécanisme de l'Exploit
### Exploit Mechanism

**Français :**

Contrairement aux attaques traditionnelles qui nécessitent un brouillage du signal (jamming) et plusieurs captures, l'exploit DarkWeb fonctionne avec une seule capture d'un appui sur le bouton de la télécommande. Deux méthodes principales sont utilisées :

1. **Rétro-ingénierie de la séquence :** Le firmware analyse la capture unique pour déterminer l'algorithme de génération des codes tournants et prédire les codes suivants.

2. **Attaque RollBack :** L'exploit utilise une technique de désynchronisation pour forcer le récepteur du véhicule à accepter des codes plus anciens, contournant ainsi la protection du code tournant.

Une fois exploitée, cette vulnérabilité permet à l'attaquant d'émuler toutes les fonctions de la télécommande originale (déverrouillage, verrouillage, coffre, démarrage).

**Conséquence importante :** Suite à l'attaque, la télécommande originale du propriétaire devient désynchronisée et inutilisable jusqu'à une réinitialisation du système.

**English :**

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
