from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.phi_p_slider_box import PhiPSliderBox
from tuning_slider_boxes.w_x_ff_slider_box import WXFFSliderBox
from tuning_slider_boxes.w_x_error_p_slider_box import WXErrorPSliderBox
from tuning_slider_boxes.w_x_error_i_slider_box import WXErrorISliderBox
from tuning_slider_boxes.theta_p_slider_box import ThetaPSliderBox
from tuning_slider_boxes.w_y_ff_slider_box import WYFFSliderBox
from tuning_slider_boxes.w_y_error_p_slider_box import WYErrorPSliderBox
from tuning_slider_boxes.w_y_error_i_slider_box import WYErrorISliderBox
from tuning_slider_boxes.w_z_ff_slider_box import WZFFSliderBox
from tuning_slider_boxes.w_z_error_p_slider_box import WZErrorPSliderBox
from tuning_slider_boxes.w_z_error_i_slider_box import WZErrorISliderBox
from tuning_slider_boxes.servo_offset_slider_boxes import Servo1OffsetSliderBox, Servo2OffsetSliderBox, Servo3OffsetSliderBox, Servo4OffsetSliderBox

class MainPanel (QWidget):
  def __init__ (self):
    super().__init__()
    self.layout = QHBoxLayout()
    self.layout.addWidget(PhiPSliderBox())
    self.layout.addWidget(WXFFSliderBox())
    self.layout.addWidget(WXErrorPSliderBox())
    self.layout.addWidget(WXErrorISliderBox())
    self.layout.addWidget(ThetaPSliderBox())
    self.layout.addWidget(WYFFSliderBox())
    self.layout.addWidget(WYErrorPSliderBox())
    self.layout.addWidget(WYErrorISliderBox())
    self.layout.addWidget(WZFFSliderBox())
    self.layout.addWidget(WZErrorPSliderBox())
    self.layout.addWidget(WZErrorISliderBox())
    
    self.layout.addWidget(Servo1OffsetSliderBox())
    self.layout.addWidget(Servo2OffsetSliderBox())
    self.layout.addWidget(Servo3OffsetSliderBox())
    self.layout.addWidget(Servo4OffsetSliderBox())
    self.setLayout(self.layout)
