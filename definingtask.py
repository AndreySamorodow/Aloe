from ultralytics import YOLO
import cv2
import numpy as np

# Загрузка модели YOLOv8
model = YOLO('Aloe/best.pt')

# Функция для обработки изображения
def process_image(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)
    results = model(image)[0]
    
    # Получение классов и координат
    classes_names = results.names
    boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)

    # Подготовка списка для хранения координат
    crd = []

    # Сбор координат
    for box in boxes:
        x1, y1, x2, y2 = box
        crd.append((x1, y1, x2, y2))

    # Возвращаем координаты как последовательный список
    return [coords for box in crd for coords in box]
