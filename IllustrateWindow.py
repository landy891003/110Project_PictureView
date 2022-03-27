from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import ImageQt

import cv2

from illustrate import Ui_MainWindow
from opencv_engine import opencv_engine

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        self.setup_control()


    def setup_control(self):
        # TODO        
        # self.img_path = 'dog.jpg'
        self.ui.btn_open_file.clicked.connect(self.open_file) 
        self.ui.btn_zoom_in.clicked.connect(self.func_zoom_out) 
        self.ui.btn_zoom_out.clicked.connect(self.func_zoom_in)
        self.ui.btn_out_file.clicked.connect(self.func_out_file)

        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.ui.label.mousePressEvent = self.get_clicked_position
        self.ui.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) # 將圖片置中

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if filename == '':
            return
        self.img = cv2.imread(filename, -1)
        self.ui.file_name.setText(f'filename: {filename}')
        if self.img.size == 1:
            return
        self.display_img()

    def display_img(self):
        self.origin_height, self.origin_width, channel = self.img.shape
        bytesPerline = 3 * self.origin_width
        self.qimg = QImage(self.img, self.origin_width, self.origin_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))

    def func_zoom_in(self):
        self.qpixmap_height -= 100
        self.img_resize()

    def func_zoom_out(self):
        self.qpixmap_height += 100
        self.img_resize()

    def img_resize(self):        
        scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        print(f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        self.ui.img_shape.setText(f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        self.ui.label.setPixmap(scaled_pixmap)
    
    def __update_text_clicked_position(self):
        self.ui.position.setText(f"Real postion = ({int(self.norm_x*self.origin_width)}, {int(self.norm_y*self.origin_height)})")
    
    def get_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y() 
        self.norm_x = x/self.qpixmap.width()
        self.norm_y = y/self.qpixmap.height()
        self.__update_text_clicked_position()

    def func_out_file(self):
        img = ImageQt.fromqpixmap(self.ui.label.pixmap())
        fdir,ftype=QFileDialog.getSaveFileName(self,"Save Image","./","Image Files (*.jpg)")
        img.save(fdir)



  
