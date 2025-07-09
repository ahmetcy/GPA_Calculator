import tkinter as tk
from tkinter import messagebox

class Ders:
    def __init__(self, ders_adi, alinan_not, kredi):
        self.ders_adi = ders_adi
        self.alinan_not = alinan_not.upper()  
        self.kredi = float(kredi)
        self.sayi_not = self.harf_notunu_sayiya_cevir()

    def harf_notunu_sayiya_cevir(self):
        if self.alinan_not == "AA":
            return 4
        elif self.alinan_not == "BA":
            return 3.5
        elif self.alinan_not == "BB":
            return 3
        elif self.alinan_not == "CB":
            return 2.5
        elif self.alinan_not == "CC":
            return 2
        else:
            return 0  

class GPA_Hesaplama_Uygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Hesaplama Uygulaması")
        self.root.geometry("400x500")  
        self.root.configure(bg='light cyan') 

        self.dersler = []
        self.selected_index = None 

        self.ders_bilgileri_label = tk.Label(root, text="Ders bilgilerini giriniz:", bg='light cyan')
        self.ders_bilgileri_label.pack()

        self.ders_adi_label = tk.Label(root, text="Ders Adı:", bg='light cyan')
        self.ders_adi_label.pack()

        self.ders_adi_entry = tk.Entry(root)
        self.ders_adi_entry.pack()

        self.alinan_not_label = tk.Label(root, text="Alınan Not:", bg='light cyan')
        self.alinan_not_label.pack()

        self.alinan_not_entry = tk.Entry(root)
        self.alinan_not_entry.pack()

        self.kredi_label = tk.Label(root, text="Kredi:", bg='light cyan')
        self.kredi_label.pack()

        self.kredi_entry = tk.Entry(root)
        self.kredi_entry.pack()

        self.ders_ekle_button = tk.Button(root, text="Ders Ekle", command=self.ders_ekle)
        self.ders_ekle_button.pack()

        self.dersler_listbox = tk.Listbox(root)
        self.dersler_listbox.pack()
        self.dersler_listbox.bind('<<ListboxSelect>>', self.ders_sec) 

        self.ders_guncelle_button = tk.Button(root, text="Dersi Güncelle", command=self.ders_guncelle)
        self.ders_guncelle_button.pack()

        self.hesapla_button = tk.Button(root, text="GPA Hesapla", command=self.gpa_hesapla)
        self.hesapla_button.pack()

        self.sonuc_label = tk.Label(root, text="", bg='light cyan')
        self.sonuc_label.pack()

    def ders_ekle(self):
        ders_adi = self.ders_adi_entry.get()
        alinan_not = self.alinan_not_entry.get()
        kredi = self.kredi_entry.get()

        if ders_adi and alinan_not and kredi:
            yeni_ders = Ders(ders_adi, alinan_not, kredi)
            self.dersler.append(yeni_ders)

            self.dersler_listbox.insert(tk.END, f"{ders_adi} - {alinan_not} - {kredi}")

            self.ders_adi_entry.delete(0, tk.END)
            self.alinan_not_entry.delete(0, tk.END)
            self.kredi_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Uyarı", "Lütfen tüm bilgileri doldurun.")

    def ders_sec(self, event):
        if self.dersler_listbox.curselection():
            self.selected_index = self.dersler_listbox.curselection()[0]
            selected_ders = self.dersler[self.selected_index]

            self.ders_adi_entry.delete(0, tk.END)
            self.ders_adi_entry.insert(tk.END, selected_ders.ders_adi)

            self.alinan_not_entry.delete(0, tk.END)
            self.alinan_not_entry.insert(tk.END, selected_ders.alinan_not)

            self.kredi_entry.delete(0, tk.END)
            self.kredi_entry.insert(tk.END, selected_ders.kredi)

    def ders_guncelle(self):
        if self.selected_index is not None:
            ders_adi = self.ders_adi_entry.get()
            alinan_not = self.alinan_not_entry.get()
            kredi = self.kredi_entry.get()

            if ders_adi and alinan_not and kredi:
                guncel_ders = Ders(ders_adi, alinan_not, kredi)
                self.dersler[self.selected_index] = guncel_ders

                self.dersler_listbox.delete(self.selected_index)
                self.dersler_listbox.insert(self.selected_index, f"{ders_adi} - {alinan_not} - {kredi}")

                self.ders_adi_entry.delete(0, tk.END)
                self.alinan_not_entry.delete(0, tk.END)
                self.kredi_entry.delete(0, tk.END)

                self.selected_index = None
            else:
                messagebox.showwarning("Uyarı", "Lütfen tüm bilgileri doldurun.")
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir dersi seçin.")

    def gpa_hesapla(self):
        toplam_not = 0
        toplam_kredi = 0

        for ders in self.dersler:
            toplam_not += ders.sayi_not * ders.kredi
            toplam_kredi += ders.kredi

        gpa = toplam_not / toplam_kredi if toplam_kredi != 0 else 0
        self.sonuc_label.config(text=f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = GPA_Hesaplama_Uygulamasi(root)
    root.mainloop()
