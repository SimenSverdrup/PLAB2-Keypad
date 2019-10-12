""" led board """
import RPi.GPIO as GPIO
import time
import random as rand

class LEDBoard:
    """ LED Board class """
    mode = None
    LED_pin_settings = []  # Helper-array to setup pin setting to light a particular LED (LED i at index i)
    pins = [16, 20, 21]  # this is subject to change, pins[i] refers to pin i

    def __init__(self):
        """ init """
        self.setup()

    def setup(self):
        """ Set the proper mode via: GPIO.setmode(GPIO.BCM)
        The pin settings corresponding to each LED should be saved in a dictionary
        or array such that when the agent requests lighting of the kth LED, your code can fetch the kth
        setting set and send it to a method that performs the proper in/out and high/low assignments. """
        self.mode = GPIO.BCM
        GPIO.setmode(GPIO.BCM)  # Might use GPIO.BOARD instead, depends on the input pins
        self.LED_pin_settings = [  # 0=LOW, 1=HIGH and -1=INPUT
            [1, 0, -1],     # to light up LED 0
            [0, 1, -1],     # to light up LED 1
            [0, -1, 1],     # to light up LED 2
            [-1, 0, 1],     # to light up LED 3
            [-1, 1, 0],     # to light up LED 4
            [1, -1, 0]      # to light up LED 5
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
        LOW settings on the output pins. """
        for pin_index, pin_state in enumerate(self.LED_pin_settings[led]):
            self.set_pin(pin_index, pin_state)
        time.sleep(k)
        for pin_index in self.LED_pin_settings[led]:
            self.set_pin(pin_index, -1)  # reset the pins to turn off the LED

    def flash_all_leds(self):
        """ Flash all 6 LEDs on and off, used when the user enters the wrong passcode.
        To light more than one at a time, you need to run a refresh loop that
        keeps the desired state of the LEDs in an array and refreshes the display,
        turning on the LEDs that need to be on before moving on to the next.
        It must do this sufficiently fast so that it appears that more than one of the LEDs is on at the same time.
        The more LEDs you use when it comes to making it appear that more than one LED is on at a time,
        the less time the LED will actually be lit, and the dimmer the LEDs will become."""
        for times in range(3):  # flash all the LEDs three times on and off
            for rounds in range(100):  # probably have to fine-tune the amount of rounds
                for led in range(6):
                    self.light_led(led, 0.001)  # probably have to fine-tune the input-time
            time.sleep(0.4)  # probably have to fine-tune the time between flashes

    def twinkle_all_leds(self):
        """  The lightshow to run when the user successfully authenticates """
        for rounds in range(50):  # probably have to fine-tune the amount of rounds
            self.light_led(rand.randint(0, 5), 0.05)  # probably have to fine-tune the input-time

    def startup_lightshow(self):
        """ The lightshow sequence to run when the keypad is started """
        for rounds in range(3):  # 3 rounds, clockwise
            for led in range(6):
                self.light_led(led, 0.15)  # probably have to fine-tune the input-time

    def shutdown_lightshow(self):
        """The lightshow sequence to run when the keypad is shut down"""
        for rounds in range(3):
            for led in range(5, -1, -1):  # 3 rounds,  counterclockwise
                self.light_led(led, 0.15)  # probably have to fine-tune the input-time
