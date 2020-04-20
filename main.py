# coding: utf-8

import classes
import random


def main():
    chargement = classes.Chargement()
    chargement.initialisation_labyrinthe()
    macgyver = classes.MacGyver([13, 1], chargement.liste_labyrinthe)
    affichage = classes.Affichage(macgyver.coordonnees, chargement.liste_labyrinthe)
    affichage.ajouter_macgyver()
    affichage.affichage_labyrinthe()
    game = classes.GameManager()
    game.init_items(game.find_empty_square(chargement.liste_labyrinthe))

    exit()
    #item = classes.Item(chargement.liste_labyrinthe)
    #item.initialisation_objets()
    #print(item.coordonnees_tube)
    while 1:
        print()
        choix = input("zqsd ou e pour quitter: ")
        if choix == 'e':
            break
        else:
            macgyver.deplacement(choix)
            affichage.ajouter_macgyver()
            affichage.affichage_labyrinthe()


if __name__ == "__main__":
    main()

