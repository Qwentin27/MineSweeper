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

def createTabBool():        # Création du tableau de booléens (sous forme de matrice)
    
    tabl = []
    cpt = 0

    for i in range(nbline):                 
        ligne = []
        for j in range(nbcol):
            ligne.append(L[cpt])
            cpt += 1
        tabl.append(ligne)
    return tabl

def fillTabBool(t):
    
    for i in range(nbline):
        for j in range(nbcol):
            t[i][j] = False
           
    
def createTab2D():        # Création du tableau des ids des cases (sous forme de matrice)
    
    t = []
    cpt = 0

    for i in range(nbline):                 
        ligne = []
        for j in range(nbcol):
            ligne.append(L[cpt])
            cpt += 1
        t.append(ligne)
    return t
    
def fillField(t):        # Remplissage du tableau (de façon aléatoire avec des mines ou non)
    
    indx1 = []
    indx2 = []
    n, p = len(t), len(t[0])
    
    for i in range(n):           # Création d'une liste contenant tous les indices des lignes du tableau
        indx1.append(i)
        
    for i in range(p):           # Création d'une liste contenant tous les indices des colonnes du tableau
        indx2.append(i)
        
    for i in range(nb):                              # Ajout des mines
        ind1 = indx1[randint(0, len(indx1)-1)]
        ind2 = indx2[randint(0, len(indx2)-1)]
        indx1.remove(ind1)
        indx2.remove(ind2)
        t[ind1][ind2] = -1

        
    
# REPRIS D'UN TP ATTENTION !
            
def voisins(t, i, j):   # Renvoie les indices / valeurs des voisins autour de la case concernée
    
                            #       De N à N sens horaire
    Lx = [(a,b) for (a, b) in [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1,j), (i+1, j-1), (i, j-1), (i-1, j-1)] if a in range(len(t)) and b in range(len(t))]

    Lv = []
    
    for k in range(len(Lx)):
        Lv.append(t[Lx[k][0]][Lx[k][1]])
    
    return Lx, Lv     # Eventuellement renvoyer aussi les coordonnées des voisins pour discovery  
    



def createGrid(t):         # Création de l'espace de jeu (graphiquement)
    x = 0
    y = 0
    for i in range(len(t)):
        y = i*c
        for j in range(len(t[i])):
            x = j*c
            case = cnv.create_rectangle((x, y), (x+c, y+c), fill="grey")
            ids[i][j] = case
            cnv.pack()
            
            
def discovery(t, i, j):            # Découverte des cases lors du "1er clic" (aspect graphique à prendre en compte) 
    
    
    L = []
    L2 = [(i, j)]
    
    while len(L2) != 0:
        
        n, p = L2.pop(0)   
        v = voisins(t, n, p)
            
        for k in range(len(v[0])):
            
            
            if not(v[0][k] in L):
                
                L.append(v[0][k])
                
                if v[1][k] == 0 :
                
                    L2.append(v[0][k])
                
    return L
                
                
        
def mineDetect(t):           # Algorithme de détection des mines pour une case (et numéro affiché en conséquence)
    
    for i in range(len(t)):
        for j in range (len(t[0])):
            if t[i][j] != -1:  
                nb = 0
                n = len(voisins(t, i, j)[1])
                for k in range(n):
                    if voisins(t, i, j)[1][k] == -1:
                        nb = 1
                        t[i][j] += nb


def caseNumber(i, j):       # Affichage des numéros (graphiquement)
    
    for k in range(1, 8):
        
        if tab[i][j] == k:
            
            #print(tab[i][j])
            cnv.create_image(j*20+10, i*20+10, image = LImg[k])
            
            
        elif tab[i][j] == -1:
            
            cnv.create_image(j*20+10, i*20+10, image = LImg[0])
            
    
  
           
#def gameState():        # WIN or GAME OVER

# + gérer l'incrémentation du compteur, gérer les composants visuels 

def tabState(t):
    
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == True:
                cnv.delete(ids[i][j])
                caseNumber(i, j)
                
                



def caseClick(event):         
    x,y = event.x, event.y   # Récupère les coordonnées lors d'un clic 
    line = y//c
    col = x//c
    tabl[line][col] = True   # Effectuer un test si la case a déjà été cliquée
    
    if tab[line][col] == 0:
        L = discovery(tab, line, col)
        for k in range(len(L)):
            tabl[L[k][0]][L[k][1]] = True
    tabState(tabl)
    #gameState()

#   Images à mettre sur le plateau 

mine = PhotoImage(file="moins1.png")
un = PhotoImage(file="1.png")
deux = PhotoImage(file="2.png")
trois = PhotoImage(file="3.png")
quatre = PhotoImage(file="4.png")
cinq = PhotoImage(file="5.png")
six = PhotoImage(file="6.png")
sept = PhotoImage(file="7.png")
huit = PhotoImage(file="8.png")

#   Liste contenant les images

LImg = [mine, un, deux, trois, quatre, cinq, six, sept, huit]



        						
tab = createTab()              
ids = createTab2D()
tabl = createTabBool()
fillTabBool(tabl)
createGrid(ids)
fillField(tab)
mineDetect(tab)


    
#print(*tab, sep='\n')   # Affiche le tableau, sous forme de matrice (mais avec des crochets)
print(*ids, sep='\n')
#print(voisins(t, 0, 0))  #TEST
print()
print(*tab, sep='\n')
print()
print(*tabl, sep='\n')
print()
#+print(discovery(tab, 4, 3))


cnv.bind("<Button>", caseClick)
master.mainloop()
