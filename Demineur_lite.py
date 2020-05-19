from tkinter import * 
master = Tk()
HEIGHT = 500    # Dimensions du Canvas
WIDTH = 500

cnv = Canvas(master, height=HEIGHT, width=WIDTH, bg='ivory')

c = 20
N = c * c  # Aire du carré
L = [0] * N # Création d'une liste remplie de 0

tab = [[0, 0, 0, 0, 0, 0, 0, 1,-1, 1],
       [1, 1, 2, 3, 2, 1, 0, 1, 1, 1],
       [1,-1,-1,-1, 1, 0, 0, 0, 0, 0],
       [1, 2, 3, 2, 2, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 1,-1, 2, 1, 0, 0],
       [0, 0, 0, 0, 1, 2,-1, 1, 0, 0],
       [1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
      [-1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
       [1, 1, 0, 0, 1,-1, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]]

#nb = 5 + 6 + 1 + 3 + 4 + 18
#print(nb)
""" 
nb = 5 + 6 + 1 + 3 + 4 + 18

    discovery(tab, 4, 3):
       L = [(3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (4, 2), (3, 2)]
       L2 = [(5, 3), (5, 2), (4, 2)]
       
       while len(L2) != 0:
           
           for n, p in L2:
               
               v = ([(3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (4, 2), (3, 2)], 
                     [2,        2,      1,      1,      0,      0,      0,      3])
               
               for k in range(8):
                   
                   
                   if 0 == 0 and not ((5, 2) in L):
                       
                       L2.append((5, 2))
                       
                       
                       
                   L.append((5, 3))
                   
               L2.remove((4, 3))
               """


def voisins(tab, i, j):   # Renvoie les indices / valeurs des voisins autour de la case concernée
    
                            #       De N à N sens horaire
    Lx = [(a,b) for (a, b) in [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1,j), (i+1, j-1), (i, j-1), (i-1, j-1)] if a in range(len(tab)) and b in range(len(tab))]

    Lv = []
    
    for k in range(len(Lx)):
        Lv.append(tab[Lx[k][0]][Lx[k][1]])
    
    return Lx, Lv

#print(voisins(tab, 4, 3))

def discovery(tab, i, j):   
    
    L = []
    L2 = [(i, j)]
    
    while len(L2) != 0:
        
        n, p = L2.pop(0)   
        v = voisins(tab, n, p)
            
        for k in range(len(v[0])):
            
            
            if not(v[0][k] in L):
                
                L.append(v[0][k])
                
                if v[1][k] == 0 :
                
                    L2.append(v[0][k])
                
    return L
            
def createTab2D():        # Création du tableau des ids des cases (sous forme de matrice)
    
    t = []
    cpt = 0

    for i in range(10):                 
        ligne = []
        for j in range(10):
            ligne.append(L[cpt])
            cpt += 1
        t.append(ligne)
    return t
        
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

def img():
   logo = PhotoImage(file="1.png")
   cnv.create_image(10, 10, image = logo)

    
def caseClick(event):         
    x,y = event.x, event.y   # Récupère les coordonnées lors d'un clic 
    line = y//c
    col = x//c
    cnv.delete(ids[line][col])

    
ids = createTab2D()
createGrid(tab)
img()

del(ids[5][5])

cnv.bind("<Button>", caseClick)
master.mainloop()