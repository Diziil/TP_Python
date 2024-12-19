 #Initialisation de ma chaine
def Ma_Chaine1(N):
    MaChaine = "abcdefghijklmnopqrstuvwxyz" * N
    return MaChaine

def afficher_machaine(MaChaine):
    print("Ma Chaine", MaChaine)


#Copie des 17 derniers caractères
def  copier_17_derniers_caractères(MaChaine): 
    TaChaine=MaChaine [-17:]
    return TaChaine

#Alertance miniscule MAJ
def minuscule_MAJUSCULE(MaChaine):
    m_M= ""
    for i, caracteres in enumerate(MaChaine):
        if i % 2 == 0:
            m_M += caracteres.lower()
        else:
            m_M += caracteres.upper()
    return m_M

#Chaine inversé
def ma_chaine_inversé (MaChaine):
    inverse = MaChaine [::-1]
    print ("Voici ma chaine inversée :", inverse)

#Création de la pyramide depuis TaChaine
def pyramide (TaChaine):
    for i in range (1, len(TaChaine)+1):
        print(TaChaine[:i].center(len(TaChaine)))

#Recherche sous chaine
def recherche_sous_chaine(TaChaine, longeur):
    if longeur > len(TaChaine):
        print("La longeur de la sous chaine est trop grande")
        return
    for i in range(len(TaChaine) - longeur + 1):
        sous_chaine = TaChaine[i:i + longeur]
        print(f"La longeur de sous chaine est {longeur}: {sous_chaine}")

def trie_TaChaine (TaChaine):
     TaChaine_liste = list(TaChaine)
     TaChaine_liste.sort()
     print("Trie de TaChaine:", "".join(TaChaine_liste))

def Application_Script():
     N = int(input ("Entrez un valeur (>=5):"))
     while N < 5:
        print ("N doit etre une valeur superieur ou égale à 5:")
        N = int(input ("Saisir un nombre entier superieur à 5:"))
     return N 
        
N = Application_Script ()

#Création de machaine
MaChaine = Ma_Chaine1 (N)

#Afficher Ma Chaine
afficher_machaine(MaChaine)

#Copier 17 dernier caractères
TaChaine = copier_17_derniers_caractères(MaChaine)

#Alternance
MaChaine_alternee = minuscule_MAJUSCULE (MaChaine)
print("Machaine Alernée :", MaChaine_alternee)

#Inverser machaine
ma_chaine_inversé(MaChaine)

#Pyramide
print("Voici ta pyramide faite depuis TaChaine :")
pyramide(TaChaine)

taille_sous_chaine = int(input("Saisir la taille de la sous chaine à chercher :"))
recherche_sous_chaine(TaChaine, taille_sous_chaine,)

trie_TaChaine(TaChaine)