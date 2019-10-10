""" finite state machine """


def state_0_rule_condition(state, signal):
    return state == "s0" and signal != '*'

def state_0_rule_condition_2(state, signal):
    return state == 's0' and signal == '*'

def state_1_rule_condition(state, signal):
    return state == 's1' and signal in ['1', '2', '3', '4', '5', '6']

def state_2_rule_condition(state, signal):
    return state == 's2' and signal not in ['*', '#']
   
def state_2_rule_condition_2(state, signal):
    return state == 's2' and signal == '*'
  

state_0_rule_consequence = ["s0", 0]
state_0_rule_consequence_2 = ["s1", 1]
state_1_rule_consequence = ["s2", 2]
state_2_rule_consequence = ["s2", 3]
state_2_rule_consequence_2 = ["s1", 4]


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
        self.add_rule([state_0_rule_condition, state_0_rule_consequence])
        self.add_rule([state_0_rule_condition_2, state_0_rule_consequence_2])
        self.add_rule([state_1_rule_condition, state_1_rule_consequence])
        self.add_rule([state_2_rule_condition, state_2_rule_consequence])
        self.add_rule([state_2_rule_condition_2, state_2_rule_consequence_2])
        #TODO: add multiple rules
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
        print("MAYBE NEW STATE: ", rule[1][0])

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
            self.KPC_pointer.light_one_led()
            self.state = rule[1][0]       
        # TODO: implement multiple different agent actions

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
