# Défini les règles et comment tout avance dans le temps

# il coordone
# le temps : nb de steps / tours de la simulation
def run_simulation_step():
    pass

# l'appel aux cellules: pour chaque cellule, lui faire vivre un tour
def update_cells():
    pass

# le lien entre la cellule et l'environnement:
# cellule sur case avec nourriture : elle en gagne
# cellule qui veut se divisier: la simulation demande à la grille ou la nouvelle peut apparaitre
def cell_environment_interaction():
    pass

# À chaque tour, une cellule peut
# perdre de l'énergie
# gagner de l'énergie s'il y a de la nourriture
# se diviser si elle est ssez "riche"
# mourir si elle n'a plus d'énergie
