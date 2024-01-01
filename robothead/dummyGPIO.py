import os
import warnings
import time

BOARD = 10
BCM = 11
TEGRA_SOC = 1000
CVM = 1001

PUD_OFF = 0
PUD_DOWN = 1
PUD_UP = 2

HIGH = 1
LOW = 0

RISING = 1
FALLING = 2
BOTH = 3

UNKNOWN = -1
OUT = 0
IN = 1
HARD_PWM = 43

_channel_data = {}
_gpio_warnings = False
_gpio_mode = None
_channel_configuration = {}

def setwarnings(state):
    global _gpio_warnings
    _gpio_warnings = bool(state)

def setmode(mode):
    global _gpio_mode, _channel_data

    # check if a different mode has been set
    if _gpio_mode and mode != _gpio_mode:
        raise ValueError("A different mode has already been set!")

    mode_map = {
        BOARD: 'BOARD',
        BCM: 'BCM',
        CVM: 'CVM',
        TEGRA_SOC: 'TEGRA_SOC',
    }

    # check if mode parameter is valid
    if mode not in mode_map:
        raise ValueError("An invalid mode was passed to setmode()!")

    _gpio_mode = mode

def getmode():
    return _gpio_mode


# Mutable class to represent a default function argument.
# See https://stackoverflow.com/a/57628817/2767322
class _Default:
    def __init__(self, val):
        self.val = val


# Function used to setup individual pins or lists/tuples of pins as
# Input or Output. Param channels must an integer or list/tuple of integers,
# direction must be IN or OUT, pull_up_down must be PUD_OFF, PUD_UP or
# PUD_DOWN and is only valid when direction in IN, initial must be HIGH or LOW
# and is only valid when direction is OUT
def setup(channels, direction, pull_up_down=PUD_OFF, initial=None, consumer='Jetson-gpio'):
    if direction != OUT and direction != IN:
        raise ValueError("An invalid direction was passed to setup()")

    if direction == OUT and pull_up_down != PUD_OFF:
        raise ValueError("pull_up_down parameter is not valid for outputs")

    if (pull_up_down != PUD_OFF and pull_up_down != PUD_UP and
            pull_up_down != PUD_DOWN):
        raise ValueError("Invalid value for pull_up_down; should be one of"
                         "PUD_OFF, PUD_UP or PUD_DOWN")

# Function used to cleanup channels at the end of the program.
# The param channel can be an integer or list/tuple of integers specifying the
# channels to be cleaned up. If no channel is provided, all channels are
# cleaned
def cleanup(channel=None):
    # warn if no channel is setup
    if _gpio_mode is None:
        if _gpio_warnings:
            warnings.warn("No channels have been set up yet - nothing to "
                          "clean up! Try cleaning up at the end of your "
                          "program instead!", RuntimeWarning)
        return

# Function used to return the current value of the specified channel.
# Function returns either HIGH or LOW
def input(channel):
    return HIGH 


# Function used to set a value to a channel or list/tuple of channels.
# Parameter channels must be an integer or list/tuple of integers.
# Values must be either HIGH or LOW or list/tuple
# of HIGH and LOW with the same length as the channels list/tuple
def output(channels, values):
    pass

# Function used to add threaded event detection for a specified gpio channel.
# Param gpio must be an integer specifying the channel, edge must be RISING,
# FALLING or BOTH. A callback function to be called when the event is detected
# and an integer bounctime in milliseconds can be optionally provided. A optional
# polltime in second can be provided to indicate the max time waiting for an edge.
# Note that one channel only allows one event, which the duplicated event will
# be ignored.
def add_event_detect(channel, edge, callback=None, bouncetime=None, polltime=0.2):
    if (not callable(callback)) and callback is not None:
        raise TypeError("Callback Parameter must be callable")

    # edge must be rising, falling or both
    if edge != RISING and edge != FALLING and edge != BOTH:
        raise ValueError("The edge must be set to RISING, FALLING, or BOTH")

    # if bouncetime is provided, it must be int and greater than 0
    if bouncetime is not None:
        if type(bouncetime) != int:
            raise TypeError("bouncetime must be an integer")

        elif bouncetime < 0:
            raise ValueError("bouncetime must be an integer greater than 0")

# Function used to remove event detection for channel
# Timeout param for the max time to wait for thread (event detecion) to end
def remove_event_detect(channel, timeout=0.5):
    pass


# Function used to check if an event occurred on the specified channel.
# Param channel must be an integer.
# This function return True or False
def event_detected(channel):
    return False 


# Function used to add a callback function to channel, after it has been
# registered for events using add_event_detect()
def add_event_callback(channel, callback):
    if not callable(callback):
        raise TypeError("Parameter must be callable")

# Function used to wait for a edge event in blocking mode, it is also one-shoot.
def wait_for_edge(channel, edge, bouncetime=None, timeout=None):

    # edge provided must be rising, falling or both
    if edge != RISING and edge != FALLING and edge != BOTH:
        raise ValueError("The edge must be set to RISING, FALLING_EDGE "
                         "or BOTH")

    # if bouncetime is provided, it must be int and greater than 0
    if bouncetime is not None:
        if type(bouncetime) != int:
            raise TypeError("bouncetime must be an integer")

        elif bouncetime < 0:
            raise ValueError("bouncetime must be an integer greater than 0")

    # if timeout is specified, it must be an int and greater than 0
    if timeout is not None:
        if type(timeout) != int:
            raise TypeError("Timeout must be an integer")

        elif timeout < 0:
            raise ValueError("Timeout must greater than 0")

    return None


# Function used to check the currently set function of the channel specified.
# Param channel must be an integers. The function returns either IN, OUT,
# or UNKNOWN
def gpio_function(channel):
    return UNKNOWN


class PWM(object):
    def __init__(self, channel, frequency_hz):
        self._started = False
        self._frequency_hz = -1 * frequency_hz

    def start(self, duty_cycle_percent):
        pass

    def ChangeFrequency(self, frequency_hz):
        pass

    def ChangeDutyCycle(self, duty_cycle_percent):
        pass

    def stop(self):
        pass
