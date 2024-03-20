from os import system

def menu():
    print("|--Menu Minuman:\t           |")
    print("|1. Es Teh Manis\t Rp 4.000  |")
    print("|2. Es Teh Tawar\t Rp 3.000  |")
    print("|3. Air Mineral \t Rp 2.000  |")
    print("|--Menu Makanan:\t           |")
    print("|4. Ayam Bakar  \t Rp 12.000 |")
    print("|5. Ayam Goreng \t Rp 12.000 |")
    print("|6. Nasi Goreng \t Rp 10.000 |")
    print("|7. Mie Ayam    \t Rp 10.000 |")
    print('='*35)
   

def pesan_menu():

    while True: 
        pilihan = int(input("Pilih hidangan (masukkan nomor dari menu makanan di atas): "))
        if pilihan in range(1, 8):
            item = None
            harga = None
            if pilihan == 1:
                item = "Es Teh Manis"
                harga = 4000
            elif pilihan == 2:
                item = "Es Teh Tawar"
                harga = 3000
            elif pilihan == 3:
                item = "Air Mineral"
                harga = 2000
            elif pilihan == 4:
                item = "Ayam Bakar"
                harga = 12000
            elif pilihan == 5:
                item = "Ayam Goreng"
                harga = 12000
            elif pilihan == 6:
                item = "Nasi Goreng"
                harga = 10000
            elif pilihan == 7:
                item = "Mie Ayam"
                harga = 10000
            
            while True:
                try:
                    jumlah = int(input(f"Berapa banyak {item} yang ingin Anda pesan: "))
                    if jumlah > 0:
                        return item, harga * jumlah, jumlah
                    else:
                        print("Jumlah tidak valid. Silakan masukkan angka yang lebih besar dari 0.")
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka.") 
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
        continue
        

def finish():
    global total_pembelian, pesanan

    print("--------------------------------------------")
    print("Pesanan:")
    for item, harga, jumlah in pesanan:
        print(f"| {item:15} x {jumlah} \t: Rp {harga:8,.2f}")
    print("--------------------------------")
    print(f"| Total Pembelian \t: Rp {total_pembelian:,.2f}")
    total_bayar = float(input("Masukkan total harga yang dibayar oleh pelanggan: "))
    # Menghitung kembalian
    kembalian = total_bayar - total_pembelian

    print("============================================")
    print("============= Struk Pembelian ==============")
    for item, harga, jumlah in pesanan:
        print(f"{item:15} x {jumlah} \t: Rp {harga:8,.2f}")
    print("============================================")
    print(f"Total Pembelian \t: Rp {total_pembelian:,.2f}")
    print(f"Total Bayar     \t: Rp {total_bayar:,.2f}")
    print(f"Kembalian       \t: Rp {kembalian:,.2f}")
    print("--------------------------------------------")


def review_order():
    global total_pembelian, pesanan 

    print("--------------------------------------------")
    print("Pesanan:")
    for item, harga, jumlah in pesanan:  # Menyertakan juga nilai jumlah dari setiap pesanan
        print(f"| {item:15} x {jumlah} \t: Rp {harga:8,.2f}")
    print("--------------------------------------------")
    print(f"| Total Pembelian \t: Rp {total_pembelian:,.2f}")

def main():
    system('cls')
    print('='*35)
    print('      WARUNG MAKAN IBU MIRNA      ')
    print('='*35)
    menu()

    global total_pembelian, pesanan 
    total_pembelian = 0
    pesanan = []

    while True:
        print("\nPilih Menu:")
        print("1. Pesan")
        print("2. Cetak Struk")
        print("3. Lihat Pesanan")


        pilihan = int(input("Masukkan pilihan (1/2/3): "))

        if pilihan == 1:
            item, harga, jumlah = pesan_menu()
            total_pembelian += harga
            pesanan.append((item, harga, jumlah))
            jumlah = 1  # Reset jumlah setelah menambahkan pesanan
        elif pilihan == 2:
            finish()
            break
        elif pilihan == 3:
            review_order()
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")


if __name__ == "__main__":
    main()
