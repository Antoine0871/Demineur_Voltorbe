import random
import sys
import os

CONST_NOMBRE_DE_VOLTORBES = 12

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def init(longueur,val): #initialise une matrice de longueur "longueur" avec des valeurs "val"
    M = []
    for i in range(longueur):
        L = []
        for j in range(longueur):
            L.append(val)
        M.append(L)
    return M

def init_Voltorbe(M,nb): #initialise de façon aléatoire l'emplacement des volorbes
    while(nb>0):
        for i in range(len(M)):
            for j in range(len(M)):
                if(random.randint(1, 10) == 1):
                    if(M[i][j] != 'x' and nb != 0):
                        M[i][j] = 'x'
                        nb-=1

def nb_of_voltorbe_in_line(L): #renvoie le nombre de voltorbe dans la liste (ligne) donné
    count = 0
    for element in L:
        if(element == 'x'):
            count+=1
    return count

def nb_of_voltorbe_in_column(M,j): #renvoie le nombre de voltorbe dans la colonne j
    count = 0
    for i in range(len(M)):
        if(M[i][j]) == 'x':
            count+=1
    return count

def print_game(M, M_bomb):  #imprime le jeu 
    string_for_delimitate_top_and_bottom = " " #créé une ligne de tiret pour délimité le haut et le bas du jeu
    for i in range(42):
        string_for_delimitate_top_and_bottom += "-"
    print(string_for_delimitate_top_and_bottom)

    string_of_voltorbe_in_column = "      " #créé une ligne qui permet d'imprimé le nombre de voltorbe dans les colonnes
    for i in range(len(M[0])):
        string_of_voltorbe_in_column += "{" + str(nb_of_voltorbe_in_column(M_bomb, i)) + "}" + "   "
    print(string_of_voltorbe_in_column)

    for i in range (len(M)):                             #imprime la matrice & le nombre de voltorbe par lignes
        string = "{" + str(nb_of_voltorbe_in_line(M_bomb[i]))+ "}" + " |  "
        for j in M[i]:
            string += str(j) + "  *  "
        print(string + " | " + "{" + str(nb_of_voltorbe_in_line(M_bomb[i])) + "}")

    print(string_of_voltorbe_in_column)
    print(string_for_delimitate_top_and_bottom)


def reveal_case(M, M_solution,i,j):
    M[i][j] = M_solution[i][j]    

def where_do_you_want_to_play(i,j):
    while(j == -1 or i == -1):
            i = -1
            j = -1
            coordonnees = input(" where do you want to play ?")
            for letter in coordonnees:
                if(letter >='0' and letter <= '4'):
                    if(i == -1):
                        i = int(letter)
                    else:
                        j = int(letter)
    return i,j

def print_end_game(M,M_bomb):
    print_game(M, M_bomb)
    print_game(M_bomb,M_bomb)
    print("############################")
    print("BOOOOOMM vous avez perdu")
    print("############################")

def print_win_game():
    print("Vous avez GAGNER !!!")


def main():
    clearConsole()
    end_game = False
    M = init(5,'?')
    M_bomb = init(5,'0')
    init_Voltorbe(M_bomb, CONST_NOMBRE_DE_VOLTORBES)
    number_of_blank_case = 25 - CONST_NOMBRE_DE_VOLTORBES

    while(not(end_game) and number_of_blank_case != 0):
        print_game(M,M_bomb)
        #print_game(M_bomb,M_bomb)

        i,j = -1,-1
        i,j = where_do_you_want_to_play(i, j)
        reveal_case(M, M_bomb, i, j)

        if(M_bomb[i][j] == "x"):    #vous êtes tombé sur un voltorbe !
            end_game = True

        else:                       #sinon vous êtes tombé sur une case blanche et le jeu continue...
            number_of_blank_case -=1
        clearConsole()

    if(end_game == True):
        print_end_game(M, M_bomb)
    else:
        print_win_game()
