#!/usr/bin/python
#coding=utf-8

"""
python 3.3.5 
PyQt5
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
import sys
from ui.ContentBar import ContextBar
from ui.Coder import Coder
from ui.Menu import *
from util.ReadStyleSheet import ReadStyleSheetFile
from ui.StatusBar import *
from ui.res.images import *
from ui.FileTreeViewer import FileTreeViewer

class PyCoder(QWidget):
	"""docstring for PyCoder"""

	__mousedown__ = False
	__maxed__ = False
	__border__ = 1

	def __init__(self):
		super(PyCoder, self).__init__()
		self.resize(1000,650)
		self.setWindowFlags(Qt.FramelessWindowHint)#FramelessWindowHint CustomizeWindowHint
		self.__setupUi__()
		self.setMouseTracking(True)

	def __setupUi__(self):

		self.setWindowIcon(QIcon(":/coder.png"))
		self.coder = Coder()
		self.menubar = MenuBar()
		self.createMenu()
		self.titlebar = ContextBar(self,"Coder")
		self.titlebar.setOnCloseListener(self.closeAction)
		self.titlebar.setOnMaxListener(self.maxEvent)
		self.titlebar.setOnMinListener(self.minEvent)
		self.titlebar.setOnDoubleClickListener(self.doubleClickEvent)
		self.titlebar.setOnMouseMoveListener(self.moveWindowEvent)
		self.statusbar = StatusBar()

		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(self.__border__,self.__border__,self.__border__,self.__border__)
		self.layout.setSpacing(0)

		self.splitter = QSplitter(self)
		#self.splitter.setFrameStyle(QFrame.NoFrame)
		self.splitter.setOrientation(Qt.Horizontal)
		sizes = [300,1000]

		listview = FileTreeViewer()
		self.splitter.addWidget(listview)
		self.splitter.addWidget(self.coder)
		self.splitter.setSizes(sizes)

		self.layout.addWidget(self.titlebar)
		self.layout.addWidget(self.menubar)
		#self.layout.addWidget(self.coder)
		self.layout.addWidget(self.splitter)
		self.layout.addWidget(self.statusbar)

		self.setLayout(self.layout)

	def createMenu(self):
		filemenu = MenuItem("&File")
		font = QFont()
		font.setFamily("微软雅黑 Light")
		font.setPointSize(10)
		filemenu.setFont(font)
		newAct = QAction("&New", filemenu, shortcut="ctrl+n",triggered=create)
		filemenu.menu().addAction(newAct)
		self.menubar.addItem(filemenu)

		tempemnu = QMenu("&Temp")
		tempaction = QAction("&Temp", self, shortcut="ctrl+f",triggered=create)
		tempemnu.addAction(tempaction)

		widgetaction = QAction("&Temp", self, shortcut="ctrl+d",triggered=create)
		self.addAction(widgetaction)

		newAct.setMenu(tempemnu)

	def mouseMoveEvent(self,event):
		pass

	def minEvent(self):
		self.showMinimized()

	def maxEvent(self):
		self.maxWindow()

	def doubleClickEvent(self):
		self.maxWindow()

	def closeAction(self):
		self.close()

	def moveWindowEvent(self,pos):
		self.move(pos)
		if self.__maxed__ == True:
			self.__maxed__ = False
			self.resize(self.__pos__.width(),self.__pos__.height())

	def maxWindow(self):
		if self.__maxed__ == False:
			self.__maxed__ = True
			self.__pos__ = self.frameGeometry()
			maxSize = QApplication.desktop().availableGeometry()
			self.move(0,0)
			self.resize(maxSize.width(),maxSize.height())
		else:
			self.__maxed__ = False
			self.resize(self.__pos__.width(),self.__pos__.height())
		
def loadStyleSheet():
	stylesheet = ""
	temp = ReadStyleSheetFile("ui/res/TitleBar.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/Coder.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/PyCoder.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/Scintilla.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/Scrollbar.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/Menu.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/Common.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/StatusBar.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/Tree.css")
	stylesheet += temp
	temp = ReadStyleSheetFile("ui/res/Splitter.css")
	stylesheet += temp
	return stylesheet

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = PyCoder()
	widget.setStyleSheet(loadStyleSheet())
	widget.show()
	sys.exit(app.exec_())
	pass