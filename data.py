import math
import matplotlib.pyplot as plt

def hitung_statistik(data):
    """Menghitung statistik dasar dari sebuah list angka"""
    # Struktur data dictionary untuk menyimpan hasil
    hasil = {
        'jumlah': sum(data),
        'rerata': sum(data)/len(data),
        'maksimum': max(data),
        'minimum': min(data),
        'standar_deviasi': math.sqrt(sum((x - (sum(data)/len(data)))**2 for x in data) / len(data))
    }
    return hasil

def plot_grafik(data):
    """Membuat grafik dari data menggunakan matplotlib"""
    # Struktur kontrol perulangan untuk membuat list warna
    warna = []
    for nilai in data:
        if nilai > 50:
            warna.append('r')  # merah untuk nilai > 50
        else:
            warna.append('b')  # biru untuk nilai <= 50
    
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(data)), data, color=warna)
    plt.title('Visualisasi Data')
    plt.xlabel('Indeks Data')
    plt.ylabel('Nilai')
    plt.grid(True)
    plt.show()

def main():
    print("Program Analisis Data Sederhana")
    print("===============================")
    
    # Input data dari pengguna
    data_input = input("Masukkan beberapa angka, pisahkan dengan spasi: ")
    data_list = [float(x) for x in data_input.split()]
    
    # Struktur kontrol percabangan
    if not data_list:
        print("Tidak ada data yang dimasukkan!")
        return
    
    # Hitung statistik
    statistik = hitung_statistik(data_list)
    
    print("\nHasil Analisis:")
    print("--------------")
    for key, value in statistik.items():
        print(f"{key.capitalize()}: {value:.2f}")
    
    # Plot grafik
    plot_grafik(data_list)

if __name__ == "__main__":
    main()