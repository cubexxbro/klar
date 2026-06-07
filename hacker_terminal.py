import os
import sys
import time
import random
import ctypes
import webbrowser

LOGO_TEXT = r"""
██╗  ██╗██╗      █████╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║ ██╔╝██║     ██╔══██╗██╔══██╗    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
█████╔╝ ██║     ███████║██████╔╝    ███████║███████║██║     ███████║█████╗  ██████╔╝
██╔═██╗ ██║     ██╔══██║██╔══██╗    ██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██╗███████╗██║  ██║██║  ██║    ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)

def show_logo():
    print(f"\033[32m{LOGO_TEXT}\033[0m")

def system_collapse():
    clear()
    for _ in range(50):
        os.system("color 4f")
        sys.stdout.write("SYSTEM_CORRUPTED!" * 5 + "\n")
        time.sleep(0.04)
        os.system("color 07")
        sys.stdout.write("DEATH_SEQUENCE_INIT!" * 5 + "\n")
        time.sleep(0.04)
    os.system("color 0a")

def animate_logo():
    clear()
    colors = ['\033[31m', '\033[32m', '\033[36m', '\033[37m']
    try:
        for _ in range(40):
            clear()
            color = random.choice(colors)
            shift = " " * random.randint(0, 8)
            print(f"{color}")
            for line in LOGO_TEXT.split('\n'):
                print(shift + line)
            sys.stdout.flush()
            time.sleep(0.04)
        os.system("color 0a")
    except KeyboardInterrupt: pass

def matrix_storm():
    clear()
    try:
        colors = ['\033[1;32m', '\033[32m', '\033[0;32m', '\033[1;37m']
        while True:
            line = "".join([random.choice("018$#@!%&") if random.random() > 0.3 else " " for _ in range(80)])
            sys.stdout.write(f"{random.choice(colors)}{line}\033[0m\n")
            sys.stdout.flush()
            time.sleep(0.005)
    except KeyboardInterrupt: pass

def exploit_sequence():
    clear()
    steps = ["INITIALIZING BUFFER OVERFLOW...", "INJECTING MALICIOUS PAYLOAD...", "BYPASSING KERNEL MEMORY PROTECTION...", "ESTABLISHING ROOT ACCESS...", "EXFILTRATING DATA STREAMS...", "WIPING SYSTEM LOGS..."]
    for step in steps:
        print(f"\033[31m[!] {step}\033[0m")
        time.sleep(0.5)
        for _ in range(5):
            print(f"0x{random.randint(1000000, 9999999):X} : {random.choice(['ACCESS_GRANTED', 'ACCESS_DENIED', 'FAIL'])}")
            time.sleep(0.05)
    print("\n\033[1;32m[+] SYSTEM COMPROMISED.\033[0m")
    input("\nPRESS ENTER TO CONTINUE.")

def connection_test():
    clear()
    try:
        while True:
            target = f"{random.randint(10,250)}.{random.randint(10,250)}.{random.randint(1,250)}"
            latency = random.randint(1, 999)
            color = "\033[32m" if latency < 300 else "\033[33m"
            print(f"{color}[PING] {target} | LATENCY: {latency}ms | PACKET: {'#'*int(latency/50)}\033[0m")
            sys.stdout.flush()
            time.sleep(0.05)
    except KeyboardInterrupt: pass

def decrypt_sim():
    clear()
    target = "ROOT_ACCESS_KEY_X99"
    current = ["_" for _ in target]
    for i in range(len(target)):
        for _ in range(10):
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            sys.stdout.write(f"\r[CRACKING] {''.join(current[:i])}{char}{''.join(current[i+1:])}")
            sys.stdout.flush()
            time.sleep(0.02)
        current[i] = target[i]
    print("\n[SUCCESS] KEY BYPASSED.")
    time.sleep(1)

def firewall_breach():
    clear()
    for i in range(1, 11):
        print(f"[{i*10}%] BRUTEFORCING FIREWALL SHIELD...")
        time.sleep(0.2)
    print("\033[1;31m[!] FIREWALL CRITICAL FAILURE\033[0m")
    time.sleep(1)

def system_overheat():
    clear()
    for _ in range(20):
        os.system("color 4f")
        print("CRITICAL TEMP: 99C | CORE_FAILURE_IMMINENT")
        time.sleep(0.1)
    os.system("color 0a")

def data_extraction():
    clear()
    files = ["DB_ADMIN.sql", "USR_PW.txt", "SEC_KEY.bin", "KERNEL_LOG.sys"]
    for f in files:
        for i in range(0, 101, 20):
            sys.stdout.write(f"\r[EXTRACTING] {f}: {i}%")
            sys.stdout.flush()
            time.sleep(0.1)
        print(f" -> OK")
    time.sleep(1)

def open_repo():
    webbrowser.open('https://github.com/cubexxbro/klar')
    print("[SYSTEM] NAVIGATING...")
    time.sleep(1)

def main():
    set_title("KLAR HACKER TERMINAL - v3.0-TERROR")
    os.system("color 0a")
    while True:
        clear()
        show_logo()
        print("    SYSTEM STATUS: [CONNECTED] | USER: ROOT | VERSION: 3.0-TERROR")
        print("    ----------------------------------------------------------")
        print("    [1] MATRIX STORM      [7] SYSTEM OVERHEAT")
        print("    [2] AUTO EXPLOIT      [8] DATA EXTRACTION")
        print("    [3] NETWORK PING      [9] OPEN REPOSITORY")
        print("    [4] DECRYPT SIM       [10] GLITCH ANIMATION")
        print("    [5] FIREWALL BREACH   [11] SYSTEM COLLAPSE (SCARY)")
        print("    [6] EXIT TERMINAL     [12] PACKET SNIFFER")
        print("    ----------------------------------------------------------")
        choice = input("    root@KLAR:~# SELECT OPTION [1-12]: ").strip()
        if choice == '1': matrix_storm()
        elif choice == '2': exploit_sequence()
        elif choice == '3': connection_test()
        elif choice == '4': decrypt_sim()
        elif choice == '5': firewall_breach()
        elif choice == '6': break
        elif choice == '7': system_overheat()
        elif choice == '8': data_extraction()
        elif choice == '9': open_repo()
        elif choice == '10': animate_logo()
        elif choice == '11': system_collapse()
        elif choice == '12': packet_sniffer = None; clear(); print("REDACTED"); time.sleep(1)
        else: time.sleep(0.5)

if __name__ == "__main__":
    main()
