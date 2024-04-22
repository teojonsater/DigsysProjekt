class State:
    """
    Grundklass för alla tillstånd i tillståndsmaskinen.
    Representerar ett tillstånd, som kan ha en entry- och exit-funktioner

    :param name: Namnet på tillståndet
    :type name: str

    :var state_machine: En referens till den tillståndsmaskin som tillståndet är en del av
    :type state_machine: StateMachine | None
    """

    def __init__(self, name):
        self.name = name
        self.state_machine = None

    def set_state_machine(self, state_machine):
        self.state_machine = state_machine

    def on_entry(self):
        pass

    def on_exit(self):
        pass

    def handle_event(self, event):
        pass


class StateMachine:
    """
    En enkel tillståndsmaskin som kan hantera tillstånd och övergångar mellan dem.

    :param initial_state: Det initiala tillståndet
    :type initial_state: State

    :var current_state: Det nuvarande tillståndet
    :type current_state: State
    """

    def __init__(self, initial_state):
        self.current_state = initial_state
        self.current_state.set_state_machine(self)
        self.current_state.on_entry()

    def transition_to(self, new_state):
        self.current_state.on_exit()
        self.current_state = new_state
        self.current_state.set_state_machine(self)
        self.current_state.on_entry()

    def handle_event(self, event):
        new_state = self.current_state.handle_event(event)
        if new_state:
            self.transition_to(new_state)
