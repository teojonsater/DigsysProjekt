class ButtonHandler:
    """
    Klass som hanterar en knapp.

    :param button_pin: Pin på mikrokontrollern som knappen är kopplad till.
    :type button_pin: string
    """

    def __init__(self, button_pin):
        self.button_pin = button_pin

    def is_pressed(self):
        """
        Metod som kollar om knappen är nedtryckt.

        :return: True om knappen är nedtryckt, annars False.
        :rtype: bool
        """

        pin = self.button_pin
        return False
