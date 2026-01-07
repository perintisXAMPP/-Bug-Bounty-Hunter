import time
from utils import clear_screen, print_header, Colors, get_input, slow_print
from recon_lab import subdomain_finder_sim, dir_buster_sim
from vulnerability_lab import vuln_scanner_sim
from bug_bounty_lab import sqli_lab, xss_lab, idor_lab, bug_report_generator
from progress_tracker import add_xp

def start_campaign():
    clear_screen()
    print_header("BUG BOUNTY CAMPAIGN: MISSION START")
    
    slow_print(f"{Colors.CYAN}Misi Anda: Temukan dan laporkan kerentanan pada 'GlobalTech Inc'.{Colors.ENDC}")
    slow_print("Target: globaltech.com")
    slow_print("Reward: Up to 500 XP & Legendary Badge\n")
    
    input(f"{Colors.WARNING}Tekan ENTER untuk memulai fase RECONNAISSANCE...{Colors.ENDC}")
    
    # Step 1: Recon
    subdomain_finder_sim()
    dir_buster_sim()
    
    clear_screen()
    print_header("CAMPAIGN PROGRESS: RECON COMPLETE")
    slow_print(f"{Colors.GREEN}[+] Data Terkumpul: Subdomain 'dev.globaltech.com' dan direktori '/admin' ditemukan.{Colors.ENDC}")
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk lanjut ke VULNERABILITY SCANNING...{Colors.ENDC}")
    
    # Step 2: Vuln Scan
    vuln_scanner_sim()
    
    clear_screen()
    print_header("CAMPAIGN PROGRESS: VULNERABILITIES IDENTIFIED")
    slow_print(f"{Colors.FAIL}[!] Temuan Kritis: Versi Apache rentan terhadap SQL Injection.{Colors.ENDC}")
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk lanjut ke EXPLOITATION LAB...{Colors.ENDC}")
    
    # Step 3: Exploitation (Pilih salah satu yang relevan)
    print("\nPilih teknik eksploitasi yang ingin Anda verifikasi:")
    print("1. SQL Injection (Bypass Admin)")
    print("2. XSS (Steal Session)")
    print("3. IDOR (Access User Data)")
    
    choice = get_input("\nPilihan Anda (1-3): ")
    if choice == '1':
        sqli_lab()
    elif choice == '2':
        xss_lab()
    else:
        idor_lab()
        
    clear_screen()
    print_header("CAMPAIGN PROGRESS: VERIFICATION COMPLETE")
    slow_print(f"{Colors.GREEN}[+] Bug Terverifikasi! Sekarang buat laporan untuk mendapatkan bounty.{Colors.ENDC}")
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk membuka BUG REPORT GENERATOR...{Colors.ENDC}")
    
    # Step 4: Reporting
    bug_report_generator()
    
    clear_screen()
    print_header("MISSION ACCOMPLISHED!")
    slow_print(f"{Colors.HEADER}{Colors.BOLD}Selamat! Laporan Anda telah diterima oleh GlobalTech Inc.{Colors.ENDC}")
    slow_print(f"{Colors.GREEN}Bounty: 200 XP Bonus ditambahkan ke akun Anda!{Colors.ENDC}")
    
    add_xp(200)
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali ke Menu Utama...{Colors.ENDC}")
