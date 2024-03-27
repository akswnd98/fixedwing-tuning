from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WYErrorPSliderBox (TuningStateUpdater):
  TUNING_IDX = 6

  def __init__ (self):
    super().__init__('w-y-error-p', TuningContainer.tunings[WYErrorPSliderBox.TUNING_IDX], WYErrorPSliderBox.TUNING_IDX)
