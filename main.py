# coding: utf-8

import classes
import random


def main():
    loading = classes.Loading()
    loading.labyrinth_initialization()
    game = classes.GameManager(loading.labyrinth_list)
    game.loop()


if __name__ == "__main__":
    main()

