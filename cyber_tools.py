import hashlib
import socket
import time
from utils import clear_screen, print_header, Colors, get_input

def hash_cracker_sim():
    clear_screen()
    print_header("SIMULASI HASH CRACKER")
    print("Mencoba memecahkan hash SHA256 dengan brute force sederhana.\n")
    
    target_pass = "admin123"
    target_hash = hashlib.sha256(target_pass.encode()).hexdigest()
    
    print(f"Target Hash: {Colors.FAIL}{target_hash}{Colors.ENDC}")
    print(f"Wordlist: ['admin', 'password', '123456', 'admin123', 'qwerty']\n")
    
    wordlist = ['admin', 'password', '123456', 'admin123', 'qwerty']
    
    input(f"{Colors.WARNING}Tekan ENTER untuk mulai cracking...{Colors.ENDC}")
    
    for word in wordlist:
        print(f"Mencoba: {word}...", end="\r")
        time.sleep(0.5)
        current_hash = hashlib.sha256(word.encode()).hexdigest()
        if current_hash == target_hash:
            print(f"\n\n{Colors.GREEN}[+] Password Ditemukan: {word}{Colors.ENDC}")
            break
    else:
        print(f"\n\n{Colors.FAIL}[-] Password tidak ditemukan di wordlist.{Colors.ENDC}")
        
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def port_scanner_sim():
    clear_screen()
    print_header("SIMULASI PORT SCANNER")
    print("Memeriksa port yang terbuka pada localhost (Simulasi).\n")
    
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    target = "127.0.0.1"
    
    input(f"{Colors.WARNING}Tekan ENTER untuk mulai scanning...{Colors.ENDC}")
    
    found_ports = []
    for port in ports:
        print(f"Scanning Port {port}...", end="\r")
        time.sleep(0.2)
        if port in [22, 80, 443, 3306]:
            service = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}.get(port, "Unknown")
            print(f"{Colors.GREEN}[+] Port {port} OPEN  ({service}){Colors.ENDC}")
            found_ports.append(port)
        else:
            print(f"{Colors.FAIL}[-] Port {port} CLOSED{Colors.ENDC}")
            
    print(f"\n{Colors.BLUE}Scan Selesai. Ditemukan {len(found_ports)} port terbuka.{Colors.ENDC}")
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def network_scanner_sim():
    clear_screen()
    print_header("SIMULASI NETWORK SCANNER")
    print("Mencari perangkat aktif dalam jaringan lokal (Simulasi).\n")
    
    base_ip = "192.168.1."
    devices = [
        {"ip": "192.168.1.1", "mac": "AA:BB:CC:DD:EE:01", "vendor": "Router-TP-Link"},
        {"ip": "192.168.1.5", "mac": "AA:BB:CC:DD:EE:05", "vendor": "Samsung-Phone"},
        {"ip": "192.168.1.12", "mac": "AA:BB:CC:DD:EE:12", "vendor": "MacBook-Pro"},
    ]
    
    input(f"{Colors.WARNING}Tekan ENTER untuk mulai scanning jaringan...{Colors.ENDC}")
    
    print(f"{'IP Address':<15} | {'MAC Address':<17} | {'Vendor'}")
    print("-" * 50)
    
    for i in range(1, 20):
        current_ip = f"{base_ip}{i}"
        print(f"Scanning {current_ip}...", end="\r")
        time.sleep(0.1)
        
        for device in devices:
            if device["ip"] == current_ip:
                print(f"{Colors.GREEN}{device['ip']:<15} | {device['mac']:<17} | {device['vendor']}{Colors.ENDC}")
                break
                
    print(f"\n{Colors.BLUE}Scan Jaringan Selesai.{Colors.ENDC}")
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")

def cyber_menu():
    while True:
        clear_screen()
        print_header("CYBER SECURITY LAB")
        print("1. Simulasi Hash Cracker")
        print("2. Simulasi Port Scanner")
        print("3. Simulasi Network Scanner")
        print("4. Kembali ke Menu Utama")
        
        choice = get_input("\nPilihan Anda (1-4): ")
        if choice == '1':
            hash_cracker_sim()
        elif choice == '2':
            port_scanner_sim()
        elif choice == '3':
            network_scanner_sim()
        elif choice == '4':
            break
