import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QHBoxLayout

def showKMeansUi():
    widget = uic.loadUi('uifiles/kmeans.ui')
    layout = QHBoxLayout()
    layout.addWidget(widget)

    kValues = [str(i) for i in range(2, 10)]

    widget.comboBox.addItems(kValues)

    window.frame.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("app.ui")
window.pbKMeans.clicked.connect(showKMeansUi)

print(window.frame)


window.show()
app.exec()