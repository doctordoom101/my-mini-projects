import tkinter as tk
from tkinter import simpledialog

class MenuApp:
    def __init__(self, master):
        self.master = master
        master.title("Warung Makan Ibu Mirna")

        self.total_pembelian = 0
        self.pesanan = []

        self.menu_label = tk.Label(master, text="Menu Makanan & Minuman")
        self.menu_label.pack()

        self.menu_listbox = tk.Listbox(master, height=10, width=50)
        self.menu_listbox.pack()

        self.show_menu()

        self.pesan_button = tk.Button(master, text="Pesan", command=self.pesan_menu)
        self.pesan_button.pack()

        self.review_button = tk.Button(master, text="Lihat Pesanan", command=self.review_order)
        self.review_button.pack()

        self.finish_button = tk.Button(master, text="Cetak Struk", command=self.finish)
        self.finish_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def show_menu(self):
        menu_items = [
            "Es Teh Manis\t - Rp 4000",
            "Es Teh Tawar\t - Rp 3000",
            "Air Mineral\t - Rp 2000",
            "Ayam Bakar\t - Rp 12000",
            "Ayam Goreng\t - Rp 12000",
            "Nasi Goreng\t - Rp 10000",
            "Mie Ayam\t - Rp 10000"
        ]
        for item in menu_items:
            self.menu_listbox.insert(tk.END, item)

    def pesan_menu(self):
        selected_index = self.menu_listbox.curselection()
        if selected_index:
            item = self.menu_listbox.get(selected_index)
            jumlah = simpledialog.askinteger("Pesan", f"Berapa banyak {item.split('-')[0]} yang ingin Anda pesan:")
            if jumlah is not None and jumlah > 0:
                harga = float(item.split('Rp')[1].replace(',', '').strip()) * jumlah
                self.total_pembelian += harga
                self.pesanan.append((item.split('-')[0].strip(), harga, jumlah))
                self.result_label.config(text="Pesanan ditambahkan.")
            else:
                self.result_label.config(text="Jumlah tidak valid.")
        else:
            self.result_label.config(text="Pilih item terlebih dahulu.")

    def format_price(self, harga):
        return "{:,.2f}".format(harga).replace(",", ".")

    def finish(self):
        if self.total_pembelian > 0:
            total_bayar = simpledialog.askfloat("Cetak Struk", "Masukkan total harga yang dibayar oleh pelanggan:")
            if total_bayar is not None:
                kembalian = total_bayar - self.total_pembelian
                struk = f"{'='*35}\n"
                struk += "============= Struk Pembelian ==============\n"
                for item, harga, jumlah in self.pesanan:
                    struk += f"{item:15} x {jumlah} \t: Rp {self.format_price(harga)}\n"
                struk += "="*45 + "\n"
                struk += f"Total Pembelian \t: Rp {self.format_price(self.total_pembelian)}\n"
                struk += f"Total Bayar     \t: Rp {self.format_price(total_bayar)}\n"
                struk += f"Kembalian       \t: Rp {self.format_price(kembalian)}\n"
                struk += "-"*45
                self.result_label.config(text=struk)
            else:
                self.result_label.config(text="Total bayar tidak valid.")
        else:
            self.result_label.config(text="Belum ada pesanan.")

    def review_order(self):
        if self.total_pembelian > 0:
            pesanan_text = "Pesanan:\n"
            for item, harga, jumlah in self.pesanan:
                pesanan_text += f"{item:15} x {jumlah} \t: Rp {self.format_price(harga)}\n"
            pesanan_text += "-"*45 + "\n"
            pesanan_text += f"Total Pembelian \t: Rp {self.format_price(self.total_pembelian)}"
            self.result_label.config(text=pesanan_text)
        else:
            self.result_label.config(text="Belum ada pesanan.")

def main():
    root = tk.Tk()
    app = MenuApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
