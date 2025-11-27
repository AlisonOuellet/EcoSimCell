CELL_TYPES = {
    "Saccharomyces cerevisiae (Levure)": {
        "energy": 10,
        "division_threshold": 20,
        "max_age": 70,
        "speed": 0.2,
        "food_preference": "glucose",
        "division_mode": "budding",  # bourgeonnement
        "notes": "Eucaryote modèle, pousse rapidement sur glucose."
    },

    "Candida albicans": {
        "energy": 12,
        "division_threshold": 22,
        "max_age": 80,
        "speed": 0.25,
        "food_preference": "glucose",
        "division_mode": "budding/hyphal",
        "notes": "Peut changer de forme (levure ↔ filament). Pathogène opportuniste."
    },

    "Schizosaccharomyces pombe": {
        "energy": 11,
        "division_threshold": 25,
        "max_age": 90,
        "speed": 0.15,
        "food_preference": "glucose",
        "division_mode": "fission",  # scissiparité
        "notes": "Modèle du cycle cellulaire. Division parfaitement symétrique."
    },

    "Chlamydomonas reinhardtii (Algue unicellulaire)": {
        "energy": 15,
        "division_threshold": 30,
        "max_age": 100,
        "speed": 0.8,  # elle nage vraiment
        "food_preference": "acetate",
        "division_mode": "multiple fission",
        "notes": "Algue verte mobile (flagelles). Peut faire photosynthèse."
    },

    "Tetrahymena thermophila (Protozoaire mobile)": {
        "energy": 18,
        "division_threshold": 28,
        "max_age": 60,
        "speed": 1.5,  # c'est l'une des cellules eucaryotes unicellulaires les plus rapides
        "food_preference": "bacteria",
        "division_mode": "binary fission",
        "notes": "Protiste cilié très mobile. Étudié pour la membrane et la phagocytose."
    },

    "Amoeba proteus": {
        "energy": 20,
        "division_threshold": 35,
        "max_age": 120,
        "speed": 0.4,  # mouvement lent et fluide
        "food_preference": "particles",
        "division_mode": "binary fission",
        "notes": "Protiste célèbre pour ses pseudopodes et sa forme variable."
    }
}
