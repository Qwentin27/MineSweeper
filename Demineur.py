from tkinter import *                     # Importations des librairies/modules
from random import shuffle, randint
                    
master = Tk()   # Fenêtre principale

HEIGHT = 400    # Dimensions du Canvas
WIDTH = 400

frame = Frame(background="lightgrey")
frame.pack()

cnv = Canvas(frame, height=HEIGHT, width=WIDTH, bg='lightblue')    # Création du Canvas
cnv.pack(padx=20, pady=10)

c = 20  # Côté carré
N = c * c  # Aire du carré
L = [0] * N # Création d'une liste remplie de 0
nbline = 20 # Nombre de lignes du plateau
nbcol = 20  # Nombre de colonnes du plateau
nbMine = 50 # Nombre de mines

#game message status
strStatus = StringVar()
Label(master, textvariable=strStatus, font = 'Arial 15 bold').pack()
strStatus.set("")

#flagCount
strFlag = StringVar()
Label(frame, textvariable=strFlag, font = 'Arial 15 bold').pack(side='right')
strFlag.set(nbMine)

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



def fillTabBool(t, state):     # Remplissage du tableau de Booléens
    
    for i in range(nbline):
        for j in range(nbcol):
            t[i][j] = state
           



def fillField(t):      # Remplissage du tableau (de façon aléatoire avec des mines ou non)
    
    n, p = len(t), len(t[0])
    
    for i in range(nbMine):     
                        
        x = randint(0, n-1)
        y = randint(0, p-1)
        
        while t[x][y] == -1:
        
            x = randint(0, n-1)
            y = randint(0, p-1)
            
        t[x][y] = -1    # Ajout des mines
        
    
    
            
def voisins(t, i, j):   # Renvoie les indices / valeurs des voisins autour de la case concernée
    
                            #       De N à N / sens horaire
                      
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
            t[i][j] = case
            cnv.pack(side=BOTTOM)
            
           
            
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
                        
                        t[i][j] += 1 # Incrémentation de la valeur de la case si mine voisine 


def displaySquare(i, j, originalY, originalX):
    
    for k in range(1, 8):
        
        if tab[i][j] == k:
            
            cnv.create_image(j*20+10, i*20+10, image = LImg[k])

        if tab[i][j] == -1:
            
            if i == originalY and j == originalX :  # Test de premier clic
                
                cnv.create_image(j*20+10, i*20+10, image = LImg[9])
                
            else :
                
                cnv.create_image(j*20+10, i*20+10, image = LImg[0])

            

def displayMine(originalY, originalX):
    
    for n in range(len(tab)):
        
        for p in range(len(tab[0])):
            
            if tab[n][p] == -1:
                
                if n == originalY and p == originalX :
                    
                    cnv.create_image(p*20+10, n*20+10, image = LImg[9])
                    
                else :
                    
                    cnv.create_image(p*20+10, n*20+10, image = LImg[0])
    
        




def refresh(t, originalY, originalX):    # Rafraîchissement du tableau
    
    for i in range(len(t)):
        
        for j in range(len(t[0])):
            
            if t[i][j] == True and flags[i][j] == False:
                
                cnv.delete(ids[i][j])
                cnv.pack()
                displaySquare(i, j, originalY, originalX) 
               
                
                
def endGame(state):
    
    msg = "Vous avez gagné" if state else "Vous avez perdu"
    strStatus.set(msg)

    refresh(tabl, -1, -1)
    fillTabBool(tabl, True)
    fillTabBool(flags, False)
          
    
    
def manageState(line, col):  #analyse current state of the game
    
    win = True #win the game
    end = False #game still running

    for n in range(len(tab)):
        
        for p in range(len(tab[0])):
            
            if tabl[n][p] == True and tab[n][p] == -1 and flags[n][p] == False: #mine displayed without flag
                
                end = True
                
            elif tabl[n][p] == False and tab[n][p] != -1: #hidden number
                
                win = False
                
    if win == True :
        
        endGame(True)
        
    if end == True :
        
        endGame(False)
        displayMine(line, col)



def caseClick(event):    # Gestion lors d'un clic
    
    x,y = event.x, event.y 
    line = y//c
    col = x//c
    

    if tabl[line][col] == False and flags[line][col] == False :
        
        tabl[line][col] = True  
    
        if tab[line][col] == 0: #click on empty space
            
            cnv.create_image(col*20+10, line*20+10, image = default)
            L = discovery(tab, line, col)
            
            for k in range(len(L)):
                
                    tabl[L[k][0]][L[k][1]] = True
                    
        refresh(tabl, line, col)
        manageState(line, col)
        


def flag(event):    #display flag at x,y and block it

    x,y = event.x, event.y
    line = y//c
    col = x//c        

    if tabl[line][col] == False : #hidden square
        
        if (int(strFlag.get()) > 0):
            
            strFlag.set(int(strFlag.get()) - 1)
            cnv.create_image(col*20+10, line*20+10, image = fla)
            flags[line][col] = True
            tabl[line][col] = True   # Bloque le clic gauche sur la case avec drapeau
    else:
        
        if flags[line][col] == True : #flag on hidden square
            
            if (int(strFlag.get()) < 50):
                
                strFlag.set(int(strFlag.get()) + 1)
                cnv.create_image(col*20+10, line*20+10, image = gris)
                flags[line][col] = False
                tabl[line][col] = False
            

        

#   Images / Images à mettre sur le plateau 

mine = PhotoImage(file="moins1.png")
un = PhotoImage(file="1.png")
deux = PhotoImage(file="2.png")
trois = PhotoImage(file="3.png")
quatre = PhotoImage(file="4.png")
cinq = PhotoImage(file="5.png")
six = PhotoImage(file="6.png")
sept = PhotoImage(file="7.png")
huit = PhotoImage(file="8.png")
mineR = PhotoImage(file="mineR.png")
emot = PhotoImage(file="emot.png")
default = PhotoImage(file="default.png")
fla = PhotoImage(file="flag.png")
gris = PhotoImage(file="g.png")


#   Liste contenant les images

LImg = [mine, un, deux, trois, quatre, cinq, six, sept, huit, mineR, fla, gris, default]


# Création et remplissage des différents tableaux  
 				
tab = createTab()              
ids = createTab()
tabl = createTab()
flags = createTab()
fillTabBool(tabl, False)
fillTabBool(flags, False)
fillField(tab)
mineDetect(tab)
createGrid(ids)



def replay():       # Réinitialisation du plateau pour rejouer une partie
    
    cnv.delete(ALL)
    global tab, ids, tabl      
    tab = createTab()              
    ids = createTab()
    tabl = createTab()
    flags = createTab()
    fillTabBool(tabl, False)
    fillField(tab)
    mineDetect(tab)
    createGrid(ids)
    strStatus.set("")
    strFlag.set(nbMine)
    

    

# Bouton replay (associé à sa fonction)

btn = Button(frame, image=emot, width= 24, height= 24, bg= "white", command=replay)
btn.pack(side=TOP, pady = 10)

cnv.bind("<Button-1>", caseClick)    # Appel à caseClick() si clic gauche de la souris
cnv.bind("<Button-3>", flag)         # Appel à flag() si clic droit de la souris
master.mainloop()
