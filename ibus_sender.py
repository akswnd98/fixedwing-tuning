import ctypes

class IBusSender:
  NUM_OF_TUNINGS = 16

  def __init__ (self, ser):
    self.ser = ser

  def send (self, tunings):
    payload = (ctypes.c_uint16 * (IBusSender.NUM_OF_TUNINGS + 2))()
    payload[0] = 0x4020
    for i in range(1, IBusSender.NUM_OF_TUNINGS + 1):
      payload[i] = tunings[i - 1]
    check_sum = 0
    for i in range (0, IBusSender.NUM_OF_TUNINGS + 1):
      check_sum += (payload[i] & 0x00ff) + ((payload[i] & 0xff00) >> 8)
    payload[IBusSender.NUM_OF_TUNINGS + 1] = 0xffff - check_sum
    self.ser.write(bytes(payload))
