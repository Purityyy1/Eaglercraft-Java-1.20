from tkinter import *
from time import sleep


root = Tk()
root.title('Eaglercraft 1.20')
root.geometry('800x600')

def do_eagtek_screen():
    eagtek_photo = PhotoImage(file='assets/start-screen/eagtek.png')
    eagtek_label = Label(image=eagtek_photo)
    eagtek_label.pack()

    root.update()
    root.after(2000)
    eagtek_label.destroy()


do_eagtek_screen()

enable_photo = PhotoImage(file='assets/start-screen/enable.png')
enable_label = Label(image=enable_photo)
enable_label.pack()







root.mainloop()
