import time
import glob


class Idle(object):
    @staticmethod
    def idle(relay_controller, debug, active, delay):
        """Sit idle for awhile, with the lights either all on, or all off."""
        if debug:
            print "Idle.idle (%s seconds)" % delay

        if active:
            relay_controller.on(glob.ch_all, delay)
        else:
            relay_controller.off(glob.ch_all, delay)
        return


class FlashEffect(object):
    @staticmethod
    def flash(relay_controller, channel):
        """Flashes a single channel"""
        FlashEffect._flash(relay_controller, channel, glob.flash_count, glob.flash_delay)

    @staticmethod
    def alternate(relay_controller, group1, group2):
        """Flashes two groups of channels alternately"""
        FlashEffect._alternate(relay_controller, group1, group2, glob.flash_count, glob.flash_delay)

    @staticmethod
    def strobe(relay_controller, channel, count=glob.strobe_count, delay=glob.strobe_delay):
        """Strobes a single channel"""
        FlashEffect._flash(relay_controller, channel, count, delay)

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


class PulseEffect(object):
    # The channel flashes on and off, speeding up
    def pulse(self, relay_controller, channel, count=1):

        for delay in [.5, .4, .3, .2, .1]:
            for y in range(0, count):
                relay_controller.off(channel, delay)
                relay_controller.on(channel, delay)
                count += 1


class CycleEffect(object):
    """Produces a cycle effect where a single element appears to run in a circle. """

    @staticmethod
    def cycle_lit_element_single_speed(relay_controller, *channels):
        """Cycles <count> times at a single speed."""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(ch, .5)

    @staticmethod
    def cycle_lit_element_with_speedup(relay_controller, *channels):
        """Cycles multiple times at ever-increasing speed."""

        for count, delay in ((1, .5), (1, .4), (2, .3), (3, .2), (5, .1)):
            for x in range(0, count):
                for ch in channels:
                    relay_controller.set(ch, delay)

    @staticmethod
    def cycle_darkened_element_single_speed(relay_controller, *channels):
        """Chases <count> times at a single speed."""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(glob.ch_all & ~ch, .5)

    @staticmethod
    def cycle_darkened_element_with_speedup(relay_controller, *channels):
        """Chases multiple times at ever-increasing speed."""

        for count, delay in ((1, .5), (1, .4), (2, .3), (3, .2), (5, .1)):
            for x in range(0, count):
                for ch in channels:
                    relay_controller.set(glob.ch_all & ~ch, delay)

    @staticmethod
    def bounce_lit_element(relay_controller, *channels):
        """A single lit element travels back and forth, Like a cylon eye"""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(ch, .3)
            for ch in reversed(channels):
                relay_controller.set(ch, .3)

    @staticmethod
    def bounce_darkened_element(relay_controller, *channels):
        """A single lit element travels back and forth, Like a cylon eye"""

        for x in range(0, 3):
            for ch in channels:
                relay_controller.set(glob.ch_all & ~ch, .3)
            for ch in reversed(channels):
                relay_controller.set(glob.ch_all & ~ch, .3)


class MorseCodeEffect(object):
    # Morse code and timing definitions come from
    # https://en.wikipedia.org/wiki/Morse_code
    _time_unit_len = 0.1  # increasing/decreasing this will affect all lengths proportionately
    _dot_len = 1 * _time_unit_len
    _dash_len = 3 * _time_unit_len
    _inter_element_gap_len = 1 * _time_unit_len
    _short_gap_len = 3 * _time_unit_len
    _medium_gap_len = 7 * _time_unit_len

    _morse = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', ' ': '',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '----',
    }

    def display_as_morse(self, relay_controller, debug, channel, text):
        for letter in text.lower():

            if letter in self._morse:
                dots_and_dashes = self._morse[letter]
                if debug: print letter, dots_and_dashes

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
                if debug: print "Skipping", letter
        return

    def _dot(self, relay_controller, channel):
        relay_controller.on(channel, self._dot_len)
        relay_controller.off(channel, self._inter_element_gap_len)
        return

    def _dash(self, relay_controller, channel):
        relay_controller.on(channel, self._dash_len)
        relay_controller.off(channel, self._inter_element_gap_len)
        return
