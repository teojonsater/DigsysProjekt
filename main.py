from state_machine import StateMachine


class Main:
    """
    Main-class som kör programmet.
    """

    @staticmethod
    def main():
        """
        Main-metod som skapar en instans av StateMachine och kör programmet.
        """

        machine = StateMachine()
        machine.run()

    @staticmethod
    def test_main():
        """
        Testfunktion som används för att testa nya funktioner innan de implementeras i main.
        """

        pass


if __name__ == '__main__':
    Main.main()
