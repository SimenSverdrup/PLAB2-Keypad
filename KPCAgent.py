""" KPC Agent """

from Keypad import Keypad
from LEDBoard import LEDBoard
from FSM import FiniteStateMachine


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
        FiniteStateMachine(self)

    def init_passcode_entry(self):
        """ Clear the passcode buffer and initiate a power up lighting sequence on the LED Board """
        self.input_buffer = ""
        self.led_board_pointer.startup_lightshow()

    def get_next_signal(self):
        # TODO: function need configuration, override_signal might have been misunderstood
        #  self.input_buffer should be filled here, I think
        """ Return the override-signal or query keypad for next signal """
        if self.override_signal:
            return_signal = self.override_signal
            self.override_signal = None
            return return_signal
        else:
            return self.keypad_pointer.get_next_signal()

    def add_to_buffer(self, signal):
        """ Add signal from FSM to self.input_buffet """
        print("RUN ADD TO BUFFER: ", signal)
        self.input_buffer += (signal)

    def verify_login(self):
        """ Check that the password just entered via the keypad matches that in the password file.
        Store the result (Y or N) in the override-signal.
        Also, this should call the LED Board to initiate the
        appropriate lighting pattern for login success or failure. """
        print("RUN VERIFY LOGIN")
        print("INPUT_BUFFER: ", self.input_buffer)
        f = open(self.password_path, "r")
        passcode = ""
        if f.mode == "r":
            passcode = f.readline()
        f.close()
        print("PASSCODE: ", passcode)
        if self.input_buffer == passcode:  # the input buffer should contain the current passcode input
            #self.override_signal = "Y"
            self.twinkle_all_leds()
        else:
            #self.override_signal = "N"
            self.flash_leds()

    def validate_passcode_change(self, new_passcode):
        """  Check that the new password is legal. If so, write the new password in the password file.
        A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
        As in verify login, this should use the LED Board to signal success or failure in changing the password. """
        if self.is_legal_passcode(new_passcode):
            f = open(self.password_path, "w")  # open file for writing
            if f.mode == "w":
                f.write(new_passcode)
            f.close()
            self.twinkle_all_leds()
        else:
            self.flash_leds()

    def is_legal_passcode(self, passcode):
        """ Returns true if passcode is legal, false if not.
         A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9."""
        return (len(passcode) >= 4) and passcode.isdigit()
        # Return true if all characters in the string are digits
        # and there is at least one character, false otherwise

    def light_one_led(self, Lid, Ldur):
        """  Using values stored in the Lid and Ldur slots,
        call the LED Board and request that LED # Lid be turned on for Ldur seconds. """
        self.led_board_pointer.light_led(Lid, Ldur)

    def flash_leds(self):
        """ Call the LED Board and request the flashing of all LEDs. """
        self.led_board_pointer.flash_all_leds()

    def twinkle_all_leds(self):
        """  Call the LED Board and request the twinkling of all LEDs. """
        self.led_board_pointer.twinkle_all_leds()

    def shutdown_lightshow(self):
        """ Call the LED Board to initiate the power down lighting sequence. """
        self.led_board_pointer.shutdown_lightshow()
