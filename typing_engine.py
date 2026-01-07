import time
import random
from utils import clear_screen, print_header, Colors, get_input
from lessons import TYPING_TEXTS
from progress_tracker import update_typing_stats, add_xp

def run_typing_test():
    clear_screen()
    print_header("TYPING MASTER - PYTHON EDITION")
    
    target_text = random.choice(TYPING_TEXTS)
    print(f"{Colors.BLUE}Ketik teks di bawah ini secepat dan seakurat mungkin:{Colors.ENDC}")
    print(f"\n{Colors.BOLD}{target_text}{Colors.ENDC}\n")
    
    input(f"{Colors.WARNING}Tekan ENTER untuk mulai...{Colors.ENDC}")
    
    start_time = time.time()
    user_input = input(f"{Colors.CYAN}> {Colors.ENDC}")
    end_time = time.time()
    
    duration = end_time - start_time
    
    # Hitung Akurasi
    correct_chars = 0
    for i in range(min(len(target_text), len(user_input))):
        if target_text[i] == user_input[i]:
            correct_chars += 1
            
    accuracy = (correct_chars / len(target_text)) * 100 if len(target_text) > 0 else 0
    
    # Hitung WPM (Words Per Minute)
    # Standar: 1 kata = 5 karakter
    wpm = (len(user_input) / 5) / (duration / 60)
    
    print(f"\n{Colors.GREEN}--- HASIL ---{Colors.ENDC}")
    print(f"Waktu    : {duration:.2f} detik")
    print(f"Kecepatan: {wpm:.2f} WPM")
    print(f"Akurasi  : {accuracy:.2f}%")
    
    if accuracy == 100:
        print(f"{Colors.BOLD}Luar biasa! Sempurna!{Colors.ENDC}")
    elif accuracy > 80:
        print("Bagus! Terus berlatih.")
    else:
        print("Jangan menyerah, coba lagi!")
        
    # Simpan progres
    update_typing_stats(wpm, accuracy)
    print(f"\n{Colors.BLUE}Progres Anda telah disimpan.{Colors.ENDC}")
        
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali ke menu...{Colors.ENDC}")

def run_time_attack():
    clear_screen()
    print_header("TIME ATTACK MODE")
    print(f"{Colors.FAIL}Tantangan: Ketik sebanyak mungkin dalam 30 detik!{Colors.ENDC}\n")
    
    input(f"{Colors.WARNING}Tekan ENTER untuk mulai...{Colors.ENDC}")
    
    start_time = time.time()
    total_chars = 0
    
    while time.time() - start_time < 30:
        target = random.choice(TYPING_TEXTS)
        print(f"\n{Colors.BOLD}{target}{Colors.ENDC}")
        user_input = input(f"{Colors.CYAN}> {Colors.ENDC}")
        
        if user_input == target:
            total_chars += len(target)
            print(f"{Colors.GREEN}Sempurna! +{len(target)} poin{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}Salah!{Colors.ENDC}")
            
    wpm = (total_chars / 5) / (30 / 60)
    print(f"\n{Colors.HEADER}--- WAKTU HABIS ---{Colors.ENDC}")
    print(f"Total Karakter: {total_chars}")
    print(f"Kecepatan     : {wpm:.2f} WPM")
    
    xp_gained = int(total_chars / 2)
    add_xp(xp_gained)
    print(f"{Colors.GREEN}+ {xp_gained} XP didapatkan!{Colors.ENDC}")
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")