import serial
import threading
from settings_container import SettingsContainer
from send_request_container import SendRequestContainer
from ibus_sender_container import IBusSenderContainer
from tuning_container import TuningContainer
from time import sleep

class SendRequestObserverThread:
  def __init__ (self):
    pass

  def observe_send_request (self):
    while True:
      if not SendRequestContainer.is_requested or IBusSenderContainer.ibus_sender == None:
        continue

      IBusSenderContainer.ibus_sender.send(TuningContainer.tunings)

      SendRequestContainer.is_requested = False
      sleep(0.1)

  def start (self):
    thread = threading.Thread(target=self.observe_send_request, daemon=True)
    thread.start()
