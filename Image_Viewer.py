from tkinter import *
from PIL import Image, ImageTk

import os

root = Tk()
root.geometry("600x600")


def resize_image(root, copy_of_image, Label1):
    new_height = 600
    new_width = 600
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo


def next():
    global n
    global items_list
    n = n+1
    img1 = items_list[n]
    print(img1)

    image = Image.open('./PicsForImageViewer/' + img1)

    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.bind('<configure>', resize_image(root, copy_of_image, label1))
    label.pack()


n = 0

items_list = os.listdir('PicsForImageViewer')
img1 = items_list[n]

#


image = Image.open('./PicsForImageViewer/' + img1)

copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)

label1 = Label(root, image=photo)
label1.bind('<configure>', resize_image(root, copy_of_image, label1))
label1.pack()


b1 = Button(root, text=">>", width=6, height=12, command=next)
b1.place(x=570, y=150)

root.mainloop()
