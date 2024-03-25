from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class ThetaPSliderBox (GainStateUpdater):
  GAIN_IDX = 4

  def __init__ (self):
    super().__init__('theta-p', ThetaPSliderBox.GAIN_IDX)
