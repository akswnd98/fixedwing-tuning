from tuning_slider_boxes.tuning_slider_box import TuningSliderBox
from ibus_sender_container import IBusSenderContainer
from tuning_container import TuningContainer
from send_request_container import SendRequestContainer

class TuningStateUpdater (TuningSliderBox):
  def __init__ (self, label_text, initial_value, tuning_idx):
    super().__init__(label_text, initial_value)
    self.tuning_idx = tuning_idx
  
  def handle_text_changed(self):
    super().handle_text_changed()
    TuningContainer.tunings[self.tuning_idx] = int(self.get_value())
    SendRequestContainer.is_requested = True
  
  def handle_slider_changed(self, pos):
    super().handle_slider_changed(pos)
    TuningContainer.tunings[self.tuning_idx] = int(self.get_value())
    SendRequestContainer.is_requested = True
