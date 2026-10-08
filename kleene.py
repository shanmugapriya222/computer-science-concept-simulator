class State:
    def __init__(self):
        self.transitions = {}


class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


def add_transition(state, symbol, next_state):
    if symbol not in state.transitions:
        state.transitions[symbol] = []
    state.transitions[symbol].append(next_state)


def regex_to_nfa(regex):
    """
    Convert a simple regular expression into an NFA.

    Supported:
    |  -> Union
    *  -> Kleene Star
    +  -> Positive Closure
    () -> Grouping
    Concatenation
    """

    regex = regex.replace(" ", "")

    if not regex:
        raise ValueError("Regular expression cannot be empty.")

    tokens = add_concat_operator(regex)
    postfix = to_postfix(tokens)

    stack = []

    for token in postfix:
        if token == ".":
            right = stack.pop()
            left = stack.pop()

            add_transition(left.accept, "ε", right.start)
            stack.append(NFA(left.start, right.accept))

        elif token == "|":
            right = stack.pop()
            left = stack.pop()

            start = State()
            accept = State()

            add_transition(start, "ε", left.start)
            add_transition(start, "ε", right.start)

            add_transition(left.accept, "ε", accept)
            add_transition(right.accept, "ε", accept)

            stack.append(NFA(start, accept))

        elif token == "*":
            nfa = stack.pop()

            start = State()
            accept = State()

            add_transition(start, "ε", nfa.start)
            add_transition(start, "ε", accept)

            add_transition(nfa.accept, "ε", nfa.start)
            add_transition(nfa.accept, "ε", accept)

            stack.append(NFA(start, accept))

        elif token == "+":
            nfa = stack.pop()

            start = State()
            accept = State()

            add_transition(start, "ε", nfa.start)

            add_transition(nfa.accept, "ε", nfa.start)
            add_transition(nfa.accept, "ε", accept)

            stack.append(NFA(start, accept))

        else:
            start = State()
            accept = State()

            add_transition(start, token, accept)

            stack.append(NFA(start, accept))

    if len(stack) != 1:
        raise ValueError("Invalid regular expression.")

    return stack[0]


def add_concat_operator(regex):
    result = []

    for i, current in enumerate(regex):
        result.append(current)

        if i + 1 < len(regex):
            next_char = regex[i + 1]

            if (
                (current.isalnum() or current == ")" or current in "*+")
                and
                (next_char.isalnum() or next_char == "(")
            ):
                result.append(".")

    return result


def to_postfix(tokens):
    precedence = {
        "|": 1,
        ".": 2,
        "*": 3,
        "+": 3
    }

    output = []
    operators = []

    for token in tokens:

        if token.isalnum():
            output.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())

            if not operators:
                raise ValueError("Mismatched parentheses.")

            operators.pop()

        elif token in precedence:

            while (
                operators
                and operators[-1] != "("
                and precedence[operators[-1]] >= precedence[token]
            ):
                output.append(operators.pop())

            operators.append(token)

        else:
            raise ValueError(f"Unsupported symbol: {token}")

    while operators:
        if operators[-1] == "(":
            raise ValueError("Mismatched parentheses.")
        output.append(operators.pop())

    return output


def epsilon_closure(states):
    closure = set(states)
    stack = list(states)

    while stack:
        state = stack.pop()

        for next_state in state.transitions.get("ε", []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return closure


def move(states, symbol):
    result = set()

    for state in states:
        for next_state in state.transitions.get(symbol, []):
            result.add(next_state)

    return result


def accepts(nfa, input_string):
    current_states = epsilon_closure({nfa.start})

    for symbol in input_string:
        current_states = epsilon_closure(
            move(current_states, symbol)
        )

    return nfa.accept in current_states


def get_transitions(nfa):
    """
    Return all NFA transitions in a readable format.
    """

    transitions = []
    visited = set()
    queue = [nfa.start]

    state_numbers = {nfa.start: 0}
    next_number = 1

    while queue:
        state = queue.pop(0)

        if state in visited:
            continue

        visited.add(state)

        for symbol, destinations in state.transitions.items():

            for destination in destinations:

                if destination not in state_numbers:
                    state_numbers[destination] = next_number
                    next_number += 1
                    queue.append(destination)

                transitions.append(
                    (
                        state_numbers[state],
                        symbol,
                        state_numbers[destination]
                    )
                )

    return transitions, state_numbers[nfa.start], state_numbers[nfa.accept]