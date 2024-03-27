from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from tuning_slider_boxes.tuning_state_updater import TuningStateUpdater
from tuning_container import TuningContainer

class Servo1OffsetSliderBox (TuningStateUpdater):
  TUNING_IDX = 11

  def __init__ (self):
    super().__init__('servo1-offset', TuningContainer.tunings[Servo1OffsetSliderBox.TUNING_IDX], Servo1OffsetSliderBox.TUNING_IDX)

class Servo2OffsetSliderBox (TuningStateUpdater):
  TUNING_IDX = 12

  def __init__ (self):
    super().__init__('servo2-offset', TuningContainer.tunings[Servo2OffsetSliderBox.TUNING_IDX], Servo2OffsetSliderBox.TUNING_IDX)

class Servo3OffsetSliderBox (TuningStateUpdater):
  TUNING_IDX = 13

  def __init__ (self):
    super().__init__('servo3-offset', TuningContainer.tunings[Servo3OffsetSliderBox.TUNING_IDX], Servo3OffsetSliderBox.TUNING_IDX)

class Servo4OffsetSliderBox (TuningStateUpdater):
  TUNING_IDX = 14

  def __init__ (self):
    super().__init__('servo4-offset', TuningContainer.tunings[Servo4OffsetSliderBox.TUNING_IDX], Servo4OffsetSliderBox.TUNING_IDX)
