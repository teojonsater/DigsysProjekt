import digitalio
from global_constants import GlobalConstants


class LightsController:
    """
    Klass som hanterar tändande och släckande av sensorvärdesindikatorlampor.

    :cvar red_diode: DigitalInOut-objekt för den röda lampan
    :type red_diode: DigitalInOut
    :cvar green_diode: DigitalInOut-objekt för den gröna lampan
    :type green_diode: DigitalInOut
    :cvar yellow_diode: DigitalInOut-objekt för den gula lampan
    :type yellow_diode: DigitalInOut
    """

    red_diode = digitalio.DigitalInOut(GlobalConstants.PIN_CONFIGS[GlobalConstants.RED_LED_PIN])
    red_diode.direction = digitalio.Direction.OUTPUT

    green_diode = digitalio.DigitalInOut(GlobalConstants.PIN_CONFIGS[GlobalConstants.GREEN_LED_PIN])
    green_diode.direction = digitalio.Direction.OUTPUT

    yellow_diode = digitalio.DigitalInOut(GlobalConstants.PIN_CONFIGS[GlobalConstants.YELLOW_LED_PIN])
    yellow_diode.direction = digitalio.Direction.OUTPUT

    @staticmethod
    def lights_on(lights):
        """
        Metod som tänder lamporna utifrån en inpasserad array av booleska värden.

        :param lights: En array av booleska värden som anger vilka lampor som ska tändas.
        :type lights: list[bool]
        """

        LightsController.red_diode.value = lights[0]
        LightsController.green_diode.value = lights[1]
        LightsController.yellow_diode.value = lights[2]
