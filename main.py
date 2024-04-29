import time
from state_machine import StateMachine
from states import CheckSensorsState, DisplayTempState, DisplayCO2State, DisplayHumState


def main():
    sensor_state_machine = StateMachine(
        CheckSensorsState("Check Sensors"))  # Initialiserar CheckSensorsState som starttillstånd

    sensor_state_machine.start()


if __name__ == '__main__':
    main()
