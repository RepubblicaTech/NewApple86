import customtkinter as CTk
import libs.window as window

def log(text="Hello"):
    print(text)

CTk.set_appearance_mode("System")  # Modes: system (default), light, dark
CTk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

mainWindow = window.Window("Apple86 Reborn",
                           '600x300',
                           False,
                           False)

mainWindow.button = CTk.CTkButton(mainWindow,
                                  text='OMOa',
                                  command=lambda: log('Button was clicked')).grid(padx=20,
                                                                                  pady=20)

mainWindow.mainloop()
