class Vehicle:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def make_sound(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self._num_wheels = num_wheels

    def make_sound(self):
        return "Vroom!"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self._num_wheels = num_wheels

    def make_sound(self):
        return "Vroom vroom!"

class Garage:
    def __init__(self, vehicles):
        self._vehicles = vehicles

    def add_vehicle(self, vehicle):
        self._vehicles.append(vehicle)

    def list_vehicles(self):
        for vehicle in self._vehicles:
            print(f"{type(vehicle).__name__}: {vehicle.get_make()} {vehicle.get_model()} ({vehicle.get_year()})")

# Create some vehicles
car1 = Car("Toyota", "Corolla", 2015, 4)
motorcycle1 = Motorcycle("Harley Davidson", "Street Glide", 2020, 2)

# Create a garage and add the vehicles
my_garage = Garage([car1, motorcycle1])

# Add another vehicle
car2 = Car("Honda", "Civic", 2018, 4)
my_garage.add_vehicle(car2)

# List the vehicles in the garage
my_garage.list_vehicles()
