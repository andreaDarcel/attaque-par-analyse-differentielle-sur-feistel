import random

M: int
keys = {}
L = {}
R = {}
nbre_tours = 8                                     ## nombre de tours
moitie = 8                                         ## vu que la taille c'est 16 bits , la moitie c'est 8 bits

def generate_cle(nbre_tours , M):
    
    for i in range(1, nbre_tours+1):
        keys[f'k{i}'] = random.getrandbits(moitie)
    return keys


def diviser_en_deux(M, moitie):                     ## pour diviser le mot en gauche et droite

    L[f'0'] = M >> moitie                      ## decalage vers la droite du nombre de bits moitie
    mask = (1 << moitie) -1 
    R[f'0'] = M & mask
    
    return L[f'0'], R[f'0']

def fonction_xor (z: bin,y : bin):
        return z^y

def fonction(k, r):
                                                # fonction F du Feistel (simplifiée)
    return fonction_xor(k,r)

def chiffrement_feistel(keys, M: int):
    L['0'],R['0'] = diviser_en_deux(M, moitie)
    
    for i in range (1, nbre_tours + 1):
        
        L[f'{i}'] = R[f'{i-1}']
        R[f'{i}'] = fonction_xor( L[f'{i-1}'] ,fonction(keys[f'k{i}'] , R[f'{i-1}']) )
    
    mot_chiffre = (L[f'{nbre_tours}'] << moitie ) | R[f'{nbre_tours}']
    
    return format(mot_chiffre, '016b')





def get_bit(x: bin, i):
            return (x >> i) & 1
            
            for i in range (moitie):
                if get_bit(z,i) == get_bit(y,i) :
                    return 0
                else:
                    return 1