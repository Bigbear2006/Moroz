# Вводится количество секунд с начала дня. Рассчитать количество полных минут с начал дня
import tkinter as tk
from tkinter import ttk


def calculate_minutes():
    try:
        seconds = int(entry_seconds.get())
        minutes = seconds // 60
        result_label.config(text=f"Количество полных минут: {minutes}")
    except ValueError:
        result_label.config(text="Введите корректное число секунд.")


app = tk.Tk()
app.title("Рассчитать полные минуты")

frame = ttk.Frame(app, padding="10 10 10 10")
frame.grid(row=0, column=0)

label_seconds = tk.Label(frame, text="Введите количество секунд:")
label_seconds.grid(row=0, column=0, sticky=tk.W, pady=2)
entry_seconds = tk.Entry(frame)
entry_seconds.grid(row=0, column=1, pady=2)

calculate_button = ttk.Button(frame, text="Рассчитать", command=calculate_minutes)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=2)

app.mainloop()
