import board
import digitalio


class ButtonHandler:
    """
    Klass som kan hantera en knapp.
    """

    pin_config = {
        "A0": board.A0,
        "A1": board.A1,
        "A2": board.A2,
        "A3": board.A3,
        "D4": board.D4,
        "D5": board.D5,
        "D6": board.D6,
        "D9": board.D9,
        "D10": board.D10,
        "D11": board.D11,
        "D12": board.D12,
        "D13": board.D13
    }

    @staticmethod
    def is_pressed(btn_pin: str):
        """
        Metod som kollar om knappen är nedtryckt. Returnerar True när knappen har släppts.

        :param btn_pin: Pin-nummer för knappen.
        :type btn_pin: str

        :return: True om knappen är nedtryckt, annars False.
        :rtype: bool
        """

        btn_pin = digitalio.DigitalInOut(ButtonHandler.pin_config[btn_pin])
        btn_pin.direction = digitalio.Direction.INPUT
        btn_pin.pull = digitalio.Pull.UP

        btn_value = not btn_pin.value
        btn_pin.deinit()
        return btn_value
