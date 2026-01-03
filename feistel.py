import random

M: int
keys = {}
L = {}
R = {}
nbre_tours = 4                                    ## nombre de tours
moitie = 2                                         ## vu que la taille c'est 16 bits , la moitie c'est 8 bits

def generate_cle(nbre_tours , moitie):
    
    for i in range(1, nbre_tours+1):
        keys[f'k{i}'] = random.getrandbits(moitie)
    return keys


def diviser_en_deux(M, moitie):                     ## pour diviser le mot en gauche et droite

    Left = M >> moitie                      ## decalage vers la droite du nombre de bits moitie
    mask = (1 << moitie) -1 
    Right = M & mask
    
    return Left, Right

def fonction_xor (z: bin,y : bin):
        return z^y

def fonction(k, r):
                                                # fonction F du Feistel (simplifiée)
    return fonction_xor(k,r)

def chiffrement_feistel(keys, M: int):
    L,R = diviser_en_deux(M, 2)
    
    for i in range (1, nbre_tours + 1):
        
        L,R = R, fonction_xor( L ,fonction(keys[f'k{i}'] , R) )
    
    mot_chiffre = (L << moitie ) | R
    
    return mot_chiffre





# def get_bit(x: bin, i):
#             return (x >> i) & 1
            
#             for i in range (moitie):
#                 if get_bit(z,i) == get_bit(y,i) :
#                     return 0
#                 else:
#                     return 1