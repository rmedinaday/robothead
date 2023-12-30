import importlib
try:
    import Jetson.GPIO as GPIO
except:
    import robothead.dummyGPIO as GPIO

def setup_gpio(config, callback):
    pin = config['input']['trigger']['pin']
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=callback)

def cleanup_gpio():
    GPIO.cleanup()
