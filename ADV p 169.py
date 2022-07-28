# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:08:43 2022

@author: ankit computer
"""

from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("900x600")
root.title("Using classes to create elements")

class CreateElements:
    def _int_(self):
        print("This is the CreateElements class")
    def createNewElements(self):
        chosen = dropdown.get()
        if(chose=="label"):
            
            label = Label(root,text="This label is created by class",fg="red")
            label.pack()
        elif(chose=="button"):
            
            
           btn = Button(root,text="button",command = self.message)
           btn.pack(padx=20,pady=10)
        elif(chose=="dropdown box"):
            box = ttk.Combobox(root,status="readonly",value=['1','2'])
    def message(self):
        messagebox.showinfo("showinfo","This button was created by class")
        
obj_of_createElements = CreateElements()
dropdown = ttk.Combobox(root,status="readonly",value=["label","button",'dropdown box'])
dropdown.pack()
btn = Button(root,text="Click to create element",command=obj_of_createElements.createNewElements)
btn.pack(padx=20,pady=10)

root.mainloop()
    