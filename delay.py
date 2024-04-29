import time

from button_handler import ButtonHandler


class Delay:
    """
    Klass som hanterar olika typer av fördröjningar.
    """

    @staticmethod
    def aware_delay(seconds, button_pin):
        """
        Metod som skapar en fördröjning som är medveten om att den kan bli avbruten. Kollar kontinuerligt om knappen är
        nedtryckt och avbryter fördröjningen om så är fallet.

        :param seconds: Antal sekunder att vänta
        :type seconds: int
        :param button_pin: Vilken pin som knappen är kopplad till
        :type button_pin: string
        ryckts ned, annars False
        :return: True om knappen har tryckts ned, annars False
        :rtype: bool
        """

        start_time = time.time()
        button_handler = ButtonHandler()

        while time.time() - start_time < seconds:
            if button_handler.is_pressed():
                return True
        else:
            return False
