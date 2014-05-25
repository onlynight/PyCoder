#!/usr/bin/python
#encoding=utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
import sys
sys.path.append("../")
from util.ReadStyleSheet import ReadStyleSheetFile

class FunctionButton(QPushButton):
	"""docstring for FunctionButton"""
	def __init__(self, content):
		super(FunctionButton, self).__init__(content)
		self.setMouseTracking(True)

	def mouseMoveEvent(self,event):
		self.setCursor(Qt.ArrowCursor)
		pass


class CloseButton(FunctionButton):
	"""docstring for CloseButton"""
	def __init__(self,content):
		super(CloseButton, self).__init__(content)

class MinButton(FunctionButton):
	"""docstring for CloseButton"""
	def __init__(self,content):
		super(MinButton, self).__init__(content)

class MaxButton(FunctionButton):
	"""docstring for CloseButton"""
	def __init__(self,content):
		super(MaxButton, self).__init__(content)

class ContextBarLabel(QLabel):
	def __init__(self,content):
		super(ContextBarLabel, self).__init__(content)

class ContextBar(QWidget):
	"""docstring for TitleBar"""

	__dragpos__ = None
	__label__ = None
	__onCloseListener__ = None
	__onMaxListener__ = None
	__onMinListener__ = None
	__onDoubleClickListener__ = None
	__onMouseMoveListener__ = None

	__move__ = False

	def __init__(self,parent,label):
		super(ContextBar, self).__init__()
		self.tlabel = label
		self.parent = parent

		self.__initui__()
		self.__layout__()

		self.setMaximumSize(100000,30)
		self.setMinimumSize(150,30)

		self.resize(1000,500)
		self.setMouseTracking(True)

	def __initui__(self):
		self.__label__ = ContextBarLabel(self.tlabel)
		font = QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(10)
		self.__label__.setFont(font)
		self.__label__.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)

		self.__min__ = MinButton("")
		self.__max__ = MaxButton("")
		self.__close__ = CloseButton("")
		self.__min__.setMaximumSize(30,30)
		self.__max__.setMaximumSize(30,30)
		self.__close__.setMaximumSize(30,30)

		self.__min__.clicked.connect(self.minEvent)
		self.__max__.clicked.connect(self.maxEvent)
		self.__close__.clicked.connect(self.closeEvent)

	def __layout__(self):
		self.__layout__ = QHBoxLayout()
		self.__layout__.addWidget(self.__label__)
		self.__layout__.addWidget(self.__min__)
		self.__layout__.addWidget(self.__max__)
		self.__layout__.addWidget(self.__close__)
		self.__layout__.setContentsMargins(0,0,0,0)
		self.__layout__.setSpacing(0)
		self.setLayout(self.__layout__)

	def mousePressEvent(self,event):
		self.__move__ = True
		self.__dragpos__ = event.globalPos() - self.parent.frameGeometry().topLeft()
		event.accept()

	def mouseReleaseEvent(self,event):
		self.__move__ = False
		pass

	def mouseMoveEvent(self,event):
		self.setCursor(Qt.ArrowCursor)
		if (self.__onMouseMoveListener__ != None) & (self.__move__==True):
			self.__onMouseMoveListener__(event.globalPos() - self.__dragpos__)

	def minEvent(self,event):
		if self.__onMinListener__ != None:
			self.__onMinListener__()

	def maxEvent(self,event):
		if self.__onMaxListener__ != None:
			self.__onMaxListener__()

	def closeEvent(self,event):
		if self.__onCloseListener__ != None:
			self.__onCloseListener__()

	def mouseDoubleClickEvent(self,event):
		if self.__onDoubleClickListener__ != None:
			self.__onDoubleClickListener__()

	def setOnCloseListener(self,listener):
			self.__onCloseListener__ = listener

	def setOnMaxListener(self,listener):
		self.__onMaxListener__ = listener

	def setOnMinListener(self,listener):
		self.__onMinListener__ = listener

	def setOnDoubleClickListener(self,listener):
		self.__onDoubleClickListener__ = listener

	def setOnMouseMoveListener(self,listener):
		self.__onMouseMoveListener__ = listener

	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	titlebar = ContextBar("label")
	titlebar.setStyleSheet(ReadStyleSheetFile("TitleBar.css"))
	sys.exit(app.exec_())