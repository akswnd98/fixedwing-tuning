from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WXFFSliderBox (TuningStateUpdater):
  TUNING_IDX = 1

  def __init__ (self):
    super().__init__('w-x-ff', TuningContainer.tunings[WXFFSliderBox.TUNING_IDX], WXFFSliderBox.TUNING_IDX)
