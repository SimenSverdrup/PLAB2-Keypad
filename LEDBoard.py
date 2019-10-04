""" led board """
import RPi.GPIO as GPIO
import time

class LEDBoard:
    """ LED Board class """
    mode = None
    LED_pin_settings = []  # Helper-array to setup pin setting to light a particular LED (LED i at index i)
    pins = [18, 23, 24]  # this is subject to change, pins[i] refers to pin i

    def __init__(self):
        """ init """
        self.setup()

    def setup(self):
        """ Set the proper mode via: GPIO.setmode(GPIO.BCM)
        The pin settings corresponding to each LED should be saved in a dictionary
        or array such that when the agent requests lighting of the kth LED, your code can fetch the kth
        setting set and send it to a method that performs the proper in/out and high/low assignments.
        """
        self.mode = GPIO.BCM
        GPIO.setmode(GPIO.BCM)  # Might use GPIO.BOARD instead, depends on the input pins
        self.LED_pin_settings = [  # 0=LOW, 1=HIGH and -1=INPUT
            [1, 0, -1],  # to light up LED 0
            [0, 1, -1],  # to light up LED 1
            [-1, 1, 0],  # to light up LED 2
            [-1, 0, 1],  # to light up LED 3
            [1, -1, 0],  # to light up LED 4
            [0, -1, 1]   # to light up LED 5
        ]

    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)  # pin_state should be GPIO.HIGH or GPIO.LOW

    def light_led(self, led, k):
        """ Turn on one of the 6 LEDs for k seconds
        (where k is an argument of the method and led specifies which LED to light), by making the appropriate
        combination of input and output declarations,
        and then making the appropriate HIGH /
        LOW settings on the output pins.
        """
        for pin_index, pin_state in enumerate(self.LED_pin_settings[led]):
            self.set_pin(pin_index, pin_state)
        time.sleep(k)
        for pin_index, pin_state in enumerate(self.LED_pin_settings[led]):
            self.set_pin(pin_index, -1)  # reset the pins to turn off the LED

    def flash_all_leds(self):
        """ Flash all 6 LEDs on and off, used when the user enters the wrong passcode """
        # TODO

    def twinkle_all_leds(self):
        """  The lightshow to run when the user successfully authenticates """
        # TODO

    def startup_lightshow(self):
        """ The lightshow sequence to run when the keypad is started """
        for rounds in range(3):  # clockwise
            for index1 in range(6):
                for index2 in range(3):
                    self.set_pin(index2, self.LED_pin_settings[index1][index2])
                time.sleep(0.15)

    def shutdown_lightshow(self):
        """The lightshow sequence to run when the keypad is shut down"""
        for rounds in range(3):
            for index1 in range(5, -1, -1):  # counterclockwise
                for index2 in range(3):
                    self.set_pin(index2, self.LED_pin_settings[index1][index2])
                time.sleep(0.15)

