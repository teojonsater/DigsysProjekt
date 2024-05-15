import time
import pwmio

from global_constants import GlobalConstants


class FanHandler:
    @staticmethod
    def fan_on(fan_levels):
        """
        Metod som sätter fläkten på en viss nivå.

        :param fan_levels: En array av boolska värden som anger vilka fläktnivåer som ska vara på.
        :type fan_levels: list[bool]
        """

        # Räknar ut vilken fläktnivå som ska vara på, beroende på hur många True-värden som finns i fan_levels
        fan_level = sum(fan_levels)

        # Sätter fläkten på rätt nivå
        max_fan_speed = 30000
        if fan_level == 0:
            GlobalConstants.FAN_PWM.duty_cycle = 0
        elif fan_level == 1:
            GlobalConstants.FAN_PWM.duty_cycle = max_fan_speed  # Boost fan
            time.sleep(0.5)
            GlobalConstants.FAN_PWM.duty_cycle = int(max_fan_speed / 3)
        elif fan_level == 2:
            GlobalConstants.FAN_PWM.duty_cycle = max_fan_speed  # Boost fan
            time.sleep(0.5)
            GlobalConstants.FAN_PWM.duty_cycle = int(max_fan_speed / 2)
        elif fan_level == 3:
            GlobalConstants.FAN_PWM.duty_cycle = max_fan_speed
        else:
            raise ValueError("Invalid fan level")
