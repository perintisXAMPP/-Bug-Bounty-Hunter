PYTHON_LESSONS = [
    {
        "title": "Variabel & Tipe Data",
        "content": """
Di Python, variabel digunakan untuk menyimpan data.
Contoh:
nama = "Manus"  # String
umur = 25       # Integer
pi = 3.14       # Float

Python adalah bahasa 'dynamically typed', artinya Anda tidak perlu 
mendeklarasikan tipe data secara eksplisit.
        """,
        "quiz": {
            "question": "Manakah cara penulisan variabel string yang benar?",
            "options": ["A. x = 5", "B. x = 'Halo'", "C. x = True"],
            "answer": "B"
        }
    },
    {
        "title": "Struktur Kontrol (If-Else)",
        "content": """
If-Else digunakan untuk mengambil keputusan.
Contoh:
if umur >= 18:
    print("Dewasa")
else:
    print("Anak-anak")

Penting: Python menggunakan indentasi (spasi) untuk menentukan blok kode!
        """,
        "quiz": {
            "question": "Apa yang digunakan Python untuk menentukan blok kode?",
            "options": ["A. Kurung kurawal {}", "B. Titik koma ;", "C. Indentasi (Spasi)"],
            "answer": "C"
        }
    },
    {
        "title": "Perulangan (Loops)",
        "content": """
For loop digunakan untuk mengulang sesuatu.
Contoh:
for i in range(5):
    print(i)

Ini akan mencetak angka 0 sampai 4.
        """,
        "quiz": {
            "question": "Apa hasil dari range(3)?",
            "options": ["A. 0, 1, 2", "B. 1, 2, 3", "C. 0, 1, 2, 3"],
            "answer": "A"
        }
    },
    {
        "title": "Python for Cyber Security: Hashing",
        "content": """
Dalam keamanan siber, hashing digunakan untuk memverifikasi integritas data.
Python memiliki library 'hashlib' untuk ini.
Contoh:
import hashlib
teks = "password123"
hash_obj = hashlib.sha256(teks.encode())
print(hash_obj.hexdigest())

Hash bersifat satu arah, artinya Anda tidak bisa mengembalikan hash ke teks asli.
        """,
        "quiz": {
            "question": "Library apa yang digunakan untuk hashing di Python?",
            "options": ["A. crypto", "B. hashlib", "C. secure_hash"],
            "answer": "B"
        }
    },
    {
        "title": "Network Security: Socket Programming",
        "content": """
Socket adalah titik akhir komunikasi antar mesin. Python menggunakan library 'socket'.
Contoh membuat koneksi sederhana:
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))

Ini adalah dasar untuk membuat Port Scanner atau alat audit jaringan.
        """,
        "quiz": {
            "question": "Apa fungsi socket.connect()?",
            "options": ["A. Memutus koneksi", "B. Membuat koneksi ke host/port", "C. Mengirim email"],
            "answer": "B"
        }
    },
    {
        "title": "Bug Bounty: SQL Injection (SQLi)",
        "content": """
SQL Injection terjadi ketika input pengguna langsung dimasukkan ke query database.
Bahaya: Penyerang bisa melihat data sensitif atau menghapus database.

Cara Mengatasi (Mitigasi):
Gunakan 'Parameterized Queries'. Jangan pernah menggabungkan string input langsung!
Contoh Aman:
cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))
        """,
        "quiz": {
            "question": "Apa cara terbaik mencegah SQL Injection?",
            "options": ["A. Menghapus database", "B. Parameterized Queries", "C. Menggunakan password panjang"],
            "answer": "B"
        }
    },
    {
        "title": "Bug Bounty: Cross-Site Scripting (XSS)",
        "content": """
XSS memungkinkan penyerang menjalankan JavaScript di browser korban.
Contoh Payload: <script>alert('Hacked!')</script>

Cara Mengatasi (Mitigasi):
Selalu lakukan 'Output Encoding'. Ubah karakter khusus seperti < menjadi &lt;
sehingga browser tidak mengeksekusinya sebagai kode.
        """,
        "quiz": {
            "question": "Apa yang dijalankan penyerang dalam serangan XSS?",
            "options": ["A. SQL Query", "B. JavaScript", "C. Python Script"],
            "answer": "B"
        }
    },
    {
        "title": "Recon: Subdomain Enumeration",
        "content": """
Pengintaian dimulai dengan mencari subdomain. Banyak bug ditemukan di subdomain
yang terlupakan oleh developer (seperti dev atau staging).

Python dapat melakukan ini dengan mencoba melakukan DNS lookup pada daftar kata.
Contoh:
import socket
subdomains = ['www', 'dev', 'api', 'mail']
for sub in subdomains:
    try:
        ip = socket.gethostbyname(f"{sub}.target.com")
        print(f"Ditemukan: {sub}.target.com -> {ip}")
    except:
        pass
        """,
        "quiz": {
            "question": "Mengapa mencari subdomain itu penting?",
            "options": ["A. Untuk mempercepat internet", "B. Menemukan aset yang kurang terjaga", "C. Untuk mengganti nama domain"],
            "answer": "B"
        }
    },
    {
        "title": "Recon: Directory Busting",
        "content": """
Directory busting adalah teknik mencari folder tersembunyi di web server.
Target utama: /.env, /admin, /config, /backup.

Gunakan library 'requests' untuk mengecek status code HTTP.
Status 200 berarti folder ada, 404 berarti tidak ada, 403 berarti dilarang.
        """,
        "quiz": {
            "question": "HTTP Status Code mana yang menunjukkan folder ditemukan?",
            "options": ["A. 404", "B. 200", "C. 500"],
            "answer": "B"
        }
    },
    {
        "title": "Vulnerability Analysis: CVSS Scoring",
        "content": """
CVSS (Common Vulnerability Scoring System) digunakan untuk menilai tingkat bahaya bug.
Skala:
- 0.1 - 3.9: Low
- 4.0 - 6.9: Medium
- 7.0 - 8.9: High
- 9.0 - 10.0: Critical

Bug Bounty Hunter fokus pada bug High dan Critical untuk mendapatkan bounty besar.
        """,
        "quiz": {
            "question": "Berapa skor minimal untuk kategori kerentanan 'Critical'?",
            "options": ["A. 7.0", "B. 8.0", "C. 9.0"],
            "answer": "C"
        }
    },
    {
        "title": "Vulnerability Scanning: CVE Lookup",
        "content": """
CVE (Common Vulnerabilities and Exposures) adalah ID unik untuk setiap bug yang ditemukan.
Contoh: CVE-2021-44228 (Log4Shell).

Python dapat digunakan untuk mencari informasi CVE melalui API publik.
Mencocokkan versi software dengan daftar CVE adalah inti dari Vulnerability Scanning.
        """,
        "quiz": {
            "question": "Apa kepanjangan dari CVE?",
            "options": ["A. Common Vulnerabilities and Exposures", "B. Cyber Virus Entry", "C. Central Vulnerability Engine"],
            "answer": "A"
        }
    },
    {
        "title": "Advanced: Malware Analysis with Python",
        "content": """
Python sering digunakan untuk menganalisis file mencurigakan.
Teknik dasar: Mencocokkan hash file dengan database malware (seperti VirusTotal).

Contoh Kode Deteksi Sederhana:
import hashlib
def get_hash(file):
    return hashlib.md5(open(file, 'rb').read()).hexdigest()

Jika hash cocok dengan daftar hitam, file tersebut dianggap berbahaya.
        """,
        "quiz": {
            "question": "Metode apa yang digunakan untuk identifikasi malware berbasis signature?",
            "options": ["A. Hashing", "B. Kompresi", "C. Enkripsi"],
            "answer": "A"
        }
    },
    {
        "title": "Advanced: Network Manipulation (Scapy)",
        "content": """
Scapy adalah library Python yang sangat kuat untuk manipulasi paket jaringan.
Anda bisa membuat, mengirim, dan mengendus paket kustom.

Contoh Membuat Paket ICMP (Ping):
from scapy.all import IP, ICMP, send
packet = IP(dst="8.8.8.8")/ICMP()
send(packet)

Ini digunakan untuk audit jaringan tingkat lanjut dan pengujian firewall.
        """,
        "quiz": {
            "question": "Library Python apa yang populer untuk manipulasi paket jaringan?",
            "options": ["A. Requests", "B. Scapy", "C. BeautifulSoup"],
            "answer": "B"
        }
    },
    {
        "title": "Case Study: Brute Force Detection",
        "content": """
Studi Kasus: Mendeteksi serangan Brute Force dari log server.
Log: '2023-10-01 10:00:01 - Failed login from 192.168.1.50'

Analisis: Jika satu IP gagal login > 5 kali dalam 1 menit, tandai sebagai serangan.
Python dapat memproses ribuan baris log dalam hitungan detik menggunakan library 'pandas'.
        """,
        "quiz": {
            "question": "Apa indikator utama serangan Brute Force dalam log?",
            "options": ["A. Login berhasil", "B. Banyak kegagalan login dari satu IP", "C. Server restart"],
            "answer": "B"
        }
    }
]

