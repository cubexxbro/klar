import os
import sys
import time
import random
import ctypes

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title) if os.name == 'nt' else None

def show_logo():
    print("""
    ==================================================================
    ██╗  ██╗██╗      █████╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║ ██╔╝██║     ██╔══██╗██╔══██╗    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
    █████╔╝ ██║     ███████║██████╔╝    ███████║███████║██║     ███████║█████╗  ██████╔╝
    ██╔═██╗ ██║     ██╔══██║██╔══██╗    ██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗
    ██║  ██╗███████╗██║  ██║██║  ██║    ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    ==================================================================
    """)

def matrix_rain():
    clear()
    print("[SYSTEM] INITIALIZING MATRIX RAIN... PRESS CTRL+C TO STOP.")
    time.sleep(1)
    try:
        while True:
            row = "".join(random.choice("018$#@!%&") for _ in range(80))
            sys.stdout.write(f"\033[32m{row}\033[0m\n")
            sys.stdout.flush()
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass

def code_cascade():
    clear()
    print("[SYSTEM] DUMPING SOURCE CODE STACK...")
    time.sleep(1)
    for _ in range(150):
        hex_dump = f"0x{random.randint(10000000, 99999999)} : {random.choice(['MOV', 'PUSH', 'POP', 'XOR', 'LEA', 'JMP'])}"
        sys.stdout.write(f"\033[32m{hex_dump}\033[0m\n")
        sys.stdout.flush()
        time.sleep(0.01)
    input("\n[SUCCESS] CASCADE COMPLETE. PRESS ENTER TO RETURN.")

def local_scan():
    clear()
    print("[SYSTEM] INITIATING DEEP LOCAL SCAN...")
    for i in range(101):
        progress = "=" * (i // 5) + "-" * (20 - (i // 5))
        sys.stdout.write(f"\r[+] SCANNING SECTORS: [{progress}] {i}%")
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n\n[!] VULNERABILITY DETECTED: BUFFER_OVERFLOW_0xAF")
    print("[+] ACCESS GRANTED. SYSTEM ROOTED.")
    input("\n[SUCCESS] SCAN FINISHED. PRESS ENTER TO RETURN.")

def about_screen():
    clear()
    print("==========================================================")
    print("            KLAR HACKER TERMINAL - v2.1                   ")
    print("==========================================================")
    print(" DEVELOPER: cubexxbro")
    print(" REPOSITORY: https://github.com/cubexxbro/klar")
    print(" LICENSE: MIT")
    print("==========================================================")
    input("\nPRESS ENTER TO RETURN TO COMMAND CENTER...")

def main():
    set_title("KLAR HACKER v2.1")
    os.system("color 0a")
    
    while True:
        clear()
        show_logo()
        print("    SYSTEM STATUS: [CONNECTED] | USER: ROOT | VERSION: 2.1")
        print("    ----------------------------------------------------------")
        print("    [1] LOCAL DISK SCANNER      [2] MATRIX RAIN EFFECT")
        print("    [3] CODE CASCADE DUMP       [4] ABOUT & CREDITS")
        print("    [5] EXIT TERMINAL")
        print("    ----------------------------------------------------------")
        
        choice = input("    root@KLAR:~# SELECT COMMAND [1-5]: ").strip()
        
        if choice == '1':
            local_scan()
        elif choice == '2':
            matrix_rain()
        elif choice == '3':
            code_cascade()
        elif choice == '4':
            about_screen()
        elif choice == '5':
            print("\n[SYSTEM] WIPING LOGS...")
            time.sleep(1)
            break
        else:
            print(f"\n[-] ERROR: '{choice}' IS NOT A VALID COMMAND. RETRY.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
