#!/usr/bin/python
#encoding=utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MenuItem(QPushButton):
	"""docstring for MenuItem"""

	__menu__ = None
	__id__ = 0

	def __init__(self,content):
		super(MenuItem, self).__init__(content)

		self.__menu__ = QMenu(content)
		self.setMenu(self.__menu__)
		self.setFlat(True)

		"""
		newAct = QAction("&New", self, shortcut="ctrl+shift+alt+b",triggered=self.create)
		self.__menu__.addAction(newAct)

		tempemnu = QMenu("&Temp")
		tempaction = QAction("&Temp", self, shortcut="ctrl+b",triggered=self.create)
		tempemnu.addAction(tempaction)

		widgetaction = QAction("&Temp", self, shortcut="ctrl+d",triggered=self.create)
		self.addAction(widgetaction)

		newAct.setMenu(tempemnu)
		"""

	def getId(self):
		return self.__id__

	def setId(self,id):
		self.__id__ = id
		

	def create(self):
		print("ctrl+shift+alt+b")

class MenuBar(QWidget):
	"""docstring for MenuBar"""

	__id__ = 0
	__items__ = []

	def __init__(self):
		super(MenuBar, self).__init__()
		self.__initui__()

	def __initui__(self):
		self.layout = QHBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		self.layout.setSpacing(0)
		self.layout.setAlignment(Qt.AlignLeft)

		self.setMaximumSize(5000,20)
		self.setMinimumSize(500,20)

		self.setLayout(self.layout)

	def __getId__(self):
		self.__id__ += 1
		return self.__id__

	def addItem(self,item):
		"""

		ddItem(self,item)
		item must be the MenuItem

		"""
		item.setId(self.__getId__())
		self.layout.addWidget(item)
		self.__items__.append(item)

	def getItem(self,id):
		for i in self.__id__:
			if self.__items__[i].getId() == i:
				return self.__items__[i]

def create():
	print("create")

def createMenu(menuitem,widget):
	newAct = QAction("&New", menuitem, shortcut="ctrl+shift+alt+b",triggered=create)
	menuitem.menu().addAction(newAct)
	tempemnu = QMenu("&Temp")
	tempaction = QAction("&Temp", menuitem, shortcut="ctrl+b",triggered=create)
	tempemnu.addAction(tempaction)
	widgetaction = QAction("&Temp", menuitem, shortcut="ctrl+d",triggered=create)
	widget.addAction(widgetaction)
	newAct.setMenu(tempemnu)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	menubar = MenuBar()
	filemenu = MenuItem("&File")
	createMenu(filemenu,menubar)
	menubar.addItem(filemenu)
	sys.exit(app.exec_())
