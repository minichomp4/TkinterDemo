import PIL
import tkinter
from tkinter import *
from PIL import Image, ImageTk

# general setup
startUp = tkinter.Tk()
startUp.geometry("1280x960")
startUp.title("Startup Page")

# adding main background
bgImage = Image.open("StartUpPage1.jpg")
render = ImageTk.PhotoImage(bgImage)
img = Label(startUp, image = render)
img.place(x=0, y=0)


# adding buttons
# button4=tkinter.Button(startUp, text="BOTTOM")
# button4.pack(side=tkinter.BOTTOM)
# button3=tkinter.Button(startUp, text="BOTTOM1")
# button3.pack(side=tkinter.BOTTOM)

startUp.mainloop()
