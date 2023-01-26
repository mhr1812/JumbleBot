import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers = ["America","India","Australia","Argentina","France","Portugal","Spain","Netherlands","Croatia","China","Japan"]
questions = []

for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)

num = random.randint(0,len(questions)-1)

def initial():
    global questions,num 
    lb1.configure(text=questions[num])

def answercheck():
    global questions,num,answers
    userinput = e1.get()
    if userinput==answers[num]:
        messagebox.showinfo('Success','Your answer is correct')
    else:
        messagebox.showerror('Error','Your answer is wrong')
        e1.delete(0,END)

def resetswitch():
    global questions,answers,num
    num = random.randint(0,len(questions)-1)
    lb1.configure(text=questions[num])
    e1.delete(0,END)

window = Tk()
window.geometry("300x300")
window.configure(background="#0D0D0D")
window.title("JumbleBot")
window.iconbitmap(r"j.ico")

lb1 = Label(window,font='times 20',bg='#CAD5E2')
lb1.pack(pady=40,ipady=0,ipadx=10)

answer = StringVar()
e1 = Entry(window,textvariable=answer)
e1.pack(ipady=5,ipadx=5)

b1 = Button(window,text="Check",width=20,command=answercheck,bg='#00D84A')
b1.pack(pady=40)

b2 = Button(window,text="Reset",width=20,command=resetswitch,bg='#E21717')
b2.pack()

initial()

window.mainloop()