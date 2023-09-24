# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_perkalian.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton,QFileDialog, QDialog
from PyQt5.QtGui import QPixmap, QColor, QImage, qRgb
from PyQt5.QtCore import Qt

class Ui_ao_NOT(QDialog):
    def setupUi(self, Ui_ao_NOT):
        Ui_ao_NOT.setObjectName("Ui_ao_NOT")
        Ui_ao_NOT.resize(1234, 924)
        self.Img1 = QtWidgets.QLabel(Ui_ao_NOT)
        self.Img1.setGeometry(QtCore.QRect(10, 80, 601, 411))
        self.Img1.setFrameShape(QtWidgets.QFrame.Box)
        self.Img1.setText("")
        self.Img1.setObjectName("Img1")
        self.Img2 = QtWidgets.QLabel(Ui_ao_NOT)
        self.Img2.setGeometry(QtCore.QRect(620, 80, 601, 411))
        self.Img2.setFrameShape(QtWidgets.QFrame.Box)
        self.Img2.setText("")
        self.Img2.setObjectName("Img2")
        self.LbOuput = QtWidgets.QLabel(Ui_ao_NOT)
        self.LbOuput.setGeometry(QtCore.QRect(310, 500, 601, 411))
        self.LbOuput.setFrameShape(QtWidgets.QFrame.Box)
        self.LbOuput.setText("")
        self.LbOuput.setObjectName("LbOuput")
        self.btn_open = QtWidgets.QPushButton(Ui_ao_NOT)
        self.btn_open.setGeometry(QtCore.QRect(210, 20, 251, 41))
        self.btn_open.setObjectName("btn_open")
        self.btn_open.clicked.connect(self.openImage)
        self.btn_progress = QtWidgets.QPushButton(Ui_ao_NOT)
        self.btn_progress.setGeometry(QtCore.QRect(490, 20, 251, 41))
        self.btn_progress.setObjectName("btn_progress")
        self.btn_progress.clicked.connect(self.prosesNOT)
        self.btn_save = QtWidgets.QPushButton(Ui_ao_NOT)
        self.btn_save.setGeometry(QtCore.QRect(770, 20, 251, 41))
        self.btn_save.setObjectName("btn_save")
        self.btn_save.clicked.connect(self.saveImage)

        self.retranslateUi(Ui_ao_NOT)
        QtCore.QMetaObject.connectSlotsByName(Ui_ao_NOT)

    def retranslateUi(self, Ui_ao_NOT):
        _translate = QtCore.QCoreApplication.translate
        Ui_ao_NOT.setWindowTitle(_translate("Ui_ao_NOT", "Form"))
        self.btn_open.setText(_translate("Ui_ao_NOT", "Open"))
        self.btn_progress.setText(_translate("Ui_ao_NOT", "Progress"))
        self.btn_save.setText(_translate("Ui_ao_NOT", "Save"))
    
    
    
    def openImage(self):
        if self.Img1.pixmap() is not None:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Open image","","Images(*.png *.jpg);;All Files(*)", options=options)
            if file_name:
                pixmap = QPixmap(file_name)
                self.Img2.setPixmap(pixmap)
                self.Img2.setScaledContents(True)
            
        else :
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Open image","","Images(*.png *.jpg);;All Files(*)", options=options)
            if file_name:
                pixmap = QPixmap(file_name)
                self.Img1.setPixmap(pixmap)
                self.Img1.setScaledContents(True)
    
    def prosesNOT(self):
        pixmap1 = self.Img1.pixmap()
        pixmap2 = self.Img2.pixmap()
        if pixmap1 and pixmap2 :
            img1 = pixmap1.toImage()
            img2 = pixmap2.toImage()

            if img1.size() != img2.size():
                self.LbOuput.setText("gambar harus memiliki ukuran yg sama")

            resul_keseluruhan = QImage(img1.size(), QImage.Format_RGB32)
            for x in range(img1.width()):
                for y in range(img1.height()):
                    pixel1 = QColor(img1.pixel(x,y))
                    pixel2 = QColor(img2.pixel(x,y))
            
                    # jumlah_r = min(pixel1.red() + pixel2.red(), 255)
                    # jumlah_g = min(pixel1.green() + pixel2.green(), 255)
                    # jumlah_b = min(pixel1.blue() + pixel2.blue(), 255)
                    r1, g1, b1, _ = pixel1.getRgb()
                    r2, g2, b2, _ = pixel2.getRgb()
                    r = r1 + r2
                    g = g1 + g2
                    b = b1 + b2

                    rf = 255-r
                    gf = 255-g
                    bf = 255-b
                    resul_keseluruhan.setPixel(x,y , qRgb(rf, gf, bf))

            jumlah_pixmap = QPixmap.fromImage(resul_keseluruhan)
            self.LbOuput.setPixmap(jumlah_pixmap)
            self.LbOuput.setScaledContents(True)
            self.displayed_pixmap = jumlah_pixmap
    
    def saveImage(self):
        pixmap = self.LbOuput.pixmap()
        if pixmap:
            saveFile = QtWidgets.QFileDialog()
            saveFile.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
            saveFile.setNameFilter("JPG File(*.jpg);; PNG FIles(*.png)")

            if saveFile.exec_() == QtWidgets.QDialog.Accepted:
                save_path = saveFile.selectedFiles()[0]
                self.displayed_pixmap.save(save_path)
                
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_ao_NOT = QtWidgets.QWidget()
    ui = Ui_ao_NOT()
    ui.setupUi(Ui_ao_NOT)
    Ui_ao_NOT.show()
    sys.exit(app.exec_())
