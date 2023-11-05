# Trabalhando com classes e herança no PySide6
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget,
                               QGridLayout)  # , QHBoxLayout, QVBoxLayout


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha linda janela!')

        # Botão
        self.botao1 = self.make_button('Botão 1')
        self.botao1.clicked.connect(self.segunda_acao_marcada)

        self.botao2 = self.make_button('Botão 2')

        self.botao3 = self.make_button('Botão 3')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro Menu')
        self.primeiro_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeiro_acao.triggered.connect(self.muda_menssagem_da_status_bar)

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.segunda_acao_marcada)
        self.segunda_acao.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_menssagem_da_status_bar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado? ', self.segunda_acao.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 40px; color: red;')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # o loop da aplicação
