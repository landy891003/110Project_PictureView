from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap
import cv2

class img_controller(object):
    def __init__(self, img_path, label, label_file_path, label_ratio, label_img_shape):
        self.img_path = img_path
        self.label = label
        self.label_file_path = label_file_path
        self.label_ratio= label_ratio
        self.label_img_shape = label_img_shape
        self.ratio_value = 50
        self.read_file_and_init()
        self.__update_img()

    def read_file_and_init(self):
        self.img = cv2.imread(self.img_path,-1)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.origin_qpixmap = QPixmap.fromImage(self.qimg)
        self.ratio_value = 50        
        self.set_img_ratio()

    def set_img_ratio(self):
        self.ratio_rate = pow(10, (self.ratio_value - 50)/50)
        qpixmap_height = self.origin_height * self.ratio_rate
        self.qpixmap = self.origin_qpixmap.scaledToHeight(qpixmap_height)
        self.__update_img()
        self.__update_text_ratio()
        self.__update_text_img_shape()

    def set_path(self, img_path):
        self.img_path = img_path
        self.read_file_and_init()
        self.__update_img()

    def __update_img(self):       
        self.label.setPixmap(self.qpixmap)
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    def __update_text_file_path(self):
        self.label_file_path.setText(f"File path = {self.img_path}")

    def __update_text_ratio(self):
        self.label_ratio.setText(f"{int(100*self.ratio_rate)} %")

    def __update_text_img_shape(self):
        current_text = f"Current img shape = ({self.qpixmap.width()}, {self.qpixmap.height()})"
        origin_text = f"Origin img shape = ({self.origin_width}, {self.origin_height})"
        self.label_img_shape.setText(current_text+"\t"+origin_text)

    def set_zoom_in(self):
        self.ratio_value = max(0, self.ratio_value - 1)
        self.set_img_ratio()

    def set_zoom_out(self):
        self.ratio_value = min(100, self.ratio_value + 1)
        self.set_img_ratio()

    def set_slider_value(self, value):
        self.ratio_value = value
        self.set_img_ratio()
