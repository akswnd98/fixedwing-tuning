from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class PhiDotErrorISliderBox (GainStateUpdater):
  GAIN_IDX = 3

  def __init__ (self):
    super().__init__('phi-dot-error-i', PhiDotErrorISliderBox.GAIN_IDX)
