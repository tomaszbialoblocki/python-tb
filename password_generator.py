import tkinter as tk
from tkinter import ttk
import random
import string

# Funkcja do generowania hasła:
def generate_password():
    length = int(length_var.get())
    use_special = special_var.get()
    use_lower_upper = lower_upper_var.get()
    use_digits = digits_var.get()

    characters = ""
    if use_special:
        characters += string.punctuation
    if use_lower_upper:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits

    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    else:
        password_var.set("Wybierz przynajmniej jedną opcję znaków.")

# Tworzenie głównego okna aplikacji:
root = tk.Tk()
root.title("GENERATOR HASEŁ")

# Zmienna do przechowywania długości hasła:
length_var = tk.StringVar(value="8")

# Zmienna do przechowywania opcji:
special_var = tk.BooleanVar()
lower_upper_var = tk.BooleanVar()
digits_var = tk.BooleanVar()

# Zmienna do przechowywania wygenerowanego hasła:
password_var = tk.StringVar()

# Etykieta i pole tekstowe dla długości hasła:
length_label = ttk.Label(root, text="Długość hasła:")
length_label.pack(pady=5)

length_entry = ttk.Entry(root, textvariable=length_var, width=5)
length_entry.pack(pady=5)

# Opcje dla znaków specjalnych, małych i wielkich liter oraz cyfr:
special_check = ttk.Checkbutton(root, text="Użycie znaków specjalnych", variable=special_var)
special_check.pack(pady=5)

lower_upper_check = ttk.Checkbutton(root, text="Użycie małych i wielkich znaków", variable=lower_upper_var)
lower_upper_check.pack(pady=5)

digits_check = ttk.Checkbutton(root, text="Użycie cyfr", variable=digits_var)
digits_check.pack(pady=5)

# Przycisk do generowania hasła:
generate_button = ttk.Button(root, text="Generuj hasło", command=generate_password)
generate_button.pack(pady=5)

# Pole tekstowe do wyświetlania wygenerowanego hasła:
password_label = ttk.Label(root, text="Wygenerowane hasło:")
password_label.pack(pady=5)

password_entry = ttk.Entry(root, textvariable=password_var, width=50, state='readonly')
password_entry.pack(pady=5)

# Uruchomienie głównej pętli aplikacji:
root.mainloop()
