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

nb = 5 + 6 + 1 + 3 + 4 + 18
print(nb)
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
            
        
print(len(discovery(tab, 4, 3)))
    
    
    