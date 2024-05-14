import digitalio

from global_constants import GlobalConstants


class ButtonHandler:
    """
    Klass som kan hantera en knapp.
    """

    @staticmethod
    def is_pressed(btn_pin: str):
        """
        Metod som kollar om knappen är nedtryckt. Returnerar True när knappen har släppts.

        :param btn_pin: Pin-nummer för knappen.
        :type btn_pin: str

        :return: True om knappen är nedtryckt, annars False.
        :rtype: bool
        """

        btn_pin = digitalio.DigitalInOut(GlobalConstants.PIN_CONFIGS[btn_pin])
        btn_pin.direction = digitalio.Direction.INPUT
        btn_pin.pull = digitalio.Pull.UP

        btn_value = not btn_pin.value
        btn_pin.deinit()
        return btn_value
