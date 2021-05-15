from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("CheckkBoxes")
		self.resize(1280,720)

		grid = QStackedLayout()



		grid.addWidget(QLabel("stuff1"))
		grid.addWidget(QLabel("stuff1"))
		grid.addWidget(QLabel("stuff1"))
		
		widget = QWidget()
		widget.setLayout(grid)
		self.setCentralWidget(widget)

	
		



app = QApplication([])
window = MainWindow()
window.show()
app.exec()