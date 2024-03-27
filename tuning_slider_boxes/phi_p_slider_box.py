from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class PhiPSliderBox (TuningStateUpdater):
  TUNING_IDX = 0

  def __init__ (self):
    super().__init__('phi-p', TuningContainer.tunings[PhiPSliderBox.TUNING_IDX], PhiPSliderBox.TUNING_IDX)
