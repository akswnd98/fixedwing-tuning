from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WZErrorISliderBox (TuningStateUpdater):
  TUNING_IDX = 10

  def __init__ (self):
    super().__init__('w-z-error-i', TuningContainer.tunings[WZErrorISliderBox.TUNING_IDX], WZErrorISliderBox.TUNING_IDX)
