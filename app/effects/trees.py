import inspect

from app.constants import BASIC
from constants import CH_1_TREE, CH_2_TREES, CH_ALL_TREES
from effectsutils import FlashEffects


class OneTree(object):
    @staticmethod
    def flash(relay_controller, debug):
        """Flash OneTree"""
        if debug >= BASIC:
            print "OneTree.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.flash(relay_controller, CH_1_TREE)

    @staticmethod
    def strobe(relay_controller, debug):
        """Strobe OneTree"""
        if debug >= BASIC:
            print "OneTree.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.strobe(relay_controller, CH_1_TREE)

    @staticmethod
    def pulse(relay_controller, debug):
        """The OneTree flashes on and off, speeding up"""
        if debug >= BASIC:
            print "OneTree.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.pulse(relay_controller, CH_1_TREE)


class TwoTrees(object):
    @staticmethod
    def flash(relay_controller, debug):
        """Flash TwoTrees"""
        if debug >= BASIC:
            print "TwoTrees.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.flash(relay_controller, CH_2_TREES)

    @staticmethod
    def strobe(relay_controller, debug):
        """Strobe TwoTrees"""
        if debug >= BASIC:
            print "TwoTrees.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.strobe(relay_controller, CH_2_TREES)

    @staticmethod
    def pulse(relay_controller, debug):
        """The TwoTrees flashes on and off, speeding up"""
        if debug >= BASIC:
            print "TwoTrees.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.pulse(relay_controller, CH_2_TREES)


class AllTrees(object):
    @staticmethod
    def flash(relay_controller, debug):
        """Flash AllTrees"""
        if debug >= BASIC:
            print "AllTrees.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.flash(relay_controller, CH_ALL_TREES)

    @staticmethod
    def strobe(relay_controller, debug):
        """Strobe AllTrees"""
        if debug >= BASIC:
            print "AllTrees.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.strobe(relay_controller, CH_ALL_TREES)

    @staticmethod
    def pulse(relay_controller, debug):
        """The AllTrees flashes on and off, speeding up"""
        if debug >= BASIC:
            print "AllTrees.%s" % inspect.currentframe().f_code.co_name

        FlashEffects.pulse(relay_controller, CH_ALL_TREES)
