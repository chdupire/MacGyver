class Personnage:
    """Création des personnages?"""
    def __init__(self, coordonnees):
        """Coordonnees est une liste [abscisse, ordonnee] avec pour origine le coin supérieur gauche"""
        self.coordonnees = coordonnees


class MacGyver(Personnage):
    """Gestion de MacGyver"""
    def __init__(self, coordonnees):
        super().__init__(coordonnees)

    def deplacement(self, commande):
        """déplace MacGyver en fonction du choix de l'utilisateur: (ZQSD) pour Haut/Bas/Gauche/Droite """
        if commande == 'z':
            self.coordonnes[1] -= 1
        if commande == 'q':
            self.coordonnees[0] -= 1
        if commande == 's':
            self.coordonnees[1] += 1
        if commande == 'd':
            self.coordonnees[0] += 1


class Gardien(Personnage):
    pass


class Affichage:
    """Gestion de l'affichage du labyrinthe, des murs, du sol des objets et des personnages."""
    def __init__(self, coordonnees_macgyver):
        # coordonnees_macgyver est un tuple (abscisse, ordonnee) avec pour origine le coin supérieur gauche
        self.coordonnees_macgyver = coordonnees_macgyver
        # Le labyrinthe est représenté par une liste de listes
        self.liste = []

    def initialisation_labyrinthe(self):
        """Initialisation de la liste de listes à partir du fichier labyrinthe.txt"""
        fichier_labyrinthe = open("labyrinthe.txt", "r")
        ligne = fichier_labyrinthe.readline()
        liste_ligne = list(ligne)
        self.liste.append(liste_ligne)
        while ligne:
            ligne = fichier_labyrinthe.readline()
            liste_ligne = list(ligne)
            self.liste.append(liste_ligne)
        fichier_labyrinthe.close()


    def ajout_position_macgyver(self):
        """modifie la liste afin d'ajouter la position de macgyver désigné par 'H' """
        ligne = self.liste[self.coordonnees_macgyver[1]]
        caractere = ligne[self.coordonnees_macgyver[0]]
        if caractere == ' ':
            ligne[self.coordonnees_macgyver[0]] = 'H'

    def affichage_labyrinthe(self):
        """"affiche le labyrinthe avec la position de MacGyver"""
        for ligne in self.liste:
            for carac in ligne:
                print(carac, end='')


class GameManager:
    """Boucle du jeu, détermine les conditions de la victoire/défaite"""
    # importer les objets?
    # boucle de jeu
    # Conditions de victoire/défaite
    pass




