#!/usr/bin/python
#encoding=utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
import sys

class FileTreeViewer(QTreeWidget):
	"""docstring for FileTreeViewer"""
	def __init__(self):
		super(FileTreeViewer, self).__init__()
		self.__initui__()

	def __initui__(self):
		self.setHeaderHidden(True)
		headeritem = QTreeWidgetItem(None,QTreeWidgetItem.UserType)
		headeritem.setText(0,"File")
		headeritem.setText(1,"Sumary")
		#self.setHeaderItem(headeritem)
		root = QTreeWidgetItem(self,QTreeWidgetItem.UserType)
		root.setText(0,"Root")
		root_sibling = QTreeWidgetItem(self,QTreeWidgetItem.UserType)
		root_sibling.setText(0,"Root-Sidling")

		root_child1 = QTreeWidgetItem(root,QTreeWidgetItem.UserType)
		root_child1.setText(0,"Root-Child1")

		code_py = QTreeWidgetItem(root_child1,QTreeWidgetItem.UserType)
		code_py.setText(0,"Code.py")
		code_py.setIcon(0,QIcon(":/coder.png"))

		code_java = QTreeWidgetItem(root_child1,QTreeWidgetItem.UserType)
		code_java.setText(0,"Code.java")
		code_java.setIcon(0,QIcon(":/coder.png"))

		root_child2 = QTreeWidgetItem(root,QTreeWidgetItem.UserType)
		root_child2.setText(0,"Root-Child2")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = FileTreeViewer()
	widget.show()
	sys.exit(app.exec_())
	pass
		