#!/usr/bin/python3.3.5
#encoding=utf-8

from PyQt5.QtCore import *

def ReadStyleSheetFile(path):
	ssf = QFile(path)
	ssf.open(QFile.ReadOnly)
	stream = QTextStream(ssf)
	return stream.readAll()