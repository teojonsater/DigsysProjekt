import board
from time import sleep
from adafruit_ht16k33 import segments

from global_constants import GlobalConstants


class DisplayController:
    """
    Klassen DisplayController är en kontroller för att visa information på en skärm.
    """

    @staticmethod
    def display(text: any):
        """
        Visar text på en skärm.
        :param text: Texten som ska visas.
        :type text: any
        """

        i2c = board.I2C()
        display = segments.Seg14x4(i2c)

        if len(text) > 4:
            display.marquee(text, GlobalConstants.SCROLL_SPEED, False)
        else:
            display.print(text)

    @staticmethod
    def display_temperature(temp):
        """
        Visar temperaturen.
        :param temp: Temperaturen som ska visas.
        :type temp: int
        """

        i2c = board.I2C()
        display = segments.Seg14x4(i2c)

        display.marquee("TEMP " + str(temp) + "'C", GlobalConstants.SCROLL_SPEED, False)
        sleep(GlobalConstants.DISPLAY_DELAY)
        display.fill(False)

    @staticmethod
    def display_co2(co2):
        """
        Visar CO2-nivån.
        :param co2: CO2-nivån som ska visas.
        :type co2: int
        """

        i2c = board.I2C()
        display = segments.Seg14x4(i2c)

        display.marquee("CO2 PPM " + str(co2) + "", GlobalConstants.SCROLL_SPEED, False)
        sleep(GlobalConstants.DISPLAY_DELAY)
        display.fill(False)

    @staticmethod
    def display_humidity(hum):
        """
        Visar luftfuktigheten.
        :param hum: Luftfuktigheten som ska visas.
        :type hum: int
        """

        i2c = board.I2C()
        display = segments.Seg14x4(i2c)

        display.marquee("HUM " + str(hum) + "%", GlobalConstants.SCROLL_SPEED, False)
        sleep(GlobalConstants.DISPLAY_DELAY)
        display.fill(False)
