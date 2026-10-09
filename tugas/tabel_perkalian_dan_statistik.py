
# Tugas 3: Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")
n = int(input("Masukkan n: "))

# Validasi agar n harus positif
while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

# Akumulator keseluruhan dan counter hasil genap
total_semua = 0
count_genap = 0

# Loop luar mengatur baris
for i in range(1, n + 1):
    total_baris = 0

    # Loop dalam mengatur kolom
    for j in range(1, n + 1):
        hasil = i * j

        # Menampilkan hasil perkalian
        print(f"{hasil:4}", end="")

        # Akumulasi jumlah baris dan keseluruhan
        total_baris += hasil
        total_semua += hasil

        # Menghitung banyak hasil genap
        if hasil % 2 == 0:
            count_genap += 1

    # Dilakukan setelah satu baris selesai
    print(f"   | jumlah baris = {total_baris}")

# Statistik akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
