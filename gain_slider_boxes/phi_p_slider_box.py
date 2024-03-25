from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class PhiPSliderBox (GainStateUpdater):
  GAIN_IDX = 0

  def __init__ (self):
    super().__init__('phi-p', PhiPSliderBox.GAIN_IDX)
