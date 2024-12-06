print('Lesson 11: AI model. Threat image')

# cmd command for install the next libraries:
#   pip install opencv-python
#   pip install pillow

import cv2
from PIL import Image

image_cat_path = 'CAT.jpeg'
image_sunglasses_path = 'sun_glasses.jpg'  # Убедитесь, что этот файл существует
image_cat = cv2.imread(image_cat_path)

# Проверка, что изображение кота загружено
if image_cat is None:
    print(f"Ошибка: не удалось загрузить изображение {image_cat_path}")
    exit()

cat_face_handler = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

# Получение координат лица кота
cat_face_coordinates = cat_face_handler.detectMultiScale(image_cat)

# Проверка, найдено ли лицо кота
if len(cat_face_coordinates) == 0:
    print("Ошибка: лицо кота не найдено.")
    exit()

# Рисуем прямоугольник вокруг лица кота
for (x, y, w, h) in cat_face_coordinates:
    cv2.rectangle(image_cat, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imshow('Bob cat', image_cat)

# Подготовка изображения для объединения
cat = Image.open(image_cat_path)
sun_glasses = Image.open(image_sunglasses_path)

cat = cat.convert('RGB')
sun_glasses = sun_glasses.convert('RGB')

(x, y, w, h) = cat_face_coordinates[0]
sun_glasses = sun_glasses.resize((w, int(h / 3)))

# Объединение двух изображений
cat.paste(sun_glasses, (x, int(y + h / 4)))
cat.save('cat_with_sunglasses.jpeg')

# Сохранение и чтение нового изображения после обработки
cat_with_sunglasses = cv2.imread('cat_with_sunglasses.jpeg')

# Проверка, что новое изображение загружено
if cat_with_sunglasses is None:
    print("Ошибка: не удалось загрузить изображение cat_with_sunglasses.jpeg")
    exit()

cv2.imshow('Bob cat with sunglasses', cat_with_sunglasses)

cv2.waitKey(0)
cv2.destroyAllWindows()