
make Python + OpenCV + cvzone + MediaPipe 

note : kalo versi py nya versi 3.10 atau dibawah nya ga usah make cvzone
( cvzone buat yg versi py nya diatas 10 )

 inti nya Saat gesture peace sign ( ✌️ ) terdeteksi,
kamera akan otomatis blur secara realtime.

---

# 📥 1. Requirements

- Python 3.10 – 3.13  
- Webcam / Kamera  
- Git (opsional)

Download Python: https://www.python.org/downloads/

---

# 📁 2. Download Project

git clone https://github.com/USERNAME/fotokitablur.git  
cd fotokitablur

---

# 🐍 3. Setup Virtual Environment (ENV)

python -m venv env

Aktifkan:

Windows:
env\Scripts\activate

Jika berhasil:
(env) PS D:\fotokitablur>

---

# 📦 4. Install Dependencies

pip install -r requirements.txt

Jika belum ada requirements.txt:
pip install opencv-python cvzone mediapipe

---

# ▶️ 5. Run Project

python main.py

---

# 🎮 6. Cara Pakai

- Tunjukkan tangan ke kamera  
- Buat gesture ✌️ (peace sign)  
- Kamera akan blur otomatis  
- Tekan ESC untuk keluar  

---

# 📁 7. Project Structure

fotokitablur/
├── main.py
├── requirements.txt
├── .gitignore
└── env/   (JANGAN di-upload)

---

# ⚠️ 8. Notes

- Pastikan webcam aktif  
- Jika lag, gunakan resolusi 640x480  
- cvzone membutuhkan MediaPipe  
- Python 3.10–3.11 lebih stabil  

---

# 🚀 9. Troubleshooting

Kamera tidak muncul:
cv2.VideoCapture(1)

---

Lag:
640x480

---

Error mediapipe:
Gunakan Python 3.10 / 3.11

---

# 👨‍💻 Author

Ishac Kurnia Sandy 
Mahasiswa bukan Mahasiswi

---

# ⭐ Support

Kalau project ini membantu, kasih ⭐ di repository ini!
