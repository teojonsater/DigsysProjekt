import board


class GlobalConstants:
    SLEEP_UPDATE_INTERVAL = 3  # (sekunder) Hur ofta sensordata ska uppdateras.
    SCROLL_SPEED = 0.3  # (sekunder) Hur snabbt texten ska scrolla, dvs hur lång tid mellan varje tecken.
    DISPLAY_DELAY = 1  # (sekunder) Hur lång tid texten ska visas innan den går vidare till nästa.
    PIN_CONFIGS = {
        "A0": board.A0,
        "A1": board.A1,
        "A2": board.A2,
        "A3": board.A3,
        "D4": board.D4,
        "D5": board.D5,
        "D6": board.D6,
        "D9": board.D9,
        "D10": board.D10,
        "D11": board.D11,
        "D12": board.D12,
        "D13": board.D13
    }
    BUTTON_PIN = "A1"
    RED_LED_PIN = "D11"
    GREEN_LED_PIN = "D12"
    YELLOW_LED_PIN = "D13"
    TOLERABLE_SENSOR_LEVELS = {
        "TEMPERATURE": {
            "WINTER": range(20, 25),
            "SUMMER": range(20, 27)
        },
        "CO2": range(0, 1001),
        "HUMIDITY": range(30, 71)
    }
