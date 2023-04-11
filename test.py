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
    
#arbre = ["Storyline","choixA","choixB",["storyA","choixC","ChoixD"],["storyB","choixE","ChoixF"]

arbuste = ArbreBinaire('A')
arbuste.insert_gauche('B')
arbuste.insert_droit('F')

B_node = arbuste.get_gauche() # on defini le noeud B et ses enfants
B_node.insert_gauche('C')
B_node.insert_droit('D')

C_node = B_node.get_gauche() # on defini le noeud C et son enfants
C_node.insert_droit('E')

F_node = arbuste.get_droit() # on defini le noeud F et ses enfants
F_node.insert_gauche('G')
F_node.insert_droit('H')

G_node = F_node.get_gauche() # on defini le noeud G et son enfants
G_node.insert_gauche('I')

H_node = F_node.get_droit() # on defini le noeud H et son enfants
H_node.insert_droit('J')


window = Tk()
window.title("Jeu a Choix")
window.geometry("540x720")

                     
global storyline
storyline = StringVar()
Label(window, textvariable=storyline,pady=10).pack()
storyline.set("Bienvenu dans la galaxy")

global frame
frame = Frame(window)
frame.pack(side="top")


def button_maker(textA, textB):
    global btnA
    global btnB
    btnA = Button(frame, text=textA, relief=GROOVE, width=5, command = lambda: choiceA())
    btnB = Button(frame, text=textB, relief=GROOVE, width=5, command = lambda: choiceB())
    btnA.pack(side="top")
    btnB.pack(side="bottom")

def choiceA():
    storyline.set(arbuste.get_valeur)
    btnA.destroy()
    btnB.destroy()
    button_maker(arbuste.get_droit, arbuste.get_gauche)
    
def choiceB():
    storyline.set(arbuste.get_valeur)
    btnA.destroy()
    btnB.destroy()
    button_maker(arbuste.get_gauche, arbuste.get_droit)
    
button_maker(arbuste.get_gauche, arbuste.get_droit)

window.mainloop()
