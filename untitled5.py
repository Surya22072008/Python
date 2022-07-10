

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root=Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.configure(background="ligtblue")

label = Label(root,bg="skyblue",highlightthickness=5)
label.place(rely=0.2,rely=0.1,anchor=CENTER)
img_path= filedialog.askopenfilename(title="Open text file",filetypes=[("Image files","*.jpg;*.gif;*.jpg;;*.png;*txt" )])
def OpenImage():
    
