# 1. Création et initialisation interactive de Caractéristique_PC
def Caractéristique_PC():
    My_PC = {}
    print("Veuillez entrer les informations pour le PC :")
    My_PC["Nom du poste"] = input("Nom du poste : ")  # Nouveau champ "Nom du poste"
    My_PC["Processeur"] = input("Processeur (ex: M1, Intel, AMD) : ")
    My_PC["Nombre de cœurs"] = int(input("Nombre de cœurs du processeur : "))  # Nouveau champ
    My_PC["RAM"] = int(input("Quantité de RAM (en Go) : "))
    My_PC["Stockage"] = int(input("Capacité de stockage (en Go) : "))
    My_PC["Carte graphique"] = input("Carte graphique (ex: NVIDIA, AMD) : ")
    My_PC["Système d'exploitation"] = input("Système d'exploitation (ex: Windows, Linux, MacOs) : ")
    return My_PC

# Afficher les clés de My_PC
def afficher_cle(my_pc):
    print("Les clés du dictionnaire sont :")
    for key in my_pc:
        print(key)

# Afficher les valeurs de My_PC
def afficher_valeur(my_pc):
    print("Les valeurs du dictionnaire sont :")
    for value in my_pc.values():
        print(value)

# Extraction des clés dans une liste
def extraction_cle(my_pc):
    return list(my_pc.keys())

# Extraction des valeurs dans une liste
def extraction_valeur(my_pc):
    return list(my_pc.values())

# Correction de la quantité de RAM
def correction_ram(my_pc):
    nouvelle_ram = int(input("Entrez la nouvelle quantité de RAM en Go : "))
    my_pc["RAM"] = nouvelle_ram
    print(f"La RAM a été mise à jour à {nouvelle_ram} Go.")

# Tri de My_PC selon la quantité de stockage
def trier_par_stockage(my_pc):
    sorted_pc = sorted(my_pc.items(), key=lambda x: x[1] if isinstance(x[1], int) else 0, reverse=True)
    print("Dictionnaire trié par la quantité de stockage :")
    for item in sorted_pc:
        print(item)

# Inverser deux paramètres du dictionnaire
def inverser_parametres(my_pc):
    param1 = input("Entrez le premier paramètre à inverser (ex: RAM, Stockage) : ")
    param2 = input("Entrez le deuxième paramètre à inverser (ex: RAM, Stockage) : ")

    if param1 in my_pc and param2 in my_pc:
        my_pc[param1], my_pc[param2] = my_pc[param2], my_pc[param1]
        print(f"Les paramètres {param1} et {param2} ont été inversés.")
    else:
        print("Erreur : Un ou les deux paramètres n'existent pas dans le dictionnaire.")

# Sauvegarde de My_PC dans un autre dictionnaire CP_MyPC
def sauvegarder_my_pc(my_pc):
    CP_MyPC = my_pc.copy()  # Sauvegarde une copie de My_PC
    print("Le dictionnaire a été sauvegardé dans CP_MyPC.")
    return CP_MyPC

# Afficher le PC le plus performant de My_PC
def afficher_pc_performant(my_pc):
    meilleur_pc = max(my_pc, key=lambda x: my_pc[x] if isinstance(my_pc[x], int) else 0)
    print(f"Le PC le plus performant a pour paramètre : {meilleur_pc} avec la valeur {my_pc[meilleur_pc]}.")

# Fonction principale
def Execution_Script():
    # Créer My_PC
    My_PC = Caractéristique_PC()

    # Afficher les clés de My_PC
    afficher_cle(My_PC)

    # Afficher les valeurs de My_PC
    afficher_valeur(My_PC)

    # Extraction des clés
    liste_cle = extraction_cle(My_PC)
    print("Liste des clés :", liste_cle)

    # Extraction des valeurs
    liste_valeur = extraction_valeur(My_PC)
    print("Liste des valeurs :", liste_valeur)

    # Correction de la RAM
    correction_ram(My_PC)

    # Tri de My_PC par stockage
    trier_par_stockage(My_PC)

    # Inverser deux paramètres
    inverser_parametres(My_PC)

    # Sauvegarde de My_PC
    CP_MyPC = sauvegarder_my_pc(My_PC)

    # Afficher le PC le plus performant
    afficher_pc_performant(My_PC)

# Exécuter le programme principal
if __name__ == "__main__":
    Execution_Script()
