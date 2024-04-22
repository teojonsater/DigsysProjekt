import time
from state_machine import StateMachine
from states import CheckSensorsState, DisplayTempState, DisplayCO2State, DisplayHumState


def main():
    machine = StateMachine(CheckSensorsState("Check Sensors"))
    time.sleep(1)
    machine.handle_event("btn_pressed")


if __name__ == '__main__':
    main()
