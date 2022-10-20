# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 618)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(918, 618))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(900, 600))
        self.frame.setMaximumSize(QtCore.QSize(900, 600))
        self.frame.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 490, 181, 91))
        self.pushButton.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 121))
        self.label.setStyleSheet("color: rgb(238, 238, 236);\n"
                                 "font: 28pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.image_preview = QtWidgets.QFrame(self.frame)
        self.image_preview.setGeometry(QtCore.QRect(309, 119, 541, 441))
        self.image_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_preview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_preview.setObjectName("image_preview")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 420, 211, 41))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Executar simulção"))
        self.label.setText(_translate("MainWindow", "Fractal de Mandelbrot"))
        self.textEdit.setPlaceholderText(
            _translate("MainWindow", "Insert the file name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())