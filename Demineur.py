from tkinter import *                     # Importations des librairies/modules
from random import shuffle, randint
                    
master = Tk()   # Fenêtre principale

HEIGHT = 500    # Dimensions du Canvas
WIDTH = 500

cnv = Canvas(master, height=HEIGHT, width=WIDTH, bg='ivory')    # Création du Canvas
cnv.pack()

c = 20  # Côté carré
N = c * c  # Aire du carré
L = [0] * N # Création d'une liste remplie de 0
nb = 20 # Nombre de mines

shuffle(L)

tab = []
cpt = 0

for i in range(c):                  # Remplissage du tableau (sous forme de matrice)
    ligne = []
    for j in range(c):
        ligne.append(L[cpt])
        cpt += 1
    tab.append(ligne)
    
indx1 = []
indx2 = []

n, p = len(tab), len(tab[0])

for i in range(n):           # Création d'une liste contenant tous les indices des lignes du tableau
    indx1.append(i)
    
for i in range(p):        # Création d'une liste contenant tous les indices des colonnes du tableau
    indx2.append(i)
    
for i in range(nb):                         # Ajout des mines
    ind1 = indx1[randint(0, len(indx1)-1)]
    ind2 = indx2[randint(0, len(indx2)-1)]
    indx1.remove(ind1)
    indx2.remove(ind2)
    tab[ind1][ind2] = -1
    
"""   
for i in range(n):           # Indication nombre de bombes aux alentours de la case
    for j in range(p):
        if tab[i][j] != -1:
"""          



def creategrid(table):              # Création de l'espace de jeu
    x = 0
    y = 0
    for i in range(len(table)):
        y = i*c
        for j in range(len(table[i])):
            x = j*c
            cnv.create_rectangle((x, y), (x+c, y+c), fill="grey")
            
"""
APRES DECOUVERTE DE LA CASE

-1 : mine (test : si négatif, alors bombe)
0 : pas de mine
1 : 1 mine à proximité
2 : 2 mines à proximité
3...
4... 
...
8...

"""
            
print(*tab, sep='\n')
creategrid(tab)

master.mainloop()
