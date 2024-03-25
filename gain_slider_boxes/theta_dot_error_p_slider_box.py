from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class ThetaDotErrorPSliderBox (GainStateUpdater):
  GAIN_IDX = 6

  def __init__ (self):
    super().__init__('theta-dot-error-p', ThetaDotErrorPSliderBox.GAIN_IDX)
