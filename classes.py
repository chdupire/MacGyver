import random


class Personnage:
    """Création des personnages?"""
    def __init__(self, coordonnees):
        """Coordonnees est une liste [abscisse, ordonnee] avec pour origine le coin supérieur gauche"""
        self.coordonnees = coordonnees


class MacGyver(Personnage):
    """Gestion de MacGyver"""
    def __init__(self, coordonnees, liste_labyrinthe):
        super().__init__(coordonnees)
        self.liste_labyrinthe = liste_labyrinthe

    def deplacement(self, commande):
        """déplace MacGyver en fonction du choix de l'utilisateur: (ZQSD) pour Haut/Bas/Gauche/Droite """
        if commande == 'z':
            ligne = self.liste_labyrinthe[self.coordonnees[1] - 1]
            if ligne[self.coordonnees[0]] == ' ':
                self.coordonnees[1] -= 1
        if commande == 'q':
            ligne = self.liste_labyrinthe[self.coordonnees[1]]
            if ligne[self.coordonnees[0] - 1] == ' ':
                self.coordonnees[0] -= 1
        if commande == 's':
            ligne = self.liste_labyrinthe[self.coordonnees[1] + 1]
            if ligne[self.coordonnees[0]] == ' ':
                self.coordonnees[1] += 1
        if commande == 'd':
            ligne = self.liste_labyrinthe[self.coordonnees[1]]
            if ligne[self.coordonnees[0] + 1] == ' ':
                self.coordonnees[0] += 1


class Gardien(Personnage):
    pass


class Chargement:
    """Chargement des fichiers textes et images"""
    def __init__(self):
        # Le Labyrinthe est représenté par une liste de listes
        self.liste_labyrinthe = []

    def initialisation_labyrinthe(self):
        """Chargement de la liste de listes à partir du fichier labyrinthe.txt"""
        fichier_labyrinthe = open("labyrinthe.txt", "r")
        lignes = fichier_labyrinthe.readlines()
        for ligne in lignes:
            ligne = list(ligne.strip())
            self.liste_labyrinthe.append(ligne)
        fichier_labyrinthe.close()


class Affichage:
    """Gestion de l'affichage du labyrinthe, des murs, du sol des objets et des personnages."""
    def __init__(self, coordonnees_macgyver, liste_labyrinthe):
        # coordonnees_macgyver est un tuple (abscisse, ordonnee) avec pour origine le coin supérieur gauche
        self.coordonnees_macgyver = coordonnees_macgyver
        self.liste_labyrinthe = liste_labyrinthe

    def ajouter_macgyver(self):
        """modifie la liste afin d'ajouter la position de macgyver désigné par 'O' """
        # On commence par effacer l'ancienne position
        for ligne in self.liste_labyrinthe:
            for i in range(15):
                if ligne[i] == 'O':
                    ligne[i] = ' '
        # Puis on ajoute la nouvelle position
        ligne = self.liste_labyrinthe[self.coordonnees_macgyver[1]]
        ligne[self.coordonnees_macgyver[0]] = 'O'

    def affichage_labyrinthe(self):
        """"affiche le labyrinthe"""
        for ligne in self.liste_labyrinthe:
            ligne = ''.join(ligne)
            print(ligne)


class GameManager:
    """Boucle du jeu, détermine les conditions de la victoire/défaite"""
    # importer les objets?
    # boucle de jeu
    # Conditions de victoire/défaite
    pass


class Item:
    """Création et gestion des objets aiguille(A), éther(E), seringue(S), tube(T)"""
    def __init__(self, liste_labyrinthe):
        self.coordonnees_aiguille = [0, 0]
        self.coordonnees_ether = [0, 0]
        self.coordonnees_seringue = [0, 0]
        self.coordonnees_tube = [0, 0]
        self.liste_labyrinthe = liste_labyrinthe


    def initialisation_objets(self):
        """Dispose aléatoirement les objets dans le labyrinthe"""
        for coordonnees in [self.coordonnees_aiguille, self.coordonnees_ether, self.coordonnees_seringue,
                            self.coordonnees_tube]:
            while coordonnees == [0, 0]:
                abscisse = random.randrange(1, 15)
                ordonnee = random.randrange(1, 15)
                if self.liste_labyrinthe[ordonnee][abscisse] == ' ':
                    coordonnees = [abscisse, ordonnee]
                    print('coucou')


