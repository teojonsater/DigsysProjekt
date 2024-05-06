import adafruit_sgp30
import adafruit_ahtx0
import board


class SensorDataGetter:
    """
    Klass som hanterar interaktion med sensorer. Kan hämta temperatur, CO2-nivå och luftfuktighet.
    """

    @staticmethod
    def get_temperature():
        """
        Hämtar nuvarande temperatur från sensorerna.

        :return: Temperatur i Celsius.
        :rtype: int
        """

        aht20 = adafruit_ahtx0.AHTx0(board.I2C())

        temp = aht20.temperature
        return int(temp)

    @staticmethod
    def get_co2():
        """
        Hämtar nuvarande CO2-nivå från sensorerna.

        :return: CO2-nivå i ppm.
        :rtype: int
        """

        sgp30 = adafruit_sgp30.Adafruit_SGP30(board.I2C())

        eco2 = sgp30.iaq_measure()[0]
        return int(eco2)

    @staticmethod
    def get_humidity():
        """
        Hämtar nuvarande luftfuktighet från sensorerna.

        :return: Luftfuktighet i %.
        :rtype: int
        """

        aht20 = adafruit_ahtx0.AHTx0(board.I2C())
        
        hum = aht20.relative_humidity
        return int(hum)
