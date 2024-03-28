# ------------------------------------------------
# [실습] 자율비행자동차 클래스 / 상속 적용
# - Added Atrr. : Ai_level, max_altitude, weight
# - Added func : auto_drive, flight, landing
# ------------------------------------------------
import ex_class_02 as e2

class AutoVehicle(e2.Car):
    # Class Attr.
    auto_drive = True

    # instance initial
    def __init__(
        self, wheel, color, number, kind, Ai_level, max_altitude, weight
        ):
        # inheriant properties
        super().__init__(wheel, color, number, kind)

        # designate properties
        self.Ai_level = Ai_level
        self.max_altitude = max_altitude
        self.weight = weight    

    # Additional instance Method
    def auto_drive(self):
        print('Auto drive mode on : driving level=',self.Ai_level)

    def flight(self):
        print(f'flight mode on:\nCheck weight level...')
        if self.weight > 1000: print('Overweight; Mode disabled')
        else: 
            print('Setting max altitude :', self.max_altitude)

    @staticmethod
    def landing():
        print('Landing Complete')

def main():
    Vehicle1 = AutoVehicle(12, 'red', 1233, 'SUV', 5, 1500, 1200)
    Vehicle1.auto_drive()
    Vehicle1.flight()
    Vehicle1.landing()

if __name__ == '__main__': main()