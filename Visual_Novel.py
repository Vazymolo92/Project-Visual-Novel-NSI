from tkinter import *

class ArbreBinaire:
    """classe permetant de simuler un arbre binaire"""
    def __init__(self, val=None):
        self.valeur=val
        self.enfant_gauche=None
        self.enfant_droit=None
        
    def insert_gauche(self,valeur):
        if self.enfant_gauche==None:
            self.enfant_gauche=ArbreBinaire(valeur)
        else:
            arbre_gauche=ArbreBinaire(valeur)
            arbre_gauche.enfant_gauche=self.enfant_gauche
            self.enfant_gauche=arbre_gauche
            
    def insert_droit(self,valeur):
        if self.enfant_droit==None:
            self.enfant_droit=ArbreBinaire(valeur)
        else:
            arbre_droit=ArbreBinaire(valeur)
            arbre_droit.enfant_droit=self.enfant_droit
            self.enfant_droit=arbre_droit
            
    def get_valeur(self):
        return self.valeur
    
    def get_droit(self):
        return self.enfant_droit
    
    def get_gauche(self):
        return self.enfant_gauche
    
    def __str__(self):
        return f'({self.valeur},{self.enfant_gauche},{self.enfant_droit})' 
    
def binary_tree():
    """fonction créant un arbre binaire pour y implémenter l'histoire"""
    #sous la forme (background, storyline, choixA, choixB)
    racine=ArbreBinaire((16,"Amine se réveille sous les bruits sourds des bombardement nazis et fuit à toute vitesse, cependant il a oublié Billy","Demi-Tour", "On s'en fiche"))
    racine.insert_gauche((10,"Mais où allez vous le cherchez ?", "La cité voisine", "la maison"))
    racine.insert_droit((10,"Vous quittez les lieux mais les nazis vous attrape, vous êtes emprisonnés", None, None))

    demiTour=racine.get_gauche()
    demiTour.insert_gauche((15,"Vous atteignez la cité voisine, Andrew Tate chef de la rebellion vous propose de le rejoindre", "rejoindre la rebellion", "continuer en solo"))
    demiTour.insert_droit((6,"Vous arrivez à la maison mais celle-ci à est perquisitionné par les nazis", "coopérer", "résister"))
    
    rejoindreRebellion=racine.demiTour.get_gauche()
    rejoindreRebellion.insert_gauche((18,"Vous rejoignez la rebellion, on vous propose de participer à la prochaine opération", "participer", "rester au QG"))
    rejoindreRebellion.insert_droit((18,"Vous souhaitez partir mais Andrew ne pux pas vous laisser partir et vous élimine", None, None))
    
    return racine

def parcours(arbre):
    pass
    

def creation_fenetre():
    # Creer une 1ere fenetre
    window = Tk()

    textA="choiceA"
    textB="choiceB"
    storyline="Storyline"
    background=1

    # Personnaliser cette fenetre
    window.title("Jeu à Choix")
    window.geometry("540x720")
    window.minsize(540, 360)
    window.config(background='#7D9479')
    
    # Creer la frame
    frame=Frame(window, bg='#7D9479')

    # Creer 1er image (dans la frame)
    width = 256*2
    height = 192*2
    image = PhotoImage(file="background1.png")

    canvas = Canvas(frame, width=width, height=height, bg='black', bd=0, highlightthickness=0)
    canvas.create_image(width/2, height/2, image=image)
    canvas.grid(row=0, column=0, sticky=N)

    # Creer une sous-frame
    down_frame = Frame(frame, bg='#7D9479')

    # Ajouter 1er texte (dans la sous-frame)
    label_storyline = Label(down_frame, text=storyline, font=("Helvetica",15), bg='#7D9479', fg='black')
    label_storyline.pack()

    # Ajouter le bouton du choix A (dans la sous-frame)
    play_buttonA = Button(down_frame, text=textA, font=("Courrier",15), bg='#3C6036', fg='white')
    play_buttonA.pack()

    # Ajouter le bouton du choix B (dans la sous-frame)
    play_buttonB = Button(down_frame, text=textB, font=("Courrier",15), bg='#3C6036', fg='white')
    play_buttonB.pack()

    #Placer la sous-frame dans la frame principale
    down_frame.grid(row=1, column=0, sticky=S)

    # Afficher la Frame
    frame.pack(expand=YES)

    # Afficher
    window.mainloop()

