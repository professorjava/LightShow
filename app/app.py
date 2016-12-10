import sys
import getopt

from constants import OFF, NORMAL, TEST
from display import Display

always_on = False
debug = OFF
controller_mode = NORMAL


def process_command_line_args(argv):
    try:
        opts, args = getopt.getopt(argv, 'hand:', ['help', 'always_on', 'no_relays', 'debug='])
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                show_usage_and_exit()
            elif opt in ('-a', '--always_on'):
                global always_on
                always_on = True
            elif opt in ('-n', '--no_relays'):
                global controller_mode
                controller_mode = TEST
            elif opt in ('-d', '--debug'):
                global debug
                debug = int(arg)

    except getopt.GetoptError as err:
        print str(err)  # will print something like "option -a not recognized"
        show_usage_and_exit(2)


def show_usage_and_exit(exit_value=None):
    print 'usage: ./LightShow [OPTIONS]'
    print 'Options:'
    print '  -a, --always_on  Ignores time of day restrictions'
    print '  -d, --debug      Print debug information to the console'
    print '  -h, --help       Displays this help information'
    print '  -n, --no_relays  Do not output to the relay controller'

    if exit_value is None:
        sys.exit()
    else:
        sys.exit(exit_value)


def main(argv):
    process_command_line_args(argv)
    display = Display(always_on, debug, controller_mode)
    display.start()

