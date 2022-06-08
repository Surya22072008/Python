# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:03:36 2022

@author: ankit computer
"""

from tkinter import *
root=Tk()
root.title("3d array")
root.geometry("400x400")
label=Label(root)
glabel=Label(root)
entry=Entry(root)
array_3d = [[['1','2','3','4','5','6'],['Head','Trail'],['A','B','C','D','E','F','G','H']]]
print(array_3d[0][2][3])
def newpassword() :
    glabel["text"] ="Guessed Password  "+ entry.get()
    random_num1 = randint(0,6)
    random_num2 = randint(0,1)
    random_num3 = randint(0,7)
    letter1 = str(array_3d[0][0][random_num1])
    letter2 = str(array_3d[0][1][random_num2])
    letter3 = str(array_3d[0][2][random_num3])
    label["text"] = "Generated Password "+letter1 + " " + letter2 + " " +letter3
btn = Button(root,text="Guess Password Password",command=newpassword)
entry.place(relx="0.5",rely="0.3",anchor=CENTER)
btn.place(relx="0.5",rely="0.5",anchor=CENTER)
label.place(relx="0.5",rely="0.6",anchor=CENTER)
glabel.place(relx="0.5",rely="0.4",anchor=CENTER)