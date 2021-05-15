from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("CheckkBoxes")
		self.resize(1280,720)

		layout = QVBoxLayout()

		input_filed = QLineEdit()
		layout.addWidget(input_filed)
		input_filed.returnPressed.connect(lambda: print(input_filed.text()))


		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	
		



app = QApplication([])
window = MainWindow()
window.show()
app.exec()