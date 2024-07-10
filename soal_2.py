import pandas as pd

# Membuat DataFrame dengan data yang diberikan
data = {
    'Nama': ['Farel', 'Izat', 'Atha'],
    'Algoritma dan Struktur Data 2': [90, 50, 65],
    'Matematika Numerik': [80, 60, 70]
}

df = pd.DataFrame(data)

# Menghitung rata-rata nilai untuk setiap mata kuliah
avg_alg_struktur = df['Algoritma dan Struktur Data 2'].mean()
avg_matematika_numerik = df['Matematika Numerik'].mean()

print("Rata-rata nilai Algoritma dan Struktur Data 2:", avg_alg_struktur)
print("Rata-rata nilai Matematika Numerik:", avg_matematika_numerik)

# Menghitung rata-rata nilai untuk setiap mahasiswa
df['Rata-rata'] = df[['Algoritma dan Struktur Data 2', 'Matematika Numerik']].mean(axis=1)

print("\nRata-rata nilai untuk setiap mahasiswa:")
print(df[['Nama', 'Rata-rata']])
