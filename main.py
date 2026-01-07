from utils import clear_screen, print_header, Colors, slow_print, get_input
from lessons import PYTHON_LESSONS
from typing_engine import run_typing_test, run_time_attack
from progress_tracker import update_lesson_status, display_progress
from cyber_tools import cyber_menu
from bug_bounty_lab import bug_bounty_menu
from recon_lab import recon_menu
from vulnerability_lab import vulnerability_menu
from campaign_manager import start_campaign
from advanced_labs import advanced_menu

def show_lesson(lesson):
    clear_screen()
    print_header(f"MATERI: {lesson['title']}")
    slow_print(lesson['content'])
    
    print(f"\n{Colors.YELLOW}--- KUIS SINGKAT ---{Colors.ENDC}")
    print(lesson['quiz']['question'])
    for opt in lesson['quiz']['options']:
        print(opt)
        
    ans = get_input("\nJawaban Anda (A/B/C): ").upper()
    if ans == lesson['quiz']['answer']:
        print(f"\n{Colors.GREEN}Benar! Anda hebat.{Colors.ENDC}")
        update_lesson_status(lesson['title'])
    else:
        print(f"\n{Colors.FAIL}Salah. Jawaban yang benar adalah {lesson['quiz']['answer']}.{Colors.ENDC}")
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk lanjut...{Colors.ENDC}")

def main_menu():
    while True:
        clear_screen()
        print_header("PYTHON LEARNING & TYPING MASTER")
        print(f"{Colors.BLUE}Selamat datang! Pilih menu untuk memulai:{Colors.ENDC}")
        print(f"{Colors.YELLOW}{Colors.BOLD}>>> 0. START BUG BOUNTY CAMPAIGN (FULL MISSION) <<<{Colors.ENDC}")
        print("1. Belajar Dasar Python (Materi & Kuis)")
        print("2. Latihan Mengetik (Sintaks Python)")
        print("3. Mode Time Attack (Tantangan 30 Detik)")
        print("4. Reconnaissance & Footprinting Lab (Pengintaian)")
        print("5. Vulnerability Scanning & Analysis Lab (Identifikasi)")
        print("6. Cyber Security Lab (Simulasi)")
        print("7. Bug Bounty Hunter Lab (Eksploitasi & Mitigasi)")
        print("8. Advanced Cyber Security Lab (Malware & Forensics)")
        print("9. Lihat Progres Belajar")
        print("10. Tentang Program")
        print("11. Keluar")
        
        choice = get_input("\nPilihan Anda (0-11): ")
        
        if choice == '0':
            start_campaign()
        elif choice == '1':
            for lesson in PYTHON_LESSONS:
                show_lesson(lesson)
        elif choice == '2':
            run_typing_test()
        elif choice == '3':
            run_time_attack()
        elif choice == '4':
            recon_menu()
        elif choice == '5':
            vulnerability_menu()
        elif choice == '6':
            cyber_menu()
        elif choice == '7':
            bug_bounty_menu()
        elif choice == '8':
            advanced_menu()
        elif choice == '9':
            display_progress()
        elif choice == '10':
            clear_screen()
            print_header("TENTANG PROGRAM")
            print("Program ini dirancang untuk membantu pemula")
            print("menguasai dasar Python sambil melatih kecepatan mengetik.")
            print("Dibuat dengan cinta oleh Manus.")
            input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")
        elif choice == '11':
            print(f"\n{Colors.GREEN}Terima kasih telah belajar! Sampai jumpa.{Colors.ENDC}")
            break
        else:
            print(f"\n{Colors.FAIL}Pilihan tidak valid!{Colors.ENDC}")
            time.sleep(1)

if __name__ == "__main__":
    import time
    main_menu()
