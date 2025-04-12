import flet as ft
from g4f.client import Client

def main(page: ft.Page):
    page.title = "ALOE"
    page.window.icon = "Materials/icon.png"
    page.theme_mode = "dark"
    page.window.width = 600
    page.window.height = 1000
    page.window.min_width = 600
    page.window.min_height = 500
    page.window.always_on_top = True

    def insert(text):
        words = text.split()  # Разделяем строку на слова
        result = []  # Список для результата
        for i in range(0, len(words), 12):
            result.append(' '.join(words[i:i+12]))  # Объединяем каждые 6 слов
        return '\n'.join(result)  # Объединяем результаты с переводами строки

    def search_answer(text="defining_task()"):
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"{text}. Дай только четкий ответ, либо ответ из предложенных вариантов, если не знаешь пиши незнаю. После ответа писать ничего не нужно."}],
        )
        return response.choices[0].message.content

    def event(e):
        from Apps.answer import defining_task
        answer_text = insert(search_answer(defining_task()))
        text_widget.value = answer_text
        page.update()

    text_widget = ft.Text("", text_align=ft.TextAlign.CENTER)

    page.add(
        ft.Row([ft.Image(src="Materials/img.png")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Image(src="Materials/img2.png")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                ft.ElevatedButton(
                    adaptive=True,
                    content=ft.Text("НАЧАТЬ", color=ft.Colors.WHITE),
                    bgcolor=ft.CupertinoColors.ACTIVE_GREEN,
                    on_click=event 
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [text_widget],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
