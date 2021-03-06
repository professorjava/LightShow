# Channel constants
CH_NONE = 0

CH_BROKEN = 1

CH_GREEN_BOX = 8
CH_BLUE_BOX = 4
CH_RED_BOX = 2
CH_ALL_BOXES = CH_GREEN_BOX + CH_RED_BOX + CH_BLUE_BOX
CH_ALL_BOXES_LIST = (CH_GREEN_BOX, CH_BLUE_BOX, CH_RED_BOX)

CH_SANTA = 16
CH_DOG = 32
CH_ALL_PORCH = CH_ALL_BOXES + CH_SANTA + CH_DOG
CH_ALL_PORCH_LIST = (CH_GREEN_BOX, CH_SANTA, CH_BLUE_BOX, CH_RED_BOX, CH_DOG)

CH_1_TREE = 64
CH_2_TREES = 128
CH_ALL_TREES = CH_1_TREE + CH_2_TREES
CH_ALL_TREE_LIST = (CH_1_TREE, CH_2_TREES)

CH_ALL = CH_ALL_BOXES + CH_SANTA + CH_DOG + CH_ALL_TREES
CH_ALL_LIST = (CH_GREEN_BOX, CH_SANTA, CH_BLUE_BOX, CH_RED_BOX, CH_DOG, CH_1_TREE, CH_2_TREES)

FLASH_COUNT = 3
FLASH_DELAY = .5

ALTERNATE_COUNT = 8
ALTERNATE_DELAY = .3

STROBE_COUNT = 7
STROBE_DELAY = .1


