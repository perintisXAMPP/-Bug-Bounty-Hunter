import time
import hashlib
from utils import clear_screen, print_header, Colors, get_input, slow_print
from progress_tracker import add_xp

def malware_scanner_sim():
    clear_screen()
    print_header("ADVANCED: MALWARE SCANNER SIMULATOR")
    print("Memindai direktori untuk mencari file berbahaya berdasarkan MD5 Signature.\n")
    
    # Database signature malware simulasi
    malware_db = {
        "d41d8cd98f00b204e9800998ecf8427e": "Trojan.Generic",
        "5d41402abc4b2a76b9719d911017c592": "Ransomware.WannaCry.Sim",
        "7d41402abc4b2a76b9719d911017c593": "Spyware.Keylogger"
    }
    
    files = ["document.pdf", "setup.exe", "photo.jpg", "crack.bat", "system.dll"]
    
    input(f"{Colors.WARNING}Tekan ENTER untuk mulai pemindaian sistem...{Colors.ENDC}")
    
    found_count = 0
    for f in files:
        print(f"Menganalisis {f}...", end="\r")
        time.sleep(0.6)
        
        # Simulasi hashing
        if f in ["setup.exe", "crack.bat"]:
            # Kita anggap file ini memiliki hash yang ada di DB
            h = "5d41402abc4b2a76b9719d911017c592" if f == "setup.exe" else "7d41402abc4b2a76b9719d911017c593"
            print(f"{Colors.FAIL}[!] TERDETEKSI: {f} -> {malware_db[h]}{Colors.ENDC}")
            found_count += 1
        else:
            print(f"{Colors.GREEN}[+] Bersih: {f:<20}{Colors.ENDC}")
            
    print(f"\n{Colors.BLUE}Pemindaian Selesai. {found_count} ancaman ditemukan.{Colors.ENDC}")
    add_xp(60)
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def log_analyzer_sim():
    clear_screen()
    print_header("ADVANCED: LOG ANALYZER (THREAT HUNTING)")
    print("Menganalisis log akses web untuk mendeteksi serangan Brute Force.\n")
    
    logs = [
        "192.168.1.50 - [10:00:01] - Login Failed",
        "192.168.1.50 - [10:00:02] - Login Failed",
        "192.168.1.50 - [10:00:03] - Login Failed",
        "192.168.1.50 - [10:00:04] - Login Failed",
        "192.168.1.50 - [10:00:05] - Login Failed",
        "10.0.0.12 - [10:05:00] - Login Success",
        "192.168.1.50 - [10:00:06] - Login Success"
    ]
    
    input(f"{Colors.WARNING}Tekan ENTER untuk memproses log file...{Colors.ENDC}")
    
    failed_attempts = {}
    for line in logs:
        print(f"Processing: {line}")
        time.sleep(0.4)
        if "Login Failed" in line:
            ip = line.split(" - ")[0]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
            
    print(f"\n{Colors.CYAN}Hasil Analisis:{Colors.ENDC}")
    for ip, count in failed_attempts.items():
        if count >= 5:
            print(f"{Colors.FAIL}[!] ALARM: Terdeteksi Brute Force dari {ip} ({count} percobaan gagal){Colors.ENDC}")
        else:
            print(f"{Colors.GREEN}[+] {ip}: Normal ({count} percobaan gagal){Colors.ENDC}")
            
    add_xp(50)
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def advanced_menu():
    while True:
        clear_screen()
        print_header("ADVANCED CYBER SECURITY LAB")
        print("1. Malware Scanner Simulator (Signature Based)")
        print("2. Log Analyzer (Threat Hunting Simulation)")
        print("3. Kembali ke Menu Utama")
        
        choice = get_input("\nPilihan Anda (1-3): ")
        if choice == '1':
            malware_scanner_sim()
        elif choice == '2':
            log_analyzer_sim()
        elif choice == '3':
            break
