from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class ThetaDotFFSliderBox (GainStateUpdater):
  GAIN_IDX = 5

  def __init__ (self):
    super().__init__('theta-dot-ff', ThetaDotFFSliderBox.GAIN_IDX)
