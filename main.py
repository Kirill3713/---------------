# Импортируем модуль
from PIL import Image, ImageDraw, ImageFont
# pip install pillow - скачивание библиотеки
# Приветствие
print("Программа запущена.")
print("Добро пожаловать в генератор мемов!")
# Принимаем текст
try:
    text_type = int(input("Сколько будет текстов на картинке: 1 или 2? "))
except ValueError:
    print("Введено некорректное значение!")
    quit()
if text_type == 1:
    bottom_text = input("Введите нижний текст: ")
    top_text = ""
elif text_type == 2:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print("Введено неправильное значение.")
    quit()
# Список картинок
images = ["Кот в очках.png", "Кот в ресторане.png"]
print("Доступные картинки:")
a = 1
for i in images:
    print(f"{a}. {i}")
    a += 1
try:
    number_of_image  = int(input("Введите номер нужной картинки: "))
except ValueError:
    print("Введено некорректное значение!")
    quit()
# Открываем картинку.
image = Image.open(images[number_of_image - 1])
width, height = image.size
print("Размер картинок: ", width, height)
# Печатаем текст на картинке
draw = ImageDraw.Draw(image)
my_font = ImageFont.truetype("arial.ttf", size = 70)
draw.text(xy=(width / 2, 60),
          text = top_text, 
          font = my_font, 
          fill = "black", 
          anchor = "mt")

draw.text(xy=(width / 2, height - 60),
          text = bottom_text, 
          font = my_font, 
          fill = "black", 
          anchor = "mb")
# Сохраняем результат
image.save("new_image.png")
print("Картинка сохранена!")