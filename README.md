​⚡ WIFI-SLAYER V.2.1: Ultimate Security Toolkit
​Developer: SilverBulletEX
GitHub: silverbulletex0-debug
​WIFI-SLAYER is an all-in-one wireless and network security auditing tool designed for Kali Linux. It integrates industry-standard tools like Aircrack-ng, MDK4, and Bettercap into a single, smart-interface terminal UI.
​🚀 Features
​Smart Detection: Automatically discovers available interfaces (wlan0, wlan1, etc.).
​WiFi Auditing: Persistent scanning, targeted deauthentication, and beacon flooding.
​MITM Suite: Built-in Man-in-the-Middle capabilities for ARP spoofing and sniffing.
​Security & Anonymity: Integrated MAC address changer and network recovery.
​⚠️ Disclaimer
​This tool is for EDUCATIONAL PURPOSES ONLY. The author (SilverBulletEX) is not responsible for any misuse or damage caused by this program. Use it ONLY on networks you own or have explicit permission to test. Unauthorized access to computer systems is illegal.


🛠️ WIFI-SLAYER V.2.1: Key Features & Technical Details
1. Persistent WiFi Scan (Airodump-ng)
Description: Performs a real-time 802.11 network discovery.
Functionality: Launches in a dedicated terminal window to ensure target data (BSSID, Channel, PWR) remains visible while executing other attacks.
Core Tool: airodump-ng
2. MDK4 - Deauth All (Mass Disconnection)
Description: A high-intensity deauthentication flood.
Functionality: Sends deauth packets to all access points and clients within range, effectively clearing the wireless spectrum.
Command: mdk4 <interface> d
3. MDK4 - Beacon Flood (Fake AP Generation)
Description: Floods the area with thousands of fake SSID beacons.
Functionality: Creates a "WiFi Graveyard" to confuse scanners, hide legitimate networks, or perform a Denial of Service (DoS) on client devices.
Command: mdk4 <interface> b -c 1
4. Aireplay-ng - Targeted Deauth (Precision Strike)
Description: A surgical deauthentication attack against a specific client.
Functionality: Forces a specific device to disconnect from its router, often used to capture WPA handshakes or disrupt a single user.
Command: aireplay-ng -0 0 -a <BSSID> -c <Client_MAC> <interface>
5. MITM - Bettercap (Man-in-the-Middle) 🛡️
Description: A powerful network manipulation and sniffing suite.
Functionality: Performs ARP Spoofing to intercept traffic between a victim and the gateway once you are connected to the network.
In-App Commands:
net.probe on : Discover all local network devices.
net.show : List discovered hosts and identify the target IP.
set arp.spoof.targets <IP_TARGET> : Set the specific victim for spoofing.
arp.spoof on : Start intercepting the data flow.
net.sniff on : Monitor and capture plain-text credentials and URLs.
6. Crack Handshake (WPA/WPA2 Recovery)
Description: Automated WPA/WPA2 password cracking.
Functionality: Utilizes the CPU to compare captured 4-way handshakes against the rockyou.txt wordlist.
Command: aircrack-ng <file.cap> -w /usr/share/wordlists/rockyou.txt
7. Exit & Restore Network (Kill-Switch)
Description: Total system cleanup and service restoration.
Functionality: Automatically kills all attack processes, disables Monitor Mode, and restarts the NetworkManager service to restore internet connectivity.
