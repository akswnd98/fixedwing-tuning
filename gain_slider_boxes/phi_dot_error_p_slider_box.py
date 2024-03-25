from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class PhiDotErrorPSliderBox (GainStateUpdater):
  GAIN_IDX = 2

  def __init__ (self):
    super().__init__('phi-dot-error-p', PhiDotErrorPSliderBox.GAIN_IDX)
