from battery.battery import Battery
from utils import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_Service_date = last_service_date
    def needs_service(self):
        servicetime = add_years_to_date(self.last_Service_date, 4)
        if servicetime < self.current_date:
            return True
        else:
            return False
