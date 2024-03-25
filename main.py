import sys
from main_window import MainWindow
from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtWidgets import QApplication
from send_request_observer_thread import SendRequestObserverThread
from receive_thread import ReceiveThread

if __name__ == '__main__':
  app = QApplication(sys.argv)

  send_request_thread = SendRequestObserverThread()
  send_request_thread.start()

  receive_thread = ReceiveThread()
  receive_thread.start()

  window = MainWindow()

  window.show()
  app.exec()
