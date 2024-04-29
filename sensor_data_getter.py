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

        # TODO: Implementera temperaturhämtning
        return 25

    @staticmethod
    def get_co2():
        """
        Hämtar nuvarande CO2-nivå från sensorerna.

        :return: CO2-nivå i ppm.
        :rtype: int
        """

        # TODO: Implementera CO2-hämtning
        return 400

    @staticmethod
    def get_humidity():
        """
        Hämtar nuvarande luftfuktighet från sensorerna.

        :return: Luftfuktighet i %.
        :rtype: int
        """

        # TODO: Implementera luftfuktighetshämtning
        return 50
