from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from matplotlib.pyplot import margins 
from BukuTelefon import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection.py')
os.system('python CreateTable.py')

global id, nama, kelas, kota, telefon, email

# Users (id INT, Nama TEXT, kelas TEXT, Kota TEXT, Telefon TEXT, Email TEXT)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.pushButtonDAFTARClick()
        self.ui.pushButtonDAFTAR.clicked.connect(self.pushButtonDAFTARClick)
        self.ui.pushButtonSIMPAN.clicked.connect(self.pushButtonSIMPANClick)
        self.ui.pushButtonHAPUS.clicked.connect(self.pushButtonHAPUSClick)
        self.ui.pushButtonPERBARUI.clicked.connect(self.pushButtonPERBARUIClick)
        self.ui.tableWidgetDaftar.clicked.connect(self.ListOnClick) 
 
    def pushButtonClear(self):
        self.ui.lineEditID.clear()
        self.ui.lineEditNAMA.clear()
        self.ui.lineEditKELAS.clear()
        self.ui.lineEditKOTA.clear()
        self.ui.lineEditTELEFON.clear()
        self.ui.lineEditEMAIL.clear()

    def ListOnClick(self): 
        self.ui.lineEditID.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 0).text())
        self.ui.lineEditNAMA.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 1).text())
        self.ui.lineEditKELAS.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 2).text())
        self.ui.lineEditKOTA.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 3).text())
        self.ui.lineEditTELEFON.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 4).text())
        self.ui.lineEditEMAIL.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 5).text())
 
    def pushButtonSIMPANClick(self): 
        id = self.ui.lineEditID.text()
        nama = self.ui.lineEditNAMA.text()
        kelas = self.ui.lineEditKELAS.text()
        kota = self.ui.lineEditKOTA.text()
        telefon = self.ui.lineEditTELEFON.text()
        email = self.ui.lineEditEMAIL.text()

        try:
            self.conn = sql.connect("BukuTelefon.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO Users VALUES (?,?,?,?,?,?)",(id,nama,kelas,kota,telefon,email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is added successfully to the database.')
        except Exception:
            print('Error', 'Could not add student to the database.')
        
        self.pushButtonClear()
        self.pushButtonDAFTARClick()

    def pushButtonDAFTARClick(self):  
        self.ui.tableWidgetDaftar.clear()
        self.ui.tableWidgetDaftar.setColumnCount(6)
        self.ui.tableWidgetDaftar.setHorizontalHeaderLabels(('ID','Nama','Kelas','Kota','Telefon','Email'))
        self.ui.tableWidgetDaftar.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('BukuTelefon.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM Users"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tableWidgetDaftar.setRowCount(len(rows))
        
        for rowIndeks, rowData in enumerate(rows):
            for columnIndeks, columnData in enumerate (rowData):
                self.ui.tableWidgetDaftar.setItem(rowIndeks,columnIndeks,QTableWidgetItem(str(columnData))) 
    
    def pushButtonPERBARUIClick(self):  
        id = self.ui.lineEditID.text()
        nama = self.ui.lineEditNAMA.text()
        kelas = self.ui.lineEditKELAS.text()
        kota = self.ui.lineEditKOTA.text()
        telefon = self.ui.lineEditTELEFON.text()
        email = self.ui.lineEditEMAIL.text()

        try:
            self.conn = sql.connect("BukuTelefon.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE Users SET nama = ?, kelas = ?, kota = ?, \
                telefon = ?, email = ? WHERE id = ?",(nama,kelas,kota,telefon,email,id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is updated successfully to the database.')
        except Exception:
            print('Error', 'Could not update student to the database.')

        self.pushButtonClear()
        self.pushButtonDAFTARClick()

    def pushButtonHAPUSClick(self): 
        id = self.ui.lineEditID.text() 

        try:
            self.conn = sql.connect("BukuTelefon.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM Users WHERE id = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is deleted successfully from the database.')
        except Exception:
            print('Error', 'Could not delete student to the database.')
        
        self.pushButtonClear()
        self.pushButtonDAFTARClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()