import os
import sys
import time
import random
import ctypes
import webbrowser

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)

def show_logo():
    print(r"""
==========================================================================================
██╗  ██╗██╗      █████╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║ ██╔╝██║     ██╔══██╗██╔══██╗    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
█████╔╝ ██║     ███████║██████╔╝    ███████║███████║██║     ███████║█████╗  ██████╔╝
██╔═██╗ ██║     ██╔══██║██╔══██╗    ██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██╗███████╗██║  ██║██║  ██║    ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
==========================================================================================
    """)

def matrix_rain():
    clear()
    try:
        colors = ['\033[32m', '\033[1;32m', '\033[36m']
        while True:
            row = "".join(random.choice("018$#@!%&") for _ in range(80))
            sys.stdout.write(f"{random.choice(colors)}{row}\033[0m\n")
            sys.stdout.flush()
    except KeyboardInterrupt: pass

def binary_stream():
    clear()
    try:
        while True:
            row = "".join(random.choice("01 ") for _ in range(80))
            sys.stdout.write(f"\033[1;37m{row}\033[0m\n")
            sys.stdout.flush()
    except KeyboardInterrupt: pass

def hex_dump():
    clear()
    while True:
        chunk = " ".join([f"{random.randint(0, 255):02X}" for _ in range(16)])
        addr = f"0x{random.randint(0x1000, 0xFFFF):04X}"
        sys.stdout.write(f"\033[33m{addr}: {chunk}\033[0m\n")
        sys.stdout.flush()
        time.sleep(0.01)

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

def packet_sniffer():
    clear()
    while True:
        ip = f"{random.randint(1,254)}.{random.randint(1,254)}"
        port = random.randint(80, 9000)
        sys.stdout.write(f"\033[35m[CAPTURE] SRC: {ip} -> DST: LOCAL | PORT: {port} | STATUS: ALLOWED\033[0m\n")
        sys.stdout.flush()
        time.sleep(0.03)

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
    set_title("KLAR HACKER TERMINAL - v2.2-PRO")
    os.system("color 0a")
    while True:
        clear()
        show_logo()
        print("    SYSTEM STATUS: [CONNECTED] | USER: ROOT | VERSION: 2.2-PRO")
        print("    ----------------------------------------------------------")
        print("    [1] MATRIX RAIN       [6] PACKET SNIFFER")
        print("    [2] BINARY STREAM     [7] SYSTEM OVERHEAT")
        print("    [3] HEX MEMORY DUMP   [8] DATA EXTRACTION")
        print("    [4] DECRYPT SIM       [9] OPEN REPOSITORY")
        print("    [5] FIREWALL BREACH   [10] EXIT TERMINAL")
        print("    ----------------------------------------------------------")
        choice = input("    root@KLAR:~# SELECT OPTION: ").strip()
        if choice == '1': matrix_rain()
        elif choice == '2': binary_stream()
        elif choice == '3': hex_dump()
        elif choice == '4': decrypt_sim()
        elif choice == '5': firewall_breach()
        elif choice == '6': packet_sniffer()
        elif choice == '7': system_overheat()
        elif choice == '8': data_extraction()
        elif choice == '9': open_repo()
        elif choice == '10': break
        else: time.sleep(0.5)

if __name__ == "__main__":
    main()
