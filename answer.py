import pytesseract
from PIL import ImageGrab
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from definingtask import process_image

def defining_task(name_img="0.png"):
    ImageGrab.grab().save(name_img)
    cord_mis = process_image(name_img)
    os.remove(name_img)
    screenshot = ImageGrab.grab(bbox=cord_mis)
    screenshot = screenshot.convert('L')
    text = pytesseract.image_to_string(screenshot, lang='rus')
    return text





