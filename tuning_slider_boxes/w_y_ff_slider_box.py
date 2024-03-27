from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class WYFFSliderBox (TuningStateUpdater):
  TUNING_IDX = 5

  def __init__ (self):
    super().__init__('w-y-ff', TuningContainer.tunings[WYFFSliderBox.TUNING_IDX], WYFFSliderBox.TUNING_IDX)
