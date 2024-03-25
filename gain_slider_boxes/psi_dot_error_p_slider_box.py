from gain_slider_boxes.gain_slider_box import GainSliderBox
from gain_slider_boxes.gain_state_updater import GainStateUpdater

class PsiDotErrorPSliderBox (GainStateUpdater):
  GAIN_IDX = 8

  def __init__ (self):
    super().__init__('psi-dot-error-p', PsiDotErrorPSliderBox.GAIN_IDX)
