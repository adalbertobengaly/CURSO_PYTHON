import sys

from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

from main_window import MainWindow

if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 100px')
    window.addWidgetToVLayout(label1)
    window.adjustFixedSize()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
