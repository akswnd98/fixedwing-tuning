from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WXErrorPSliderBox (TuningStateUpdater):
  TUNING_IDX = 2

  def __init__ (self):
    super().__init__('w-x-error-p', TuningContainer.tunings[WXErrorPSliderBox.TUNING_IDX], WXErrorPSliderBox.TUNING_IDX)
