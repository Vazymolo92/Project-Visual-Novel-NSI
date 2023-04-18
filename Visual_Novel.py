from tkinter import *
import classe_arbre_binaire

# création d'un arbre pour acceuillir l'histoire sous la forme ["Storyline","Question", "ChoixA", "Choix"B]   

# Création de la racine de l'arbre
arbre = classe_arbre_binaire.ArbreBinaire(["POLOGNE 1940 : Vous vous réveillez sous le fracas des bombardements.", "Que faire ?", "Fuir", "Rassembler vos affaires"])
arbre.insert_gauche(["Vous partez en direction de l'Est Mais rencontrez un régiment Nazi.", "Que faire ?", "Les attaquer", "Essayer de ne pas se faire remarquer"]) # B_node
arbre.insert_droit(['Vous récuperez des soupes en conserves puis pliez bagages.', "Que faire ?", "Aller chercher votre ami", "Fuire seul"]) # C_node

# Récupération du noeud B
B_node = arbre.get_gauche() 
B_node.insert_gauche(["Vous attaquez les soldats et parvenez à récuperer un fusil.", "Continuer à combattre?", "Se rendre", "Continuer le combat"]) # D_node
B_node.insert_droit(["Vous essayez de passer innaperçu mais les nazis vous ont reperer.", "Que faire ?", "Se faire passer pour un russe", "Les insulter, après tout vous n'avez plus rien à perdre"]) # E_node

# Récupération du noeud C
C_node = arbre.get_droit()
C_node.insert_gauche(["Vous Partez vers la ville pour retrouver votre ami.", "Où chercher ?", "Sa maison", "La cité voisine"]) # F_node
C_node.insert_droit(["Vous n'avez aucun sens de l'amitié et décidez de faire cavalier seul.", "Par quel moyen allez vous fuir ?", "En bateau", "En train"]) # G_node

# Récupération du noeud D et ajout des choix pour le noeud F
D_node = B_node.get_gauche()
D_node.insert_gauche(["Les nazis vous capture et vous amène à leur colonel.", "Que faire ?", "Le supplier de vous épargner", "Se faire passer pour un tchetchene"]) # H_node
D_node.insert_droit(["Vous recevez une balle à l'épaule et battez en retraite, vous rencontrez un marchand.", "Que faire ?", "Lui voler ses médicaments", "Tenter de s'associer à lui"]) # I_node

# Récupération du noeud E et ajout des choix pour le noeud J
E_node = B_node.get_droit()
E_node.insert_gauche(["Vous bafouillez des sons russe, les Nazis prennent peur et vous laisse.", "Que faire ?", "Rejoindre un village", "Continuer votre chemin"]) # J_node
E_node.insert_droit(["Vous décidez de sortir pour chercher de l'aide et croisez un groupe de résistants.", "Que faire ?", "Les rejoindre", "Continuer seul"]) # K_node

# Récupération du noeud F et ajout des choix pour les noeuds G et H
F_node = C_node.get_gauche()
F_node.insert_gauche(["Vous réussissez à fuir et trouvez refuge dans une petite ville.", "Que faire ?", "Rejoindre la résistance", "Rester caché"]) # L_node
F_node.insert_droit(["Vous attaquez avec succès les soldats ennemis et continuez votre mission.", "Que faire ?", "Chercher de l'aide", "Continuer seul"]) # M_node

# Récupération du noeud G et ajout des choix pour les noeuds de fin de l'histoire
G_node = C_node.get_droit()
G_node.insert_gauche(["Vous rejoignez la résistance et participez à plusieurs missions réussies.", "FIN", None, None])
G_node.insert_droit(["Vous restez caché jusqu'à la fin de la guerre, mais avec des souvenirs traumatisants de la guerre.", "FIN", None, None])

# Récupération du noeud H et ajout des fins pour les noeuds de fin de l'histoire
H_node = D_node.get_gauche()
H_node.insert_gauche(["Vous êtes finalement rentré chez vous, fier de votre contribution à la libération de votre pays.", "FIN", None, None])
H_node.insert_droit(["En parlant tchechene vous vous êtes transformé en Super Saiyan et les avez tués.", "VICTOIRE", None])

# Récupération du noeud I et ajout des fins pour les noeuds de fin de l'histoire
I_node = D_node.get_droit()
I_node.insert_gauche(["Vous avez réussi à fuir et êtes finalement rentré chez vous, mais avec des souvenirs traumatisants de la guerre.", None, None, None])
I_node.insert_droit(["Vous avez attaqué avec succès les soldats ennemis et êtes devenu un héros de la résistance.", "FIN", None, None])

# Récupération du noeud J et ajout des fins pour les noeuds de fin de l'histoire
J_node = E_node.get_gauche()
J_node.insert_gauche(["Vous êtes finalement sorti pour chercher de l'aide et avez réussi à rejoindre la résistance.", "FIN", None, None])
J_node.insert_droit(["Vous êtes resté caché jusqu'à la fin de la guerre, mais avec des souvenirs traumatisants de la guerre.", "FIN", None, None])

# Récupération du noeud K et ajout des choix pour le noeud L
K_node = E_node.get_droit()
K_node.insert_droit(["Vous décidez de continuer seul et vous tombez sur un groupe de soldats ennemis.", "Que faire ?", "Fuir", "Attaquer"]) # L_node
K_node.insert_droit(["Vous trouvez un marchand d'arme.", "Que faire ?", "Le voler", "Attaquer"])

# Récupération du noeud L et ajout des fins pour les noeuds de fin de l'histoire
L_node = F_node.get_gauche()
L_node.insert_gauche(["Vous avez réussi à fuir et êtes finalement rentré chez vous, mais avec des souvenirs traumatisants de la guerre.", "VICTOIRE", None, None])
L_node.insert_droit(["Vous avez attaqué avec succès les soldats ennemis et êtes devenu un héros de la résistance.", "VICTOIRE", None, None])

# Création d'une fenêtre Tkinter
window = Tk()

# Définition du titre de la fenêtre
window.title("Jeu a Choix")

# Définition des dimensions de la fenêtre
window.geometry("540x720")

# Définition d'une zone de text histoire avec une variable pour la modifier           
global storyline
storyline = StringVar()
Label(window, textvariable=storyline,pady=10).pack()
storyline.set("Storyline")

# Définition d'une zone de text question avec une variable pour la modifier 
global question
question = StringVar()
Label(window, textvariable=question,pady=10).pack()
storyline.set("Question")

# Définition d'une frame pour acceuillir les boutons 
global frame
frame = Frame(window)
frame.pack(side="top")

#définition des boutons de choix
global btnA
global btnB
btnA = Button(frame, text="videA", relief=GROOVE, width=5)
btnB = Button(frame, text="videB", relief=GROOVE, width=5)

def jeu(arbre):
    """fonction permettant de parcourir l'arbre binaire et d'effectuer une partie"""
    global btnA
    global btnB
    btnA.destroy()
    btnB.destroy()
    storyline.set(arbre.get_valeur()[0])
    question.set(arbre.get_valeur()[1])
    if arbre.get_valeur()[1] != None and arbre.get_valeur()[2] != None:    
        btnA = Button(frame, text=arbre.get_valeur()[2], relief=GROOVE, width=20, command = lambda: jeu(arbre.get_gauche()))
        btnB = Button(frame, text=arbre.get_valeur()[3], relief=GROOVE, width=20, command = lambda: jeu(arbre.get_droit()))
        btnA.pack(side="top")
        btnB.pack(side="bottom")
        
jeu(arbre)

window.mainloop()
