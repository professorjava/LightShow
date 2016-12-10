import inspect

from app.constants import BASIC
from constants import CH_DOG
from effectsutils import FlashEffects


class Dog(object):
    @staticmethod
    def flash(relay_controller, debug):
        """Flash Dog"""
        if debug >= BASIC:
            print "Dog.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.flash(relay_controller, CH_DOG)
        return

    @staticmethod
    def strobe(relay_controller, debug):
        """Strobe Dog"""
        if debug >= BASIC:
            print "Dog.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.strobe(relay_controller, CH_DOG)
        return

    @staticmethod
    def pulse(relay_controller, debug):
        """The Dog flashes on and off, speeding up"""
        if debug >= BASIC:
            print "Dog.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.pulse(relay_controller, CH_DOG)
        return
