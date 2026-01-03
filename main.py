from feistel import generate_cle, chiffrement_feistel
from attaque import recherche_lastkey, generation_paires_test, keys_last
import secrets

# Paramètres globaux
TAILLE_BLOC = 16
NBRE_TOURS = 8
MOITIE = 8

# Message clair aléatoire
M = secrets.randbits(TAILLE_BLOC)

# Génération des clés
keys = generate_cle(NBRE_TOURS, MOITIE)

print("Message clair :", M)
print(keys)

# Chiffrement
C = chiffrement_feistel(keys, M)
print("Message chiffré :", C)

# Attaque différentielle
score, cle_devinee, search_k4 = recherche_lastkey(pairs=generation_paires_test(), keys_last=keys_last)

print("\nClé réelle (dernière ronde) :", keys[f'k{NBRE_TOURS}'])
print("Clé devinée :", bin(cle_devinee))
print("Scores :", score)
