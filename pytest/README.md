# Zoo Management API

Versi 1.0.0

API ini dirancang untuk mengelola jadwal pemberian makan dan laporan terkait kebun binatang. Proyek ini dibangun menggunakan Flask dan menggunakan database SQLite untuk menyimpan data secara permanen.

## Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Fitur](#fitur)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Instalasi dan Pengaturan](#instalasi-dan-pengaturan)
- [Menjalankan Proyek](#menjalankan-proyek)
- [Menggunakan API](#menggunakan-api)
- [Pengujian](#pengujian)
- [Dokumentasi API](#dokumentasi-api)
- [Struktur Proyek](#struktur-proyek)
- [Fitur Selanjutnya](#fitur-selanjutnya)

## Tentang Proyek

Zoo Management API adalah aplikasi backend yang memungkinkan pengguna mengelola berbagai aspek kebun binatang, seperti jadwal pemberian makan hewan. Aplikasi ini dilengkapi dengan API yang mendukung operasi CRUD (Create, Read, Update, Delete) pada data jadwal pemberian makan. Swagger digunakan untuk mendokumentasikan API agar mudah dipahami dan diakses oleh pengembang lain.

## Fitur

- Menambahkan Jadwal Pemberian Makan: Endpoint untuk menambahkan jadwal pemberian makan baru untuk hewan.
- Mendapatkan Semua Jadwal Pemberian Makan: Mengambil daftar semua jadwal yang ada.
- Memperbarui Jadwal Pemberian Makan: Mengubah informasi pada jadwal pemberian makan.
- Menghapus Jadwal Pemberian Makan: Menghapus jadwal pemberian makan berdasarkan ID.
- Dokumentasi API: Menggunakan Swagger UI untuk mempermudah pengujian dan penggunaan API.

## Teknologi yang Digunakan

- Python 3.12 - Bahasa pemrograman yang digunakan.
- Flask - Web Framework untuk membuat API.
- Flask-Migrate - Untuk migrasi database.
- SQLite - Database lokal yang digunakan untuk menyimpan data.
- SQLAlchemy - ORM untuk mengelola database.
- Flasgger - Untuk dokumentasi API menggunakan Swagger.
- Pytest - Untuk pengujian unit dan integrasi.
- Poetry - Manajemen dependensi dan virtual environment.

## Instalasi dan Pengaturan

### Prasyarat

- Python 3.12 harus terinstal di sistem Anda.
- Poetry untuk manajemen dependensi, bisa diinstal dengan perintah:

``
  pip install poetry
  
``

### Langkah Instalasi:

1. Clone repositori ini:
``
   git clone <URL_REPOSITORY>
   cd <root_project_directory>

   ``
2. Instal dependensi:

``
   poetry install

``

3.Inisialisasi migrasi database:

``
   poetry run flask db init
   poetry run flask db migrate
   poetry run flask db upgrade

``

## Menjalankan Proyek

### Jalankan Aplikasi

Aktifkan lingkungan virtual dan jalankan aplikasi:

poetry run flask run

Aplikasi akan berjalan di ``http://localhost:5000.``

## Menggunakan API

API dapat diakses menggunakan alat seperti Postman atau Swagger UI yang sudah disediakan.

- Swagger UI: Dokumentasi interaktif API tersedia di `http://localhost:5000/apidocs/`.
- Endpoint Utama:
  - GET /feedings - Mendapatkan semua jadwal pemberian makan.
  - POST /feedings - Menambahkan jadwal pemberian makan baru.
  - PUT /feedings/{id} - Memperbarui jadwal pemberian makan berdasarkan ID.
  - DELETE /feedings/{id} - Menghapus jadwal pemberian makan berdasarkan ID.

## Pengujian

Proyek ini menggunakan Pytest untuk pengujian.

### Menjalankan Pengujian

Gunakan perintah berikut untuk menjalankan semua pengujian:

poetry run pytest

### Cakupan Pengujian

Untuk melihat cakupan kode yang diuji, gunakan:

poetry run pytest --cov=app

## Dokumentasi API

API ini didokumentasikan menggunakan Swagger. Anda bisa melihat semua endpoint, bersama dengan contoh input dan output, di Swagger UI pada http://localhost:5000/apidocs/.

File dokumentasi Swagger terdapat di swagger/swagger.json.

## Struktur Proyek

Berikut adalah struktur proyek setelah pengembangan fitur dasar selesai:

/<root_project_directory>/
│
├── app/
│   ├── __init__.py          # Inisialisasi aplikasi Flask dan konfigurasi
│   ├── config.py            # File konfigurasi untuk aplikasi, seperti konfigurasi database
│   ├── models.py            # Model database menggunakan SQLAlchemy
│   ├── routes.py            # Endpoint dan route aplikasi Flask
│   └── templates/           # Template HTML (contoh index.html)
│
├── swagger/
│   └── swagger.json         # File spesifikasi Swagger (OpenAPI) untuk dokumentasi API
│
├── tests/
│   ├── conftest.py          # Fixtures untuk pytest
│   └── test_feedings.py     # File berisi unit tests untuk jadwal pemberian makan
│
├── migrations/              # Folder yang digunakan oleh Flask-Migrate untuk migrasi database
├── static/                  # File statis (CSS/JS) jika diperlukan
├── app.py                   # File utama untuk menjalankan aplikasi Flask
├── pyproject.toml           # File konfigurasi Poetry
├── poetry.lock              # File kunci untuk memastikan versi dependensi tetap sama
├── README.md                # Dokumentasi proyek
└── .gitignore               # File gitignore untuk mengabaikan file/folder tertentu saat commit

## Fitur Selanjutnya

- Validasi Input: Tambahkan validasi untuk memastikan bahwa input yang diberikan sesuai dengan spesifikasi.
- Feeding Schedule Notifications: Tambahkan fitur untuk mengingatkan pengguna mengenai jadwal pemberian makan.
- Deployment ke Server: Deploy aplikasi ke layanan cloud seperti Heroku, AWS, atau DigitalOcean.
- Frontend Interface: Buat interface pengguna dengan framework seperti React atau menggunakan template HTML.
