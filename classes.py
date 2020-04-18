class Personnage:
    """Création des personnages?"""
    def __init__(self, coordonnees):
        """Coordonnees est un tuple (abscisse, ordonnee) avec pour origine le coin supérieur gauche"""
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
        """coordonnees_macgyver est un tuple (abscisse, ordonnee) avec pour origine le coin supérieur gauche"""
        self.coordonnees_macgyver = coordonnees_macgyver

    def creation_liste_labyrinthe(self):
        """création d'une liste de chaine de caractères pour représenter le labyrinthe"""
        liste_labyrinthe = []
        fichier_labyrinthe = open("labyrinthe.txt", "r")
        ligne = fichier_labyrinthe.readline()
        liste_ligne = list(ligne)
        liste_labyrinthe.append(liste_ligne)
        while ligne:
            ligne = fichier_labyrinthe.readline()
            liste_ligne = list(ligne)
            liste_labyrinthe.append(liste_ligne)
        fichier_labyrinthe.close()
        return liste_labyrinthe

    def ajout_position_macgyver(self, liste):
        """modifie la liste afin d'ajouter la position de macgyver désigné par 'H' """
        ligne = liste[self.coordonnees_macgyver[1]]
        caractere = ligne[self.coordonnees_macgyver[0]]
        if caractere == ' ':
            ligne[self.coordonnees_macgyver[0]] = 'H'
        return liste

    def affichage_labyrinthe(self, liste):
        """"affiche le labyrinthe à partir d'une liste de chaines de caractère"""
        for ligne in liste:
            for carac in ligne:
                print(carac, end='')


class GameManager:
    # importer les objets?
    # boucle de jeu
    # Conditions de victoire/défaite
    pass




