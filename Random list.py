# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:58:25 2022

@author: ankit computer
"""

from tkinter import *
root=Tk()
root.title("Ran word generator")
root.geometry("400x400")
label = Label(root)
alpha_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]                                       

def random_number():
    ran_num1 = random.ranint(0,25)
    ran_num2 = random.ranint(0,25)
    ran_num3 = random.ranint(0,25)
    ran_num4 = random.ranint(0,25)
    ran_num5 = random.ranint(0,25)
    ran_alpha1 = alpha_list[ran_num2]
    ran_alpha2 = alpha_list[ran_num3]
    ran_alpha3 = alpha_list[ran_num3]
    ran_alpha4 = alpha_list[ran_num4]
    ran_alpha5 = alpha_list[ran_num5]
    label["text"] = ran_alpha1+ran_alpha2+ran_alpha3+ran_alpha4+ran_alpha5
btn = Button(root)
btn = Button(root,text="Generate word", command=random_number)

btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()