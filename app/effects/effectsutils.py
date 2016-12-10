import time
import constants
from app.constants import BASIC


class Idle(object):
    """Not necessarily an effect. But turns all elements on or off as needed"""

    @staticmethod
    def idle(relay_controller, debug, active, delay):
        """Sit idle for awhile, with the lights either all on, or all off."""
        if debug >= BASIC:
            print "Idle.idle (%s seconds)" % delay

        if active:
            relay_controller.on(constants.CH_ALL, delay)
        else:
            relay_controller.off(constants.CH_ALL, delay)
        return


class FlashEffects(object):
    """Effects that flash or strobe some number of elements"""

    @staticmethod
    def flash(relay_controller, channel):
        """Flashes a single channel"""
        FlashEffects._flash(relay_controller, channel, constants.FLASH_COUNT, constants.FLASH_DELAY)

    @staticmethod
    def alternate(relay_controller, group1, group2):
        """Flashes two groups of channels alternately"""
        FlashEffects._alternate(relay_controller, group1, group2,
                                constants.ALTERNATE_COUNT, constants.ALTERNATE_DELAY)

    @staticmethod
    def strobe(relay_controller, channel, count=constants.STROBE_COUNT, delay=constants.STROBE_DELAY):
        """Strobes a single channel"""
        FlashEffects._flash(relay_controller, channel, count, delay)

    @staticmethod
    def _flash(relay_controller, channel, count, delay):
        for x in range(0, count):
            relay_controller.off(channel, delay)
            relay_controller.on(channel, delay)

    @staticmethod
    def _alternate(relay_controller, group1, group2, count, delay):
        for x in range(0, count):
            relay_controller.off(group2)
            relay_controller.on(group1, delay)

            relay_controller.off(group1)
            relay_controller.on(group2, delay)

    @staticmethod
    def pulse(relay_controller, channel):
        """The channel flashes on and off, speeding up"""

        for count, delay in ((1, .5), (1, .4), (2, .3), (3, .2), (5, .1)):
            for y in range(0, count):
                relay_controller.off(channel, delay)
                relay_controller.on(channel, delay)
                # count += 1


class CycleEffects(object):
    """Effects to do with cycling around a line of elements"""

    @staticmethod
    def cycle_lit_element_single_speed(relay_controller, channels):
        """Cycles <count> times at a single speed."""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(ch, .5)

    @staticmethod
    def cycle_lit_element_with_speedup(relay_controller, channels):
        """Cycles multiple times at ever-increasing speed."""

        for count, delay in ((1, .5), (1, .4), (2, .3), (3, .2), (5, .1)):
            for x in range(0, count):
                for ch in channels:
                    relay_controller.set(ch, delay)

    @staticmethod
    def cycle_darkened_element_single_speed(relay_controller, channels):
        """Chases <count> times at a single speed."""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(constants.CH_ALL & ~ch, .5)

    @staticmethod
    def cycle_darkened_element_with_speedup(relay_controller, channels):
        """Chases multiple times at ever-increasing speed."""

        for count, delay in ((1, .5), (1, .4), (2, .3), (3, .2), (5, .1)):
            for x in range(0, count):
                for ch in channels:
                    relay_controller.set(constants.CH_ALL & ~ch, delay)

    @staticmethod
    def bounce_lit_element(relay_controller, channels):
        """A single lit element travels back and forth, Like a cylon eye"""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(ch, .3)
            for ch in reversed(channels):
                relay_controller.set(ch, .3)

    @staticmethod
    def bounce_darkened_element(relay_controller, channels):
        """A single lit element travels back and forth, Like a cylon eye"""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(constants.CH_ALL & ~ch, .3)
            for ch in reversed(channels):
                relay_controller.set(constants.CH_ALL & ~ch, .3)


class MorseCodeEffects(object):
    """Morse code and timing definitions come from
        https://en.wikipedia.org/wiki/Morse_code
    """

    _dots_and_dashes = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', ' ': '',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '----',
    }

    # Represents a single time unit. Other lengths (e.g,. dot length) are each multiples
    #   of this value. To adjust the timing of the code, adjust this value
    _time_unit_len = 0.1

    def __init__(self):
        self._dot_len = 1 * MorseCodeEffects._time_unit_len
        self._dash_len = 3 * MorseCodeEffects._time_unit_len
        self._inter_element_gap_len = 1 * MorseCodeEffects._time_unit_len
        self._short_gap_len = 3 * MorseCodeEffects._time_unit_len
        self._medium_gap_len = 7 * MorseCodeEffects._time_unit_len

    def display_as_morse(self, relay_controller, debug, channel, text):
        """Convert the text to dots and dashes, then display them"""
        for letter in text.lower():

            if letter in self._dots_and_dashes:
                dots_and_dashes = self._dots_and_dashes[letter]
                if debug >= BASIC:
                    print letter, dots_and_dashes

                for d in dots_and_dashes:
                    if d == '.':
                        self._dot(relay_controller, channel)

                    elif d == '-':
                        self._dash(relay_controller, channel)

                    elif d == ' ':
                        # Gap between words
                        time.sleep(self._medium_gap_len)

                # Gap between letters
                time.sleep(self._short_gap_len)
            else:
                if debug >= BASIC:
                    print 'Skipping', letter

    def _dot(self, relay_controller, channel):
        """Display a dot"""
        relay_controller.on(channel, self._dot_len)
        relay_controller.off(channel, self._inter_element_gap_len)

    def _dash(self, relay_controller, channel):
        """Display a dash"""
        relay_controller.on(channel, self._dash_len)
        relay_controller.off(channel, self._inter_element_gap_len)
