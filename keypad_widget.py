# keypad_widget.py

from PySide6.QtCore import Signal # Crear señales personalizadas
from PySide6.QtWidgets import (
    QWidget, # Base para todos los widgets
    QPushButton, # Widget para botones
    QGridLayout # Organiza widgets en filas y columnas (como una tabla)
)

class Keypad(QWidget):
    """
    Widget compuesto para el teclado numérico básico de la calculadora
    Este widget crea y organiza los botones numéricos y el punto decimal.
    No contiene ninguna lógica de cálculo. Su única responsabilidad es
    notificar al mundo exterior qué botón fue presionado.
    Emite una señal 'button_pressed' con el texto del botón que fue presionado.
    """

    # Definir la señal personalizada que se emitirá al ser presionado el botón. Pasa un 'str' como argumento.
    button_pressed = Signal(str)

    def __init__(self):
        """Constructor del widget Keypad"""
        super().__init__()

        # Crear el layout de cuadrícula
        layout = QGridLayout()
        # Establecer el layout para este widget
        self.setLayout(layout)

        self._create_buttons(layout)

    def _create_buttons(self, layout):
        """Crea los botones y los añade al layout."""
        botones = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2),
            '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '1': (2, 0), '2': (2, 1), '3': (2, 2),
            '0': (3, 0), '.': (3, 1),
        }

        # Iterar sobre el diccionario
        for btn_text, pos in botones.items():
            # Crear el botón con su texto correspondiente
            btn = QPushButton(btn_text)
            # Añadir el botón al layout en la posición correcta
            layout.addWidget(btn, pos[0], pos[1])
            # Conectar la señal clicked de cada botón a un slot que emite nuestra señal personalizada
            btn.clicked.connect(lambda checked, text=btn_text: self.button_pressed.emit(text))