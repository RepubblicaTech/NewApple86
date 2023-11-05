import customtkinter as CTk


class Window(CTk.CTk):
    def __init__(self, title="CustomTkinter", size='400x300', resizableX=True, resizableY=True):
        super().__init__()
        self.title(title)
        self.geometry(str(size))
        self.resizable(resizableX, resizableY)
