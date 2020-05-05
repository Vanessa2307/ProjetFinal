from tkinter import *
from tkinter import ttk
from random import *

def acceuil_afficher():
    tout_effacer()

    L_nom.place(x=90,y=140)
    B1.place(x=150,y=250)

def acceuil_effacer():
    L_nom.place_forget()
    B1.place_forget()

#fenêtre des règles :


def regles_afficher():
    tout_effacer()
    
    L_regles_1.place(x=130, y=20)
    L_regles_2.place(x=20,y=70)
    L_regles_3.place(x=20,y=100)
    L_regles_4.place(x=20,y=120)
    L_regles_5.place(x=190,y=220)
    B2.place(x=150,y=250)

def regles_effacer():
    L_regles_1.place_forget()
    L_regles_2.place_forget()
    L_regles_3.place_forget()
    L_regles_4.place_forget()
    L_regles_5.place_forget()
    B2.place_forget()

def tout_effacer():
    acceuil_effacer()
    regles_effacer()
    information_effacer()

#fenêtre d'information :

def information_afficher():
    tout_effacer()

    listeCombo.place(x=20,y=20)
    E_prenom_1.place(x=40,y=100)
    E_prenom_2.place(x=40,y=120)

def information_effacer():
    listeCombo.place_forget()
    E_prenom_1.place_forget()
    E_prenom_2.place_forget()

    # E_prenom_1= Entry()

#fenêtre de support :
fenetre = Tk()
fenetre.title('Jeu de compatibilite')
fenetre.configure(width=500,height=300,bg='#FFCCCC')

#Elements de la fenetre d'acceuil
L_nom= Label(fenetre,text="Bienvenue sur le jeu de compatibilité amoureuse",fg='#CC0033',width=40)
B1=Button(fenetre,text="continuer",width=20,command=regles_afficher)

#Elements de la fenetre de règles
L_regles_1= Label (fenetre,text="Les règles du jeu :", fg='#CC0033',width=30)
L_regles_2= Label (fenetre, text="Les règles sont simples !", fg='#CC0033',width=20)
L_regles_3= Label(fenetre, text="Il faut entrer le prénom de deux personnes", fg='#CC0033', width=34)
L_regles_4= Label (fenetre,text="et leurs signes asstrologiques !",fg='#CC0033',width=25)
L_regles_5= Label (fenetre,text="à vous de jouer !",fg='#CC0033',width=15)
B2= Button(fenetre,text="continuer",width=20,command=information_afficher)

#Elements de la fenetre de jeu
L_prenom_1= Label (fenetre,text="Prénom 1 :",fg='#CC0033',width=20)
L_prenom_2= Label (fenetre,text="Prénom 2 :",fg='#CC0033',width=20)
E_prenom_1= Entry (fenetre,width=30)
E_prenom_2= Entry (fenetre,width=30)
listeSignes=["Gémeaux","Lion"]
listeCombo=ttk.Combobox(fenetre, values=listeSignes)
acceuil_afficher()

fenetre.mainloop()