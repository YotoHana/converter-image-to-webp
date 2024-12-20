import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PIL import Image

global img_list

def openFileDialog():
    options = QFileDialog.Options()
    files, _ = QFileDialog.getOpenFileNames(window, 'Выберите файлы', '', 'All Files (*)', options=options)
    if files:
        file_list.clear()
        total_size = 0
        for file in files:
            img_list.append(file)
            file_list.addItem(file)
            total_size += os.path.getsize(file)
        size_label.setText(f'Общий размер файлов: {total_size / 1024:.2f} KB')

def update_label(value):
    label.setText(str(value))

def startConvert():
    for i in img_list:
        convert(i)

def convert(input_path):
    img = Image.open(input_path)
    output_path = os.path.splitext(input_path)[0] + '.webp'
    img.save(output_path, 'WEBP', quality=slider.value())
    file_list.clear()
    size_label.setText('Конвертирование прошло успешно!')

img_list = []

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Конвертер Webp')

layout = QVBoxLayout()
layout_slider = QHBoxLayout()

slider = QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(80)
slider.setFixedSize(200, 20)
layout_slider.addWidget(slider)

label = QLabel(str(slider.value()))
layout_slider.addWidget(label)
slider.valueChanged.connect(update_label)
layout.addLayout(layout_slider)

file_list = QListWidget()
layout.addWidget(file_list)

size_label = QLabel('Размер файлов будет показан здесь')
layout.addWidget(size_label)

select_button = QPushButton('Выбрать файлы')
select_button.clicked.connect(openFileDialog)
layout.addWidget(select_button)

convert_button = QPushButton('Конвертировать')
convert_button.clicked.connect(startConvert)
layout.addWidget(convert_button)



window.setLayout(layout)
window.resize(400,400)
window.setMaximumSize(1000, 400)
window.setMinimumSize(300, 400)
window.show()
sys.exit(app.exec_())