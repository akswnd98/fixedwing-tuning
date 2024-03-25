from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSize
from menu.menu_bar import MenuBar
from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtWidgets import (
  QApplication, QMainWindow, QWidget,
  QHBoxLayout, QMenuBar, QMenu
)
from main_panel import MainPanel

class MainWindow (QMainWindow):
  def __init__ (self):
    super().__init__()

    self.setWindowTitle('fixedwing-tunning')
    self.setBaseSize(QSize(1000, 600))
    self.resize(QSize(1000, 600))
    self.setMenuBar(MenuBar())
    self.closeEvent = self.handle_close

    self.setCentralWidget(MainPanel())

  def handle_close (self, event):
    event.accept()
