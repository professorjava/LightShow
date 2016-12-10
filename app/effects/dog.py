from glob import ch_dog
from effectsutils import FlashEffect, PulseEffect

class Dog(object):

    # Flash Dog
    def flash(self, relay_controller, debug):
        if debug: print "Dog.flash"

        FlashEffect().flash(relay_controller, ch_dog);
        return

    # Strobe Dog
    def strobe(self, relay_controller, debug):
        if debug: print "Dog.strobe"

        FlashEffect().strobe(relay_controller, ch_dog);
        return

    # The Dog flashes on and off, speeding up
    def pulse(self, relay_controller, debug):
        if debug: print "Dog.pulse"

        PulseEffect().pulse(relay_controller, ch_dog);
        return
