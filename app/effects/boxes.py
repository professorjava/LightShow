from glob import *
from effectsutils import FlashEffect, PulseEffect


class Boxes(object):
    # The boxes' lights cycle in a circle
    def cycle(self, relay_controller, debug):
        if debug: print "Boxes.cycle"

        count = 3
        delay = .5
        for x in range(0, count):
            relay_controller.off(ch_all_boxes);
            relay_controller.on(ch_green_box, delay)
            relay_controller.off(ch_all_boxes);
            relay_controller.on(ch_red_box, delay)
            relay_controller.off(ch_all_boxes);
            relay_controller.on(ch_blue_box, delay)
        return

    # An unlit box chases around the circle
    def chase(self, relay_controller, debug):
        if debug: print "Boxes.chase"

        count = 5
        delay = .1
        for x in range(0, count):
            relay_controller.on(ch_all_boxes, delay);
            relay_controller.off(ch_blue_box, delay)
            relay_controller.on(ch_all_boxes, delay);
            relay_controller.off(ch_green_box, delay)
            relay_controller.on(ch_all_boxes, delay);
            relay_controller.off(ch_red_box, delay)
        return

    # The boxes flash relay_controller.on and relay_controller.off together
    def strobe_all(self, relay_controller, debug):
        if debug: print "Boxes.flash"

        FlashEffect().flash(relay_controller, ch_all_boxes)
        return

    # The boxes flash relay_controller.on and relay_controller.off together, speeding up
    def pulse(self, relay_controller, debug):
        if debug: print "Boxes.pulse"

        PulseEffect().pulse(relay_controller, ch_all_boxes)
        return

    # Strobe the green box
    def strobe_green(self, relay_controller, debug):
        if debug: print "Boxes.strobe_green"

        FlashEffect().strobe(relay_controller, ch_green_box)
        return

    # Strobe the blue box
    def strobe_blue(self, relay_controller, debug):
        if debug: print "Boxes.strobe_blue"

        FlashEffect().strobe(relay_controller, ch_blue_box)
        return

    # Strobe the red box
    def strobe_red(self, relay_controller, debug):
        if debug: print "Boxes.strobe_red"

        FlashEffect().strobe(relay_controller, ch_red_box)
        return

    # A single lit box travels back and forth, Like a cylon eye
    def cylon_eyes(self, relay_controller, debug):
        if debug: print "Boxes.cylon_eyes"

        count = 5
        delay = .3
        relay_controller.off(ch_all_boxes)
        for x in range(0, count):
            relay_controller.on(ch_green_box, delay);
            relay_controller.off(ch_green_box)
            relay_controller.on(ch_blue_box, delay);
            relay_controller.off(ch_blue_box)
            relay_controller.on(ch_red_box, delay);
            relay_controller.off(ch_red_box)
            relay_controller.on(ch_blue_box, delay);
            relay_controller.off(ch_blue_box)
        return
