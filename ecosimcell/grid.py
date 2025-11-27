# Définit le monde dans lequel les cellules vivent et interagissent
# 2D
# taille des populations, diversité génétique

# Gère la grille, la position des cellules, l'environnement (l'endroit qu'il y a de la nourriture et éventuellemnt ou il y a des obstacles, zones spéciales)

# un rectangle de taille fixes
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}  # position -> cellule
        self.food = set()  # positions avec de la nourriture
        self.special_zones = set()  # positions spéciales


# Qu'est-ce que l'environnement fait à chaque tour?
# 1. la nourriture peut repousser?
# 2. certaines zones sont plus riches?
# 3. tous restes fixes?