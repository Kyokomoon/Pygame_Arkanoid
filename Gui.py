from tkinter import *
from Arkanoid_lvl1 import lel
root = Tk()
root.geometry('200x200')
mainmenu = Menu(root)
root.config(menu=mainmenu)
def start(event):
    root.destroy()
    lel()
def out(event):
    exit()
def start_lvl1():
    root.destroy()
    lel()
def start_lvl2():
    root.destroy()
    import Arkanoid_lvl2
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Уровень 1",command=start_lvl1)
filemenu.add_command(label="Уровень 2",command=start_lvl2)
mainmenu.add_cascade(label="Уровень", menu=filemenu)
root.title("PlatformShelter")
b1 = Button(text='Старт', width= 15, height=5)
b2 = Button(text='Выход', width= 15, height=2)
l1 = Label(text="PlatformShelter", font="Arial 20")
l1.config(bd=20, bg='#ffaaaa')

b1.bind('<Button-1>', start)
b2.bind('<Button-1>', out)
b1.pack()
b2.pack()
l1.pack()
root.mainloop()
