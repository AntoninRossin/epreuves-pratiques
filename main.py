#Sujet 10

#Ex 1
def occurence(phrase):
    occu = {}
    for i in range(len(phrase)):
        if phrase[i] in occu.keys():
            occu[phrase[i]] += 1
        else:
            occu[phrase[i]] = 1
    return occu
test = "Hello World"
print(occurence(test))

#Ex 2

def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 = i1 + 1
        else:
            L12[i] = L2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        L12[i] = L1[i1]
        i1 = i1 + 1
        i = i+1
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i = i+1
    return L12

print(fusion([1,6,10],[0,7,8,9]))


#Caesar:

def caesar(mot,clef):
    alphabet_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = str()

    for i in range(len(mot)):
        lettre = mot[i].lower()
        if lettre == " ":
            result += " "
        elif alphabet_dict[lettre] + clef > len(alphabet):
            result += alphabet[alphabet_dict[lettre] + clef - len(alphabet)]
        else:
            result += alphabet[alphabet_dict[lettre] + clef]
    return result

mot = "Hello World"
print (caesar(mot,3))


#Sujet 18 palindromes.

#Ex 1:
def mini(releve,date):
    mini = releve[0]
    date_mini = date[0]
    for i in range(1,len(releve)):
        if releve[i] < mini:
            mini = releve[i]
            date_mini = date[i]
    return mini,date_mini

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(mini(t_moy, annees))

def inverse_chaine(chaine):
    result = str()
    for caractere in chaine:
        result = caractere + result
    return result
def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine("bac"))
print(est_palindrome("NSI"))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))

#sujet 19

def multiplication(n1,n2):
    result = 0
    nb_0 = 0
    if n1 < 0:
        n1 = -n1
        nb_0 += 1
    if n2 < 0:
        n2 = -n2
        nb_0 += 1
    for i in range(n2):
        result += n1
    if nb_0 ==1:
        result = -result
    return result

def multiplication2(n1,n2):
    result = 0
    if n1< 0:
        n1 = -n1
        for i in range(n1):
            result += n2
        result = -result
        return result
    for i in range(n1):
        result += n2
    return result


print(multiplication(3,5))
print(multiplication(-3,5))
print(multiplication(3,-5))
print(multiplication(-3,-5))
print(multiplication2(3,5))
print(multiplication2(-3,5))
print(multiplication2(3,-5))
print(multiplication2(-3,-5))

#Ex 2

def chercher(T,n,i,j):
    if i < 0 or j >= len(T):
        print("Erreur")
        return None
    if i > j:
        return None
    m = (i+j) // 2
    if T[m] < n:
        return chercher(T,n,i+1,j)
    elif T[m] > n:
        return chercher(T,n,i,j-1)
    else:
        return m
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10),
chercher([1,5,6,6,9,12],7,0,5),
chercher([1,5,6,6,9,12],9,0,5),
chercher([1,5,6,6,9,12],6,0,5))

#Ex1
def taille(arbre,lettre):
    fils = arbre[lettre]
    result = 1
    if fils[0] == "" and fils[1] == "":
        return result
    elif fils[0] == "":
        result +=  taille(arbre,fils[1])
        return result
    elif fils[1] == "":
        result += taille(arbre,fils[0])
        return result
    else:
        for i in range(2):
            result += taille(arbre, fils[i])
        return result

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],'H':['','']}


print(taille(a,"F"))

#Ex 2

def tri_iteratif(tab):
    for k in range(len(tab)-1, 0, -1):
        imax = k
        for i in range(0,imax):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k]:
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab

print(tri_iteratif([41, 55, 21, 18, 12, 6, 25]))



# SUjet 30 ex 1

def fusion(tab1,tab2):
    result = list()
    while len(tab1) != 0 or len(tab2) != 0:
        while tab1[0] < tab2[0]:
            result.append(tab1[0])
            tab1.pop(0)
        while tab2[0] < tab1[0]:
            result.append(tab2[0])
            tab2.pop(0)
        if tab1[0] == tab2[0]:
            result.append(tab1[0])
            result.append(tab2[0])
            tab1.pop(0)
            tab2.pop(0)
    if len(tab1) != 0:
        for i in range(len(tab1)):
            result.append(tab1[i])
    elif len(tab2) != 0:
        for i in range(len(tab2)):
            result.append(tab2[i])
    return result

print(fusion([3, 5], [2, 5]))


#Exercice 2

#Sujet 38 et 39:

