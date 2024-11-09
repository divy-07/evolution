from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
print("Application closed")
