from tkinter import *
from PIL import ImageTk, Image
from demineur_voltorbe import nb_of_voltorbe_in_column,nb_of_voltorbe_in_line,init_Voltorbe,init,print_game
import time
import pygame

file_calimero = 'Songs/calimero-trop-injuste.mp3'
file_applaudissement = 'Songs/CRWDCheer_Cris et applaudissements d ados 1 (ID 0236)_LS.mp3'
file_suspense = 'Songs/musique-a-suspense-bruitage-gratuit.mp3'

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file_suspense)
musique = pygame.mixer.music.play()


CONST_NOMBRE_DE_VOLTORBES = 8 
CONST_BLANK_CASE = 25 - CONST_NOMBRE_DE_VOLTORBES
#fenêtre de l'application
window = Tk()
plateau = init(5, 0)
init_Voltorbe(plateau, CONST_NOMBRE_DE_VOLTORBES)
#print_game(plateau, plateau)

#personalisation de la fenêtre
window.title("Demineur_volorbe")    #nom de la fenêtre
window.geometry("900x700")          #taille standard
window.minsize(900,700)             #taille minimale
window.maxsize(900,700)

icone = ImageTk.PhotoImage(Image.open("ui_application/voltorbepokemon_1.ico")) #changement de l'icone de l'application
window.tk.call('wm', 'iconphoto', window._w, icone)

case = ImageTk.PhotoImage(Image.open("ui_application/point_interrogation.jpg")) #image des cases de notre application
case_nothing = ImageTk.PhotoImage(Image.open("ui_application/nothing_calimero.png"))
case_bomb = ImageTk.PhotoImage(Image.open("ui_application/bomb_calimero.jpg"))
img_0 = ImageTk.PhotoImage(Image.open("ui_application/0.jpg"))
img_1 = ImageTk.PhotoImage(Image.open("ui_application/1.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("ui_application/2.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("ui_application/3.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("ui_application/4.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("ui_application/5.jpg"))



window.config(background = 'White')                           #Changer le fond de la fenêtre

#creer la frame
frame = Frame(window,bg='white')

#Titre de l'application
label_title = Label(window,text="Bienvenue sur l'application démineur Voltorbe!",font = ("Courrier",20),bg= 'white',fg = 'Black')
label_title.pack()


#Dessiner la grille

DIM_CASE = 100                                     #Dimension de chaque case
INTERSECTION_CASE = 5                              #Intersection entre chaque case (delimitation)
DIM_TOTAL = DIM_CASE + 2 * INTERSECTION_CASE       #Dimension Total d'une case

NB_LIGNE = 6                                       #Nombre de ligne de notre jeu
NB_COLONNE = 6                                     #Nombre de colonne de notre jeu

WIDTH_CANVAS = NB_COLONNE * DIM_TOTAL              #Largeur total du Canvas
HEIGHT_CANVAS = NB_LIGNE * DIM_TOTAL               #Hauteur total du Canvas


#Définition du Canvas et implémentation dans la fenêtre
canvas = Canvas(window, width = WIDTH_CANVAS, height = HEIGHT_CANVAS,background = 'Gray') 
canvas.pack()

#List qui permet de récuperer les élements qui couvrent les cases
List_cover = []

#Construction de la grille
for line in range(NB_LIGNE):
    L = []
    for colonne in range(NB_COLONNE): 
        centre =(colonne*DIM_TOTAL + DIM_TOTAL//2,line*DIM_TOTAL + DIM_TOTAL//2)
        if(line!= 0 or colonne != 0):
            if(line == 0 or colonne == 0):
                if(line == 0):
                    colonne-=1
                    nb_bomb = nb_of_voltorbe_in_column(plateau, colonne)
                    if(nb_bomb == 0):
                        canvas.create_image(centre,image = img_0)
                    elif(nb_bomb == 1):
                        canvas.create_image(centre,image = img_1)
                    elif(nb_bomb == 2):
                        canvas.create_image(centre,image = img_2)
                    elif(nb_bomb == 3):
                        canvas.create_image(centre,image = img_3)
                    elif(nb_bomb == 4):
                        canvas.create_image(centre,image = img_4)
                    elif(nb_bomb == 5):
                        canvas.create_image(centre,image = img_5)
                    colonne+=1
                else:
                    line-=1
                    nb_bomb = nb_of_voltorbe_in_line(plateau[line])
                    if(nb_bomb == 0):
                        canvas.create_image(centre,image = img_0)
                    elif(nb_bomb == 1):
                        canvas.create_image(centre,image = img_1)
                    elif(nb_bomb == 2):
                        canvas.create_image(centre,image = img_2)
                    elif(nb_bomb == 3):
                        canvas.create_image(centre,image = img_3)
                    elif(nb_bomb == 4):
                        canvas.create_image(centre,image = img_4)
                    elif(nb_bomb == 5):
                        canvas.create_image(centre,image = img_5)
                    line+=1
            else:
                #récupérer l'élément dans le plateau
                if(line != 0):
                    line-=1
                if(colonne!=0):
                    colonne-=1
                element = plateau[line][colonne]
                if(element == 'x'):
                    canvas.create_image(centre,image = case_bomb)
                else:
                    canvas.create_image(centre,image = case_nothing)
                cover = canvas.create_image(centre,image=case)
                L.append(cover)
                if(line+1 != 0):
                    line+=1
                if(colonne+1!=0):
                    colonne+=1
    List_cover.append(L)

#Fonction du click de souris

def on_click(event):
    global plateau              #plateau du jeu
    global CONST_BLANK_CASE
    X,Y = (event.x, event.y)    #Coordonnées du click
    COL = X//DIM_TOTAL         #Coordonnées du click dans le plateau du jeu
    LIGNE = Y//DIM_TOTAL
    #print(LIGNE,COL)            #imprime les coordonnées
    #print(plateau[LIGNE][COL])  #imprime l'objet qu'il y a dans la plateau a ces coordonnées

    #récupération de la case qui se trouve à l'endroit où on a clicker 
    if(COL!=0):
        COL-=1
    cover_clicked = List_cover[LIGNE][COL]
    canvas.delete(cover_clicked)

    if(LIGNE != 0):
        LIGNE-=1

    if(plateau[LIGNE][COL] == 'x'):
        new_window = Tk()
        for line in List_cover:
            for element in line:
                canvas.delete(element)
        end_message = Label(new_window,text="Vous avez perdu!",font = ("Courrier",25),bg= 'white',fg = 'Red')
        end_message.pack()
        pygame.mixer.music.load(file_calimero)
        pygame.mixer.music.play()
    else:
        if(CONST_BLANK_CASE == 1):
            new_window = Tk()
            window.destroy()
            end_message = Label(new_window,text="Vous avez gagné!",font = ("Courrier",25),bg= 'white',fg = 'Blue')
            end_message.pack()
            pygame.mixer.music.load(file_applaudissement)   
            pygame.mixer.music.play()

        else:
            CONST_BLANK_CASE-=1
            if(not(pygame.mixer.music.get_busy())):
                pygame.mixer.music.load(file_suspense)
                pygame.mixer.music.play()




#Interprétation du clique de souris
canvas.bind("<Button>",on_click)


#ajouter la frame a la fenêtre
#frame.pack(expand = YES)

#affichage de la fenêtre
window.mainloop()