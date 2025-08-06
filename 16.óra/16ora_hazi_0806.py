#### These are the helper functions of the homework ####
import json

def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = json.load(file)
        return content


def write_json(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(content, file, ensure_ascii=False)
        print("Data is saved")

def save_carpark_to_json(carpark, filename):
    all_vehicles = []
    for car in carpark.passengercar:
        all_vehicles.append(car.to_dict())
    for truck in carpark.truck:
        all_vehicles.append(truck.to_dict())

    write_json(filename, all_vehicles)
########################################################
class Car:
    def __init__(self, number,manufacturer, model, year, fuel, mileage, color):
        self.number = number
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.fuel = fuel
        self.mileage = mileage
        self.color = color

    def to_dict(self):
        return {
            "number": self.number,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "year": self.year,
            "fuel": self.fuel,
            "mileage": self.mileage,
            "color": self.color
        }

class PassengerCar(Car):
    def __init__(self, number, manufacturer, model, year, fuel, mileage, color, door_number):
        super().__init__(number, manufacturer, model, year, fuel, mileage, color)
        self.door_number = door_number

    def set_door_number(self, value):
        self.door_number = value

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "PassengerCar"
        data["door_number"] = self.door_number
        return data


class Truck(Car):
    def __init__(self, number, manufacturer, model, year, fuel, mileage, color, load_capacity):
        super().__init__(number, manufacturer, model, year, fuel, mileage, color)
        self.load_capacity = load_capacity

    def set_load_capacity(self, value):
        self.load_capacity = value

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Truck"
        data["load_capacity"] = self.load_capacity
        return data


class DataProcess:
    def filter_by_manufacturer(self):
        car_park = read_json("carpark.json")
        ford_car = []
        for car in car_park:
            if car["manufacturer"] == "Ford":
                ford_car.append(car)
        return ford_car


class CarPark:
    def __init__(self, name):
        self.name = name
        self.passengercar=  []
        self.truck = []

    def add_passengercar(self, car):
        self.passengercar.append(car)

    def add_truck(self, car):
        self.truck.append(car)

    def list_vehicles(self):
        print("Passenger cars:")
        for car in self.passengercar:
            print(car.to_dict())

        print("Trucks:")
        for truck in self.truck:
            print(truck.to_dict())

def main():
    carpark = CarPark("car park")
    print("Welcome in the editing system of the car park.")
    answer = input("Press 1 to add a new vehicle. \nPress 2 to delete a vehicle. \nPress 3 to filter out Ford vehicles. Press enter/q/quit to leave the program.\n")
    while answer.lower() not in ["end", "q", "quit"]:
        if answer == "1":
            car_or_truck = input("Would you like to add a passenger car (1) or a truck (2)? \nTo quit press enter/q/quit.\n")
            while car_or_truck not in ["end", "q", "quit"]:
                if car_or_truck == "1":
                    passenger_number = input("What is the number?")
                    passenger_manufacturer = input("Who is the manufacturer?")
                    passenger_model = input("What is the model?")
                    passenger_year = input("What is the year?")
                    passenger_fuel = input("What is the fuel?")
                    passenger_mileage = input("What is the mileage?")
                    passenger_color = input("What is the color?")
                    passenger_door_number = input("How many door the car has?")
                    passenger = PassengerCar(passenger_number, passenger_manufacturer, passenger_model, passenger_year, passenger_fuel, passenger_mileage, passenger_color, passenger_door_number)
                    carpark.add_passengercar(passenger)

                elif car_or_truck == "2":
                    truck_number = input("What is the number?")
                    truck_manufacturer = input("Who is the manufacturer?")
                    truck_model = input("What is the model?")
                    truck_year = input("What is the year?")
                    truck_fuel = input("What is the fuel?")
                    truck_mileage = input("What is the mileage?")
                    truck_color = input("What is the color?")
                    truck_load = input("What is the load capacity?")
                    truck = Truck(truck_number, truck_manufacturer, truck_model, truck_year, truck_fuel, truck_mileage, truck_color, truck_load)
                    carpark.add_truck(truck)
                car_or_truck = input("Would you like to add a passenger car (1) or a truck (2)? \nTo quit press enter/q/quit.\n")
            save_carpark_to_json(carpark, "carpark.json")


        elif answer == "2":
            number_to_delete = input("What is the license number of the vehicle to delete?")
            carpark.passengercar = [car for car in carpark.passengercar if car.number != number_to_delete]
            carpark.truck = [truck for truck in carpark.truck if truck.number != number_to_delete]
            save_carpark_to_json(carpark, "carpark.json")
        elif answer == "3":
            processor = DataProcess()
            ford = processor.filter_by_manufacturer()
            print("Ford vehicles:")
            for car in ford:
                print(car)
        carpark.list_vehicles()
        answer = input(
            "What would you like to do next? \nPress 1 to add a new vehicle. \nPress 2 to delete a vehicle. \nPress 3 to filter out Ford vehicles. \nPress enter/q/quit to leave the program.\n")

main()
