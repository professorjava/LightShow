import inspect

from effectsutils import FlashEffect, CycleEffect
import glob


class AllElements(object):
    """Effects that involve every element in the display"""

    @staticmethod
    def cycle1(relay_controller, debug):
        """Cycle all of the elements at a single speed"""

        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffect.cycle_lit_element_single_speed(relay_controller, glob.ch_green_box, glob.ch_santa, glob.ch_blue_box,
                                                   glob.ch_red_box, glob.ch_dog, glob.ch_1_tree, glob.ch_2_trees)

    @staticmethod
    def cycle2(relay_controller, debug):
        """Cycle all of the elements at increasing speed"""

        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffect.cycle_lit_element_with_speedup(relay_controller, glob.ch_green_box, glob.ch_santa, glob.ch_blue_box,
                                                   glob.ch_red_box, glob.ch_dog, glob.ch_1_tree, glob.ch_2_trees)

    @staticmethod
    def chase1(relay_controller, debug):
        """Chase all of the elements at a single speed"""

        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffect.cycle_darkened_element_single_speed(relay_controller, glob.ch_green_box, glob.ch_santa, glob.ch_blue_box,
                                                        glob.ch_red_box, glob.ch_dog, glob.ch_1_tree, glob.ch_2_trees)

    @staticmethod
    def chase2(relay_controller, debug):
        """Chase all of the elements at increasing speed"""

        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        CycleEffect.cycle_darkened_element_with_speedup(relay_controller, glob.ch_green_box, glob.ch_santa,
                                                        glob.ch_blue_box, glob.ch_red_box, glob.ch_dog,
                                                        glob.ch_1_tree, glob.ch_2_trees)

    @staticmethod
    def bounce1(relay_controller, debug):
        """Cylon eyes across all elements"""
        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        CycleEffect.bounce_lit_element(relay_controller, glob.ch_green_box, glob.ch_santa, glob.ch_blue_box,
                                       glob.ch_red_box, glob.ch_dog, glob.ch_1_tree, glob.ch_2_trees)

    @staticmethod
    def bounce2(relay_controller, debug):
        """Inverse Cylon eyes across all elements"""
        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        CycleEffect.bounce_darkened_element(relay_controller, glob.ch_green_box, glob.ch_santa, glob.ch_blue_box,
                                            glob.ch_red_box, glob.ch_dog, glob.ch_1_tree, glob.ch_2_trees)

    @staticmethod
    def flash_all(relay_controller, debug):
        """Flashes all of the elements together"""
        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        FlashEffect.flash(relay_controller, glob.ch_all)

    @staticmethod
    def flash_porch(relay_controller, debug):
        """Alternately flashes the gift boxes and santa + dog"""

        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        FlashEffect.alternate(relay_controller, glob.ch_all_boxes, glob.ch_santa + glob.ch_dog)

    @staticmethod
    def flash_trees(relay_controller, debug):
        """Alternately flashes the two tree groups"""

        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        FlashEffect.alternate(relay_controller, glob.ch_1_tree, glob.ch_2_trees)

    @staticmethod
    def alternate_porch_and_trees(relay_controller, debug):
        """Alternately flashes all the trees and all the porch items"""

        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name
        FlashEffect.alternate(relay_controller, glob.ch_all_porch, glob.ch_all_trees)

    # They all flash on and off together, speeding up
    @staticmethod
    def pulse(relay_controller, debug):
        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        count = 1
        for delay in [.5, .4, .3, .2, .1]:
            for y in range(0, count):
                relay_controller.off(glob.ch_all, delay)
                relay_controller.on(glob.ch_all, delay)
                count += 1

    # Turn each element on in turn, then off in turn
    @staticmethod
    def one_by_one(relay_controller, debug):
        if debug:
            print "AllElements.%s" % inspect.currentframe().f_code.co_name

        delay = 1
        relay_controller.off(glob.ch_all, delay)

        relay_controller.on(glob.ch_green_box, delay)
        relay_controller.on(glob.ch_blue_box, delay)
        relay_controller.on(glob.ch_santa, delay)
        relay_controller.on(glob.ch_red_box, delay)
        relay_controller.on(glob.ch_dog, delay)
        relay_controller.on(glob.ch_1_tree, delay)
        relay_controller.on(glob.ch_2_trees, delay)

        relay_controller.off(glob.ch_green_box, delay)
        relay_controller.off(glob.ch_blue_box, delay)
        relay_controller.off(glob.ch_santa, delay)
        relay_controller.off(glob.ch_red_box, delay)
        relay_controller.off(glob.ch_dog, delay)
        relay_controller.off(glob.ch_1_tree, delay)
        relay_controller.off(glob.ch_2_trees, delay)
