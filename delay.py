import time

from button_handler import ButtonHandler


class Delay:
    """
    Klass som hanterar olika typer av fördröjningar.

    :param state_machine: Statemaskinen som fördröjningen är kopplad till
    :type state_machine: StateMachine

    :var state_machine: Statemaskinen som fördröjningen är kopplad till
    :type state_machine: StateMachine
    """

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def aware_delay(self, seconds, button_pin):
        """
        Metod som skapar en fördröjning som är medveten om att den kan bli avbruten. Kollar kontinuerligt om knappen är
        nedtryckt och avbryter fördröjningen om så är fallet.

        :param seconds: Antal sekunder att vänta
        :type seconds: int
        :param button_pin: Vilken pin som knappen är kopplad till
        :type button_pin: string
        """

        button_handler = ButtonHandler(button_pin)
        start_time = time.time()

        while time.time() - start_time < seconds:
            if button_handler.is_pressed():
                self.state_machine.handle_event("btn_pressed")
                break
            time.sleep(0.1)
        else:
            return
