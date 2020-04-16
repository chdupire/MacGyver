#! /usr/bin/python3
# coding: utf-8

import classes


def main():
    affichage = classes.Affichage(13, 1)
    affichage.afficher_labyrinthe()
    while True:
        choix = input("Entrez 'z':haut/'q':gauche/'s':bas/'d':droite  'fin' pour quitter")
        if choix == 'q':
            break
        if choix == 'z':




if __name__ == "__main__":
    main()

