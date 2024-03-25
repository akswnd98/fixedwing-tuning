from PySide6.QtWidgets import QSlider, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QSize

MAX_VALUE = 2000

class GainSliderBox (QWidget):
  def __init__ (self, label_text):
    super().__init__()
    self.setFixedWidth(80)
    self.setFixedHeight(400)
    self.label = QLabel(label_text)
    layout = QVBoxLayout(self)
    self.slider = GainSlider()
    self.slider.valueChanged.connect(self.handle_slider_changed)
    self.line_edit = QLineEdit('0', validator=QIntValidator(0, MAX_VALUE))
    self.line_edit.returnPressed.connect(self.handle_text_changed)
    layout.addWidget(self.label)
    layout.addWidget(self.slider)
    layout.addWidget(self.line_edit)
    self.setLayout(layout)
  
  def handle_text_changed (self):
    self.slider.setValue(int(self.line_edit.text()))
  
  def handle_slider_changed (self, pos):
    self.line_edit.setText(str(pos))

  def get_value (self):
    return self.slider.get_value()

class GainSlider (QSlider):
  def __init__ (self):
    super().__init__()
    self.setRange(0, MAX_VALUE)
    self.setFixedWidth(30)
  
  def get_value (self):
    return self.value()
