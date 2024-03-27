from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WYErrorISliderBox (TuningStateUpdater):
  TUNING_IDX = 7

  def __init__ (self):
    super().__init__('w-y-error-i', TuningContainer.tunings[WYErrorISliderBox.TUNING_IDX], WYErrorISliderBox.TUNING_IDX)
