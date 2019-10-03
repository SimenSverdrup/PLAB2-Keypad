""" KPC Agent """

from Keypad import Keypad
from LEDBoard import LEDBoard


class KPCAgent:
    """ KPC Agent class """

    keypad_pointer = None
    led_board_pointer = None
    input_buffer = None
    password_path = "password.txt"
    override_signal = None
    led_id = None
    led_duration = None

    def __init__(self):
        """ init """
        self.keypad_pointer = Keypad()
        self.led_board_pointer = LEDBoard()
        self.init_passcode_entry()
        # TODO? : add more method calls

    def init_passcode_entry(self):
        """ Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED Board """
        self.input_buffer = ""
        # TODO: initiate correct led lights

    # TODO: function need configuration, override_signal might have been misunderstood
    def get_next_signal(self):
        """ Return the override-signal or query keypad for next signal """
        if self.override_signal:
            return_signal = self.override_signal
            self.override_signal = None
            return return_signal
        else:
            return self.keypad_pointer.get_next_signal()

    def verify_login(self):
        """ Check that the password just entered via the keypad matches that in the pass- word file.
        Store the result (Y or N) in the override-signal.
        Also, this should call the LED Board to initiate the
        appropriate lighting pattern for login success or failure. """
        # TODO

    def validate_passcode_change(self):
        """  Check that the new password is legal. If so, write the new pass- word in the password file.
        A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
        As in verify login, this should use the LED Board to signal success or failure in changing the password. """
        # TODO

    def light_one_led(self):
        """  Using values stored in the Lid and Ldur slots,
        call the LED Board and request that LED # Lid be turned on for Ldur seconds. """
        # TODO

    def flash_leds(self):
        """ Call the LED Board and request the flashing of all LEDs. """
        # TODO

    def light_one_led(self):
        """  Call the LED Board and request the twinkling of all LEDs. """
        # TODO

    def light_one_led(self):
        """ Call the LED Board to initiate the ”power down” lighting sequence. """
        # TODO
