import sys
import os
import pyautogui
import time
from PyQt5.QtCore import QUrl
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication,QDesktopWidget
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

app = QApplication(sys.argv)
base_url = os.getcwd()
base_url = base_url.replace('\\', '/')
browser = QWebEngineView()
browser.load(QUrl(base_url+"/demo.html"))
browser.setWindowTitle("VTuber")
browser.setFixedSize(1280,720)
screen = QDesktopWidget().screenGeometry()
size = browser.geometry()
newLeft = (screen.width() - size.width()) / 2
newTop = (screen.height() - size.height()) / 2
browser.setGeometry(newLeft,newTop,1280,720)  #窗口的大小和位置设置
browser.show()
# time.sleep(5)
# pyautogui.click(browser.geometry().x()+10, browser.geometry().x()+browser.geometry().y()-100, button ='left')  # 左击
# print("666")
# time.sleep(5)
# pyautogui.click(browser.geometry().x()+browser.geometry().width() - 100, browser.geometry().x() + browser.geometry().y() - 100,button='left')  # 左击
# print("666")
# time.sleep(5)
# pyautogui.click(browser.geometry().x()+10, browser.geometry().x()+browser.geometry().y()-100, button ='left')  # 左击
# print("666")
app.exec_()

