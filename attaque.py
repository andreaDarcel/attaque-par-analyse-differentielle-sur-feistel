from feistel import chiffrement_feistel, fonction_xor, fonction, diviser_en_deux, PBOX
import random

delta_p = 1 << 3                                                        # signifie que la difference d'entree est 100
pairs=[]
pairs_chiffre=[]


def generation_paires_test():                                           ## pour generer des paires de messages avec une seule difference a tester
    for i in range (15000):
        p = random.randint(1,250)
        p_prime = fonction_xor(delta_p, p)
        pairs.append((p,p_prime))
        
    return (pairs)

def comparaison(keys,pairs):
    for p,p_prime in pairs:
        c = chiffrement_feistel(keys, p)
        c_prime = chiffrement_feistel(keys,p_prime)
        pairs_chiffre.append((c,c_prime))
        # delta = fonction_xor(c,c_prime)
        
    return (pairs_chiffre)


def difference_sortie(delta):
    counts = {d: 0 for d in range(16)}
    for x in range(16):
        counts[PBOX[x] ^ PBOX[x ^ delta]] += 1                          # appliquer une permutation dans la Box pour se rapprocher du differentiel de sortie                  
    return max(counts, key=counts.get)

delta_sortie = difference_sortie(delta_p)

def recherche_lastkey(pairs_chiffree):
    scores = {k: 0 for k in range(16)}  
                                                                        # Clés candidates de 0 à 15 (4 bits)
    for search_kn in range(16):

        for c, c_prime in pairs_chiffree:
            if isinstance(c, str):                                      # pour transformer la valeur chiffree en un entier si elle ne l'est pas
                c = int(c, 2)
            if isinstance(c_prime, str):
                c_prime = int(c_prime, 2)
            
            L,R = diviser_en_deux(c,4)
            Ls,Rs = diviser_en_deux(c_prime,4)                          # recuperer la partie gauche et droite
            
            R_prec = fonction_xor(L, fonction(R, search_kn))
            R_pprec = fonction_xor(Ls, fonction(Rs, search_kn))         # retrouver la valeur chiffree precedente
            
            if fonction_xor(R_prec, R_pprec) == delta_sortie:
                scores[search_kn] += 1                                  # incrementer le nombre de fois qu'une valeur se rapproche de la condition

    if max(scores.values()) == 0:                                       # si le max des scores trouves vaut 0, c-a-d que rien ne match, alors on ne retoune rien
        return None, None
                    
    cle_devinee = max(scores, key=scores.get)
    return scores, cle_devinee



