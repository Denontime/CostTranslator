'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-25 22:16:37
@LastEditors: Mar Ping
@LastEditTime: 2020-04-26 00:38:52
'''
import sys
from PIL import Image

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel
from pyqt_screenshot.screenshot import Screenshot, constant

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    qtApp = QApplication(sys.argv)

    main_window = QLabel()
    
    img = Screenshot.take_screenshot(constant.RECT | constant.CLIPBOARD )
    main_window.resize(1280,720)
    
    main_window.show()
    if img is not None:
        main_window.setPixmap(QPixmap(img))
    qtApp.exec()
