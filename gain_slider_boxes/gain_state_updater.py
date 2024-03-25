from gain_slider_boxes.gain_slider_box import GainSliderBox
from ibus_sender_container import IBusSenderContainer
from gain_container import GainContainer
from send_request_container import SendRequestContainer

class GainStateUpdater (GainSliderBox):
  def __init__ (self, label_text, gain_idx):
    super().__init__(label_text)
    self.gain_idx = gain_idx
  
  def handle_text_changed(self):
    super().handle_text_changed()
    GainContainer.gains[self.gain_idx] = int(self.get_value())
    SendRequestContainer.is_requested = True
  
  def handle_slider_changed(self, pos):
    super().handle_slider_changed(pos)
    GainContainer.gains[self.gain_idx] = int(self.get_value())
    SendRequestContainer.is_requested = True
