and Gesture Recognition (Python + OpenCV + MediaPipe)

Live Hand Gesture Recognition menggunakan MediaPipe dan OpenCV. Proyek ini deteksi 4 gesture tangan secara real-time lewat webcam. Cocok untuk demo interaktif, edukasi, atau prototipe UI berbasis gesture.

Fitur Utama
Gesture	Deskripsi
Semua jari terbuka	Gesture “Haii”
Hanya jari telunjuk	Gesture “Nama Saya”
Index True + Thumb False	Gesture “Rafli Tri Hanafi”
Hanya jempol	Gesture “Kerenn Kan”

Deteksi gesture real-time menggunakan webcam.

FPS display untuk monitoring performa.

Mendukung 2 tangan sekaligus tanpa logika tumpang tindih.

Stabil di Linux, Windows, dan macOS.

Teknologi & Library

Python 3

OpenCV – untuk webcam & image processing

MediaPipe – hand tracking & landmark detection

Instalasi

Clone repository

git clone hhttps://github.com/raflitugas0905/MotionDetect_python/blob/main/handgesture.py
cd hand-gesture


Buat virtual environment (opsional)

python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


requirements.txt minimal:

opencv-python
mediapipe

Cara Menjalankan
python gesture_recognition.py


Tekan q untuk keluar.

Pastikan webcam tersambung dan bisa digunakan.

Script otomatis mendeteksi gesture dan menampilkan nama gesture di layar.

Struktur File
hand-gesture/
│
├─ gesture_recognition.py  # Script utama
├─ requirements.txt        # Library Python yang dibutuhkan
└─ README.md               # Dokumentasi proyek

Catatan

Bisa di-extend untuk gesture lebih banyak dengan menambahkan kondisi di fungsi recognize_gesture.

Stabil di Linux/Ubuntu, Windows, dan macOS.

Kontributor

Rafli Tri Hanafi – Developer & Penulis Script

Lisensi

MIT License – bebas digunakan, dimodifikasi, dan didistribusikan.
