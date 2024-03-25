import struct
import serial
import threading
from settings_container import SettingsContainer
from send_request_container import SendRequestContainer
from ibus_sender_container import IBusSenderContainer
from gain_container import GainContainer
from time import sleep
from serial_container import SerialContainer

class ReceiveThread:
  def __init__ (self):
    pass

  def receive (self):
    while True:
      if SerialContainer.ser == None:
        continue
      raw_data = SerialContainer.ser.read(1)
      print(raw_data, flush=True)

  def start (self):
    thread = threading.Thread(target=self.receive, daemon=True)
    thread.start()
