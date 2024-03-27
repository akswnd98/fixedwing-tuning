from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WZErrorPSliderBox (TuningStateUpdater):
  TUNING_IDX = 9

  def __init__ (self):
    super().__init__('w-z-error-p', TuningContainer.tunings[WZErrorPSliderBox.TUNING_IDX], WZErrorPSliderBox.TUNING_IDX)
