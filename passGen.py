# pip install pep8
# pip install pycodestyle
# pep8 --first oknoBudynek.py
# pycodestyle --first oknoBudynek.py
# coding: utf-8
from tkinter import *
from tkinter import messagebox
import random


spc = ['@','#','$','%','&']
not_spc1 = [0,1,2,3,4,5,6,7,8,9]
not_spc2 = ['@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
not_spc3 = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def password_generator():
    pg = Tk()
    pg.geometry("350x150")
    pg.title("Password Generator (P-Protect)")
    pg.resizable(0,0)
    def pass_gen():
        pass_entry_text = ""
        generated = ""
        choice_lst = []
        length = random.randint(9,10)
        for i in range(length+1):
            special = random.choice(spc)
            number = random.choice(not_spc1)
            non_special = random.choice(not_spc2)
            non_special2 = random.choice(not_spc3)
            choice_lst.append(special)
            choice_lst.append(number)
            choice_lst.append(non_special)
            choice_lst.append(non_special2)
            choice = random.choice(choice_lst)
            generated += str(choice)
        pass_entry.delete(0, END)
        pass_entry_text = generated
        pass_entry.insert(END, pass_entry_text)
        # print(generated)
    empty = Label(pg, text="        ")
    empty.pack()
    pass_label = Label(pg, text="GENERATE PASSWORD", font=('bold',14), fg="red")
    pass_label.pack()
    empty = Label(pg, text="         ")
    empty.pack()
    global pass_entry_text
    pass_entry_text = StringVar()
    global pass_entry
    pass_entry = Entry(pg, textvariable=StringVar)
    pass_entry.pack()
    empty = Label(pg, text="         ")
    empty.pack()
    pass_btn = Button(pg, text="GENERATE", font=5, fg="black", bg="yellow", command=pass_gen)
    pass_btn.pack()
    pg.mainloop()

if __name__ == '__main__':
    password_generator()