#####################################################################
#  Created by Bhupesh Pandey
#  28 May 2017; Melbourne
#  The Bull and Cow game in GUI version
#####################################################################

from Tkinter import *
import tkMessageBox
import random

global num
global bull
global cow
global g

g = 1

r = ['0', '0', '0', '0']
bull = cow = 0

for i in range(4):
    r[i] = str(random.randrange(1, 10))
    j = 0
    while j < i:
        if r[i] == r[j]:
            j = 0
            r[i] = str(random.randrange(1, 10))
            continue
        j += 1
num = r[0] + r[1] + r[2] + r[3]

top = Tk()
top.wm_title("Bull and Cow - A number guessing game")
top.minsize(400, 600)
L1 = Label(top, text="Enter your number:")
L1.pack()
E1 = Entry(top, bd=5)
E1.pack()


def win(g):
    tkMessageBox.showinfo("Game Finish", "Congratulations, You won in "+str(g)+" guesses!!!")
    exit()


def output():
    x = E1.get()

    if not str.isdigit(x):
        tkMessageBox.showinfo("!!!!!!", "Wrong input. Please input 4 digit number.")
    elif int(x)>9999 or int(x)<1000:
        tkMessageBox.showinfo("!!!!!!", "Wrong input. Please input 4 digit number.")
#    elif x == num:
#        win(g)
    else:
        bull = cow = 0
        global g
        for i in range(4):
            if x[i] == num[i]:
                bull += 1
            for j in num:
                if j == x[i]:
                    cow += 1

        cow = cow - bull
        L0 = Label(top, text="\n" + x + "\t\t" + str(bull) + "\t" + str(cow))
        g+=1
        L0.pack()
    if x == num:
        L0 = Label("This is the right guess!")
        win(g)

    E1.delete(0, END)




B = Button(top, text="Enter", command=output)

B.pack()

L2 = Label(top, text="\nYour Guess\tBull\tCow")
L2.pack()
top.mainloop()
