PYTHON_LESSONS = [
    {
        "title": "Variabel & Tipe Data",
        "content": """
Di Python, variabel digunakan untuk menyimpan data.
Contoh:
nama = "Adjie"  # String
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
    "payload = \"' OR 1=1 --\"; r = requests.post(url, data={'user': payload})"
]
