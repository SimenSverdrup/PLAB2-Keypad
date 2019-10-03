""" led board """


class LEDBoard:
    """ LED Board class """

    # TODO: implement class after better understanding

    mode = None

    def __init__(self):
        """ init """
        self.setup()

    def setup(self):
        """ Set the proper mode via: GPIO.setmode(GPIO.BCM) """
        self.mode = None
        # TODO

    def light_led(self):
        """ Turn on one of the 6 LEDs by making the appropriate
        combination of input and output declarations,
        and then making the appropriate HIGH /
        LOW settings on the output pins.
        """
        # TODO

    def flash_all_leds(self, k):
        """ Flash all 6 LEDs on and off for k seconds,
         where k is an argument of the method. """
        # TODO

    def twinkle_all_leds(self, k):
        """  Turn all LEDs on and off in sequence for k seconds,
        where k is an argument of the method. """
        # TODO
