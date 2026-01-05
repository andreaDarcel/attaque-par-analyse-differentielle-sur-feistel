from feistel import generate_cle, chiffrement_feistel
from attaque import recherche_lastkey, generation_paires_test,  comparaison
import secrets


TAILLE_BLOC = 8
NBRE_TOURS = 3
MOITIE = 4

M = secrets.randbits(TAILLE_BLOC)                                                   # Message clair aléatoire


keys = generate_cle(NBRE_TOURS, MOITIE)                                             # Génération des clés

print("Message clair :", M)
print(keys)

C = chiffrement_feistel(keys, M)                                                    # Chiffrement
print("Message chiffré :", C)
print("Message chiffré (bin):", format(C, f'08b'))

pairs_chiffree = comparaison(keys, generation_paires_test())
score, cle_devinee = recherche_lastkey(pairs_chiffree)

print("\nClé réelle (dernière ronde) :", keys[f'k{NBRE_TOURS}'])                    # cle reelle utilisee dans le projet
if cle_devinee is not None:
    print("Clé devinée  :", cle_devinee)                                            # cle a deviner pour verifier si elle est egale a la cle reelle

N = len(pairs_chiffree)
scores_ranges = sorted(                                                             # rangement des scores par ordre decroissant
    score.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nClés classées par probabilité décroissante :")
for k, v in scores_ranges:
    pct = (v / N) * 100
    print(f"{k:04b}\t {k} →  {pct:.2f}% \t ({v})")



