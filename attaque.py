from feistel import chiffrement_feistel,moitie, fonction_xor,keys
import random

delta_p = 1 << 8
pairs=[]
pairs_chiffre=[]


def generation_paires_test():               ## pour generer des paires de messages avec une seule difference a tester
    for i in range (400):
        p = random.randint(1,260)
        p_prime = fonction_xor(delta_p, p)
        pairs.append((p,p_prime))
        
    return (pairs)

def comparaison(keys,p,p_prime):
    for _ in range (400):
        c = chiffrement_feistel(keys, p)
        c_prime = chiffrement_feistel(keys,p_prime)
        pairs_chiffre.append((c,c_prime))
        # delta = fonction_xor(c,c_prime)
    return pairs_chiffre

keys_last = {
    'k1': 0,    
    'k2': 0,
    'k3': 0,
    'k4': 0,
    'k5': 0,
    'k6': 0,
    'k7': 0,
}

def recherche_lastkey(pairs, keys_last):
    scores = {k: 0 for k in range(64)}                                    # Clés candidates de 0 à 63 (6 bits)

    for search_kn in range(64):

        for C, C_prime in pairs_chiffre:
            # extraire la partie droite (8 bits)
            R  = C ^ search_kn 
            R_ = C_prime ^ search_kn 

            # test différentiel NON trivial
            if (R ^ R_)  == 0 :
                scores[search_kn] += 1

    cle_devinee = max(scores, key=scores.get)
    return scores, cle_devinee, search_kn




