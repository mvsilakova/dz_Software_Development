import math
import tkinter as tk
from tkinter import messagebox

def calculate_value():
    try:
        x = float(entry.get())
        if x < 3:
            y = x * math.cos(x**3) + x
        else:
            y = math.sqrt(x) * math.cos(0.0421 * x**2)
        result_label.config(text="Результат: " + str(y))
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный Ввод. Введите числовое значение.")

# Силакова Мария Вячеславовна, варинант 21, группа 44-22-114 
window = tk.Tk()
window.title("Расчет")
window.geometry("300x150")

input_label = tk.Label(window, text="Введите числовое значение:")
input_label.pack()
entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(window, text="Рассчитать", command=calculate_value)
calculate_button.pack()

result_label = tk.Label(window, text="Результат:")
result_label.pack()


window.mainloop()