""" finite state machine """

# TODO: remove on launch
def example_rule_condition(state, signal):
    return state == "s0" and signal == 1


# TODO: remove on launch
example_rule_consequence = ["s1", 1]


class FiniteStateMachine:
    """ Finite state machine class """

    states = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8"]
    state = "s0"
    KPC_pointer = None
    FSM_rule_list = []

    def __init__(self, agent):
        """ init """
        self.KPC_pointer = agent
        self.main_loop()
        self.add_rule(([example_rule_condition, example_rule_consequence]))

    def add_rule(self, new_rule):
        """ Adds a new rule to end of FSM_rule_list """
        self.FSM_rule_list.append(new_rule)

    def get_next_signal(self):
        """ Query the agent for next signal """
        return self.KPC_pointer.get_next_signal()

    def run_rules(self, signal):
        """ Try each rule until one of the rules is fired """
        for rule in self.FSM_rule_list:
            if self.apply_rule(rule, signal):
                self.fire_rule(rule)
                break

    def apply_rule(self, rule, signal):
        """ Check whether the conditions of a rule are met """
        return rule[0](self.state, signal)

    def fire_rule(self, rule):
        """ Use the consequent of a rule to set the next state of the FSM
        and call the appropriate agent action method """
        self.state = rule[1][0]
        if rule[1][1] == 0:
            self.KPC_pointer.light_one_led()
        elif rule[1][1] == 1:
            self.KPC_pointer.flash_leds()
            # TODO: implement multiple different agent actions

    def main_loop(self):
        """ The loop running the state machine until final state """
        print("START FSM MAIN LOOP")
        self.state = "s0"
        while self.state != "s1":
            signal = self.get_next_signal
            if signal:
                self.run_rules(signal)
        print("Final state reached.")
