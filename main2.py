from g4f.client import Client
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
























window = Tk() #Создаём окно приложения.
window.title("ALOE")
window.geometry('550x400')

def insert(text):
    words = text.split()  # Разделяем строку на слова
    result = []  # Список для результата

    for i in range(0, len(words), 6):
        result.append(' '.join(words[i:i+6]))  # Объединяем каждые 6 слов

    return '\n'.join(result)  # Объединяем результаты с переводами строки
 


lbl = Label(window, text="Введите запрос вручную\n или оставьте поле пустым для скриншота", font=("Arial Bold", 20))  
lbl.grid(column=0, row=1)

txt = Entry(window,width=80,)  
txt.grid(column=0, row=0)

answer = Label(window, text='')
answer.grid(column=0, row=3)

def clicked():
    from answer import defining_task
    def search_answer(text=defining_task()):
        client = Client()
        response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": f"{text}. Дай только четкий ответ, либо ответ из предложенных вариантов, если не знаешь пиши незнаю. После ответа писать ничего не нужно. и переноси строки"}],)
        return (response.choices[0].message.content)
    if txt.get() == '':
        answer.configure(text=insert(search_answer()))
    else:
        answer.configure(text=insert(search_answer(txt.get())))

btn = Button(window, text="Начать поиск", bg="green", fg="white", command=clicked)
btn.grid(column=0, row=2) 


window.mainloop()
