import inspect

from app.constants import BASIC
from constants import *
from effectsutils import FlashEffects, MorseCodeEffects


class Santa(object):
    @staticmethod
    def flash(relay_controller, debug):
        """Flash santa's nose"""
        if debug >= BASIC:
            print "Santa.%s" % inspect.currentframe().f_code.co_name

        FlashEffects().flash(relay_controller, CH_SANTA)

    @staticmethod
    def strobe(relay_controller, debug):
        """# Strobe santa's nose"""
        if debug >= BASIC:
            print "Santa.%s" % inspect.currentframe().f_code.co_name

        FlashEffects().strobe(relay_controller, CH_SANTA)

    @staticmethod
    def pulse(relay_controller, debug):
        """The santa flashes on and off, speeding up"""
        if debug >= BASIC:
            print "Santa.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.pulse(relay_controller, CH_SANTA)

    @staticmethod
    def merry_christmas(relay_controller, debug):
        """Flash Merry Christmas using Santa's nose"""
        if debug >= BASIC:
            print "Santa.%s" % inspect.currentframe().f_code.co_name

        MorseCodeEffects().display_as_morse(relay_controller, debug, CH_SANTA, 'Merry Christmas')
