# coding: utf-8

import classes
import random


def main():
    loading = classes.Loading()
    loading.labyrinth_initialization()
    macgyver = classes.MacGyver([13, 1], loading.labyrinth_list)
    display = classes.Display(macgyver.coordinates, loading.labyrinth_list)
    display.macgyver_display()
    display.labyrinth_display()
    #game = classes.GameManager()
    #game.init_items(game.find_empty_square(loading.labyrinth_list))
    #item = classes.Item(loading.liste_labyrinthe)
    #item.initialisation_objets()
    #print(item.coordonnees_tube)
    while 1:
        print()
        choice = input("zqsd ou e pour quitter: ")
        if choice == 'e':
            break
        else:
            macgyver.move(choice)
            display.macgyver_display()
            display.labyrinth_display()


if __name__ == "__main__":
    main()

