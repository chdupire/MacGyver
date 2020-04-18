#! /usr/bin/python3
# coding: utf-8

import classes


def main():
    macgyver = classes.MacGyver([13, 1])
    affichage = classes.Affichage(macgyver.coordonnees)
    affichage.initialisation_labyrinthe()
    affichage.ajout_position_macgyver()
    affichage.affichage_labyrinthe()
    while 1:
        print()
        choix = input("zqsd ou e pour quitter: ")
        if choix == 'e':
            break
        else:
            affichage.initialisation_labyrinthe()
            macgyver.deplacement(choix)
            affichage.ajout_position_macgyver()
            affichage.affichage_labyrinthe()


if __name__ == "__main__":
    main()

