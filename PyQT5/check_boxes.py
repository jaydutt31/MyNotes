from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("CheckkBoxes")
		self.resize(1280,720)
		layout = QVBoxLayout()
		check1 = QCheckBox("Pick up groceries")
		check1.toggled.connect(lambda :self.something_checked(check1))
		
		check2 = QCheckBox("Write code everyday")
		check2.toggled.connect(lambda: self.something_checked(check2))
		
		self.label = QLabel("You have not seleted anyhting")
		self.checked_stuff = []
		layout.addWidget(check1)
		layout.addWidget(check2)
		layout.addWidget(self.label)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	def something_checked(self, check):
		if check.isChecked() == False:
			self.checked_stuff = list(filter(lambda stuff: (stuff != check.text()), self.checked_stuff))

		#when its false
		else:
			self.checked_stuff.append(check.text())
		task_string = ''
		for task in self.checked_stuff:
			task_string += (task+"\n")


		self.label.setText(task_string)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()