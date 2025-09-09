# calculator_gui.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QGridLayout
from keypad_widget import Keypad

class MainWindow(QMainWindow):
    """Ventana principal de la aplicación"""
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal (atributos básicos)
        self.setWindowTitle("Mi primera aplicación con PySide6")
        self.setGeometry(100, 100, 400, 200)  # x, y, width, height

        # Layout principal para organizar el display y el keypad
        main_layout = QGridLayout()

        # Crear el display (aún no terminado pero iria aquí)
        self.display = QLineEdit() # Widget para mostrar texto
        self.display.setReadOnly(True)  # Solo lectura, evitamos que el usuario escriba directamente
        main_layout.addWidget(self.display, 0, 0, 1, 4) # Añadir el display al layout en la fila 0, columna 0. Ocupa 1 fila de alto y 4 columnas de ancho.

        # Crear el keypad
        self.keypad = Keypad() # Instancia del widget Keypad
        self.keypad.button_pressed.connect(self.on_keypad_button_pressed) # Pasamos la referencia de la función al slot
        main_layout.addWidget(self.keypad, 1, 0, 4, 3) # Añadir el keypad al layout en la fila 1, columna 0. Ocupa 4 filas de alto y 3 columnas de ancho.

        # Crear los botones de operadores
        self._create_operator_buttons(main_layout)

        # Establecer el widget central y su layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout) # Área de contenido principal sobre la que se colocan los widgets
        self.setCentralWidget(central_widget)

    def _create_operator_buttons(self, layout):
        """Crea los botones de operadores y los añade al layout."""
        operadores = {
            '/': (1, 3), # Fila 1, Columna 3
            '*': (2, 3), # Fila 2, Columna 3
            '-': (3, 3), # Fila 3, Columna 3
            '+': (4, 3), # Fila 4, Columna 3
            '=': (5, 3), # Fila 5, Columna 3
        }
        for btn_text, pos in operadores.items():
            btn = QPushButton(btn_text)
            layout.addWidget(btn, pos[0], pos[1])
            # Conectamos la señal clicked a un slot (method) que maneje la lógica del operador
            btn.clicked.connect(self.on_operator_button_pressed)

    def on_keypad_button_pressed(self, button_text):
        """Slot que maneja la señal button_pressed del Keypad"""
        print(f"El keypad envió: {button_text}")
        # Actualizar el display con el texto del botón presionado
        self.display.insert(button_text) # Insertar el texto al final

    def on_operator_button_pressed(self):
        """Slot para manejar los botones de operadores"""
        button = self.sender() # Obtener el botón que envió la señal
        if isinstance(button, QPushButton):
            operator = button.text() # Obtener el texto del botón
            print(f"Operador presionado: {operator}")
            self.display.insert(f" {operator} ")  # Insertar el operador con espacios alrededor

if __name__ == "__main__":
    # 1. Crear la instancia Qt
    app = QApplication(sys.argv)

    # 2. Crear la ventana principal
    window = MainWindow()

    # 3. Elementos de la interfaz (widgets)
    # button = QPushButton("¡Haz clic aquí!")
    # window.setCentralWidget(button)

    # 4. Mostrar la ventana
    window.show()

    # 5. Ejecutar el loop de eventos
    sys.exit(app.exec())