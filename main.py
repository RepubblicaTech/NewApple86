import customtkinter as CTk
import libs.window as window
from OC_Download.main import *

CTk.set_appearance_mode("System")  # Modes: system (default), light, dark
CTk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

mainWindow = window.Window("Apple86 Reborn",
                           '620x150',
                           False,
                           False)

"""
DON'T ADD PARENTHESIS ON COMMAND=function()
    - ilsetronenazionalee
"""

mainWindow.phase1 = CTk.CTkButton(mainWindow,
                                  text='Download OpenCore',
                                  command=Stage1)
mainWindow.phase1.grid(row=0,
                       column=0,
                       padx=20,
                       pady=20)

mainWindow.phase2 = CTk.CTkButton(mainWindow,
                                  text='Download Drivers, Kexts and SSDTs').grid(row=0,
                                                                                 column=1,
                                                                                 padx=20,
                                                                                 pady=20)

mainWindow.phase3 = CTk.CTkButton(mainWindow,
                                  text='Setup config.plist').grid(row=0,
                                                                  column=2)

mainWindow.phase4 = CTk.CTkButton(mainWindow,
                                  text='Advanced configuration').grid(row=1,
                                                                  column=1)

mainWindow.mainloop()
