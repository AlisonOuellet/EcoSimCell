# Choix du scénario à exécuter
# 1. Effet de la distance entre deux cellules
# 2. Effet de la quantité de nourriture
# 3. Effet de la limite d'âge sur la cellule
# 4. Effet des menaces environnementales
# 5. Effet des mutations aléatoires
# 6. Effet de la communication entre cellules
# 7. Effet des traces laissées par les cellules
#
# Paramètres de départ
# - Nombre de cellules initiales
# - Distance minimale entre cellules
# - Énergie initiale moyenne
# - Quantité de nourriture initiale
# - Type de nourriture (lipides, sucres, protéines, glucose, etc.)
#
# Durée de la simulation
# - Nombre de steps à exécuter

import sys
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QDoubleSpinBox,
    QSpinBox,
    QPushButton,
    QMessageBox,
)


class SimulationView(QWidget):
    """
    Zone de visualisation de la simulation.
    Plus tard : dessiner les cellules, la nourriture, etc.
    """

    def __init__(self, world_width=100.0, world_height=100.0, parent=None):
        super().__init__(parent)
        self.world_width = world_width
        self.world_height = world_height
        self.setMinimumSize(300, 300)  # taille minimale de la zone de dessin

    def set_world_size(self, width, height):
        """Permet de mettre à jour la taille logique du monde."""
        self.world_width = width
        self.world_height = height
        self.update()  # redessiner

    def paintEvent(self, event):
        painter = QPainter(self)

        # Fond
        painter.fillRect(self.rect(), QColor(30, 30, 30))  # gris foncé

        # Marges intérieures
        margin = 20
        area = self.rect().adjusted(margin, margin, -margin, -margin)

        # Cadre du monde
        pen = QPen(QColor(200, 200, 200))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        painter.drawRect(area)


class EcoSimCellWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EcoSimCell – Configuration")
        self.setMinimumSize(900, 500)

        # Layout principal horizontal
        central_widget = QWidget()
        main_layout = QHBoxLayout()  # gauche = contrôles, droite = simulation
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 2) Zone de gauche : contrôles
        controls_widget = QWidget()
        controls_layout = QVBoxLayout()
        controls_widget.setLayout(controls_layout)

        # 3) Zone de droite : simulation
        self.sim_view = SimulationView(world_width=100.0, world_height=100.0)

        # Ajouter les 2 sections au layout principal
        main_layout.addWidget(controls_widget, 1)   # poids 1
        main_layout.addWidget(self.sim_view, 2)     # poids 2 = plus large

        # Choix du type de nourriture
        food_layout = QHBoxLayout()
        food_label = QLabel("Type de nourriture :")
        self.food_combo = QComboBox()
        self.food_combo.addItems(["Glucose", "Lipides", "Mélange simple", "Autre"])
        food_layout.addWidget(food_label)
        food_layout.addWidget(self.food_combo)
        controls_layout.addLayout(food_layout)

        # Distance minimale entre cellules
        distance_layout = QHBoxLayout()
        distance_label = QLabel("Distance minimale entre cellules :")
        self.distance_spin = QDoubleSpinBox()
        self.distance_spin.setRange(0.0, 1000.0)
        self.distance_spin.setSingleStep(0.5)
        self.distance_spin.setValue(5.0)
        distance_layout.addWidget(distance_label)
        distance_layout.addWidget(self.distance_spin)
        controls_layout.addLayout(distance_layout)

        # Nombre de cellules initiales
        cells_layout = QHBoxLayout()
        cells_label = QLabel("Nombre de cellules initiales :")
        self.cells_spin = QSpinBox()
        self.cells_spin.setRange(1, 1000)
        self.cells_spin.setValue(10)
        cells_layout.addWidget(cells_label)
        cells_layout.addWidget(self.cells_spin)
        controls_layout.addLayout(cells_layout)

        # Quantité de nourriture totale
        food_amount_layout = QHBoxLayout()
        food_amount_label = QLabel("Quantité totale de nourriture :")
        self.food_amount_spin = QSpinBox()
        self.food_amount_spin.setRange(0, 10000)
        self.food_amount_spin.setValue(100)
        food_amount_layout.addWidget(food_amount_label)
        food_amount_layout.addWidget(self.food_amount_spin)
        controls_layout.addLayout(food_amount_layout)

        # Bouton démarrer
        self.start_button = QPushButton("Lancer la simulation")
        self.start_button.clicked.connect(self.on_start_clicked)
        controls_layout.addWidget(self.start_button)

        # Info
        info_label = QLabel(
            "Configurez les paramètres, puis cliquez sur "
            "\"Lancer la simulation\".\n"
            "(Pour l'instant, ça affiche juste un résumé.)"
        )
        controls_layout.addWidget(info_label)

        # Étireur pour pousser les contrôles vers le haut
        controls_layout.addStretch()

    def on_start_clicked(self):
        """
        Fonction appelée quand l'utilisateur clique sur le bouton.
        Pour l'instant, on affiche simplement un résumé des choix.
        Plus tard, tu pourras lancer ta vraie simulation ici.
        """
        food_type = self.food_combo.currentText()
        min_distance = self.distance_spin.value()
        n_cells = self.cells_spin.value()
        food_amount = self.food_amount_spin.value()

        summary = (
            f"Type de nourriture : {food_type}\n"
            f"Distance minimale entre cellules : {min_distance}\n"
            f"Nombre de cellules initiales : {n_cells}\n"
            f"Quantité totale de nourriture : {food_amount}"
        )

        QMessageBox.information(self, "Configuration sélectionnée", summary)


def main():
    app = QApplication(sys.argv)
    window = EcoSimCellWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
