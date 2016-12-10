import time
from abc import ABCMeta, abstractmethod
from pylibftdi import BitBangDevice

from constants import DETAILED


class RelayController(object):
    __metaclass__ = ABCMeta

    def __init__(self, observer, debug):
        self.debug = debug
        self.current_value = 0
        self.observer = observer

    def on(self, bitmask, delay=None):
        self.current_value = self._on(bitmask)
        self._finish_operation("on  ", delay)

    def off(self, bitmask, delay=None):
        self.current_value = self._off(bitmask)
        self._finish_operation("off ", delay)

    def set(self, channel, delay=None):
        self.current_value = self._set(channel)
        self._finish_operation("set ", delay)

    def _finish_operation(self, operation, delay):
        if self.observer is not None:
            self.observer.update(self.current_value)

        if self.debug >= DETAILED:
            print operation, "{0:0>8b}".format(self.current_value)

        if delay is not None:
            time.sleep(delay)

    @abstractmethod
    def _on(self, bitmask):
        pass

    @abstractmethod
    def _off(self, bitmask):
        pass

    @abstractmethod
    def _set(self, channels):
        pass


class TestRelayController(RelayController):
    def __init__(self, observer, debug):
        super(TestRelayController, self).__init__(observer, debug)

    def _on(self, bitmask):
        return self.current_value | bitmask

    def _off(self, bitmask):
        return self.current_value & ~bitmask

    def _set(self, channels):
        return channels


class FtdiRelayController(RelayController):
    def __init__(self, observer, serial_number, debug):
        super(FtdiRelayController, self).__init__(observer, debug)

        if serial_number is None:
            self.relay = BitBangDevice()
        else:
            self.relay = BitBangDevice(serial_number)

    def _on(self, bitmask):
        self.relay.port = self.relay.port | bitmask
        return self.relay.port

    def _off(self, bitmask):
        self.relay.port = self.relay.port & ~bitmask
        return self.relay.port

    def _set(self, channels):
        self.relay.port = channels
        return self.relay.port
