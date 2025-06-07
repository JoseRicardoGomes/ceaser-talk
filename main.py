from PyQt6.QtWidgets import QApplication
import MainWindow
import sys

app = QApplication(sys.argv)

# Parent window
window = MainWindow.MainWindow()

# Child windows/items


# Visibility
window.show()

# Main exec sequence
sys.exit(app.exec())

