from glob import ch_1_tree, ch_2_trees, ch_all_trees
from effectsutils import FlashEffect, PulseEffect

class OneTree(object):

    # Flash OneTree
    def flash(self, relay_controller, debug):
        if debug: print "OneTree.flash"

        FlashEffect().flash(relay_controller, ch_1_tree)

    # Strobe OneTree
    def strobe(self, relay_controller, debug):
        if debug: print "OneTree.strobe"

        FlashEffect().strobe(relay_controller, ch_1_tree)

    # The OneTree flashes on and off, speeding up
    def pulse(self, relay_controller, debug):
        if debug: print "OneTree.pulse"

        PulseEffect().pulse(relay_controller, ch_1_tree)

class TwoTrees(object):

    # Flash TwoTrees
    def flash(self, relay_controller, debug):
        if debug: print "TwoTrees.flash"

        FlashEffect().flash(relay_controller, ch_2_trees)

    # Strobe TwoTrees
    def strobe(self, relay_controller, debug):
        if debug: print "TwoTrees.strobe"

        FlashEffect().strobe(relay_controller, ch_2_trees)

    # The TwoTrees flashes on and off, speeding up
    def pulse(self, relay_controller, debug):
        if debug: print "TwoTrees.pulse"

        PulseEffect().pulse(relay_controller, ch_2_trees)

class AllTrees(object):

    # Flash AllTrees
    def flash(self, relay_controller, debug):
        if debug: print "AllTrees.flash"

        FlashEffect().flash(relay_controller, ch_all_trees)

    # Strobe AllTrees
    def strobe(self, relay_controller, debug):
        if debug: print "AllTrees.strobe"

        FlashEffect().strobe(relay_controller, ch_all_trees)

    # The AllTrees flashes on and off, speeding up
    def pulse(self, relay_controller, debug):
        if debug: print "AllTrees.pulse"

        PulseEffect().pulse(relay_controller, ch_all_trees)
    # Alternate between the 1 tree and 2 trees
