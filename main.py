import tkinter as tk
from screens.LoginScreen import LoginScreen

class App(tk.Tk):

    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.initScreen()

    def initScreen(self):
        LoginScreen(self)


if __name__ == '__main__':
    app = App("RPi IoT", "600x600")
    app.mainloop()

