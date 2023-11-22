import libs.window as window


def Stage1():
    print("log")
    downloadWindow = window.Window("OpencoreDL",
                                   '600x400',
                                   False,
                                   False)

    downloadWindow.mainloop()

def Pomza(string):
    print(str(string))
    