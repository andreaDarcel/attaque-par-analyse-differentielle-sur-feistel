from feistel import generate_cle, chiffrement_feistel
from attaque import recherche_lastkey, generation_paires_test, keys_last, comparaison
import secrets

# Paramètres globaux
TAILLE_BLOC = 16
NBRE_TOURS = 4
MOITIE = 2

# Message clair aléatoire
M = secrets.randbits(TAILLE_BLOC)

# Génération des clés
keys = generate_cle(NBRE_TOURS, MOITIE)

print("Message clair :", M)
print(keys)

# Chiffrement
C = chiffrement_feistel(keys, M)
print("Message chiffré :", C)
print("Message chiffré (bin):", format(C, f'016b'))

# Attaque différentielle
pairs_chiffree = comparaison(keys, generation_paires_test())
score, cle_devinee, search_kn = recherche_lastkey(pairs_chiffree, keys_last=keys_last)


print("\nClé réelle (dernière ronde) :", keys[f'k{NBRE_TOURS}'])
if cle_devinee is not None:
    print("Clé devinée  :", cle_devinee)
print("Scores :", score)
if search_kn is not None:
    print("Clé testée :", bin(search_kn))
