class Parking:
    def __init__(self, available_places):
        self.cars = 0
        self.available_places = available_places

    def car_input(self):
        if self.__car_input_validation():
            self.cars += 1
        else:
            print("Joy yoq")

    def car_output(self):
        if self.__car_output_validation():
            self.cars -= 1
        else:
            print("Tizimda xatolik")

    def info(self):
        print(f"{self.available_places - self.cars} ta joy qoldi")

    def __car_input_validation(self):
        return self.available_places > self.cars

    def __car_output_validation(self):
        return self.cars > 0


p = Parking(2)
p.car_input()
p.car_input()
p.car_input()
p.car_input()
p.car_input()
p.car_output()
p.car_output()
p.car_output()
p.info()
