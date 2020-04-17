#! /usr/bin/python3
# coding: utf-8

import classes


def main():
    affichage = classes.Affichage((13, 1))
    liste = affichage.creation_liste_labyrinthe()
    liste_macgyver = affichage.ajout_position_macgyver(liste)
    affichage.affichage_labyrinthe(liste_macgyver)
    #while True:
     #   choix = input("Entrez 'z':haut/'q':gauche/'s':bas/'d':droite  'fin' pour quitter")
      #  if choix == 'q':
       #     break
        #if choix == 'z':


if __name__ == "__main__":
    main()

