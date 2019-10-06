""" keypad """

import time
import RPi.GPIO as GPIO


class Keypad:
    """ keypad class """

    # TODO: class needs reconfiguration after better understanding import RPi.GPIO

    def __init__(self):
        """ Set the mode and the row pins as outputs and the column pins as inputs """
        GPIO.setmode(GPIO.BCM)
        # TODO: range needs correction
        for rp in range(0, 4):
            GPIO.setup(rp, GPIO.OUT)
        # TODO: range needs correction
        for cp in range(0, 3):
            GPIO.setup(cp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        """ Use nested loops (discussed above) to determine the
        key currently being pressed on the keypad. """
        # TODO: range needs correction
        for row_pin in range(0, 5):
            GPIO.output(row_pin, GPIO.HIGH)
            for column_pin in range(0, 3):
                if GPIO.input(column_pin) == GPIO.HIGH:
                    time.sleep(10)
                    if GPIO.input(column_pin) == GPIO.HIGH:
                        # TODO: calculate and return signal
                        return 1
                        GPIO.output(row_pin, GPIO.LOW)  # TODO: this line is unreachable
                        break

    def get_next_signal(self):
        """ Calls do_polling until a key press is detected"""
        signal = ""
        while not signal:
            signal = self.do_polling()
        return signal
