import PIL
from PIL import ImageEnhance
from PIL import Image

image = Image.open('Без названия.jfif')

"""Регулировка яркости изображения.    

    Этот класс можно использовать для управления яркостью изображения. 
    Коэффициент усиления 0,0 дает черное изображение. Коэффициент 1,0 дает 
    исходное изображение. 
    """
for pic in [0, 0.5, 2]:
    img = ImageEnhance.Brightness(image).enhance(pic)
    img.save(f'test-Brightness-{pic}.jpg')

"""Получение информации об изображении"""

print(f"Width: {img.width}")
print(f"Height: {img.height}")
print(f"Format: {img.format}")
print(f"Mode: {img.mode}")

"""Поворот изображения"""

img2 = img.rotate(90)
img2.save("forest.jpg")
