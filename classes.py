import random


class Character:
    """Character creation"""
    def __init__(self, coordinates):
        """coordinates is a list [abscissa, ordered] with origin the upper left corner"""
        self.coordinates = coordinates


class MacGyver(Character):
    """MacGyver management"""
    def __init__(self, coordinates, labyrinth_list):
        super().__init__(coordinates)
        self.labyrinth_list = labyrinth_list

    def move(self, player_choice):
        """move the character according to the player's choice: (ZQSD) for Up/Down/Left/Right """
        if player_choice == 'z':
            line = self.labyrinth_list[self.coordinates[1] - 1]
            if line[self.coordinates[0]] == ' ':
                self.coordinates[1] -= 1
        if player_choice == 'q':
            line = self.labyrinth_list[self.coordinates[1]]
            if line[self.coordinates[0] - 1] == ' ':
                self.coordinates[0] -= 1
        if player_choice == 's':
            line = self.labyrinth_list[self.coordinates[1] + 1]
            if line[self.coordinates[0]] == ' ':
                self.coordinates[1] += 1
        if player_choice == 'd':
            line = self.labyrinth_list[self.coordinates[1]]
            if line[self.coordinates[0] + 1] == ' ':
                self.coordinates[0] += 1


class Guardian(Character):
    pass


class Loading:
    """Loading text and image files"""
    def __init__(self):
        # The labyrinth is represented by a list of lists
        self.labyrinth_list = []

    def labyrinth_initialization(self):
        """Loading the list of lists from file labyrinth.txt"""
        labyrinth_file = open("labyrinth.txt", "r")
        lines = labyrinth_file.readlines()
        for line in lines:
            line = list(line.strip())
            self.labyrinth_list.append(line)
        labyrinth_file.close()


class Display:
    """Display management of labyrinth, walls, floor items and characters."""
    def __init__(self, macgyver_coordinates, labyrinth_list):
        # macgyver_coordinates is a tuple (abscissa, ordered) with origin the upper left corner
        self.macgyver_coordinates = macgyver_coordinates
        self.labyrinth_list = labyrinth_list

    def macgyver_display(self):
        """modify the list in order to add the macgyver positioon indicated by 'O' """
        # we start by erasing the old position
        for line in self.labyrinth_list:
            for i in range(15):
                if line[i] == 'O':
                    line[i] = ' '
        # then we add the new position
        line = self.labyrinth_list[self.macgyver_coordinates[1]]
        line[self.macgyver_coordinates[0]] = 'O'

    def labyrinth_display(self):
        """"display the labyrinth from the list"""
        for line in self.labyrinth_list:
            line = ''.join(line)
            print(line)


class GameManager:
    """Boucle du jeu, détermine les conditions de la victoire/défaite"""
    # importer les objets
    # boucle de jeu
    # Conditions de victoire/défaite
    # recommencer le jeu
    def find_empty_square(self, labyrinth_list):
        empty_list = []
        for x in range(15):
            for y in range(15):
                if labyrinth_list[y][x] == ' ':
                    empty_list.append([y, x])
        return empty_list

    def init_items(self, empty_list):
        positions = random.sample(empty_list, 3)


class Item:
    """Creation and management of the items: needle, plastic tube and ether"""
    def __init__(self,x, y):
        self.position = (x, y)



