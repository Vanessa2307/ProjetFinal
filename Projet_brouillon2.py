from tkinter import* 
from random import*


#Configuraton deuxième fenêtre#

def recuperation():
    P_1 = E_prenom_1.get()
    P_2 = E_prenom_2.get()
    L_prenom_1.place_forget()
    L_prenom_2.place_forget()
    E_prenom_1.place_forget()
    E_prenom_2.place_forget()
    B1.place_forget()
    L_astro_1= Label(text="Entrez le signe astrologique de nom 1:")
    L_astro_2= Label(text="Entrez le signe astrologique de nom 2:")
    L_astro_1.place(x=40,y=0)
    L_astro_2.place(x=40,y=50)
    E_astro_1=Entry(fenetre,width=20)
    E_astro_2=Entry(fenetre,width=20)
    B2= Button(fenetre,text="Valider",width=20,command=alea)
    
    L_astro_1.place(x=20, y=10)
    L_astro_2.place(x=20, y=50)
    B2.place(x=125, y=150)
    E_astro_1.place(x=255, y=10)
    E_astro_2.place(x=255, y=50)



#configuration du support#

fenetre = Tk()
fenetre.title('Jeu de compatibilite')
fenetre.configure(width=450,height=200,bg='#FFCCCC')

L_prenom_1=Label(fenetre,text="Entrez le nom 1:",fg='#CC0033',width=20)
L_prenom_2=Label(fenetre,text="Entrez le nom 2:",fg='#CC0033',width=20)
Prenom_1=StringVar()
Prenom_2=StringVar()
E_prenom_1=Entry(fenetre,width=20)
E_prenom_2=Entry(fenetre,width=20)
B1=Button(fenetre,text="Valider",width=20,command=recuperation)

L_prenom_1.place(x=50, y=10)
L_prenom_2.place(x=50, y=50

def alea():
    E_1 = E_astro_1.get()
    E_2 = E_astro_2.get()
    L_astro_1.place_forget()
    L_astro_2.place_forget()
    E_astro_1.place_forget()
    E_astro_2.place_forget()
    B2.place_forget()
    nb=randint(1,100)
    L5= Label(fenetre,text="Calcul du pourcentage en cours...",fg='black')
    L5.configure(text="Le pourcentage de compatibilite est de"+ str(nb)+'%')
    L5.place(x=100,y=50)
    B3= Button(fenetre,text="Quitter",width=10,command=fenetre.destroy)
    B3.place(x=150,y=100)


#main window
fenetre.mainloop()