import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QHBoxLayout

def showKMeansMenu():
    layout = QHBoxLayout()
    layout.addWidget(uic.loadUi('uifiles/kmeans.ui'))
    window.frame.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("app.ui")
window.pbKMeans.clicked.connect(showKMeansMenu)

print(window.frame)


window.show()
app.exec()