import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import random

# Funkcja generująca losowy kolor w formacie HEX
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Funkcja generująca kod QR
def generate_qr():
    global qr_img
    input_text = entry.get()
    if input_text:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_text)
        qr.make(fit=True)

        # Generowanie losowych kolorów
        fill_color = random_color()
        back_color = random_color()

        qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img = qr_img.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)

        qr_label.config(image=img)
        qr_label.image = img
    else:
        messagebox.showwarning("Brak danych", "Proszę wprowadzić tekst.")

# Funkcja zapisująca kod QR do pliku
def save_qr():
    if qr_img:
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if filepath:
            qr_img.save(filepath)
            messagebox.showinfo("Zapisano", f"Zapisano kod QR do pliku: {filepath}")
    else:
        messagebox.showwarning("Brak kodu QR", "Proszę najpierw wygenerować kod QR.")

# Główne okno aplikacji
root = tk.Tk()
root.title("Generator Kodów QR")

qr_img = None

# Etykieta i pole tekstowe
label = tk.Label(root, text="Wprowadź tekst:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Przycisk generowania kodu QR
generate_button = tk.Button(root, text="Generuj Kod QR", command=generate_qr)
generate_button.pack(pady=10)

# Przycisk zapisu kodu QR
save_button = tk.Button(root, text="Zapisz Kod QR", command=save_qr)
save_button.pack(pady=10)

# Etykieta do wyświetlania kodu QR
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Uruchomienie pętli głównej
root.mainloop()
