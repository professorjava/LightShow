import time
import inspect
import random

import constants
from app.constants import BASIC
from effectsutils import FlashEffects, CycleEffects


class AllElements(object):
    """Effects that involve every element in the display"""

    @staticmethod
    def cycle1(relay_controller, debug):
        """Cycle all of the elements at a single speed"""

        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffects.cycle_lit_element_single_speed(relay_controller, constants.CH_ALL_LIST)

    @staticmethod
    def cycle2(relay_controller, debug):
        """Cycle all of the elements at increasing speed"""

        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffects.cycle_lit_element_with_speedup(relay_controller, constants.CH_ALL_LIST)

    @staticmethod
    def chase1(relay_controller, debug):
        """Chase all of the elements at a single speed"""

        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffects.cycle_darkened_element_single_speed(relay_controller, constants.CH_ALL_LIST)

    @staticmethod
    def chase2(relay_controller, debug):
        """Chase all of the elements at increasing speed"""

        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffects.cycle_darkened_element_with_speedup(relay_controller, constants.CH_ALL_LIST)

    @staticmethod
    def bounce1(relay_controller, debug):
        """Cylon eyes across all elements"""
        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.bounce_lit_element(relay_controller, constants.CH_ALL_LIST)

    @staticmethod
    def bounce2(relay_controller, debug):
        """Inverse Cylon eyes across all elements"""
        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        CycleEffects.bounce_darkened_element(relay_controller, constants.CH_ALL_LIST)

    @staticmethod
    def flash_all(relay_controller, debug):
        """Flashes all of the elements together"""
        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.flash(relay_controller, constants.CH_ALL)

    @staticmethod
    def alternate(relay_controller, debug):
        """Alternately flashes the even and odd elements"""

        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.alternate(relay_controller,
                               constants.CH_GREEN_BOX + constants.CH_RED_BOX + constants.CH_1_TREE,
                               constants.CH_SANTA + constants.CH_BLUE_BOX + constants.CH_DOG + constants.CH_2_TREES)

    @staticmethod
    def alternate_porch_and_trees(relay_controller, debug):
        """Alternately flashes all the trees and all the porch items"""

        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.alternate(relay_controller, constants.CH_ALL_PORCH, constants.CH_ALL_TREES)

    # They all flash on and off together, speeding up
    @staticmethod
    def pulse(relay_controller, debug):
        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        FlashEffects.pulse(relay_controller, constants.CH_ALL)

    @staticmethod
    def sliding_doors(relay_controller, debug):
        """A pair of lights pulse out from the middle, and back, like a pair
            of sliding doors.
        """
        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        relay_controller.off(constants.CH_NONE)
        for x in range(0, 3):
            relay_controller.set(constants.CH_RED_BOX, .3)
            relay_controller.set(constants.CH_BLUE_BOX + constants.CH_DOG, .3)
            relay_controller.set(constants.CH_SANTA + constants.CH_1_TREE, .3)
            relay_controller.set(constants.CH_GREEN_BOX + constants.CH_2_TREES, .3)
            relay_controller.set(constants.CH_SANTA + constants.CH_1_TREE, .3)
            relay_controller.set(constants.CH_BLUE_BOX + constants.CH_DOG, .3)

    @staticmethod
    def one_by_one(relay_controller, debug):
        """Turn each element on in turn, then off in turn"""
        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        delay = 1
        relay_controller.off(constants.CH_ALL, delay)

        relay_controller.on(constants.CH_GREEN_BOX, delay)
        relay_controller.on(constants.CH_SANTA, delay)
        relay_controller.on(constants.CH_BLUE_BOX, delay)
        relay_controller.on(constants.CH_RED_BOX, delay)
        relay_controller.on(constants.CH_DOG, delay)
        relay_controller.on(constants.CH_1_TREE, delay)
        relay_controller.on(constants.CH_2_TREES, delay)

        relay_controller.off(constants.CH_GREEN_BOX, delay)
        relay_controller.off(constants.CH_SANTA, delay)
        relay_controller.off(constants.CH_BLUE_BOX, delay)
        relay_controller.off(constants.CH_RED_BOX, delay)
        relay_controller.off(constants.CH_DOG, delay)
        relay_controller.off(constants.CH_1_TREE, delay)
        relay_controller.off(constants.CH_2_TREES, delay)

    @staticmethod
    def twinkle(relay_controller, debug):
        """randomly turns elements quickly off and back on, creating a twinkling effect"""

        if debug >= BASIC:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        elements = random.sample(constants.CH_ALL_LIST, len(constants.CH_ALL_LIST))

        relay_controller.on(constants.CH_ALL)
        for ch in elements:
            relay_controller.off(ch, .1)
            relay_controller.on(ch)
            delay = .7 + .1 * random.randint(0, 6)
            time.sleep(delay)
