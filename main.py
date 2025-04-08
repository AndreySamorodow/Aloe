import customtkinter as CTk

from PIL import Image

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("ALOE")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("img.png"), size=(460, 150))
        

if __name__ == "__main__":
    app = App()
    app.mainloop()