import sys,sqlite3
from sqlite3 import Error
from App_Ui import * 
from Sort_Ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Mainwindow(QMainWindow):
    save_stat = "del"
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_click)
        self.ui.pushButton_2.clicked.connect(self.edit_click)
        self.ui.pushButton_3.clicked.connect(self.save_click)
        self.ui.pushButton_4.clicked.connect(self.save_click)
        self.ui.tableWidget.cellClicked.connect(self.cell_click)
        self.ui.pushButton_5.clicked.connect(self.Load)
        self.ui.pushButton_9.clicked.connect(self.close_click)
        self.ui.pushButton_8.clicked.connect(self.sort_click)
        self.Load()
        self.show

    def Load(self):
        self.ui.comboBox.clear()
        self.ui.lineEdit.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)

        self.cmbCate_Load()
        self.twg_Load()
        self.ui.lineEdit.clear()
        self.ui.comboBox.setCurrentIndex(-1)
    
    def cell_click(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.call_cmb()

    def sort_click(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Sort_Ui()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def close_click(self):
        quit()

    def add_click(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)
        self.ui.comboBox.setEnabled(True)
        self.save_stat = 'add'

    def edit_click(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)
        self.ui.comboBox.setEnabled(True)
        self.save_stat = 'edit'
        
    def cmbCate_Load(self):
        value = self.exe_query("select * from Cate")
        if(len(value)>0):
            for i in range(len(value)):
                a = value[i]
                self.ui.comboBox.addItem(str(a[1]),str(a[0]))   

    def save_click(self):
        row = self.ui.tableWidget.currentRow()
        if self.save_stat == 'add' :
            sql = "insert into Item(name,cate) values('"+ str(self.ui.lineEdit.text()) +"','"+ str(self.ui.comboBox.currentData()) +"')"
        elif self.save_stat == 'edit' :
            sql = "update Item set name = '"+ str(self.ui.lineEdit.text()) +"',cate = '"+ str(self.ui.comboBox.currentData()) +"' where id = "
            sql += "'"+ self.ui.tableWidget.item(row,0).text() +"'"     
        else:
            msg = QMessageBox.question(
                self,'Confirm','Do you want to delete?',
                QMessageBox.Yes|QMessageBox.No,
                QMessageBox.No
            )
            if(msg == QMessageBox.Yes):
                sql = "delete from Item where id = '"+ self.ui.tableWidget.item(row,0).text() +"'"
            else:
                return

        if(
            self.ui.lineEdit.text() == "" or
            self.ui.comboBox.currentIndex() == -1
        ):
            msg = QMessageBox()
            msg.critical(
                self,'error','Please complete all information!',
                QMessageBox.Ok,
                QMessageBox.Ok
            )
        else:
            self.exe_query(sql)
        self.Load()

    def call_cmb(self):
        row = self.ui.tableWidget.currentRow()
        cb1 = self.ui.comboBox.findText(self.ui.tableWidget.item(row,2).text(),QtCore.Qt.MatchFixedString)
        self.ui.lineEdit.setText(self.ui.tableWidget.item(row,1).text())
        if cb1 >= 0:
            self.ui.comboBox.setCurrentIndex(cb1)
        self.save_stat = "del"

    def twg_Load(self):
        sql = "select b.id,b.name,c.name from Item b left join Cate c on b.cate = c.id"
        data = self.exe_query(sql) 
        self.ui.tableWidget.setRowCount(len(data)) 
        for i,row in enumerate(data):     
            for j,val in enumerate(row):       
                self.ui.tableWidget.setItem(i, j,QtWidgets.QTableWidgetItem(str(val)))    

    def exe_query(self,sql):
        try:
            conn = sqlite3.connect("Item.db")
            with conn:
                cur = conn.cursor()
                result = cur.execute(sql)
                data = result.fetchall()
        except Error as e:
            msg = QMessageBox()
            msg.critical(
                self, 'Error',  '%s' % e,
                QMessageBox.Ok, 
                QMessageBox.Ok
            )
        finally:
            conn.close()
            return data
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())
