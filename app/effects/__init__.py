from random import shuffle
from allelements import AllElements
from app.effects.porch import Porch
from boxes import Boxes
from santa import Santa
from dog import Dog
from trees import OneTree, TwoTrees, AllTrees

effect_list = None


def __init__():
    global effect_list

    effect_list = [
        AllElements.cycle1,
        AllElements.cycle2,
        AllElements.chase1,
        AllElements.chase2,
        AllElements.bounce1,
        AllElements.bounce2,
        AllElements.flash_all,
        AllElements.alternate_porch_and_trees,
        AllElements.one_by_one,
        AllElements.pulse,
        AllElements.alternate,
        AllElements.sliding_doors,
        AllElements.twinkle,
        Porch.cycle1,
        Porch.cycle2,
        Porch.chase1,
        Porch.chase2,
        Porch.bounce1,
        Porch.bounce2,
        Porch.flash_all,
        Porch.alternate,
        Porch.pulse,
        OneTree.strobe,
        OneTree.pulse,
        TwoTrees.strobe,
        TwoTrees.pulse,
        AllTrees.strobe,
        AllTrees.pulse,
        Santa.merry_christmas,
        Santa.flash,
        Santa.strobe,
        Santa.pulse,
        Dog.strobe,
        Dog.pulse,
        Boxes.pulse,
        Boxes.cycle,
        Boxes.chase,
        Boxes.cylon_eyes,
        Boxes.alternate,
    ]
    shuffle(effect_list)


if effect_list is None:
    __init__()
