from glob import *
from effectsutils import FlashEffect, PulseEffect, MorseCodeEffect

class Santa(object):

    # Flash santa's nose
    def flash(self, relay_controller, debug):
        if debug: print "Santa.flash"

        FlashEffect().flash(relay_controller, ch_santa)
        return

    # Strobe santa's nose
    def strobe(self, relay_controller, debug):
        if debug: print "Santa.strobe"

        FlashEffect().strobe(relay_controller, ch_santa)
        return

    # The santa flashes on and off, speeding up
    def pulse(self, relay_controller, debug):
        if debug: print "Santa.pulse"

        PulseEffect().pulse(relay_controller, ch_santa)
        return

    # Flash Merry Christmas using Santa's nose
    def merry_christmas(self, relay_controller, debug):
        if debug: print "Santa.merry_christmas";
        
        MorseCodeEffect().display_as_morse(relay_controller, debug, ch_santa, "Merry Christmas")
        return
