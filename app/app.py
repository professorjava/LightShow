import sys
import getopt
from display import Display

always_on = False
debug = False
NORMAL = 'Normal'
TEST = 'Test'
controller_mode = NORMAL


def process_command_line_args(argv):
    try:
        opts, args = getopt.getopt(argv, "hadn", ["help", "always_on", "debug", "no_relays"])
        for opt, arg in opts:
            if opt in ('-h', "--help"):
                show_usage_and_exit()
            elif opt in ("-a", "--always_on"):
                global always_on
                always_on = True
            elif opt in ("-d", "--debug"):
                global debug
                debug = True
            elif opt in ("-n", "--no_relays"):
                global controller_mode
                controller_mode = TEST

    except getopt.GetoptError:
        show_usage_and_exit(2)
    return


def show_usage_and_exit(exit_value=None):
    print 'usage: sudo python LightShow [OPTIONS]'
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

