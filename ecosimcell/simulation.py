# Défini les règles et comment tout avance dans le temps


        # si elle trouve de la nourriture, elle la consomme et gagne de l'énergie
if on_food():
    energy += 3
# si elle se divise, une nouvelle cellule est créée avec une partie de son énergie
if energy >= division_threshold:
    create_new_cell(energy // 2)
    energy = energy // 2
# si elle doit se déplacer, elle choisit une direction aléatoire et perd de l'énergie
if decide_to_move():
    move_randomly()
    energy -= 1
# si elle reste immobile, elle ne perd pas d'énergie
if not move():
    pass
# si elle meurt, elle est retirée de la simulation
if energy <= 0 or age >= max_age:
    die()

# si elle voit une menace, elle peut tenter de fuir ou de se défendre
if detect_threat():
    evade_or_defend()

# si elle quête de la nourriture, elle peut modifier son comportement pour en trouver plus
if energy < 4:
    # la cellule doit chercher de la nourriture, se dirige vers la case le plus proche avec de la nourriture
    # son énergie diminue de 1 par tour
    
# si elle interagit avec d'autres cellules, cela peut affecter son énergie ou son état
# si elle est dans une zone spéciale, cela peut affecter son comportement ou son énergie
# si elle subit des mutations, cela peut affecter ses caractéristiques ou son comportement
# si elle est affectée par des événements environnementaux, cela peut influencer son énergie ou son état
# si elle laisse une trace, cela peut attirer ou repousser d'autres cellules
# si elle communique avec d'autres cellules, cela peut influencer son comportement ou son état

# si elle explore son environnement, elle peut découvrir de nouvelles ressources ou dangers
    pass