from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyDialog(QDialog):
	def __init__(self, *args, **kwargs):
		super(MyDialog, self).__init__(*args, **kwargs)
		self.label = QLabel("NEW")
		self.resize(200,200)
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.label)

		#important
		self.setLayout(self.layout)


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("CheckkBoxes")
		self.resize(1280,720)

		layout = QVBoxLayout()

		btn = QPushButton("press me")
		btn.pressed.connect(self.dialog_handler)

		layout.addWidget(btn)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	def dialog_handler(self):
		dialog = MyDialog()
		dialog.label.setText("newer")
		dialog.exec()

	
		



app = QApplication([])
window = MainWindow()
window.show()
app.exec()