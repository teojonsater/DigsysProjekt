import time

from sensor_data_getter import SensorDataGetter
from state_machine import StateMachine


def main():
    machine = StateMachine()
    machine.run()


def test_main():
    while True:
        print(SensorDataGetter.get_co2())
        time.sleep(0.5)


if __name__ == '__main__':
    main()
