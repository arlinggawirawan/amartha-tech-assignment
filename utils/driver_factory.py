from config.conftest import Config
class DriverFactory:
    @staticmethod
    def create_driver():
        return Config.get_driver()