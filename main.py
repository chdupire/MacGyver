#! /usr/bin/python3
# coding: utf-8

import classes


def main():
    affichage = classes.Affichage()
    affichage.afficher_labyrinthe()
    macGyver = classes.MacGyver(13, 1)


if __name__ == "__main__":
    main()

