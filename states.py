import time

from state_machine import State


class CheckSensorsState(State):
    """
    Tillstånd som hämtar data från sensorerna.
    """

    def on_entry(self):
        print("Checking sensor...")
        time.sleep(3)
        self.state_machine.handle_event("btn_pressed")

    def handle_event(self, event):
        if event == "btn_pressed":
            return DisplayTempState("Temperature Display")


class DisplayTempState(State):
    def on_entry(self):
        print("Displaying temperature...")
        time.sleep(3)
        self.state_machine.handle_event("switch_display")

    def handle_event(self, event):
        if event == "switch_display":
            return DisplayCO2State("CO2 Display")


class DisplayCO2State(State):

    def on_entry(self):
        print("Displaying CO2...")
        time.sleep(3)
        self.state_machine.handle_event("switch_display")

    def handle_event(self, event):
        if event == "switch_display":
            return DisplayHumState("Humidity Display")


class DisplayHumState(State):

    def on_entry(self):
        print("Displaying humidity...")
        time.sleep(3)
        self.state_machine.handle_event("switch_display")

    def handle_event(self, event):
        if event == "switch_display":
            return CheckSensorsState("Check Sensors")
