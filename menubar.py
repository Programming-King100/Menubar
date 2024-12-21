from tkinter import *

root=Tk()
root.title("MenuBar")
root.geometry("400x400")



#create a menubar

menubar=Menu(root)


# adding file menu
file=Menu(menubar,tearoff=0) #1 file option as a part of menubar
menubar.add_cascade(label='file',menu=file)

#adding submenus to File option
file.add_command(label='New Txt File',command=None)
file.add_command(label='bruh',command=None)
file.add_command(label='thats crazy bruh',command=None)
file.add_separator()

Ucheonpoint=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Ucheonpoint',menu=Ucheonpoint)

Ucheonpoint.add_command(label='Npo Zapp',command=None)
Ucheonpoint.add_command(label='Npo 3fm',command=None)











root.config(menu=menubar)
root.mainloop()