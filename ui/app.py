import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("app.ui")
window.show()
app.exec()

# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Data Mining Assignment')
#
# layout = QHBoxLayout()
# layout.addWidget(QPushButton('K-Means Clustering'))
# layout.addWidget(QPushButton('Agglomerative hierarchical clustering'))
#
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec())



