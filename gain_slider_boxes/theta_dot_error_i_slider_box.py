from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class ThetaDotErrorISliderBox (GainStateUpdater):
  GAIN_IDX = 7

  def __init__ (self):
    super().__init__('theta-dot-error-i', ThetaDotErrorISliderBox.GAIN_IDX)
