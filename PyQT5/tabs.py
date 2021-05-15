from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("CheckkBoxes")
		self.resize(1280,720)

		layout = QVBoxLayout()

		tabs = QTabWidget()
		tabs.setMovable(True)
		tabs.addTab(QLabel("THIS IS TAB 1\n\n"),'TAB 1')
		tabs.addTab(QLabel("THIS IS TAB 2\n\n"),'TAB 2')
		tabs.addTab(QLabel("THIS IS TAB 3\n\n"),'TAB 3')

		layout.addWidget(tabs)
		
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	
		



app = QApplication([])
window = MainWindow()
window.show()
app.exec()