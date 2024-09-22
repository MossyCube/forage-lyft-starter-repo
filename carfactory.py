from battery.nubbinbattery import nubbinbattery
from battery.spindlerbattery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class carfactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date=last_service_date
        self.current_mileage=current_mileage
        self.last_service_mileage =last_service_mileage
        return Car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date=last_service_date
        self.current_mileage=current_mileage
        self.last_service_mileage =last_service_mileage
        return Car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.current_date = current_date
        self.last_service_date=last_service_date
        self.current_mileage=warning_light_on
        return Car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date=last_service_date
        self.current_mileage=current_mileage
        self.last_service_mileage =last_service_mileage
        return Car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date=last_service_date
        self.current_mileage=current_mileage
        self.last_service_mileage =last_service_mileage
        return Car
