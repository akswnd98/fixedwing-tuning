from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QWidget, QPushButton
from PySide6.QtGui import QIntValidator
from settings_container import SettingsContainer
from settings_dialog_instance import SettingsDialogInstance
from ibus_sender_container import IBusSenderContainer
from ibus_sender import IBusSender
import serial
from serial_container import SerialContainer

class SettingsDialog (QDialog):
  def __init__ (self):
    super().__init__()
    self.resize(QSize(1000, 600))
    self.setWindowTitle('settings')
    self.closeEvent = self.handle_close
    self.setLayout(MainLayout())
  
  def handle_close (self, event):
    pass

class MainLayout (QVBoxLayout):
  def __init__ (self):
    super().__init__()
    self.port_input = PortInput()
    self.addWidget(self.port_input)
    self.baudrate_input = BaudrateInput()
    self.addWidget(self.baudrate_input)
    self.run_button = RunButton(
      self.port_input, self.baudrate_input
    )
    self.addWidget(self.run_button)

class ValueInput (QWidget):
  def __init__ (self, label, validator, initial_value):
    super().__init__()
    layout = QHBoxLayout()
    self.setLayout(layout)
    layout.addWidget(QLabel(label))
    self.line_edit = QLineEdit(validator=validator)
    layout.addWidget(self.line_edit)
    self.line_edit.setText(str(initial_value))
  
  def get_value (self):
    return self.line_edit.text()

class TextInput(ValueInput):
  def __init__ (self, label, initial_value):
    super().__init__(label, None, initial_value)

class NumberInput (ValueInput):
  def __init__ (self, label, range, initial_value):
    super().__init__(label, QIntValidator(*range), initial_value)

class PortInput (TextInput):
  def __init__ (self):
    super().__init__('port', SettingsContainer.port)

class BaudrateInput (NumberInput):
  def __init__ (self):
    super().__init__('baudrate', (), SettingsContainer.baudrate)

class RunButton (QPushButton):
  def __init__ (self, port_input, baudrate_input):
    super().__init__('run')
    self.port_input = port_input
    self.baudrate_input = baudrate_input
    self.clicked.connect(self.handle_click)
  
  def handle_click (self):
    SettingsContainer.port = self.port_input.get_value()
    SettingsContainer.baudrate = int(self.baudrate_input.get_value())
    if IBusSenderContainer.ibus_sender != None and IBusSenderContainer.ibus_sender.ser != None:
      IBusSenderContainer.ibus_sender.ser.close()
    SerialContainer.ser = serial.Serial(SettingsContainer.port, SettingsContainer.baudrate)
    IBusSenderContainer.ibus_sender = IBusSender(SerialContainer.ser)
    
    SettingsDialogInstance.instance.close()
