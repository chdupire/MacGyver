from constantes import COTE


class Personnage:
    pass


class MacGyver:
    def __init__(self, abscisse, ordonnee):
        # l'origine est le coin supérieur gauche
        self.abscisse = abscisse
        self.ordonnee : ordonnee


class Gardien:
    pass


class Affichage:
    # Gestion de l'affichage du labyrinthe, des murs, du sol des objets et des personnages.
    def __init__(self, abscisse_macgyver, ordonnee_macgyver):
        self.abscisse_macgyver = abscisse_macgyver
        self.ordonnee_macgyver = ordonnee_macgyver

    def creation_liste_labyrinthe(self):
        """création d'une liste de liste pour représenter le labyrinthe"""
        liste_labyrinthe = [COTE][COTE]
        fichier_labyrinthe = open("labyrinthe.txt", "r")
        lignes = fichier_labyrinthe.readlines()
        for numero_ligne in range(0, COTE):
            for numero_colonne in range(0, COTE):
            for carac in ligne:




#def afficher_labyrinthe(self):
     #   fichier_labyrinthe = open("labyrinthe.txt", "r")
      #  lignes = fichier_labyrinthe.readlines()
       # for countY in range(0, len(lignes)):
        #    if countY == self.ordonnee_macgyver:
                # lire la ligne caractère par caractère
         #       for countX in range(0, len(lignes[countY])):
          #         if countX == self.abscisse_macgyver:
           #             print('G', end='')
           #         else:
            #            print(lignes[countY][countX], end='')
           # else:
            #    print(lignes[countY], end='')
        # fichier_labyrinthe.close()


class GameManager:
    # importer les objets
    # boucle de jeu
    # Conditions de victoire/défaite
    pass




