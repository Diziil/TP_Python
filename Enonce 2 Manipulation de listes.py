import random

#liste1
def Ma_liste1(taille):
    liste1 = [random.randint(20, 120) for _ in range(taille)]
    return liste1

# liste2 impairs avec la liste de liste1
def Ma_Liste_Impairs(liste1):
    liste2 = [x for x in liste1 if x % 2 != 0]
    return liste2

#Afficher les deux listes dans un ordre décroissant
def afficher_listes_triees(liste1, liste2):
    liste1_triee = sorted(liste1, reverse=True)
    liste2_triee = sorted(liste2, reverse=True)
    print("Liste1 triée : ", liste1_triee)
    print("Liste2 triée : ", liste2_triee)

#Ajout de plusieurs entiers à liste1
def ajouter_elements(liste1, elements, position=None):
    if position is None:
        liste1.extend(elements)  # Ajouter à la fin de la liste
    else:
        for element in elements:
            liste1.insert(position, element)  # Ajouter à une position spécifique
    return liste1

#Suppression des occurrences d'un entier dans liste1
def supprimer_occurrences(liste1, valeur):
    if valeur not in liste1:
        print(f"La valeur {valeur} n'est pas présente dans la liste.")
    while valeur in liste1:
        liste1.remove(valeur)
    return liste1

# liste3 avec des éléments aléatoires de liste1 et liste2
def Ma_liste3(liste1, liste2):
    taille1 = min(3, len(liste1))  # Assurer qu'il y a assez d'éléments
    taille2 = min(3, len(liste2))
    liste3 = random.sample(liste1, k=taille1) + random.sample(liste2, k=taille2)
    return liste3


# Inverser la liste
def inverser_liste(liste):
    return liste[::-1]

# Eléments d'indices pairs de liste2 et éléments d'indices impairs de liste1
def separer_par_indices(liste1, liste2):
    l_pairs = [liste2[i] for i in range(0, len(liste2), 2)]  # Indices pairs de liste2
    l_impairs = [liste1[i] for i in range(1, len(liste1), 2)]  # Indices impairs de liste1
    return l_pairs, l_impairs

# Execution du script
def execution_du_script():
    print("Début de l'exécution du programme.")
    
    taille = 42
    liste1 = Ma_liste1(taille)
    print(f"Liste1 créée : {liste1}")

    liste2 = Ma_Liste_Impairs(liste1)
    print(f"Liste2 avec les entiers impairs de liste1 : {liste2}")

#Afficher des 2 listes triée
    print("Affichage des listes triées (décroissant) :")
    afficher_listes_triees(liste1, liste2)

#Ajout d'element en plus
    elements_a_ajouter = [2042, 122445, 454121, 4554251, 13658]
    liste1 = ajouter_elements(liste1, elements_a_ajouter)
    print(f"Liste1 après ajout d'éléments : {liste1}")

#Suppression d'une valeur dans liste1
    valeur_a_supprimer = int(input("Entrez une valeur à supprimer de liste1 : "))
    liste1 = supprimer_occurrences(liste1, valeur_a_supprimer)
    print(f"Liste1 après suppression des occurrences de {valeur_a_supprimer} : {liste1}")

#Liste3 avec des éléments aléatoires de liste1 et liste2
    liste3 = Ma_liste3(liste1, liste2)
    print(f"Liste3 avec éléments aléatoires de liste1 et liste2 : {liste3}")

# Inversion de la liste3
    liste3_inverse = inverser_liste(liste3)
    print(f"Liste3 inversée : {liste3_inverse}")

#Séparation des éléments par indices
    l_pairs, l_impairs = separer_par_indices(liste1, liste2)
    print(f"Liste des éléments d'indices pairs de liste2 : {l_pairs}")
    print(f"Liste des éléments d'indices impairs de liste1 : {l_impairs}")

    print("Fin de l'exécution du programme.")

execution_du_script()