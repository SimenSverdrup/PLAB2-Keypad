""" finite state machine """

from FSMrules import FSMrules


class FiniteStateMachine:
    """ Finite state machine class """

    states = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8"]
    state = "s0"
    signal = None
    KPC_pointer = None
    FSM_rule_list = []

    def __init__(self, agent):
        """ init """
        self.KPC_pointer = agent
        FSMrules(self)
        self.main_loop()

    def add_rule(self, new_rule):
        """ Adds a new rule to end of FSM_rule_list """
        self.FSM_rule_list.append(new_rule)

    def get_next_signal(self):
        """ Query the agent for next signal """
        return self.KPC_pointer.get_next_signal()

    def run_rules(self):
        """ Try each rule until one of the rules is fired """
        for rule in self.FSM_rule_list:
            print("RULE: ", rule)
            if self.apply_rule(rule):
                self.fire_rule(rule)
                break

    def apply_rule(self, rule):
        """ Check whether the conditions of a rule are met """
        print("RUN APPLY RULE: ", rule[0](self.state, self.signal))
        return rule[0](self.state, self.signal)

    def fire_rule(self, rule):
        """ Use the consequent of a rule to set the next state of the FSM
        and call the appropriate agent action method """
        print("TRIGGER SIGNAL: ", rule[1][1])

        if rule[1][1] == 0:
            self.KPC_pointer.add_to_buffer(self.signal)
            self.state = rule[1][0]
        elif rule[1][1] == 1:
            login = self.KPC_pointer.verify_login()
            if login:
                self.state = rule[1][0]  
        elif rule[1][1] == 2:
            self.KPC_pointer.set_led_id(self.signal)
            self.state = rule[1][0]     
        elif rule[1][1] == 3:
            self.KPC_pointer.add_to_buffer(self.signal)
            self.state = rule[1][0]
        elif rule[1][1] == 4:
            self.KPC_pointer.input_buffer_to_led_duration()
            self.KPC_pointer.light_one_led()
            self.state = rule[1][0]
        elif rule[1][1] == 5:
            self.KPC_pointer.init_passcode_entry()
            self.state = rule[1][0]
        elif rule[1][1] == 6:
            valid_passcode = self.KPC_pointer.set_passcode_change()
            if valid_passcode:
                self.state = rule[1][0]   
        elif rule[1][1] == 7:
            validated_passcode = self.KPC_pointer.validate_passcode_change()
            if validated_passcode:
                self.state = rule[1][0]     
            else:
                self.state = "s3" 
        elif rule[1][1] == 8:
            end_session = self.KPC_pointer.test_end(self.signal)
            if end_session:
                self.state = rule[1][0]

    def main_loop(self):
        """ The loop running the state machine until final state """
        self.state = "s0"
        while self.state != "s4":
            print("CURRENT STATE: ", self.state)
            self.signal = self.get_next_signal()
            if self.signal:
                print("SIGNAL: ", self.signal)
                self.run_rules()
            print("\n")
        print("Final state reached.")