TYPING_TEXTS = [
    "print('Hello World')",
    "for i in range(10): print(i)",
    "def hitung_luas(p, l): return p * l",
    "if x > 0: print('Positif') else: print('Negatif')",
    "my_list = [1, 2, 3, 4, 5]",
    "class Mobil: def __init__(self): pass",
    "import hashlib; h = hashlib.sha256(b'admin').hexdigest()",
    "import socket; s = socket.socket(); s.connect(('127.0.0.1', 80))",
    "import requests; r = requests.get('https://api.github.com')",
    "for port in range(1, 1024): s.connect_ex(('target', port))",
    "cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))",
    "sanitized = html.escape(user_input)",
    "if session.get('user_id') != target_id: raise AccessDenied()",
    "payload = \"' OR 1=1 --\"; r = requests.post(url, data={'user': payload})",
    "ip = socket.gethostbyname(f'{sub}.{domain}')",
    "r = requests.get(f'{url}/{path}', timeout=5)",
    "headers = requests.head(url).headers; print(headers.get('Server'))",
    "whois_data = socket.create_connection(('whois.verisign-grs.com', 43))",
    "cvss_score = 9.8; severity = 'CRITICAL' if cvss_score >= 9.0 else 'HIGH'",
    "cve_id = 'CVE-2021-44228'; r = requests.get(f'https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve_id}')",
    "if version < '2.4.49': print('Vulnerable to Path Traversal!')",
    "vulnerabilities = [v for v in db if v['software'] == target_software]",
    "pkt = IP(dst='192.168.1.1')/TCP(dport=80, flags='S')",
    "malware_hash = hashlib.sha256(file_content).hexdigest()",
    "df = pd.read_csv('access.log'); brute_ips = df[df['status'] == 401]",
    "payload = b'A' * 64 + struct.pack('<I', 0xdeadbeef)"
]
