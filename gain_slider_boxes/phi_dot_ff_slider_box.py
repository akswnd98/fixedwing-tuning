from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class PhiDotFFSliderBox (GainStateUpdater):
  GAIN_IDX = 1

  def __init__ (self):
    super().__init__('phi-dot-ff', PhiDotFFSliderBox.GAIN_IDX)
