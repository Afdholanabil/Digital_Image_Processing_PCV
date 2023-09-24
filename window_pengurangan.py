# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_pengurangan.ui'
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


class Ui_ao_pengurangan(QDialog):
    def setupUi(self, ao_pengurangan):
        ao_pengurangan.setObjectName("ao_pengurangan")
        ao_pengurangan.resize(1236, 928)
        self.Img1 = QtWidgets.QLabel(ao_pengurangan)
        self.Img1.setGeometry(QtCore.QRect(10, 90, 601, 381))
        self.Img1.setFrameShape(QtWidgets.QFrame.Box)
        self.Img1.setAlignment(QtCore.Qt.AlignCenter)
        self.Img1.setObjectName("Img1")
        self.Img2 = QtWidgets.QLabel(ao_pengurangan)
        self.Img2.setGeometry(QtCore.QRect(620, 90, 601, 381))
        self.Img2.setFrameShape(QtWidgets.QFrame.Box)
        self.Img2.setAlignment(QtCore.Qt.AlignCenter)
        self.Img2.setObjectName("Img2")
        self.LOutput = QtWidgets.QLabel(ao_pengurangan)
        self.LOutput.setGeometry(QtCore.QRect(320, 480, 601, 441))
        self.LOutput.setFrameShape(QtWidgets.QFrame.Box)
        self.LOutput.setText("")
        self.LOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.LOutput.setObjectName("LOutput")
        self.btn_proses = QtWidgets.QPushButton(ao_pengurangan)
        self.btn_proses.setGeometry(QtCore.QRect(500, 20, 241, 41))
        self.btn_proses.setObjectName("btn_proses")
        self.btn_proses.clicked.connect(self.prosesPengurangan)
        self.btn_open = QtWidgets.QPushButton(ao_pengurangan)
        self.btn_open.setGeometry(QtCore.QRect(220, 20, 241, 41))
        self.btn_open.setObjectName("btn_open")
        self.btn_open.clicked.connect(self.loadImage2)
        self.btn_save = QtWidgets.QPushButton(ao_pengurangan)
        self.btn_save.setGeometry(QtCore.QRect(780, 20, 241, 41))
        self.btn_save.setObjectName("btn_save")
        self.btn_save.clicked.connect(self.saveImage)

        self.retranslateUi(ao_pengurangan)
        QtCore.QMetaObject.connectSlotsByName(ao_pengurangan)

    def retranslateUi(self, ao_pengurangan):
        _translate = QtCore.QCoreApplication.translate
        ao_pengurangan.setWindowTitle(_translate("ao_pengurangan", "Arithmathic Operation-Pengurangan"))
        self.Img1.setText(_translate("ao_pengurangan", "Image 1"))
        self.Img2.setText(_translate("ao_pengurangan", "Image 2"))
        self.btn_proses.setText(_translate("ao_pengurangan", "Proses"))
        self.btn_open.setText(_translate("ao_pengurangan", "Open"))
        self.btn_save.setText(_translate("ao_pengurangan", "Save"))
    
    def loadImage2(self):
        if self.Img1.pixmap() is not None:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Open Image 2", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
            if file_name:
                pixmap = QPixmap(file_name)
                self.Img2.setPixmap(pixmap)
                self.Img2.setScaledContents(True)
                self.displayed_pixmap = pixmap
        
        else :
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Open Image 1", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
            if file_name:
                pixmap = QPixmap(file_name)
                self.Img1.setPixmap(pixmap)
                self.Img1.setScaledContents(True)
    
    def prosesPengurangan(self):
        pixmap1 = self.Img1.pixmap()
        pixmap2 = self.Img2.pixmap()
        if pixmap1 and pixmap2 :
            img1 = pixmap1.toImage()
            img2 = pixmap2.toImage()

            if img1.size() != img2.size():
                self.LOutput.setText("gambar harus memiliki ukuran yg sama")

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
                    r = min(r1 - r2, 255)
                    g = min(g1 - g2, 255)
                    b = min(b1 - b2, 255)
                    resul_keseluruhan.setPixel(x,y , qRgb(r, g, b))

            jumlah_pixmap = QPixmap.fromImage(resul_keseluruhan)
            self.LOutput.setPixmap(jumlah_pixmap)
            self.LOutput.setScaledContents(True)
            self.displayed_pixmap = jumlah_pixmap
    
    def saveImage(self):
        pixmap = self.LOutput.pixmap()
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
    ao_pengurangan = QtWidgets.QWidget()
    ui = Ui_ao_pengurangan()
    ui.setupUi(ao_pengurangan)
    ao_pengurangan.show()
    sys.exit(app.exec_())