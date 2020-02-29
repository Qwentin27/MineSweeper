from tkinter import *
from random import shuffle

master = Tk()

HEIGHT = 500
WIDTH = 500

cnv = Canvas(master, height=HEIGHT, width=WIDTH, bg='ivory')
cnv.pack()

c = 20  # coté carré
N = c * c  # aire du carré
L = [0] * N

for i in range(len(L)):
    L.append(1)

shuffle(L)

tab = []
cpt = 0

for i in range(c):
    ligne = []
    for j in range(c):
        ligne.append(L[cpt])
        cpt += 1
    tab.append(ligne)

def creategrid(table):
    x = 0
    y = 0
    for i in range(len(table)):
        y = i*c
        for j in range(len(table[i])):
            x = j*c
            cnv.create_rectangle((x, y), (x+c, y+c), fill="grey")
            
print(*tab, sep='\n')
creategrid(tab)

master.mainloop()
