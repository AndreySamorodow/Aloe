from ultralytics import YOLO
import cv2
import numpy as np

import pytesseract
from PIL import ImageGrab
import os

# Загрузка модели YOLOv8
model = YOLO('Apps/best.pt')

# Функция для обработки изображения
def process_image(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)
    results = model(image)[0]
    
    # Получение координат
    boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)

    # Подготовка списка для хранения координат
    crd = []

    # Сбор координат
    for box in boxes:
        x1, y1, x2, y2 = box
        crd.append((x1, y1, x2, y2))

    # Возвращаем координаты как последовательный список
    return [coords for box in crd for coords in box]

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def defining_task(name_img="0.png"):
    ImageGrab.grab().save(name_img)
    cord_mis = process_image(name_img)
    os.remove(name_img)
    screenshot = ImageGrab.grab(bbox=cord_mis)
    screenshot = screenshot.convert('L')
    text = pytesseract.image_to_string(screenshot, lang='rus')
    return text
