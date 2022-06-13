# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:45:08 2022

@author: ankit computer
"""

from tkinter import *
root=Tk()
root.title("Dictonary")
root.geometry("600x600")
import random
dictonary = {'colours':'["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan","azure","alice blue"]'}
def randomcolour():
    random_no = random.randomint(0,10)
    colour = dictonary["colours"][random_no]
    print(colour)
    root.configure(background=colour)
btn=Button(root,text="Change Background Colour",command=randomcolour)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()