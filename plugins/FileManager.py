#!/usr/bin/python
#coding=utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
import sys

class TreeWidget(QWidget):
	"""docstring for TreeWidget"""
	def __init__(self):
		super(TreeWidget, self).__init__()

def inputFilename(parent):
	dialog = QFileDialog(parent)
	dialog.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = TreeWidget()
	widget.show()
	inputFilename(widget)
	sys.exit(app.exec_())