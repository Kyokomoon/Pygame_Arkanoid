from tkinter import *
from Arkanoid_lvl1 import lel
def g_d():
    root = Tk()
    root.geometry('200x200')
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    def start():
        root.destroy()
        import Gui
    def out():
        exit()
    def start_lvl1():
        root.destroy()
        lel()
    def start_lvl2():
        root.destroy()
        import Arkanoid_lvl2
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Начать заного ",command=start_lvl1)
    filemenu.add_command(label="Выход",command=out)
    mainmenu.add_cascade(label="игра", menu=filemenu)
    root.title("PlatformShelter")
    l1 = Label(text="YOU DIED!", font=('Arial', 26,), fg='#ff0000')
    l1.config(bd=100, bg='#000000')

    l1.pack()
    root.mainloop()
