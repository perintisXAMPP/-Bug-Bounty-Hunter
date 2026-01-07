import time
import random
from utils import clear_screen, print_header, Colors, get_input
from progress_tracker import add_xp

def subdomain_finder_sim():
    clear_screen()
    print_header("SIMULASI SUBDOMAIN FINDER")
    domain = get_input("Masukkan Domain Target (contoh: target.com): ")
    
    wordlist = ['www', 'mail', 'dev', 'api', 'staging', 'admin', 'blog', 'vpn', 'test', 'internal']
    print(f"\n{Colors.CYAN}Memulai enumerasi subdomain untuk {domain}...{Colors.ENDC}\n")
    
    found = []
    for sub in wordlist:
        print(f"Mengecek: {sub}.{domain}...", end="\r")
        time.sleep(0.3)
        # Simulasi penemuan acak
        if sub in ['www', 'api', 'dev', 'admin']:
            ip = f"104.26.{random.randint(1,255)}.{random.randint(1,255)}"
            print(f"{Colors.GREEN}[+] Ditemukan: {sub}.{domain:<15} -> {ip}{Colors.ENDC}")
            found.append(f"{sub}.{domain}")
            
    print(f"\n{Colors.BLUE}Enumerasi Selesai. Ditemukan {len(found)} subdomain.{Colors.ENDC}")
    add_xp(40)
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def dir_buster_sim():
    clear_screen()
    print_header("SIMULASI DIRECTORY BUSTER")
    url = get_input("Masukkan URL Target (contoh: https://target.com): ")
    
    paths = ['/admin', '/login', '/.env', '/config', '/uploads', '/backup', '/robots.txt', '/api/v1']
    print(f"\n{Colors.CYAN}Memulai brute force direktori pada {url}...{Colors.ENDC}\n")
    
    for p in paths:
        print(f"Scanning: {p}...", end="\r")
        time.sleep(0.4)
        # Simulasi status code
        if p in ['/robots.txt', '/login']:
            print(f"{Colors.GREEN}[200 OK]      {url}{p}{Colors.ENDC}")
        elif p in ['/admin', '/.env', '/backup']:
            print(f"{Colors.WARNING}[403 Forbidden] {url}{p} (POTENSI BUG!){Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}[404 Not Found] {url}{p}{Colors.ENDC}")
            
    print(f"\n{Colors.BLUE}Scan Direktori Selesai.{Colors.ENDC}")
    add_xp(40)
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def banner_grabbing_sim():
    clear_screen()
    print_header("SIMULASI BANNER GRABBING")
    target = get_input("Masukkan IP/Domain Target: ")
    
    print(f"\n{Colors.CYAN}Mengambil informasi server dari {target}...{Colors.ENDC}\n")
    time.sleep(1)
    
    headers = {
        "Server": "Apache/2.4.41 (Ubuntu)",
        "X-Powered-By": "PHP/7.4.3",
        "Content-Type": "text/html; charset=UTF-8"
    }
    
    for key, val in headers.items():
        print(f"{Colors.BOLD}{key}:{Colors.ENDC} {val}")
        time.sleep(0.5)
        
    print(f"\n{Colors.WARNING}[!] Analisis: Versi Apache 2.4.41 mungkin memiliki kerentanan lama.{Colors.ENDC}")
    add_xp(30)
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def recon_menu():
    while True:
        clear_screen()
        print_header("RECONNAISSANCE & FOOTPRINTING LAB")
        print("1. Simulasi Subdomain Finder")
        print("2. Simulasi Directory Buster")
        print("3. Simulasi Banner Grabbing")
        print("4. Kembali ke Menu Utama")
        
        choice = get_input("\nPilihan Anda (1-4): ")
        if choice == '1':
            subdomain_finder_sim()
        elif choice == '2':
            dir_buster_sim()
        elif choice == '3':
            banner_grabbing_sim()
        elif choice == '4':
            break
