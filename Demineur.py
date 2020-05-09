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
nbline = 20
nbcol = 20
nb = 20 # Nombre de mines

shuffle(L)

def createTab():        # Création du tableau de jeu (sous forme de matrice)
    
    tab = []
    cpt = 0

    for i in range(nbline):                 
        ligne = []
        for j in range(nbcol):
            ligne.append(L[cpt])
            cpt += 1
        tab.append(ligne)
    return tab
    
def createTab2D():        # Création du tableau des ids des cases (sous forme de matrice)
    
    ids = []
    cpt = 0

    for i in range(nbline):                 
        ligne = []
        for j in range(nbcol):
            ligne.append(L[cpt])
            cpt += 1
        ids.append(ligne)
    return ids
    
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
        
    """for k in range(len(tab)):
        for l in range(len(tab[0])):
            mineDetect(tab, k, l)"""
        
    
# REPRIS D'UN TP ATTENTION !
def voisins(tab, i, j):   # Renvoie les indices / valeurs des voisins autour de la case concernée
    
                            #       De N à N sens horaire
    Lx = [(a,b) for (a, b) in [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1,j), (i+1, j-1), (i, j-1), (i-1, j-1)] if a in range(len(tab)) and b in range(len(tab))]

    Lv = []
    
    for k in range(len(Lx)):
        Lv.append(tab[Lx[k][0]][Lx[k][1]])
    
    return Lv     # Eventuellement renvoyer aussi les coordonnées des voisins pour discovery  
    

t = [[-1, -1, -1],
     [-1, 0, -1],
     [-1, -1, -1]]




def createGrid(tab):         # Création de l'espace de jeu (graphiquement)
    x = 0
    y = 0
    for i in range(len(tab)):
        y = i*c
        for j in range(len(tab[i])):
            x = j*c
            case = cnv.create_rectangle((x, y), (x+c, y+c), fill="grey")
            ids[i][j] = case                                      
            cnv.pack()
            
            
def discovery(tab, i, j):            # Découverte des cases lors du "1er clic" (aspect graphique à prendre en compte) 
    
    if tab[i][j] == -1:
        #gameState()     # renvoie au game over si clic sur bombe 
        False
    else :
        L = []
        for k in range(len(voisins(tab, i, j))):
            if voisins(tab, i, j)[k] == -1:
                #caseClick(tab, i, j)
                False
            elif voisins(tab, i, j)[1][k] == 0:
                caseClick(tab, i, j)
                n = voisins(tab, i, j)[0][k][0]
                p = voisins(tab, i, j)[0][k][1]
                return discovery(tab, n, p)
            else:
                n = voisins(tab, i, j)[0][k][0]
                p = voisins(tab, i, j)[0][k][1]
                #caseClick(tab, n, p)
            
        
def mineDetect(tab):           # Algorithme de détection des mines pour une case (et numéro affiché en conséquence)
    
    for i in range(len(tab)):
        for j in range (len(tab[0])):
            if tab[i][j] != -1:  
                nb = 0
                n = len(voisins(tab, i, j))
                for k in range(n):
                    if voisins(tab, i, j)[k] == -1:
                        nb = 1
                        tab[i][j] += nb


    
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
        

def caseNumber(i, j):       # Affichage des numéros (graphiquement)
    True
    
#def gameState():        # WIN or GAME OVER

# + gérer l'incrémentation du compteur, gérer les composants visuels 





def caseClick(event):         # Dévoilement d'une case (graphiquement)
    x,y = event.x, event.y   # Récupère les coordonnées lors d'un clic 
    line = y//c
    col = x//c
    cnv.delete(ids[line][col])
    #caseNumber(line, col)
    
        						
tab = createTab()              
ids = createTab2D()
createGrid(tab)
fillField(tab)
    
print(*tab, sep='\n')   # Affiche le tableau, sous forme de matrice (mais avec des crochets)
#print(*ids, sep='\n')
#print(voisins(t, 0, 0))  #TEST
mineDetect(tab)
print()
print(*tab, sep='\n')

cnv.bind("<Button>", caseClick)
master.mainloop()
