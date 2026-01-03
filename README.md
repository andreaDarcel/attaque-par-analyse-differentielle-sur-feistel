# Simulation d’une Attaque par Analyse Différentielle  
## sur un Schéma de Feistel Simplifié


## 1. Présentation du projet

Ce projet a pour objectif de simuler une **attaque par analyse différentielle** appliquée à un **schéma de Feistel simplifié**, dans un cadre pédagogique.

L’étude vise à montrer que :
- certaines différences d’entrée se propagent de manière non aléatoire,
- des biais statistiques apparaissent dans les différences de sortie,
- ces biais peuvent être exploités pour retrouver partiellement des sous-clés.

Le schéma de chiffrement implémenté est volontairement faible et ne doit pas être considéré comme sécurisé.


## 2. Organisation du projet

Code/
├── feistel.py
├── attaque.py
├── main.py
└── README.md


## 3. Description des fichiers

### feistel.py
Ce fichier contient l’implémentation du schéma de Feistel.

Fonctionnalités principales :
- découpage du bloc en parties gauche et droite,
- application des tours de Feistel,
- chiffrement d’un bloc binaire.

Les équations utilisées sont :
- L(i+1) = R(i)
- R(i+1) = L(i) XOR F(R(i), K(i))  avec F la fonction XOR


### differential.py
Ce fichier implémente l’attaque par analyse différentielle.

Fonctionnalités principales :
- génération de paires de messages (P, P') avec une différence d’entrée fixée,
- chiffrement des paires de messages,
- calcul des différences de sortie,
- analyse statistique des différences observées,
- test d’hypothèses sur les sous-clés du dernier tour.


### main.py
Point d’entrée du programme.

Rôle :
- définition des paramètres de la simulation,
- lancement du chiffrement,
- exécution de l’attaque différentielle,
- affichage des résultats obtenus.


## 4. Paramètres du chiffrement simulé

- Taille du bloc : 16 bits  
- Découpage : 8 bits gauche / 8 bits droite  
- Nombre de tours : 3 ou 4  
- Fonction F : opération simple non linéaire, la fonction XOR
- Sous-clés : valeurs générées pour la simulation  

Ces paramètres sont choisis afin de rendre l’attaque observable avec un nombre raisonnable de tests.


## 5. Principe de la simulation

La simulation suit les étapes suivantes :

1. Choix d’une différence d’entrée ΔP  
2. Génération de paires de messages aléatoires respectant ΔP  
3. Chiffrement des messages avec le schéma de Feistel  
4. Calcul des différences de sortie ΔC  
5. Analyse des fréquences observées  
6. Identification des sous-clés les plus probables  

Les résultats sont affichés sous forme statistique.


## 6. Exécution du programme

### Prérequis
- Python 3.x
- Aucun module externe requis

### Lancement
Depuis le dossier `Code` :

```bash
python main.py
