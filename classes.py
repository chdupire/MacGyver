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


    def afficher_labyrinthe(self):
        fichier_labyrinthe = open("labyrinthe.txt", "r")
        lignes = fichier_labyrinthe.readlines()
        for countX in range(0, len(lignes)):
            if countX == self.abscisse_macgyver:
                # lire la ligne caractère par caractère
                for countY in range(0, len(lignes[countX])):
                    if countY == self.ordonnee_macgyver:
                        print('G', end='')
                    else:
                        print(lignes[countX][countY], end='')
            else:
                print(lignes[countX], end='')
        fichier_labyrinthe.close()


class GameManager:
    # importer les objets
    # boucle de jeu
    # Conditions de victoire/défaite
    pass




