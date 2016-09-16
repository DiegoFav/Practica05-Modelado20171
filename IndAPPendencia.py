# -*- coding: utf-8 -*-
import sys
from datetime import date, timedelta
from PyQt4 import QtGui, QtCore 

class MexApp(QtGui.QWidget):
	
	#constructor de la clase MexApp
	def __init__(self):
		super().__init__()
		self.lay = QtGui.QVBoxLayout()
		self.label = QtGui.QLabel('ALGUNOS PERSONAJES:\n' 
									+'- Miguel Hidalgo\n'
									+'- Agustín de Iturbide\n'
									+'- José María Morelos\n'
									+'- Guadalupe Victoria')
		self.Binfo = QtGui.QPushButton('Aprietame...')
		
		self.setFixedSize(320, 250)
		self.move(500, 500)
		self.setWindowTitle('¡Viva México!')
		self.Binfo.resize(200, 100)
		self.label.setAlignment(QtCore.Qt.Alignment(0x0004))
		self.lay.addWidget(self.label)
		self.lay.addWidget(self.Binfo)
		
		self.setLayout(self.lay)
		self.Binfo.clicked.connect(self.calctime)
		self.show()
		
	#Método que calcula cuantos dias faltan para el siguiente 15 de sep
	def calctime(self):
		thoy = date.today()
		thasta = date(thoy.year, 9, 15)
		if thoy > thasta:
			thasta = date(thoy.year+1, 9, 15)
		diferencia = thasta-thoy
		numDias = diferencia.days	#sacamos los dias de la diferencia
		if numDias != 0:
			self.Binfo.setText('El día de la independencia es en:\n'+str(numDias)+' día(s)');
		else:
			self.Binfo.setText('¡Felíz día de la independencia!');

def main():
	app = QtGui.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('res/bandera.png'));
	ma = MexApp();
	return app.exec_()

sys.exit(main())
