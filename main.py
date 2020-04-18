#! /usr/bin/python3
# coding: utf-8

import classes


def main():
    chargement = classes.Chargement()
    chargement.initialisation_labyrinthe()
    macgyver = classes.MacGyver([13, 1])
    affichage = classes.Affichage(macgyver.coordonnees, chargement.liste)
    affichage.ajout_macgyver()
    affichage.affichage_labyrinthe()
    while 1:
        print()
        choix = input("zqsd ou e pour quitter: ")
        if choix == 'e':
            break
        else:
            affichage.effacer_macgyver()
            macgyver.deplacement(choix)
            affichage.ajout_macgyver()
            affichage.affichage_labyrinthe()


if __name__ == "__main__":
    main()

