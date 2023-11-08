from tkinter import *
from tkinter import filedialog
from tkinter import font

editor = Tk()
editor.title('File Editor')
#editor.iconbitmap()
editor.geometry('1200x660')

# makes frame
frame = Frame()
frame.pack(pady=5)

# Create scroll bar
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

# make menu
menu = Menu(editor)
editor.config(Menu=menu)

# add file menu
#TODO https://www.youtube.com/watch?v=UlQRXJWUNBA 5:40
fileMenu = Menu(menu)

# Makes text box
text = Text(frame, width=97, height=25, font=('Times New Roman', 20),
            selectbackground='blue', selectforeground='black', undo=True,
            yscrollcommand=text_scroll.set)
text.pack()

# Configure scroll bar
text_scroll.config(command=text.yview)

editor.mainloop()