#!/usr/bin/evn python33
#encoding=utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
import sys
sys.path.append("../")
from util.ReadStyleSheet import ReadStyleSheetFile

class StatusBarClickItem(QPushButton):
	"""docstring for StatusBarItem"""
	def __init__(self,parent,content):
		super(StatusBarClickItem, self).__init__(content)
		self.__parent__ = parent
		self.__content__ = content
		self.setFixedSize(100,20)

class StatusBarShowItem(QPushButton):
	"""docstring for StatusBarItem"""
	def __init__(self,parent,content):
		super(StatusBarShowItem, self).__init__(content)
		self.__parent__ = parent
		self.__content__ = content

class StatusBar(QWidget):
	"""docstring for StatusBar"""
	def __init__(self):
		super(StatusBar, self).__init__()

		self.setMaximumSize(8000,20)
		self.setMinimumSize(300,20)

		showItem = StatusBarShowItem(self,"status bar content")
		clickItem = StatusBarClickItem(self,"line: 1 , column: 1")
		clickItem.setFixedSize(150,20)
		clickItem1 = StatusBarClickItem(self,"Tab size: 4")
		clickItem2 = StatusBarClickItem(self,"python")

		self.__layout__ = QHBoxLayout()
		self.__layout__.setContentsMargins(0,0,0,0)
		self.__layout__.setSpacing(0)

		layout = QVBoxLayout()
		layout.addWidget(showItem)
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		layout.setAlignment(Qt.AlignLeft)
		self.__layout__.addLayout(layout)

		self.__layout__.addWidget(clickItem)
		self.__layout__.addWidget(clickItem1)
		self.__layout__.addWidget(clickItem2)

		self.setLayout(self.__layout__)

		self.resize(500,20)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = StatusBar()
	stylesheet = ReadStyleSheetFile("res/StatusBar.css")
	widget.setStyleSheet(stylesheet)
	widget.show()
	sys.exit(app.exec_())
	pass
		