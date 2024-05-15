import digitalio

from global_constants import GlobalConstants


class LightsHandler:
    red_diode = digitalio.DigitalInOut(GlobalConstants.PIN_CONFIGS[GlobalConstants.RED_LED_PIN])
    red_diode.direction = digitalio.Direction.OUTPUT

    green_diode = digitalio.DigitalInOut(GlobalConstants.PIN_CONFIGS[GlobalConstants.GREEN_LED_PIN])
    green_diode.direction = digitalio.Direction.OUTPUT

    yellow_diode = digitalio.DigitalInOut(GlobalConstants.PIN_CONFIGS[GlobalConstants.YELLOW_LED_PIN])
    yellow_diode.direction = digitalio.Direction.OUTPUT

    @staticmethod
    def lights_on(lights) -> None:
        """
        Metod som tänder lamporna utifrån en inpasserad array av boolska värden.

        :param lights: En array av boolska värden som anger vilka lampor som ska tändas.
        :type lights: list[bool]
        """

        LightsHandler.red_diode.value = lights[0]
        LightsHandler.green_diode.value = lights[1]
        LightsHandler.yellow_diode.value = lights[2]
