import time

from delay import Delay
from display_controller import DisplayController
from sensor_data_getter import SensorDataGetter
from state_machine import State
from sensor_data_tracker import SensorDataTracker


class CheckSensorsState(State):
    """
    Tillstånd som hämtar data från sensorerna. När knappen trycks, byter tillståndet till att cykla genom att visa
    temperatur, CO2 och fuktighet.
    """

    def on_entry(self):
        print("Entered Check Sensors State...")

        delay = Delay(self.state_machine)

        while True:
            print("Checking sensors")
            SensorDataTracker.current_temperature = SensorDataGetter.get_temperature()
            SensorDataTracker.current_co2 = SensorDataGetter.get_co2()
            SensorDataTracker.current_humidity = SensorDataGetter.get_humidity()

            if SensorDataTracker.sensors_within_limits():
                print("Sensors OK")
            else:
                self.state_machine.handle_event("alarm_triggered")
                break

            delay.aware_delay(5, "D2")

    def handle_event(self, event):
        if event == "btn_pressed":
            return DisplayTempState("Temperature Display")
        elif event == "alarm_triggered":
            return AlarmState("Alarm")


class DisplayTempState(State):
    """
    Tillstånd som visar temperaturen. Byter automatiskt till nästa visning efter 3 sekunder.
    """

    def on_entry(self):
        print("Entered Temperature Display State...")

        temperature = SensorDataTracker.current_temperature
        DisplayController.display_temperature(temperature)

        time.sleep(3)
        self.state_machine.handle_event("switch_display")

    def handle_event(self, event):
        if event == "switch_display":
            return DisplayCO2State("CO2 Display")


class DisplayCO2State(State):
    """
    Tillstånd som visar CO2-nivån. Byter automatiskt till nästa visning efter 3 sekunder.
    """

    def on_entry(self):
        print("Entered CO2 Display State...")
        time.sleep(3)
        self.state_machine.handle_event("switch_display")

    def handle_event(self, event):
        if event == "switch_display":
            return DisplayHumState("Humidity Display")


class DisplayHumState(State):
    """
    Tillstånd som visar luftfuktigheten. Byter automatiskt till sensorkontroll efter 3 sekunder.
    """

    def on_entry(self):
        print("Entered Humidity Display State...")
        time.sleep(3)
        self.state_machine.handle_event("switch_display")

    def handle_event(self, event):
        if event == "switch_display":
            return CheckSensorsState("Check Sensors")


class AlarmState(State):
    """
    Tillstånd som visar ett larmmeddelande. När knappen trycks, byter tillståndet till att kontrollera sensorerna.
    """

    def on_entry(self):
        print("ALARM! ALARM!")

    def handle_event(self, event):
        if event == "btn_pressed":
            return CheckSensorsState("Check Sensors")
