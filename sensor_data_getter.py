import adafruit_sgp30
import adafruit_ahtx0
import board


class SensorDataGetter:
    """
    Klass som hanterar interaktion med sensorer. Kan hämta temperatur, CO2-nivå och luftfuktighet.
    """

    aht20 = adafruit_ahtx0.AHTx0(board.I2C())
    sgp30 = adafruit_sgp30.Adafruit_SGP30(board.I2C())

    @staticmethod
    def get_temperature():
        """
        Hämtar nuvarande temperatur från sensorerna.

        :return: Temperatur i Celsius.
        :rtype: int
        """

        temp = SensorDataGetter.aht20.temperature
        return int(temp)

    @staticmethod
    def get_co2():
        """
        Hämtar nuvarande CO2-nivå från sensorerna.

        :return: CO2-nivå i ppm.
        :rtype: int
        """

        eco2 = SensorDataGetter.sgp30.eCO2
        return int(eco2)

    @staticmethod
    def get_humidity():
        """
        Hämtar nuvarande luftfuktighet från sensorerna.

        :return: Luftfuktighet i %.
        :rtype: int
        """

        hum = SensorDataGetter.aht20.relative_humidity
        return int(hum)
