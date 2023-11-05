# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget,
                               QGridLayout)  # , QHBoxLayout, QVBoxLayout

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha linda janela!')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px; color: red;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px')


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')


@Slot()
def mk_slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def outro_slot(checked):
    print('Está marcado? ', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeiro_acao = primeiro_menu.addAction('Primeira ação')
primeiro_acao.triggered.connect(mk_slot_example(status_bar))

segunda_acao = primeiro_menu.addAction('Segunda ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao1.clicked.connect(terceiro_slot(segunda_acao))


window.show()
app.exec()  # o loop da aplicação
