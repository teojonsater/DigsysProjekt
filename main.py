import time
from state_machine import StateMachine
from sensor_data_tracker import SensorDataTracker
from states import CheckSensorsState, DisplayTempState, DisplayCO2State, DisplayHumState
import board
import digitalio


def main():
    SensorDataTracker.btn_pin.direction = digitalio.Direction.INPUT

    sensor_state_machine = StateMachine(
        CheckSensorsState("Check Sensors"))  # Initialiserar CheckSensorsState som starttillstånd

    sensor_state_machine.start()

def test():
    btn_pin = digitalio.DigitalInOut(board.D24)
    btn_pin.direction = digitalio.Direction.INPUT

    btn_is_pressed = False
    while True:
        if btn_pin.value and not btn_is_pressed:
            btn_is_pressed = True
            print("hej")
        if not btn_pin.value:
            btn_is_pressed = False


if __name__ == '__main__':
    main()
