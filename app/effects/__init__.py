from random import shuffle
from allelements import AllElements
from boxes import Boxes
from santa import Santa
from dog import Dog
from trees import OneTree, TwoTrees, AllTrees

effect_list = None


def __init__():
    global effect_list

    effect_list = [
        # AllElements.cycle1,
        AllElements.cycle2,
        # AllElements.chase1,
        AllElements.chase2,
        # AllElements.bounce1,
        # AllElements.bounce2,
        # AllElements.flash_all,
        # AllElements.flash_porch,
        # AllElements.flash_trees,
        # AllElements.alternate_porch_and_trees,
        # OneTree().flash,
        # OneTree().strobe,
        # OneTree().pulse,
        # TwoTrees().flash,
        # TwoTrees().strobe,
        # TwoTrees().pulse,
        # AllTrees().flash,
        # AllTrees().strobe,
        # AllTrees().pulse,
        # Santa().merry_christmas,
        # Santa().flash,
        # Santa().strobe,
        # Santa().pulse,
        # Dog().strobe,
        # Dog().pulse,
        # AllElements().one_by_one,
        # AllElements().cycle,
        # AllElements().chase,
        # AllElements().flash,
        # AllElements().flash2,
        # AllElements().flash3,
        # AllElements().pulse,
        # Boxes().pulse,
        # Boxes().strobe_all,
        # Boxes().strobe_green,
        # Boxes().strobe_blue,
        # Boxes().strobe_red,
        # Boxes().cycle,
        # Boxes().chase,
        # Boxes().cylon_eyes,
    ]
    shuffle(effect_list)


if effect_list is None:
    __init__()
