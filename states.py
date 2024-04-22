import time

from state_machine import State


class CheckSensorsState(State):
    """
    Tillstånd som hämtar data från sensorerna. När knappen trycks, byter tillståndet till att cykla genom att visa
    temperatur, CO2 och fuktighet.
    """

    def on_entry(self):
        print("Checking sensor...")

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
        print("Displaying temperature...")
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
        print("Displaying CO2...")
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
        print("Displaying humidity...")
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
