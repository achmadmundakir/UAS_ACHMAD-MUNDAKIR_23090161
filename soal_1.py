mahasiswa = []

while True:
    # Input NIM
    nim = input("nim: ")

    nama = input("nama: ")

    mahasiswa.append({"nim": nim, "nama": nama})

    jawaban = input("Ingin menambahkan lagi? (iya/tidak): ")

    if jawaban.lower() != "iya":
        break

print("Data Mahasiswa:")
for mahasiswa in mahasiswa:
    print(f"NIM: {mahasiswa['23090161']}, Nama: {mahasiswa['achmad mundakir']}")

print("end")