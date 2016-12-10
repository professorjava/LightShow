import time
from time import strftime
from pygame.threads import Thread
import effects
from effects import constants
from constants import TEST, NORMAL, BASIC
from effects.effectsutils import Idle
from visualization import Visualization
from relay_controller import TestRelayController, FtdiRelayController


class Display(object):
    # Time restriction constants
    morning_hour_earliest = 5
    morning_hour_latest = 7
    evening_hour_earliest = 17
    evening_hour_latest = 23

    # Time delay constants
    active_idle_seconds = 5
    inactive_idle_seconds = 60

    def __init__(self, always_on, debug, controller_mode):
        self.always_on = always_on
        self.debug = debug

        self.visualizer = Visualization()
        self.controller = self._create_relay_controller(controller_mode)

    def start(self):
        t = Thread(target=self.visualizer.start)
        t.start()

        self.controller.on(constants.CH_ALL)

        effect_counter = 0
        while True:
            try:
                time1 = time.localtime()
                if ((Display.morning_hour_earliest <= time1.tm_hour < Display.morning_hour_latest)
                        or (Display.evening_hour_earliest <= time1.tm_hour < Display.evening_hour_latest)
                        or self.always_on):
                    self._show_effect(effect_counter)
                    effect_counter += 1
                else:
                    self._do_not_show_effect(time1)

            except KeyboardInterrupt:
                print 'Interrupted by Ctrl+C'
                break
            except Exception as e:
                print e.message

        self.visualizer.stop()
        t.join(5)

    def _show_effect(self, effect_counter):
        effect = effects.effect_list[effect_counter % len(effects.effect_list)]
        effect(self.controller, self.debug)
        Idle().idle(self.controller, self.debug, True, Display.active_idle_seconds)

    def _do_not_show_effect(self, time1):
        if self.debug >= BASIC:
            print strftime('%H:%M:%S', time1), 'is outside the allowed time window'
        Idle().idle(self.controller, self.debug, False, Display.inactive_idle_seconds)

    def _create_relay_controller(self, controller_mode):
        if controller_mode == TEST:
            if self.debug >= BASIC:
                print 'Setting relay_controller to TestRelayController'
            return TestRelayController(self.visualizer, self.debug)

        elif controller_mode == NORMAL:
            if self.debug >= BASIC:
                print 'Setting relay_controller to FtdiRelayController'
            return FtdiRelayController(self.visualizer, None, self.debug)

        else:
            raise ValueError('Unrecognized mode %s' % controller_mode)
