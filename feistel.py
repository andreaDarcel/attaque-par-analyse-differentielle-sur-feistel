import random


keys = {}
nbre_tours = 3                                    ## nombre de tours
moitie = 8                                        ## vu que la taille c'est 16 bits , la moitie c'est 8 bits

def generate_cle(nbre_tours , moitie):
    
    for i in range(1, nbre_tours+1):
        keys[f'k{i}'] = random.getrandbits(moitie)  # generation aleatoire de cles
    return keys


def diviser_en_deux(M, moitie):                     ## pour diviser le mot en gauche et droite

    Left = M >> moitie                               ## decalage vers la droite du nombre de bits moitie
    mask = (1 << moitie) -1 
    Right = M & mask
    
    return Left, Right

def fonction_xor (z: bin,y : bin):
        return z^y


PBOX = [6,4,12,5,0,7,2,14,1,15,3,13,8,10,9,11]       # boite de permuation utilisee pour rendre le resultat plus securise

def fonction(R, k):                                  # fonction F du Feistel (simplifiée)
    return PBOX[R ^ k]


def chiffrement_feistel(keys, M: int):
    L,R = diviser_en_deux(M, 4)
    
    for i in range (1, nbre_tours + 1):
        
        L,R = R, fonction_xor( L ,fonction(keys[f'k{i}'] , R) )
    
    mot_chiffre = (L << moitie ) | R
    
    return mot_chiffre