from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def convert(input_path):
    img = Image.open(input_path)
    output_path = os.path.splitext(input_path)[0] + '.webp'
    img.save(output_path, 'WEBP', quality=slider.get())
    messagebox.showinfo("Успех", "Конвертация выполнена успешно!")

def start_convert():
    for i in file_list:
        convert(i)
    print("Конвертация файлов...")
    print("Выбранное значение качества:", slider.get())
    print("Загруженные файлы:", file_list)

def upload_files():
    global file_list
    files = filedialog.askopenfilenames(title="Выберите файлы")
    file_list.extend(files)
    files_display.config(state=tk.NORMAL)
    files_display.delete(1.0, tk.END)  # Очищаем текстовое поле
    files_display.insert(tk.END, '\n'.join(file_list))  # Добавляем новые файлы
    files_display.config(state=tk.DISABLED)

# Основное окно
root = tk.Tk()
root.title("Конвертер webp")
root.geometry('400x400')
root.minsize(400, 400)

# Слайдер
slider = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, label="Выберите качество", length=200)
slider.pack(pady=10)

# Кнопка загрузки файлов
upload_button = tk.Button(root, text="Загрузить файлы", command=upload_files)
upload_button.pack(pady=10)

# Текстовое поле для отображения загруженных файлов
files_display = tk.Text(root, height=10, width=50, state=tk.DISABLED)
files_display.pack(pady=10)

# Список загруженных файлов
file_list = []

# Кнопка конвертации
convert_button = tk.Button(root, text="Конвертировать", command=start_convert)
convert_button.pack(pady=10)

# Запуск основного цикла
root.mainloop()