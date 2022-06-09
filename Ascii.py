# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:04:52 2022

@author: ankit computer
"""

from tkinter import *
root = Tk()
root.title("ASCII")
root.geometry("400x400")
root.configure(background = "snow")
enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
label = Label(root,text="Name in Ascii : ",bg="light yellow",fg="black")
label2 = Label(root,text="Encrypted code : ",bg="light yellow",fg="black")
def asciiconv():
    input_word = enter_word.get()
    
    label["text"] = ""
    label2["text"] = ""
    
    for letter in input_word:
        letter2= int(ord(letter)) + 1
        label["text"] += str(ord(letter)) + " "
        label2["text"] += str(chr(letter2))


btn = Button(root,text="Show Ascii code and encrypted value" , command=asciiconv,bg="gold",  fg="black" )
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
