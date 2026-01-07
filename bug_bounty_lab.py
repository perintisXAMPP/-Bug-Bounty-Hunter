import time
from utils import clear_screen, print_header, Colors, get_input
from progress_tracker import add_xp

def sqli_lab():
    clear_screen()
    print_header("LAB: SQL INJECTION")
    print("Target: Bypass login tanpa mengetahui password.")
    print("Query: SELECT * FROM users WHERE user='admin' AND pass='[INPUT]'")
    
    payload = get_input("\nMasukkan Payload SQLi: ")
    
    # Simulasi bypass sederhana
    if "' OR '1'='1" in payload or "' OR 1=1" in payload:
        print(f"\n{Colors.GREEN}[+] Login Berhasil! Anda masuk sebagai ADMIN.{Colors.ENDC}")
        print(f"{Colors.BLUE}Teknik: Tautologi (' OR 1=1) membuat kondisi selalu TRUE.{Colors.ENDC}")
        add_xp(50)
    else:
        print(f"\n{Colors.FAIL}[-] Login Gagal. Password salah.{Colors.ENDC}")
        
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def xss_lab():
    clear_screen()
    print_header("LAB: CROSS-SITE SCRIPTING (XSS)")
    print("Target: Jalankan alert JavaScript di halaman profil.")
    
    payload = get_input("\nMasukkan Payload XSS: ")
    
    if "<script>" in payload.lower() and "alert" in payload.lower():
        print(f"\n{Colors.GREEN}[+] XSS Berhasil! Browser mengeksekusi skrip Anda.{Colors.ENDC}")
        print(f"{Colors.BLUE}Bahaya: Penyerang bisa mencuri cookie sesi pengguna.{Colors.ENDC}")
        add_xp(50)
    else:
        print(f"\n{Colors.FAIL}[-] Payload gagal. Skrip tidak dieksekusi.{Colors.ENDC}")
        
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def idor_lab():
    clear_screen()
    print_header("LAB: IDOR (Insecure Direct Object Reference)")
    print("Anda login sebagai User ID: 105 (Budi)")
    print("URL: https://api.bank.com/v1/balance?user_id=105")
    
    target_id = get_input("\nUbah user_id di URL untuk melihat saldo orang lain: ")
    
    if target_id != "105" and target_id.isdigit():
        print(f"\n{Colors.GREEN}[+] IDOR Ditemukan!{Colors.ENDC}")
        print(f"Menampilkan Saldo User ID {target_id}: Rp 500.000.000")
        print(f"{Colors.BLUE}Mitigasi: Server harus memvalidasi apakah user berhak mengakses ID tersebut.{Colors.ENDC}")
        add_xp(50)
    else:
        print(f"\n{Colors.FAIL}[-] Gagal. Anda hanya melihat saldo sendiri.{Colors.ENDC}")
        
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def bug_report_generator():
    clear_screen()
    print_header("BUG REPORT GENERATOR")
    print("Buat laporan profesional untuk mendapatkan Bounty!\n")
    
    title = get_input("Judul Bug: ")
    severity = get_input("Severity (Low/Medium/High/Critical): ")
    steps = get_input("Langkah Reproduksi: ")
    
    report = f"""
====================================
BUG BOUNTY REPORT
====================================
TITLE    : {title}
SEVERITY : {severity}
STATUS   : Triaged
REPORTER : 303 Hunter

STEPS TO REPRODUCE:
{steps}

MITIGASI:
- Implementasi input validation
- Gunakan security headers
====================================
"""
    print(f"\n{Colors.CYAN}Laporan Berhasil Dibuat:{Colors.ENDC}")
    print(report)
    
    # Simpan ke file
    with open("bug_report.txt", "w") as f:
        f.write(report)
    print(f"{Colors.GREEN}Laporan disimpan ke 'bug_report.txt'{Colors.ENDC}")
    add_xp(30)
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def bug_bounty_menu():
    while True:
        clear_screen()
        print_header("BUG BOUNTY HUNTER LAB")
        print("1. Lab SQL Injection")
        print("2. Lab XSS")
        print("3. Lab IDOR")
        print("4. Bug Report Generator")
        print("5. Kembali ke Menu Utama")
        
        choice = get_input("\nPilihan Anda (1-5): ")
        if choice == '1':
            sqli_lab()
        elif choice == '2':
            xss_lab()
        elif choice == '3':
            idor_lab()
        elif choice == '4':
            bug_report_generator()
        elif choice == '5':
            break
