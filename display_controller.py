class DisplayController:
    """
    Klassen DisplayController är en kontroller för att visa information på en skärm.
    """

    @staticmethod
    def display_temperature(temp):
        """
        Visar temperaturen.
        :param temp: Temperaturen som ska visas.
        :type temp: int
        """

        # TODO: Visa temperaturen på en skärm
        print("Temperature: " + str(temp) + "°C")

    @staticmethod
    def display_co2(co2):
        """
        Visar CO2-nivån.
        :param co2: CO2-nivån som ska visas.
        :type co2: int
        """

        # TODO: Visa CO2-nivån på en skärm
        print("CO2: " + str(co2) + "ppm")

    @staticmethod
    def display_humidity(hum):
        """
        Visar luftfuktigheten.
        :param hum: Luftfuktigheten som ska visas.
        :type hum: int
        """

        # TODO: Visa luftfuktigheten på en skärm
        print("Humidity: " + str(hum) + "%")
