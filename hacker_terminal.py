import os
import sys
import time
import random
import ctypes

def set_title(title):
    try: ctypes.windll.kernel32.SetConsoleTitleW(title)
    except: pass

def typing(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def scan_effect():
    print("\n")
    chars = "0123456789ABCDEF!@#$%^&*()_+"
    for _ in range(50):
        line = "".join(random.choice(chars) for _ in range(90))
        sys.stdout.write(f"\033[92m{line}\033[0m\r")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

def boot_sequence():
    os.system("color 0a")
    logo = """
    ██╗  ██╗██╗      █████╗ ██████╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║ ██╔╝██║     ██╔══██╗██╔══██╗    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
    █████╔╝ ██║     ███████║██████╔╝    ███████║███████║██║     ███████║█████╗  ██████╔╝
    ██╔═██╗ ██║     ██╔══██║██╔══██╗    ██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗
    ██║  ██╗███████╗██║  ██║██║  ██║    ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """
    for line in logo.split('\n'):
        print(f"\033[92m{line}\033[0m")
        time.sleep(0.1)
    
    typing("[*] INITIALIZING KLAR KERNEL V1.1...", 0.05)
    typing("[*] ESTABLISHING ENCRYPTED UPLINK...", 0.05)
    scan_effect()
    typing("[+] CONNECTION ESTABLISHED. ACCESS GRANTED.", 0.05)
    time.sleep(1)
    os.system("cls")

def main():
    os.system("mode con: cols=100 lines=30")
    boot_sequence()
    set_title("KLAR HACKER v1.1 - COMMAND CENTER")

    while True:
        cmd = input("\033[96mKLAR@ROOT:\033[0m~# ").strip().lower()
        if cmd == "help":
            print("\n[COMMANDS]\n  scan      - Deep network vulnerability probe\n  inject    - Kernel memory payload injection\n  clear     - Wipe terminal buffers\n  exit      - Terminate session")
        elif cmd == "scan":
            typing("[!] DEPLOYING PROBE...", 0.03)
            scan_effect()
            print("[+] TARGET VULNERABILITIES FOUND: 0x4F, 0xA2, 0xFF")
        elif cmd == "inject":
            typing("[*] MEMORY OVERFLOW IN PROGRESS...", 0.04)
            for i in range(1, 101, 5):
                print(f"    Injecting buffer: {i}%", end="\r")
                time.sleep(0.1)
            os.system("color 0c")
            typing("\n[!] ROOT ACCESS GRANTED. KERNEL COMPROMISED.", 0.02)
            time.sleep(1)
            os.system("color 0a")
        elif cmd == "clear":
            os.system("cls")
        elif cmd == "exit":
            typing("[*] WIPING LOGS...", 0.05)
            break
        else:
            print("[-] Unknown command. Action logged.")

if __name__ == "__main__":
    main()
