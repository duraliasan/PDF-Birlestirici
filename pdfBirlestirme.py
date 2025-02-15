import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os
from datetime import datetime

# Dosya seçme fonksiyonu
def select_files():
    global selected_folder  # Klasör yolunu global değişken olarak tanımlıyoruz
    pdf_files = filedialog.askopenfilenames(
        title="PDF Dosyalarını Seçin", filetypes=[("PDF files", "*.pdf")]
    )
    
    if pdf_files:
        # Seçilen ilk dosyanın bulunduğu klasörü alıyoruz
        selected_folder = os.path.dirname(pdf_files[0])
        for pdf in pdf_files:
            listbox.insert(tk.END, pdf)  # Dosyayı listbox'a ekle

# Yukarı taşıma fonksiyonu
def move_up():
    try:
        # Seçilen öğeyi bul
        index = listbox.curselection()[0]
        if index > 0:
            # Seçilen öğeyi yukarı taşı
            item = listbox.get(index)
            listbox.delete(index)
            listbox.insert(index - 1, item)
            listbox.select_set(index - 1)  # Yeni öğeyi seçili yap
    except IndexError:
        pass  # Hiçbir öğe seçilmemişse hata vermez

# Aşağı taşıma fonksiyonu
def move_down():
    try:
        # Seçilen öğeyi bul
        index = listbox.curselection()[0]
        if index < listbox.size() - 1:
            # Seçilen öğeyi aşağı taşı
            item = listbox.get(index)
            listbox.delete(index)
            listbox.insert(index + 1, item)
            listbox.select_set(index + 1)  # Yeni öğeyi seçili yap
    except IndexError:
        pass  # Hiçbir öğe seçilmemişse hata vermez

# Sıralamayı uygulama fonksiyonu
def apply_order():
    # Listeyi al
    ordered_files = listbox.get(0, tk.END)
    
    # PdfMerger ile dosyaları birleştirme
    merger = PdfMerger()
    for pdf in ordered_files:
        merger.append(pdf)
    
    # Çıktıyı seçilen klasöre kaydetme
    if selected_folder:
        # Geçerli tarihi al
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"merged_output_{current_time}.pdf"
        output_path = os.path.join(selected_folder, output_filename)
        
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Başarılı", f"PDF dosyaları başarıyla birleştirildi ve '{output_path}' olarak kaydedildi.")
    else:
        messagebox.showerror("Hata", "Çıktı dosyasını kaydetmek için geçerli bir klasör seçilmedi.")

# Tkinter penceresini başlat
root = tk.Tk()
root.title("PDF Birleştirici")

# Dosya seçme butonu
select_button = tk.Button(root, text="Dosya Seç", command=select_files)
select_button.pack(pady=10)

# Listbox ile dosyaları gösterecek alan
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=20)
listbox.pack(padx=10, pady=10)

# Yukarı ve Aşağı taşıma butonları
move_up_button = tk.Button(root, text="Yukarı Taşı", command=move_up)
move_up_button.pack(pady=5)
move_down_button = tk.Button(root, text="Aşağı Taşı", command=move_down)
move_down_button.pack(pady=5)

# Sıralama butonu
order_button = tk.Button(root, text="Sıralamayı Uygula ve Birleştir", command=apply_order)
order_button.pack(pady=10)

# Pencereyi çalıştır
root.mainloop()
