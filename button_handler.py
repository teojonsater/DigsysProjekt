import board
import digitalio
from sensor_data_tracker import SensorDataTracker

class ButtonHandler:
    """
    Klass som hanterar en knapp.
    """

    def __init__(self):
        pass

    def is_pressed(self):
        """
        Metod som kollar om knappen är nedtryckt. Returnerar True när knappen har släppts.

        :return: True om knappen är nedtryckt, annars False.
        :rtype: bool
        """


        if SensorDataTracker.btn_pin.value:
            return True
        return False
