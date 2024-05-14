import time


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
    def sensors_within_limits():
        """
        Kontrollerar om sensorvärdena är inom acceptabla gränser.
        :return: Lista på om sensorvärdena är inom acceptabla gränser. Listans ordning är [temperatur, co2, luftfuktighet]
        :rtype: list[bool]
        """

        tolerable_levels = {
            "temperature": {
                "winter": range(20, 25),
                "summer": range(20, 27)
            },
            "co2": range(0, 1001),
            "humidity": range(30, 71)
        }

        # Sommartid 31 mars till 27 oktober
        # Vintertid 28 oktober till 30 mars
        current_time = time.localtime()
        if (current_time.tm_mon == 3 and current_time.tm_mday == 31
                or current_time.tm_mon in range(4, 9)
                or current_time.tm_mon == 10
                or current_time.tm_mday <= 27):
            season = "summer"
        else:
            season = "winter"

        return [
            SensorDataTracker.current_temperature not in tolerable_levels["temperature"][season],
            SensorDataTracker.current_co2 not in tolerable_levels["co2"],
            SensorDataTracker.current_humidity not in tolerable_levels["humidity"]
        ]
