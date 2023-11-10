import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from display import Display
from info import Info
from buttons import ButtonsGrid
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from styles import setupTheme

if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
