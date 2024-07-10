class Antrian:
    def __init__(self):
        self.item = []

    def kosong(self):
        return len(self.item) == 0

    def tambah_pesanan(self, pesanan):
        self.item.append(pesanan)
        print(f'Pesanan "{pesanan}" telah ditambahkan ke dalam antrian.')

    def hapus_pesanan(self):
        if self.kosong():
            return "Antrian kosong, tidak ada pesanan yang bisa dihapus."
        return f'Pesanan "{self.item.pop(0)}" telah dihapus dari antrian.'

    def ukuran(self):
        return len(self.item)

    def tampilkan(self):
        if self.kosong():
            return "Antrian kosong."
        return f"Antrian pesanan saat ini: {', '.join(self.item)}"


antrian = Antrian()

antrian.tambah_pesanan("mie ayam")
antrian.tambah_pesanan("bakso")
antrian.tambah_pesanan("pentol")

print(antrian.tampilkan())

print(antrian.hapus_pesanan())

print(antrian.tampilkan())

print(antrian.hapus_pesanan())
print(antrian.hapus_pesanan())
print(antrian.hapus_pesanan())