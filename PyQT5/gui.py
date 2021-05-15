from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("Buttons WIndow")
		self.resize(1280,720)
		#layout 
		layout = QVBoxLayout()

		btn1 = QPushButton("Button 1")
		btn2 = QPushButton("Button 2")
		self.label = QLabel("click  Button 1")
		font = self.label.font()
		font.setPointSize(40)
		self.label.setFont(font)
		self.label.setAlignment(Qt.AlignCenter)
		#add actions
		btn1.clicked.connect(self.btn_1_clicked)
		btn2.clicked.connect(self.btn_2_clicked)
		#add stuffs to a layout
		layout.addWidget(self.label)
		layout.addWidget(btn1)
		layout.addWidget(btn2)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
	def btn_1_clicked(self):
		self.label.setText("clicked btn1")

	def btn_2_clicked(self):
		self.label.setText("clicekd btn 2")




app = QApplication([])
window = MainWindow()
window.show()
app.exec()




