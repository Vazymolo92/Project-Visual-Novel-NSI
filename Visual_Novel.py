from tkinter import *
import classe_arbre_binaire

# création d'un arbre pour acceuillir l'histoire sous la forme ["Storyline","Question", "ChoixA", "Choix"B]   

# Création de la racine de l'arbre
arbre = classe_arbre_binaire.ArbreBinaire(["Vous vous réveillez sous le fracas des bombardements.", "Que faire ?", "Demi-Tour", "On s'en fiche"])
arbre.insert_gauche(["Vous faites demi-tour mais vous ne voyez pas Billy.", "Où chercher ?", "Chercher à la maison", "Chercher à la cité"]) # B_node
arbre.insert_droit(['Vous arrivez à rentrer en France Victoire.', "Que faire ?", "Non", "Oui"]) # C_node

# Récupération du noeud B
B_node = arbre.get_gauche() 
B_node.insert_gauche(["Vous cherchez à la maison mais Billy n'y est pas.", "Que faire ?", "Continuer de chercher", "Aller à la cité"]) # D_node
B_node.insert_droit(["Vous décidez d'aller à la cité et retrouvez Billy dans un abri.", "Que faire ?", "Rester caché", "Sortir pour chercher de l'aide"]) # E_node

# Récupération du noeud C
C_node = arbre.get_droit()
C_node.insert_gauche(["Vous décidez de continuer seul et vous tombez sur un groupe de soldats ennemis.", "Que faire ?", "Fuir", "Attaquer"]) # F_node

# Récupération du noeud D et ajout des choix pour le noeud F
D_node = B_node.get_gauche()
D_node.insert_gauche(["Vous continuez de chercher mais en vain.", "Que faire ?", "Rentrer chez vous", "Aller à la cité"]) # F_node
D_node.insert_droit(["Vous décidez d'aller à la cité et croisez un groupe de résistants.", "Que faire ?", "Les rejoindre", "Continuer seul"]) # G_node

# Récupération du noeud G et ajout des choix pour le noeud H
G_node = D_node.get_droit()
G_node.insert_gauche(["Vous rejoignez les résistants et participez à une mission pour saboter les lignes ennemies.", "Que faire maintenant ?", "Rentrer chez vous", "Continuer à aider la résistance"]) # H_node
G_node.insert_droit(["Vous décidez de continuer seul et vous tombez sur un groupe de soldats ennemis.", "Que faire ?", "Fuir", "Attaquer"]) # I_node

# Récupération du noeud E et ajout des choix pour le noeud J
E_node = B_node.get_droit()
E_node.insert_gauche(["Vous décidez de rester caché mais les provisions s'épuisent.", "Que faire ?", "Sortir pour chercher de l'aide", "Continuer à attendre"]) # J_node
E_node.insert_droit(["Vous décidez de sortir pour chercher de l'aide et croisez un groupe de résistants.", "Que faire ?", "Les rejoindre", "Continuer seul"]) # K_node

# Récupération du noeud F et ajout des choix pour les noeuds G et H
F_node = C_node.get_gauche()
F_node.insert_gauche(["Vous réussissez à fuir et trouvez refuge dans une petite ville.", "Que faire ?", "Rejoindre la résistance", "Rester caché"]) # G_node
F_node.insert_droit(["Vous attaquez avec succès les soldats ennemis et continuez votre mission.", "Que faire ?", "Chercher de l'aide", "Continuer seul"]) # I_node

# Récupération du noeud G et ajout des choix pour les noeuds de fin de l'histoire
G_node = F_node.get_gauche()
G_node.insert_gauche(["Vous rejoignez la résistance et participez à plusieurs missions réussies.", None, None, None])
G_node.insert_droit(["Vous restez caché jusqu'à la fin de la guerre, mais avec des souvenirs traumatisants de la guerre.", None, None, None])

# Récupération du noeud H et ajout des fins pour les noeuds de fin de l'histoire
H_node = G_node.get_gauche()
H_node.insert_gauche(["Vous êtes finalement rentré chez vous, fier de votre contribution à la libération de votre pays.", None, None, None])
H_node.insert_droit(["Vous avez continué à aider la résistance jusqu'à la fin de la guerre.", None, None, None])

# Récupération du noeud I et ajout des fins pour les noeuds de fin de l'histoire
I_node = G_node.get_droit()
I_node.insert_gauche(["Vous avez réussi à fuir et êtes finalement rentré chez vous, mais avec des souvenirs traumatisants de la guerre.", None, None, None])
I_node.insert_droit(["Vous avez attaqué avec succès les soldats ennemis et êtes devenu un héros de la résistance.", None, None, None])

# Récupération du noeud J et ajout des fins pour les noeuds de fin de l'histoire
J_node = E_node.get_gauche()
J_node.insert_gauche(["Vous êtes finalement sorti pour chercher de l'aide et avez réussi à rejoindre la résistance.", None, None, None])
J_node.insert_droit(["Vous êtes resté caché jusqu'à la fin de la guerre, mais avec des souvenirs traumatisants de la guerre.", None, None, None])

# Récupération du noeud K et ajout des choix pour le noeud L
K_node = E_node.get_droit()
K_node.insert_droit(["Vous décidez de continuer seul et vous tombez sur un groupe de soldats ennemis.", "Que faire ?", "Fuir", "Attaquer"]) # L_node

# Récupération du noeud L et ajout des fins pour les noeuds de fin de l'histoire
L_node = K_node.get_droit()
L_node.insert_gauche(["Vous avez réussi à fuir et êtes finalement rentré chez vous, mais avec des souvenirs traumatisants de la guerre.", None, None, None])
L_node.insert_droit(["Vous avez attaqué avec succès les soldats ennemis et êtes devenu un héros de la résistance.", None, None, None])

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
