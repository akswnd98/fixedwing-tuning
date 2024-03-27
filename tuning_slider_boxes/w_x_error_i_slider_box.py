from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WXErrorISliderBox (TuningStateUpdater):
  TUNING_IDX = 3

  def __init__ (self):
    super().__init__('w_x-error-i', TuningContainer.tunings[WXErrorISliderBox.TUNING_IDX], WXErrorISliderBox.TUNING_IDX)
