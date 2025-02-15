import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os
from datetime import datetime

def select_files():
    global selected_folder
    pdf_files = filedialog.askopenfilenames(
        title="Select PDF Files", filetypes=[("PDF files", "*.pdf")]
    )
    
    if pdf_files:
        selected_folder = os.path.dirname(pdf_files[0])
        for pdf in pdf_files:
            listbox.insert(tk.END, pdf)

def move_up():
    try:
        index = listbox.curselection()[0]
        if index > 0:
            item = listbox.get(index)
            listbox.delete(index)
            listbox.insert(index - 1, item)
            listbox.select_set(index - 1)
    except IndexError:
        pass

def move_down():
    try:
        index = listbox.curselection()[0]
        if index < listbox.size() - 1:
            item = listbox.get(index)
            listbox.delete(index)
            listbox.insert(index + 1, item)
            listbox.select_set(index + 1)
    except IndexError:
        pass

def apply_order():
    ordered_files = listbox.get(0, tk.END)
    
    merger = PdfMerger()
    for pdf in ordered_files:
        merger.append(pdf)
    
    if selected_folder:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"merged_output_{current_time}.pdf"
        output_path = os.path.join(selected_folder, output_filename)
        
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Başarılı", f"PDF dosyaları başarıyla birleştirildi ve '{output_path}' olarak kaydedildi.")
    else:
        messagebox.showerror("Hata", "Çıktı dosyasını kaydetmek için geçerli bir klasör seçilmedi.")

#UI
root = tk.Tk()
root.title("PDF Birleştirici")

select_button = tk.Button(root, text="Dosya Seç", command=select_files)
select_button.pack(pady=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=20)
listbox.pack(padx=10, pady=10)

move_up_button = tk.Button(root, text="Yukarı Taşı", command=move_up)
move_up_button.pack(pady=5)
move_down_button = tk.Button(root, text="Aşağı Taşı", command=move_down)
move_down_button.pack(pady=5)

order_button = tk.Button(root, text="Sıralamayı Uygula ve Birleştir", command=apply_order)
order_button.pack(pady=10)

root.mainloop()
