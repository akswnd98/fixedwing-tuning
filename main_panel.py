from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.phi_p_slider_box import PhiPSliderBox
from gain_slider_boxes.phi_dot_ff_slider_box import PhiDotFFSliderBox
from gain_slider_boxes.phi_dot_error_p_slider_box import PhiDotErrorPSliderBox
from gain_slider_boxes.phi_dot_error_i_slider_box import PhiDotErrorISliderBox
from gain_slider_boxes.theta_p_slider_box import ThetaPSliderBox
from gain_slider_boxes.theta_dot_ff_slider_box import ThetaDotFFSliderBox
from gain_slider_boxes.theta_dot_error_p_slider_box import ThetaDotErrorPSliderBox
from gain_slider_boxes.theta_dot_error_i_slider_box import ThetaDotErrorISliderBox
from gain_slider_boxes.psi_dot_error_p_slider_box import PsiDotErrorPSliderBox

class MainPanel (QWidget):
  def __init__ (self):
    super().__init__()
    self.layout = QHBoxLayout()
    self.layout.addWidget(PhiPSliderBox())
    self.layout.addWidget(PhiDotFFSliderBox())
    self.layout.addWidget(PhiDotErrorPSliderBox())
    self.layout.addWidget(PhiDotErrorISliderBox())
    self.layout.addWidget(ThetaPSliderBox())
    self.layout.addWidget(ThetaDotFFSliderBox())
    self.layout.addWidget(ThetaDotErrorPSliderBox())
    self.layout.addWidget(ThetaDotErrorISliderBox())
    self.layout.addWidget(PsiDotErrorPSliderBox())
    self.setLayout(self.layout)
