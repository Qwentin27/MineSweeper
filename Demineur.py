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

def createTab():        # Création du tableau (sous forme de matrice)
    
    tab = []
    cpt = 0

    for i in range(c):                 
        ligne = []
        for j in range(c):
            ligne.append(L[cpt])
            cpt += 1
        tab.append(ligne)
    return tab
    
    
def fillField(tab):        # Remplissage du tableau (de façon aléatoire avec des mines ou non)
    
    indx1 = []
    indx2 = []
    n, p = len(tab), len(tab[0])
    
    for i in range(n):           # Création d'une liste contenant tous les indices des lignes du tableau
        indx1.append(i)
        
    for i in range(p):           # Création d'une liste contenant tous les indices des colonnes du tableau
        indx2.append(i)
        
    for i in range(nb):                              # Ajout des mines
        ind1 = indx1[randint(0, len(indx1)-1)]
        ind2 = indx2[randint(0, len(indx2)-1)]
        indx1.remove(ind1)
        indx2.remove(ind2)
        tab[ind1][ind2] = -1
        
    
# REPRIS D'UN TP ATTENTION !
def voisins(n, i, j):   # Renvoie les voisins autour de la case concernée / longueur du tableau par défaut 
    
                                #       De N à N sens horaire
    return [(a,b) for (a, b) in [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1,j), (i+1, j-1), (i, j-1), (i-1, j-1)] if a in range(n) and b in range(n)]
 
    
#print(voisins(n, 5, 6))  TEST

        						
def createGrid(table):              # Création de l'espace de jeu (graphiquement)
    x = 0
    y = 0
    for i in range(len(table)):
        y = i*c
        for j in range(len(table[i])):
            x = j*c
            cnv.create_rectangle((x, y), (x+c, y+c), fill="grey")                                      
            cnv.pack()
            
#def discovery():            # Découverte des cases lors du 1er clic (aspect graphique à prendre en compte) 
            
            
def mineDetect(tab, i, j):           # Algorithme de détection des mines pour une case (et numéro affiché en conséquence)
    
    #if tab[i][j] == -1:
    #    gameState()
    
    nb = 0
    
    for k in range(8):
        if voisins(len(tab), i, j)[k] == -1:
            nb +=1
    return nb


    
"""def mineDetect():
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

def mineNumberInTab(tab, i, j):           # Changement des valeurs dans tab selon le nombre de mines
    
    nb = mineDetect(tab, i, j)
    tab[i][j] += nb
            
            
"""
APRES DECOUVERTE DE LA CASE

-1 : mine (test : si négatif, alors bombe)
0 : pas de mine à proximité
1 : 1 mine à proximité
2 : 2 mines à proximité
3...
4... 
...
8...

"""

 

#Espace travail Chloé

#def caseClick():        # Dévoilement d'une case (graphiquement)

#def caseNumber():       # Affichage des numéros (graphiquement)

#def gameState():        # WIN or GAME OVER

# + gérer l'incrémentation du compteur, gérer les composants visuels 


tab = createTab()
fillField(tab)
print(*tab, sep='\n')   # Affiche le tableau, sous forme de matrice (mais avec des crochets)
createGrid(tab)


master.mainloop()
