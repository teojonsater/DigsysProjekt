import time

from global_constants import GlobalConstants


class SensorDataTracker:
    """
    Klass som håller koll på sensorvärdena.

    :cvar current_temperature: Aktuell temperatur i grad Celsius
    :type current_temperature: int
    :cvar current_co2: Aktuell CO2-nivå i ppm
    :type current_co2: int
    :cvar current_humidity: Aktuell luftfuktighet i procent
    :type current_humidity: int
    """

    current_temperature = 0
    current_co2 = 0
    current_humidity = 0

    @staticmethod
    def sensors_not_within_limits():
        """
        Kontrollerar om sensorvärdena inte är inom acceptabla gränser.
        :return: Lista på om sensorvärdena är inom acceptabla gränser. Listans ordning är [temperatur, co2, luftfuktighet]
        :rtype: list[bool]
        """

        # Sommartid 31 mars till 27 oktober
        # Vintertid 28 oktober till 30 mars
        current_time = time.localtime()
        if (current_time.tm_mon == 3 and current_time.tm_mday == 31
                or current_time.tm_mon in range(4, 9)
                or current_time.tm_mon == 10
                or current_time.tm_mday <= 27):
            season = "SUMMER"
        else:
            season = "WINTER"

        return [
            SensorDataTracker.current_temperature not in GlobalConstants.TOLERABLE_SENSOR_LEVELS["TEMPERATURE"][season],
            SensorDataTracker.current_co2 not in GlobalConstants.TOLERABLE_SENSOR_LEVELS["CO2"],
            SensorDataTracker.current_humidity not in GlobalConstants.TOLERABLE_SENSOR_LEVELS["HUMIDITY"]
        ]
