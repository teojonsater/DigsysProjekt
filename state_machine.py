class State:
    """
    Grundklass för alla tillstånd i tillståndsmaskinen. Representerar ett tillstånd, som kan ha entry- och
    exit-funktioner

    :param name: Namnet på tillståndet
    :type name: str

    :var state_machine: En referens till den tillståndsmaskin som tillståndet är en del av
    :type state_machine: StateMachine | None
    """

    def __init__(self, name):
        self.name = name
        self.state_machine = None

    def set_state_machine(self, state_machine):
        """
        Sätter tillståndsmaskinen som tillståndet är en del av
        :param state_machine: Tillståndsmaskinen
        :type state_machine: StateMachine
        """

        self.state_machine = state_machine

    def on_entry(self):
        """
        Anropas när tillståndet går in
        """

        pass

    def handle_event(self, event):
        """
        Hanterar ett event och returnerar det nya tillståndet som ska användas. Om inget nytt tillstånd ska användas,
        returneras None.

        :param event: Eventet som ska hanteras
        :type event: str
        :return: Det nya tillståndet
        :rtype: State | None
        """

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

    def start(self):
        """
        Startar tillståndsmaskinen
        """

        self.current_state.on_entry()

    def transition_to(self, new_state):
        """
        Byter till ett nytt tillstånd

        :param new_state: Det nya tillståndet
        :type new_state: State
        """

        self.current_state = new_state
        self.current_state.set_state_machine(self)
        self.current_state.on_entry()

    def handle_event(self, event):
        """
        Hanterar ett event genom att skicka det till det nuvarande tillståndet

        :param event: Eventet som ska hanteras
        :type event: str
        """

        new_state = self.current_state.handle_event(event)
        if new_state:
            self.transition_to(new_state)
