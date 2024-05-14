from display_controller import DisplayController
from global_constants import GlobalConstants
from lights_handler import LightsHandler
from sensor_data_getter import SensorDataGetter
from sensor_data_tracker import SensorDataTracker
from delay import Delay


class StateMachine:
    """
    Klass som hanterar maskinens olika tillstånd.
    :ivar current_state: Aktuellt tillstånd
    :type current_state: string
    """

    def __init__(self):
        self.current_state = "sensor_update"

    def run(self):
        """
        Metod som kör maskinen och dess olika tillstånd.
        """
        while True:
            if self.current_state == "sensor_update":
                print("Updating sensor data")
                SensorDataTracker.current_temperature = SensorDataGetter.get_temperature()
                SensorDataTracker.current_humidity = SensorDataGetter.get_humidity()
                SensorDataTracker.current_co2 = SensorDataGetter.get_co2()

                # Triggering alarms if the values are above the threshold
                LightsHandler.lights_on(SensorDataTracker.sensors_within_limits())

                # If the button is pressed, the state machine should go to display_temperature state
                if Delay.aware_delay(GlobalConstants.SLEEP_UPDATE_INTERVAL, GlobalConstants.BUTTON_PIN):
                    SensorDataTracker.current_temperature = SensorDataGetter.get_temperature()
                    SensorDataTracker.current_humidity = SensorDataGetter.get_humidity()
                    SensorDataTracker.current_co2 = SensorDataGetter.get_co2()
                    self.current_state = "display_temperature"

            elif self.current_state == "display_temperature":
                print("Displaying temperature")
                DisplayController.display_temperature(SensorDataTracker.current_temperature)
                self.current_state = "display_humidity"

            elif self.current_state == "display_humidity":
                print("Displaying humidity")
                DisplayController.display_humidity(SensorDataTracker.current_humidity)
                self.current_state = "display_co2"

            elif self.current_state == "display_co2":
                print("Displaying CO2")
                DisplayController.display_co2(SensorDataTracker.current_co2)
                self.current_state = "sensor_update"

            else:
                raise ValueError("Invalid state")
