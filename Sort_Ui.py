import sys,sqlite3
from sqlite3 import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Sort_Ui(object):
    def sort_name(self):
        conn = sqlite3.connect("Item.db")
        cur = conn.cursor()

        sql = "select * from NAME order by id ASC"        
        data = str(self.exe_query(sql))

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(data)
        msgBox.setWindowTitle("Sorted Data")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass
        
    def sort_fish(self):
        conn = sqlite3.connect("Item.db")
        cur = conn.cursor()

        sql = "select * from FISH order by id ASC"        
        data = str(self.exe_query(sql))
        
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(data)
        msgBox.setWindowTitle("Sorted Data")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def sort_number(self):
        conn = sqlite3.connect("Item.db")
        cur = conn.cursor()

        sql = "select * from NUMBER order by id ASC"        
        data = str(self.exe_query(sql))
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(data)
        msgBox.setWindowTitle("Sorted Data")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def sort_country(self):
        conn = sqlite3.connect("Item.db")
        cur = conn.cursor()

        sql = "select * from COUNTRY order by id ASC"        
        data = str(self.exe_query(sql))
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(data)
        msgBox.setWindowTitle("Sorted Data")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def sort_postal(self):
        conn = sqlite3.connect("Item.db")
        cur = conn.cursor()

        sql = "select * from POSTAL order by id ASC"        
        data = str(self.exe_query(sql))

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(data)
        msgBox.setWindowTitle("Sorted Data")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_1 = QtWidgets.QPushButton(Dialog)
        self.pb_1.setObjectName("pb_1")
        self.verticalLayout.addWidget(self.pb_1)
        self.pb_2 = QtWidgets.QPushButton(Dialog)
        self.pb_2.setObjectName("pb_2")
        self.verticalLayout.addWidget(self.pb_2)
        self.pb_3 = QtWidgets.QPushButton(Dialog)
        self.pb_3.setObjectName("pb_3")
        self.verticalLayout.addWidget(self.pb_3)
        self.pb_4 = QtWidgets.QPushButton(Dialog)
        self.pb_4.setObjectName("pb_4")
        self.verticalLayout.addWidget(self.pb_4)
        self.pb_5 = QtWidgets.QPushButton(Dialog)
        self.pb_5.setObjectName("pb_5")
        self.verticalLayout.addWidget(self.pb_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pb_1.clicked.connect(self.sort_name)
        self.pb_2.clicked.connect(self.sort_fish)
        self.pb_3.clicked.connect(self.sort_number)
        self.pb_4.clicked.connect(self.sort_country)
        self.pb_5.clicked.connect(self.sort_postal)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pb_1.setText(_translate("Dialog", "Sort Names"))
        self.pb_2.setText(_translate("Dialog", "Sort Fishes"))
        self.pb_3.setText(_translate("Dialog", "Sort Numbers"))
        self.pb_4.setText(_translate("Dialog", "Sort Countries"))
        self.pb_5.setText(_translate("Dialog", "Sort Postal Codes"))
    
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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Sort_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
