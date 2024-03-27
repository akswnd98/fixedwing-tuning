from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class ThetaPSliderBox (TuningStateUpdater):
  TUNING_IDX = 4

  def __init__ (self):
    super().__init__('theta-p', TuningContainer.tunings[ThetaPSliderBox.TUNING_IDX], ThetaPSliderBox.TUNING_IDX)
