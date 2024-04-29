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
        :return: True om alla sensorvärden är inom acceptabla gränser, annars False.
        :rtype: bool
        """

        # TODO: Sätt in riktiga gränsvärden
        tolerable_levels = {
            "temperature": range(0, 30),
            "co2": range(0, 30),
            "humidity": range(0, 30)
        }

        if SensorDataTracker.current_temperature not in tolerable_levels["temperature"] or \
                SensorDataTracker.current_co2 not in tolerable_levels["co2"] or \
                SensorDataTracker.current_humidity not in tolerable_levels["humidity"]:
            return False

        return True
