
# Pertemuan 06 Nested Loop Python

**Nama:** Herfi Maulidya
**NIM:** 2225250129
**Kelas:** 3A

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan
dalam pemrograman Python.

## Struktur Proyek
- latihan/01_pasangan_indeks.py
- latihan/02_pola_segitiga.py
- latihan/03_jumlah_per_baris.py
- latihan/04_hitung_pasangan.py
- tugas/tabel_perkalian_dan_statistik.py

## Cara Menjalankan
python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
Loop luar mengatur baris dan loop dalam mengatur kolom.
Hasil perkalian i * j ditambahkan ke total_baris dan
total_semua. Jika hasil genap, count_genap bertambah satu.
Input n divalidasi menggunakan while agar harus positif.

## Hasil Pengujian

| Program | Input | Hasil yang Diharapkan | Status |
|---|---|---|---|
| Pasangan indeks | i=1..3, j=1..4 | 12 pasangan | Isi setelah diuji |
| Pola segitiga | n=1, 3, 5 | n baris | Isi setelah diuji |
| Jumlah per baris | i=1..4, j=1..3 | 6, 12, 18, 24 | Isi setelah diuji |
| Hitung pasangan | n=2, 3, 5 | 1, 3, 10 | Isi setelah diuji |
| Tugas 3 | n=1 | Total 1, genap 0 | Isi setelah diuji |
| Tugas 3 | n=2 | Total 9, genap 3 | Isi setelah diuji |
| Tugas 3 | n=3 | Total 36, genap 5 | Isi setelah diuji |

## Analisis Efisiensi
Untuk input n positif, loop dalam berjalan n kali
untuk setiap iterasi loop luar. Dengan demikian, badan
loop dalam dieksekusi n * n atau n² kali.

## Refleksi
Melalui praktikum Pertemuan 6, saya mempelajari penggunaan nested loop untuk memproses data dalam bentuk baris dan kolom. Saya memahami bahwa posisi inisialisasi variabel sangat penting, terutama dalam membedakan akumulasi jumlah per baris dengan akumulasi jumlah keseluruhan. Selain itu, penggunaan kondisi if membantu proses pencacahan berdasarkan kriteria tertentu, sedangkan while digunakan untuk memastikan input yang dimasukkan memenuhi ketentuan.

Kesulitan yang saya pelajari dalam praktikum ini adalah memahami alur perulangan bersarang dan memastikan setiap variabel diperbarui pada posisi yang tepat. Untuk mengatasinya, saya mempelajari alur program secara bertahap dan membandingkan hasil keluaran dengan perhitungan yang diharapkan. Praktikum ini membantu saya memahami bahwa ketelitian dalam menentukan batas perulangan, indentasi, dan posisi variabel sangat berpengaruh terhadap kebenaran hasil program.

## Sumber dan Bantuan
Modul Praktikum Algoritma dan Pemrograman Pertemuan 6: Nested Loop, Pola, Akumulasi, dan Pencacahan.

ChatGPT (OpenAI), digunakan sebagai bantuan untuk memahami instruksi tugas, mempelajari logika nested loop, menyusun kode program, serta membantu penjelasan dan dokumentasi praktikum.