from tkinter import *                     # Importations des librairies/modules
from random import shuffle, randint
                    
master = Tk()   # Fenêtre principale

HEIGHT = 500    # Dimensions du Canvas
WIDTH = 500

cnv = Canvas(master, height=HEIGHT, width=WIDTH, bg='ivory')    # Création du Canvas

c = 20  # Côté carré
N = c * c  # Aire du carré
L = [0] * N # Création d'une liste remplie de 0
nbline = 20
nbcol = 20
nb = 50 # Nombre de mines


shuffle(L)

def createTab():        # Création des tableaux de jeux (sous forme de matrice)
    
    tab = []
    cpt = 0

    for i in range(nbline):                 
        ligne = []
        for j in range(nbcol):
            ligne.append(L[cpt])
            cpt += 1
        tab.append(ligne)
    return tab


def fillTabBool(t):     # Remplissage du tableau de Booléens
    
    for i in range(nbline):
        for j in range(nbcol):
            t[i][j] = False
           
    


def fillField(t):      # Remplissage du tableau (de façon aléatoire avec des mines ou non)
    
    n, p = len(t), len(t[0])
    
    for i in range(nb):     
                        
        x = randint(0, n-1)
        y = randint(0, p-1)
        
        while t[x][y] == -1:
        
            x = randint(0, n-1)
            y = randint(0, p-1)
            
        t[x][y] = -1    # Ajout des mines
    
    
# REPRIS D'UN TP ATTENTION !
            
def voisins(t, i, j):   # Renvoie les indices / valeurs des voisins autour de la case concernée
    
                            #       De N à N sens horaire
    Lx = [(a,b) for (a, b) in [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1,j), (i+1, j-1), (i, j-1), (i-1, j-1)] if a in range(len(t)) and b in range(len(t))]

    Lv = []
    
    for k in range(len(Lx)):
        Lv.append(t[Lx[k][0]][Lx[k][1]])
    
    return Lx, Lv      
    



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
            
            
def discovery(t, i, j):   # Découverte des cases lors du "1er clic" (aspect graphique à prendre en compte) 
    
    
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
                
                
        
def mineDetect(t):   # Algorithme de détection des mines pour une case (et numéro affiché en conséquence)
    
    for i in range(len(t)):
        for j in range (len(t[0])):
            if t[i][j] != -1:  
                n = len(voisins(t, i, j)[1])
                for k in range(n):
                    if voisins(t, i, j)[1][k] == -1:
                        t[i][j] += 1 # 


def caseNumber(i, j):       # Affichage des numéros (graphiquement)
    
    for k in range(1, 8):
        
        if tab[i][j] == k:
            
            cnv.create_image(j*20+10, i*20+10, image = LImg[k])
            
        elif tab[i][j] == -1:
            
            cnv.create_image(j*20+10, i*20+10, image = LImg[0])
            
    
  
           
def gameState(i, j):        # Test WIN or GAME OVER
    
    if tab[i][j] == -1:
        gameMessage(False)
        for n in range(len(tab)):
            for p in range(len(tab[0])):
                if tab[n][p] == -1:
                    tabl[n][p] = True
    game()

def game():

    game = True
    
    for n in range(len(tab)):
        for p in range(len(tab[0])):
            if tab[n][p] != -1 and tabl[n][p] != True:
                game = False
    if game:
        gameMessage(True)
        
                
def gameMessage(win):
    
    #del(tab)
    #del(tabl)
    #del(ids)
    
    if win:
        print("Vous avez gagné")   # affichage d'un message de win 
        
    else:
        print("Vous avez perdu")   # affichage d'un message de lose
        


        
# + gérer l'incrémentation du compteur, gérer les composants visuels 





def tabState(t):    # Rafraîchissement du tableau
    
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == True:
                cnv.delete(ids[i][j])
                cnv.pack()
                caseNumber(i, j)
                
          

def caseClick(event):    # Gestion lors d'un clic
     
    x,y = event.x, event.y   # Récupère les coordonnées lors d'un clic 
    line = y//c
    col = x//c
    
    if tabl[line][col] != True:
        
        tabl[line][col] = True   # Effectuer un test si la case a déjà été cliquée
        gameState(line, col)
    
        if tab[line][col] == 0:
            L = discovery(tab, line, col)
            for k in range(len(L)):
                tabl[L[k][0]][L[k][1]] = True
        tabState(tabl)
    

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



# Création et remplissage des différents tableaux  
     						
tab = createTab()              
ids = createTab()
tabl = createTab()
fillTabBool(tabl)
fillField(tab)
mineDetect(tab)
createGrid(ids)


"""    TESTS
print(*tab, sep='\n')   # Affiche le tableau, sous forme de matrice (mais avec des crochets)
print()
print()
print(*ids, sep='\n')
print(voisins(t, 0, 0))  
print()
print(*tab, sep='\n')
print()
print(*tabl, sep='\n')
print()
print(discovery(tab, 4, 3))
"""

cnv.bind("<Button>", caseClick)
master.mainloop()
