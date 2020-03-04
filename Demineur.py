from tkinter import *                     # Importations des librairies/modules
from random import shuffle, randint
                    
master = Tk()   # Fenêtre principale

HEIGHT = 500    # Dimensions du Canvas
WIDTH = 500

cnv = Canvas(master, height=HEIGHT, width=WIDTH, bg='ivory')    # Création du Canvas
#cnv.pack()   T.V.

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
    
for i in range(nb):                              # Ajout des mines
    ind1 = indx1[randint(0, len(indx1)-1)]
    ind2 = indx2[randint(0, len(indx2)-1)]
    indx1.remove(ind1)
    indx2.remove(ind2)
    tab[ind1][ind2] = -1
    

def voisins(n, i, j):   # longueur du tableau par défaut 
    
                                #       De N à N sens horaire
    return [(a,b) for (a, b) in [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1,j), (i+1, j-1), (i, j-1), (i-1, j-1)] 
            if a in range(n) and b in range(n)]
    
#print(voisins(n, 5, 6))  TEST
    
    
"""def minedetect():
    #number = 0
    #posx = 0
    #posy = 0
    Lp = [-1, 0, 1]
    Lx = []
    Ly = []
    Lv = []
    for i in range(n):               # Indication nb mines aux alentours 
        for j in range(p):
            if tab[i][j] != -1:		         # Test borderline
                for k in range(len(Lp)):
                    if tab[n+k][p+k] == -1:
                        True"""
        						


def creategrid(table):              # Création de l'espace de jeu
    x = 0
    y = 0
    for i in range(len(table)):
        y = i*c
        for j in range(len(table[i])):
            x = j*c
            #cnv.create_rectangle((x, y), (x+c, y+c), fill="grey")    
            case = Button(master, height = 20, width = 20, bg = 'darkgrey', bd = 3)                                    
            cnv.pack()
            cnv.create_window(x+c, y+c, window = case, anchor='nw')
            
            
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

""" 

Espace travail Chloé

"""

master.mainloop()
