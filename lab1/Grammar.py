import random

class Grammars:
    def __init__(self, productions, start_symbol):
        self.productions = productions
        self.start_symbol = start_symbol

    def generate_string(self):
        return self._generate_string(self.start_symbol)

    def _generate_string(self, symbol):
        if symbol not in self.productions:
            return symbol
        production = random.choice(self.productions[symbol])
        return ''.join(self._generate_string(s) for s in production)

    def to_finite_automaton(self):
        start_state = 0
        auto = {start_state: {}}
        state_count = 1

        for symbol in self.productions:
            for production in self.productions[symbol]:
                current_state = start_state
                for s in production:
                    if s not in auto[current_state]:

                        auto[current_state][s] = state_count
                        auto[state_count] = {}
                        state_count += 1
                    current_state = auto[current_state][s]
                if current_state not in auto:
                    auto[current_state] = {}
                auto[current_state][''] = start_state


        return auto