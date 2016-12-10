import inspect

from app.constants import BASIC
from app.effects import constants
from effectsutils import FlashEffects, CycleEffects


class Boxes(object):
    @staticmethod
    def cycle(relay_controller, debug):
        """The boxes' lights cycle in a circle"""
        if debug >= BASIC:
            print "Boxes.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.cycle_lit_element_with_speedup(relay_controller, constants.CH_ALL_BOXES_LIST)

    @staticmethod
    def chase(relay_controller, debug):
        """An unlit box chases around the circle"""
        if debug >= BASIC:
            print "Boxes.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.cycle_darkened_element_with_speedup(relay_controller, constants.CH_ALL_BOXES_LIST)

    @staticmethod
    def strobe(relay_controller, debug):
        """The boxes flash relay_controller.on and relay_controller.off together"""
        if debug >= BASIC:
            print "Boxes.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.strobe(relay_controller, constants.CH_ALL_BOXES)

    @staticmethod
    def pulse(relay_controller, debug):
        """The boxes flash relay_controller.on and relay_controller.off together, speeding up"""
        if debug >= BASIC:
            print "Boxes.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.pulse(relay_controller, constants.CH_ALL_BOXES)

    @staticmethod
    def cylon_eyes(relay_controller, debug):
        """A single lit box travels back and forth, Like a cylon eye"""
        if debug >= BASIC:
            print "Boxes.%s" % inspect.currentframe().f_code.co_name

        CycleEffects.bounce_lit_element(relay_controller, constants.CH_ALL_BOXES_LIST)

    @staticmethod
    def alternate(relay_controller, debug):
        """Alternately flashes a pair of boxes and the remaining box"""
        if debug >= BASIC:
            print "Boxes.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.alternate(relay_controller, constants.CH_GREEN_BOX + constants.CH_RED_BOX, constants.CH_BLUE_BOX)
