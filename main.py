from time import sleep
from display_controller import DisplayController
from sensor_data_getter import SensorDataGetter
import board
import busio


def main():
    while True:
        DisplayController.display_temperature(SensorDataGetter.get_temperature())
        sleep(2)
        DisplayController.display_co2(SensorDataGetter.get_co2())
        sleep(2)
        DisplayController.display_humidity(SensorDataGetter.get_humidity())
        sleep(2)


if __name__ == '__main__':
    main()
