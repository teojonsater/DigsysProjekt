import time
import digitalio
from global_constants import GlobalConstants
from sensor_data_getter import SensorDataGetter
from state_machine import StateMachine


def main():
    machine = StateMachine()
    machine.run()


def test_main():
    pass


if __name__ == '__main__':
    main()
