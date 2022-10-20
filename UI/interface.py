# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ctypes import *
import os

path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'fractal'))

image__path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'))


fractal_functions = CDLL(path + '/fractal.so')


def generate_fractal():
    print('Generating fractal...')
    ui.pushButton.hide()
    ui.image_preview.hide()

    text = get_image_name()

    fractal_functions.generate_fractal(
        c_double(0.27085),
        c_double(0.27100),
        c_double(0.004640),
        c_double(0.004810),
        bytes("500", encoding='utf-8'),
        bytes("720", encoding='utf-8'),
        bytes(text, encoding='utf-8'),
    )
    ui.pushButton.setEnabled(True)
    ui.image_preview.show()
    ui.pushButton.show()

    ui.textEdit.clear()

    ui.image_preview.setStyleSheet(
        "background-image: url(" + text + ");")
    print('Done!')


def get_image_name():
    text = ui.textEdit.toPlainText()
    if text == '':
        text = 'pic.ppm'
    else:
        text = text + '.ppm'
    return text


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
        # on press enter generate the fractal
        self.textEdit.keyPressEvent = lambda event: generate_fractal() if event.key() == QtCore.Qt.Key_Return else QtWidgets.QTextEdit.keyPressEvent(
            self.textEdit, event)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(generate_fractal)

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
    # create a variable to save the file name
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.image_preview.hide()
    MainWindow.show()
    sys.exit(app.exec_())
