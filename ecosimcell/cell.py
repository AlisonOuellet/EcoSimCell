# Définir ce qu'est une cellule et ce qui lui arrive à chaque tour

# il s'agit du cerveau de la cellule

class Cell:
    def __init__(self, energy, position):
        self.energy = energy
        self.position = position
        self.age = 0
        self.division_threshold = 10
        self.max_age = 100
        
    def step(self):
        self.age += 1
        # vérifier si elle se déplace puis perdre de l'énergie
        # vérifier si elle consomme de la nourriture
        # vérifier si elle doit se diviser
        # vérifier si elle doit mourir
        # comportement face aux menaces
        # comportement de recherche de nourriture
        pass
