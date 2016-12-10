import threading
import time

import pygame

from color_constants import GREEN, BLUE, CRIMSON, CORNSILK3, FORESTGREEN, WHITE


class Visualization(object):
    CH_1 = 1  # Broken relay
    CH_2 = 2  # Red box
    CH_4 = 4  # Blue box
    CH_8 = 8  # Green box
    CH_16 = 16  # Santa
    CH_32 = 32  # Dog
    CH_64 = 64  # 1 tree
    CH_128 = 128  # 2 trees
    CHANNELS = (CH_1, CH_2, CH_4, CH_8, CH_16, CH_32, CH_64, CH_128)

    WIDTH = 50
    HEIGHT = 50
    MIN_WIDTH = 400

    ON = 0
    OFF = 2

    GREEN_BOX = CH_8
    SANTA = CH_16
    BLUE_BOX = CH_4
    RED_BOX = CH_2
    DOG = CH_32
    ONE_TREE = CH_64
    TWO_TREES = CH_128

    POS_TWO_TREES = 0
    POS_ONE_TREE = 1
    POS_DOG = 2
    POS_RED_BOX = 3
    POS_BLUE_BOX = 4
    POS_SANTA = 5
    POS_GREEN_BOX = 6
    POS_CH_1 = 7

    # The display is big-endian. 128 bit is on left, 1 bit on right.
    locations = {
        CH_1: [POS_CH_1 * WIDTH, 0, WIDTH, HEIGHT],
        GREEN_BOX: [POS_GREEN_BOX * WIDTH, 0, WIDTH, HEIGHT],
        SANTA: [POS_SANTA * WIDTH, 0, WIDTH, HEIGHT],
        BLUE_BOX: [POS_BLUE_BOX * WIDTH, 0, WIDTH, HEIGHT],
        RED_BOX: [POS_RED_BOX * WIDTH, 0, WIDTH, HEIGHT],
        DOG: [POS_DOG * WIDTH, 0, WIDTH, HEIGHT],
        ONE_TREE:  [[POS_ONE_TREE*WIDTH + WIDTH/2, 0], [POS_ONE_TREE*WIDTH, HEIGHT],
                    [POS_ONE_TREE*WIDTH + WIDTH-1, HEIGHT]],
        TWO_TREES: [[POS_TWO_TREES*WIDTH + WIDTH/2, 0], [POS_TWO_TREES*WIDTH, HEIGHT],
                    [POS_TWO_TREES*WIDTH + WIDTH-1, HEIGHT]],
    }

    shapes = {
        CH_1: lambda s, w: None,
        GREEN_BOX: lambda s, w: pygame.draw.rect(s, GREEN, Visualization.locations[Visualization.GREEN_BOX], w),
        SANTA: lambda s, w: pygame.draw.ellipse(s, CRIMSON, Visualization.locations[Visualization.SANTA], w),
        BLUE_BOX: lambda s, w: pygame.draw.rect(s, BLUE, Visualization.locations[Visualization.BLUE_BOX], w),
        RED_BOX: lambda s, w: pygame.draw.rect(s, CRIMSON, Visualization.locations[Visualization.RED_BOX], w),
        DOG: lambda s, w: pygame.draw.ellipse(s, CORNSILK3, Visualization.locations[Visualization.DOG], w),
        ONE_TREE: lambda s, w: pygame.draw.polygon(s, FORESTGREEN, Visualization.locations[Visualization.ONE_TREE], w),
        TWO_TREES: lambda s, w: pygame.draw.polygon(s, FORESTGREEN, Visualization.locations[Visualization.TWO_TREES], w),
    }

    def __init__(self):
        self.screen = None
        self.relays = 0
        self.done = False
        self.lock = threading.Lock()

    def update(self, relays):
        try:
            self.lock.acquire(True)
            self.relays = relays
            self.lock.release()
        except:
            self.lock.release()
            raise

    def start(self):
        pygame.init()
        size = (max(self.WIDTH * len(self.locations), Visualization.MIN_WIDTH), self.HEIGHT)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Test Window")

        clock = pygame.time.Clock()
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self._draw()
            clock.tick(60)
            time.sleep(0)

        pygame.quit()

    def stop(self):
        self.done = True

    def _draw(self):
        self.screen.fill(WHITE)
        for ch in self.CHANNELS:
            try:
                self.lock.acquire(True)
                if self.relays & ch == 0:
                    width = Visualization.OFF
                else:
                    width = Visualization.ON
            finally:
                self.lock.release()

            self.shapes[ch](self.screen, width)
        pygame.display.flip()


if __name__ == '__main__':
    Visualization().start()
