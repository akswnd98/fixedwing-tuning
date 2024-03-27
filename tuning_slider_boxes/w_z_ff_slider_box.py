from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WZFFSliderBox (TuningStateUpdater):
  TUNING_IDX = 8

  def __init__ (self):
    super().__init__('w-z-ff', TuningContainer.tunings[WZFFSliderBox.TUNING_IDX], WZFFSliderBox.TUNING_IDX)
