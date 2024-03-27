from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class CruiseSpeedSliderBox (TuningStateUpdater):
  TUNING_IDX = 15

  def __init__ (self):
    super().__init__('cruise-speed', TuningContainer.tunings[CruiseSpeedSliderBox.TUNING_IDX], CruiseSpeedSliderBox.TUNING_IDX)
