import inspect

import constants
from app.constants import BASIC
from effectsutils import FlashEffects, CycleEffects


class Porch(object):
    """Effects that involve every element on the porch"""

    @staticmethod
    def cycle1(relay_controller, debug):
        """Cycle all of the elements at a single speed"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.cycle_lit_element_single_speed(relay_controller, constants.CH_ALL_PORCH_LIST)

    @staticmethod
    def cycle2(relay_controller, debug):
        """Cycle all of the elements at increasing speed"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.cycle_lit_element_with_speedup(relay_controller, constants.CH_ALL_PORCH_LIST)

    @staticmethod
    def chase1(relay_controller, debug):
        """Chase all of the elements at a single speed"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.cycle_darkened_element_single_speed(relay_controller, constants.CH_ALL_PORCH_LIST)

    @staticmethod
    def chase2(relay_controller, debug):
        """Chase all of the elements at increasing speed"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.cycle_darkened_element_with_speedup(relay_controller, constants.CH_ALL_PORCH_LIST)

    @staticmethod
    def bounce1(relay_controller, debug):
        """Cylon eyes across all elements"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.bounce_lit_element(relay_controller, constants.CH_ALL_PORCH_LIST)

    @staticmethod
    def bounce2(relay_controller, debug):
        """Inverse Cylon eyes across all elements"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.bounce_darkened_element(relay_controller, constants.CH_ALL_PORCH_LIST)

    @staticmethod
    def flash_all(relay_controller, debug):
        """Flashes all of the elements together"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.flash(relay_controller, constants.CH_ALL_PORCH)

    @staticmethod
    def alternate(relay_controller, debug):
        """Alternately flashes the gift boxes and santa + dog"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.alternate(relay_controller,
                               constants.CH_GREEN_BOX + constants.CH_RED_BOX,
                               constants.CH_SANTA + constants.CH_BLUE_BOX + constants.CH_DOG)

    @staticmethod
    def pulse(relay_controller, debug):
        """They all flash on and off together, speeding up"""

        if debug >= BASIC:
            print "Porch.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.pulse(relay_controller, constants.CH_ALL_PORCH)
