import board
import pwmio


class GlobalConstants:
    """
    Klass som innehåller globala konstanter som används i flera filer för att undvika "magic numbers".

    :cvar SLEEP_UPDATE_INTERVAL: (sekunder) Hur ofta sensordata ska uppdateras.
    :type SLEEP_UPDATE_INTERVAL: int
    :cvar SCROLL_SPEED: (sekunder) Hur snabbt texten ska scrolla, dvs hur lång tid mellan varje tecken.
    :type SCROLL_SPEED: float
    :cvar DISPLAY_DELAY: (sekunder) Hur lång tid texten ska visas innan den går vidare till nästa.
    :type DISPLAY_DELAY: int
    :cvar PIN_CONFIGS: Dictionary med konfigurationer för varje pinne på Arduino. Används för att kunna hämta en given pin från en sträng
    :type PIN_CONFIGS: dict[str, board.Pin]
    :cvar BUTTON_PIN: Vilken pinne knappen är kopplad till.
    :type BUTTON_PIN: str
    :cvar RED_LED_PIN: Vilken pinne den röda lampan är kopplad till.
    :type RED_LED_PIN: str
    :cvar GREEN_LED_PIN: Vilken pinne den gröna lampan är kopplad till.
    :type GREEN_LED_PIN: str
    :cvar YELLOW_LED_PIN: Vilken pinne den gula lampan är kopplad till.
    :type YELLOW_LED_PIN: str
    :cvar TOLERABLE_SENSOR_LEVELS: Dictionary med acceptabla gränser för sensorvärdena.
    :type TOLERABLE_SENSOR_LEVELS: dict[str, dict[str, range or dict[str, range]]]
    :cvar FAN_PWM: PWM-objekt för fläkten. Behövs för att inte pwmio ska initieras flera gånger.
    :type FAN_PWM: pwmio.PWMOut
    """

    SLEEP_UPDATE_INTERVAL = 20
    SCROLL_SPEED = 0.3
    DISPLAY_DELAY = 1
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
    FAN_PWM = pwmio.PWMOut(PIN_CONFIGS["D5"], frequency=100)