#Ex 38.

def tri_selection(tab):
    for i in range(len(tab)):
        imin = i
        for j in range(i,len(tab)):
            if tab[j] < tab[imin]:
                imin = j
        if imin != i:
            tab[i],tab[imin] = tab[imin],tab[i]
    return tab

print(tri_selection([1,52,6,-9,12]))

#Ex2

from random import randint
def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0
    while nb_mystere != nb_test and compteur < 11 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ",nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre était ",nb_mystere)

#plus_ou_moins()

#Sujet 39

#Ex 1

def moyenne(tab):
    result = 0
    for i in range(len(tab)):
        result += tab[i]
    return result/len(tab)

def moyenne2(tab):
    return sum(tab)/len(tab)

def moyenne3(tab):
    result = 0
    i = 0
    while tab:
        result += tab.pop()
        i += 1
    return result/i


def affiche(dessin):
    ''' affichage d'une grille : les 1 sont repreente par
        des "*" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *",end="")
            else:
                print("  ",end="")
        print()


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque
       element de liste_depart'''
    liste_zoom = list()
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille,k):
    '''renvoie une grille ou les lignes sont zoomees k fois
       ET repetees k fois'''
    grille_zoom=[]
    for elt in grille:
        liste_zoom = zoomListe(elt,k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


affiche(coeur)
affiche(zoomDessin(coeur,3))

#Sujet 40

#Ex 1

def recherche(elt,tab):
    result = list()
    for i in range(len(tab)):
        if elt == tab[i]:
            result.append(i)
    return result
print(recherche(3, [3, 2, 1, 3, 2, 1]))

#Ex 2

def moyenne_(nom):
    if nom in resultats:
        notes = resultats[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note , coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients , 1 )
    else:
        return -1
resultats = {'Dupont':{'DS1' : [15.5, 4],
 'DM1' : [14.5, 1],
'DS2' : [13, 4],
'PROJET1' : [16, 3],
'DS3' : [14, 4]},
 'Durand':{'DS1' : [6 , 4],
 'DM1' : [14.5, 1],
'DS2' : [8, 4],
'PROJET1' : [9, 3],
'IE1' : [7, 2],
'DS3' : [8, 4],
 'DS4' :[15, 4]}}
print(moyenne_("Durand"))


"""

Ex NSI 

"""

#1.

"""

La fonction traitement écrite au tableau va renvoyer [5,4,2]

"""
def liste_vide():
    return list()
def est_vide(lst):
    if lst == []:
        return True
    return False
"""
def copie(lst):
    if est_vide(lst):
        return liste_vide()
    else:
        return ajoute(valeur(lst),copie(suite(list)))
"""


#3.

"""
def cherche_min(lst):
    result = valeur(lst)
    lst = suite(lst)
    while not est_vide(lst):
        if result > valeur(lst):
            result = valeur(lst)
        lst = suite(lst)

"""


"""
Sujet n14
"""

#Ex1

def correspond(mot,mot_a_trous):
    if len(mot) == len(mot_a_trous):
        for i in range(len(mot_a_trous)):
            if mot_a_trous[i] != "*":
                if mot[i] != mot_a_trous[i]:
                    return False
        return True
    return False

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'),correspond('AUTOMATIQUE', 'INFO*MA*IQUE'),correspond('INFORMATIQUE', 'INFO*MA*IQU*E'))

#Ex2

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    personne = 'A'
    N = len(plan)
    for i in range(N-1):
        if plan[personne] == "A":
            return False
        else:
            personne = plan[personne]
    return True

print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}),est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}))


"""
Sujet 15
"""

#Ex1

def nb_repetitions(elt,tab):
    result = 0
    for i in range(len(tab)):
        if tab[i] == elt:
            result += 1
    return result

print(nb_repetitions(5,[2,5,3,5,6,9,5]))

#Ex2

def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0:
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

print(binaire(0), binaire(77))

"""
Sujet 3
"""
#1.

def delta(tab):
    result = None
    if len(tab)>1:
        result = [tab[0]]
        for i in range(1,len(tab)):
            result.append(tab[i]-tab[i-1])
        return result
    elif len(tab) == 1:
        result = tab[0]
    return result
print(delta([1000, 800, 802, 1000, 1003]),delta([42]),delta([]))


class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = str()
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit)
    if e.est_une_feuille():
        return s

    return '(' + s + ')'

e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None),
'+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+',
Noeud(None, 1, None)))

print(expression_infixe(e))