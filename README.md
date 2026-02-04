# ⚡ WIFI-SLAYER V.2.1: Ultimate Security Toolkit
Developer: SilverBulletEX  
GitHub: [silverbulletex0-debug](https://github.com/silverbulletex0-debug)

---

## 🛠️ Key Features (Technical Overview)

### 1. Persistent WiFi Scan (Airodump-ng)
* Description: Performs real-time 802.11 network discovery.
* Functionality: Launches in a dedicated terminal window to ensure target data remains visible during attacks.

### 2. MDK4 - Deauth All (Mass Disconnection)
* Description: A high-intensity deauthentication flood.
* Functionality: Sends deauth packets to all access points and clients within range to clear the wireless spectrum.

### 3. MDK4 - Beacon Flood (Fake AP Generation)
* Description: Floods the area with thousands of fake SSID beacons to confuse scanners.

### 4. Aireplay-ng - Targeted Deauth (Precision Strike)
* Description: A surgical deauthentication attack against a specific client.
* Functionality: Forces a specific device to disconnect to capture handshakes.

### 5. MITM - Bettercap (Man-in-the-Middle) 🛡️
* Description: Intercepts traffic between a victim and the gateway using ARP Spoofing.
* Operational Commands:
    1. net.probe on : Discover local network devices.
    2. net.show : Identify target IP.
    3. set arp.spoof.targets <IP_TARGET> : Set the victim.
    4. arp.spoof on : Intercept data.
    5. net.sniff on : Capture credentials and URLs.

### 6. Crack Handshake (WPA/WPA2 Recovery)
* Description: Automated dictionary attack using the rockyou.txt wordlist.

### 7. Exit & Restore Network (Kill-Switch)
* Description: Disables Monitor Mode and restarts NetworkManager to restore internet.

---

## 📸 Project Gallery
*(Replace the URLs below with your actual screenshot links after uploading them to a 'screenshots' folder)*

| Startup & Interface | Main Attack Menu |
| :---: | :---: |
| ![Startup](screenshots/1.jpg) | ![Menu](screenshots/2.jpg) |

| WiFi Scanning | MITM Success |
| :---: | :---: |
| ![Scan](screenshots/3.jpg) | ![Sniff](screenshots/7.jpg) |

---

## ⚠️ Disclaimer
EDUCATIONAL PURPOSES ONLY. The author (SilverBulletEX) is not responsible for any misuse. Use ONLY on networks you own or have explicit permission to test.
