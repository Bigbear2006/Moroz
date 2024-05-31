import tkinter as tk
from tkinter import ttk, Button


def create_account():
    print("Account Created")


app = tk.Tk()
app.title("Buat Akun Google Anda")


def create_labeled_entry(frame, text, row, column, show=None, span=1):
    label = tk.Label(frame, text=text)
    label.grid(row=row, column=column, sticky=tk.W, pady=2)
    entry = tk.Entry(frame, show=show)
    entry.grid(row=row, column=column + 1, pady=2, columnspan=span, sticky=(tk.W, tk.E))
    return entry


frame = ttk.Frame(app, padding="20 20 20 20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

first_name_entry = create_labeled_entry(frame, "Nama Depan", 0, 0)
last_name_entry = create_labeled_entry(frame, "Nama Belakang", 0, 2)

username_label = tk.Label(frame, text="Pilih nama pengguna Anda")
username_label.grid(row=1, column=0, sticky=tk.W, pady=2)
username_entry = tk.Entry(frame)
username_entry.grid(row=1, column=1, pady=2, columnspan=3, sticky=(tk.W, tk.E))

email_pref_label = tk.Label(frame, text="Saya lebih suka menggunakan alamat email saya yang sekarang", fg="blue")
email_pref_label.grid(row=2, column=1, pady=2, columnspan=3, sticky=tk.W)

password_entry = create_labeled_entry(frame, "Buat sandi", 3, 0, show="*")
confirm_password_entry = create_labeled_entry(frame, "Konfirmasi sandi Anda", 4, 0, show="*")

dob_label = tk.Label(frame, text="Tanggal lahir")
dob_label.grid(row=5, column=0, sticky=tk.W, pady=2)

dob_year = ttk.Combobox(frame, values=list(map(str, range(1900, 2024))))
dob_year.grid(row=5, column=1, pady=2)

dob_month = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(1, 13)])
dob_month.grid(row=5, column=2, pady=2)

dob_day = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(1, 32)])
dob_day.grid(row=5, column=3, pady=2)

gender_label = tk.Label(frame, text="Gender")
gender_label.grid(row=6, column=0, sticky=tk.W, pady=2)

gender = ttk.Combobox(frame, values=["Saya...", "Pria", "Wanita", "Lainnya"])
gender.grid(row=6, column=1, pady=2, columnspan=3, sticky=(tk.W, tk.E))

phone_label = tk.Label(frame, text="Ponsel")
phone_label.grid(row=7, column=0, sticky=tk.W, pady=2)

phone_code_label = tk.Label(frame, text="+62")
phone_code_label.grid(row=7, column=1, sticky=tk.W, pady=2)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=7, column=2, pady=2, columnspan=2, sticky=(tk.W, tk.E))

current_email_label = tk.Label(frame, text="Alamat email Anda saat ini")
current_email_label.grid(row=8, column=0, sticky=tk.W, pady=2)
current_email_entry = tk.Entry(frame)
current_email_entry.grid(row=8, column=1, pady=2, columnspan=3, sticky=(tk.W, tk.E))

location_label = tk.Label(frame, text="Lokasi")
location_label.grid(row=9, column=0, sticky=tk.W, pady=2)

location = ttk.Combobox(frame, values=["Indonesia"])
location.grid(row=9, column=1, pady=2, columnspan=3, sticky=(tk.W, tk.E))

next_button = Button(frame, text="Langkah berikutnya", command=create_account, bg='blue', fg='white')
next_button.grid(row=10, column=0, columnspan=4, pady=10)

app.mainloop()
