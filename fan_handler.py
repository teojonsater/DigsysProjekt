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

        # TODO: Implementera fläktstyrning
