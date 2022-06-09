# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:13:13 2022

@author: ankit computer
"""

from tkinter import *
import random
root=Tk()
root.title("Random")
root.geometry("400x400")
ran_num_List = Label(root)
ran_sorted_num_list = Label(root)

def randomlistc():
    randomlist= random.sample(range(10,30),5)
    ran_num_List["text"]=  "random list : " + str(randomlist)
    randomlist.sort()
    ran_sorted_num_list["text"] = "Sorted list: " + str(randomlist)
btn = Button(root,text="Generate random list",command=randomlistc)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

ran_num_List.place(relx=0.5,rely=0.6,anchor=CENTER)
ran_sorted_num_list.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()