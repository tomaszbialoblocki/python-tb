import tkinter as tk
from tkinter import ttk

#rot13
def rot13(text):
    return text.translate(str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))

#aktualizacja tekstu live
def update_text(*args):
    input_text = input_var.get()
    encrypted_text = rot13(input_text)
    output_var.set(encrypted_text)

#okno apki
root = tk.Tk()
root.title("SZYFRATOR ROT13")

#tekst_input
input_var = tk.StringVar()
input_var.trace("w", update_text)

#tekst_encrypted
output_var = tk.StringVar()

#pole i etykieta dla tekst_output
input_label = ttk.Label(root, text="WPISZ TEKST:")
input_label.pack(pady=5)

input_entry = ttk.Entry(root, textvariable=input_var, width=50)
input_entry.pack(pady=5)

#pole i etykieta dla tekst_encrypted
output_label = ttk.Label(root, text="ZASZYFROWANY:")
output_label.pack(pady=5)

output_entry = ttk.Entry(root, textvariable=output_var, width=50, state='readonly')
output_entry.pack(pady=5)

#main_loop
root.mainloop()
