from button_handler import ButtonHandler
from display_controller import DisplayController
from sensor_data_getter import SensorDataGetter


def main():
    while True:
        if ButtonHandler.is_pressed("A1"):
            DisplayController.display_temperature(SensorDataGetter.get_temperature())
            DisplayController.display_co2(SensorDataGetter.get_co2())
            DisplayController.display_humidity(SensorDataGetter.get_humidity())


if __name__ == '__main__':
    main()
