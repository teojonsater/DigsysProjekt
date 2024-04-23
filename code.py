import time
from state_machine import StateMachine
from states import CheckSensorsState, DisplayTempState, DisplayCO2State, DisplayHumState


def main():
    StateMachine(CheckSensorsState("Check Sensors"))  # Startar statemaskinen med CheckSensorsState som starttillstånd


if __name__ == '__main__':
    main()
