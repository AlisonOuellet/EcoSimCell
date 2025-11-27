class World:
    def __init__(self, width, height):
        # stocker la taille
        # stocker la liste des cellules
        # stocker la nourriture
        pass

    def add_cell(self, cell):
        # ajouter une cellule au monde
        pass

    def remove_cell(self, cell):
        # retirer une cellule
        pass

    def add_food_patch(self, position, amount):
        # ajouter de la nourriture
        pass

    def move_cell(self, cell, dx, dy):
        # modifier sa position + gérer les bords
        pass

    def get_food_near(self, position, radius):
        # renvoyer combien de nourriture il y a autour d’une position
        pass

    def consume_food(self, position, radius, amount):
        # retirer de la nourriture autour de la cellule quand elle mange
        pass
