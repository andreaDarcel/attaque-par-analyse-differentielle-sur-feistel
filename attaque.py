from feistel import chiffrement_feistel,moitie, fonction_xor,keys, fonction, diviser_en_deux
import random

delta_p = 1 << 8
pairs=[]
pairs_chiffre=[]


def generation_paires_test():               ## pour generer des paires de messages avec une seule difference a tester
    for i in range (15000):
        p = random.randint(1,260)
        p_prime = fonction_xor(delta_p, p)
        pairs.append((p,p_prime))
        
    return (pairs)

def comparaison(keys,pairs):
    for p,p_prime in pairs:
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

def recherche_lastkey(pairs_chiffree, keys_last):
    scores = {k: 0 for k in range(16)}  
    # Clés candidates de 0 à 255 (8 bits)
    for search_kn in range(16):
        keys_candidate = keys_last.copy()
        keys_candidate['k8'] = search_kn

        for c, c_prime in pairs_chiffree:
            # if isinstance(c, str):
            #     c = int(c, 2)
            # if isinstance(c_prime, str):
            #     c_prime = int(c_prime, 2)
            
            c1 = chiffrement_feistel(keys_candidate, c)
            c1_prime = chiffrement_feistel(keys_candidate, c_prime)

            if fonction_xor(c1, c1_prime) == delta_p:
                scores[search_kn] += 1

    if scores[search_kn] != 0:
        cle_devinee = max(scores, key=scores.get)
        return scores[search_kn], cle_devinee, search_kn
    else:
        return None, None, None



