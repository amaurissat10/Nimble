##Imports
import random

##Fonctions et procédures
def newBoard(n,p): #Fonction qui retourne une liste à une dimension composée de n cases, elles-mêmes composées d'un nombre aléatoire de pions compris entre 0 et p
    list = [] #Liste vide
    for i in range (0,n):
        randomNumber = random.randint(0,p)
        list.append(randomNumber) #Ajoute un nombre aléatoire situé entre 0 et p à la liste
    return list

def display(board,n): #Procédure d'affichage du plateau de jeu
    for i in range(0,n):
        print("",board[i],"|",end="") #Affiche tous les éléments de board séparés par un "|"
    print("\n"+"-"*(n*4)) #Affiche un nombre de "-" proportionnellement au nombre d'éléments
    for i in range(1,n+1):
        print("",i,"|",end="") #Affiche le numéro de chaque case du plateau de jeu
    print("")

def possibleSquare(board,n,i): #Fonction qui teste si une case contient au moins un pion déplaçable
    if  1<=i<n: #Vérifie que i est compris entre 1 et n-1
        if board[i] > 0:
            return True #Si la case comporte au moins 1 pion alors on retourne True
        else:
            return False
    else:
        return False #Renvoi False si i inférieur à 1 car tous les pions de la case d'indice 0 ne sont pas déplaçables

def selectSquare(board,n): #Fonction qui demande un nombre à l'utilisateur et qui va vérifier que la case associée au nombre demandé comporte un pion déplaçable
    pion = int(input("Entrez le numéro d'une case contenant un pion déplaçable : "))
    while possibleSquare(board,n,pion-1) == False: #Continuera à demander un nombre à l'utilisateur tant que la case entrée ne comporte pas de pion déplaçable
        pion = int(input("Entrez le numéro d'une case contenant un pion déplaçable : "))
    return pion

def possibleDestination(board,n,i,j): #Fonction qui teste si une case j peut accepter le déplacement d'un pion venant d'une case i
    if 0 <= j < n:
        if i > j: #Retourne True si la case j a un indice inférieur à celui de la case i
            return True
        else:
            return False
    else:
        return False

def selectDestination(board,n,i): #Fonction qui demande un nombre à l'utilisateur et qui va vérifier que la case associée au nombre demandé peut accepter le déplacement d'un pion venant d'une case i
    case = int(input("Entrez le numéro d'une case où vous souhaitez déplacer le pion : "))
    while possibleDestination(board,n,i,case) == False: #Continuera à demander un nombre à l'utilisateur tant que la case entrée ne peut pas accepter le déplacement d'un pion venant d'une case i
        case = int(input("Entrez le numéro d'une case où vous souhaitez déplacer le pion : "))
    return case

def move(board,n,i,j): #Procédure qui redéfinit les valeurs du tableau de jeu aux indices i et j en décrémentant i de 1 et en incémentant j de 1
    board[i-1] -= 1
    board[j-1] += 1

def lose(board,n): #Fonction qui vérifie que le plateau comporte au moins un pion qui peut être déplacé
    for i in range(1,n):
        possibleSq = possibleSquare(board,n,i) #PossibleSq prend la valeur True si la case d'indice i contient un pion déplaçable
        if possibleSq == True:
            return False #On retourne donc False car au moins une case du plateau contient un pion déplaçable
    return True   #On retourne la valeur de PossibleSq qui reste inchangée à False si aucune case du plateau ne contient de pion déplaçable

def nimble(n,p): #Procédure du jeu
    board = newBoard(n,p) #Appelle la fonction newBoard et stocke sa valeur dans board
    player = -1 #Appelle la fonction newBoard et stocke sa valeur dans board
    print("Bienvenue sur le jeu du Nimble !")
    while lose(board,n) == False: #Tant que la fonction Lose renvoie la valeur True on peut jouer
        display(board,n) #On appelle la fonction display qui affiche le plateau
        player += 1 #On change de joueur (au début du jeu, joueur est égal à -1, donc -1 + 1 = 0)
        print("C'est au joueur",(player%2)+1,"de jouer") #On affiche la numéro du joueur qui doit actuellement jouer, pour cela on prend le modulo à 2 du numéro du joueur
        i = selectSquare(board,n) #On stocke dans i la valeur de la fonction selectSquare
        j = selectDestination(board,n,i) #On stocke dans j la valeur de la fonction selectDestination
        move(board,n,i,j) #On appelle la fonction move pour déplacer le pion
    display(board,n) #Une fois sortis de la boucle, on affiche le plateau
    print("Le joueur",(player%2)+1,"a gagné !") #Et on annonce le joueur qui a gagné

##Appel de n,p et Nimble
n = int(input("Entrez le nombre de cases du plateau : ")) #On demande à l'utilisateur d'entrer un nombre qui constituera le nombre de cases du plateau
p = int(input("Entrez le nombre maximum de pions par case au démarrage : ")) #On demande à l'utilisateur d'entrer un nombre qui constituera le nombre de pions maximum qui peut comporter une case
nimble(n,p) #On appelle la procédure Nimble
