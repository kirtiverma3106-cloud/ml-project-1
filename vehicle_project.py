from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_id, model, base_rate):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.__base_rate = base_rate
        self.__available =True
        self.is_rented = False
        

    @property
    def available(self):
        return self.__available
    @available.setter
    def available(self,value):
        self.__available = value
        
    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @property
    def model(self):
        return self.__model

    @property
    def base_rate(self):
        return self.__base_rate

    @abstractmethod
    def calculate_rent(self, days):
        pass
    
class Car(Vehicle):
     def calculate_rent(self, days):
        return self.base_rate * days

class Bike(Vehicle):
     def calculate_rent(self, days):
        return self.base_rate * days
    
class RentalSystem:
     def __init__(self):
        self.vehicles = []

     def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

     def show_vehicles(self):
      for vehicle in self.vehicles:
        status = "Rented" if vehicle.is_rented else "Available"

        print(vehicle.vehicle_id, "-", vehicle.model, "-", vehicle.base_rate, "-", status)



     def rent_vehicle(self, vehicle_id):
      for vehicle in self.vehicles:
        if vehicle.vehicle_id == vehicle_id:
            if not vehicle.is_rented:
                vehicle.is_rented = True
                print("Vehicle rented successfully!")
            else:
                print("Vehicle is already rented!")
            return

      print("Vehicle not found!")

     def return_vehicle(self, vehicle_id):
      for vehicle in self.vehicles:
        if vehicle.vehicle_id == vehicle_id:
            if vehicle.is_rented:
                vehicle.is_rented = False
                print("Vehicle returned successfully!")
            else:
                print("Vehicle was not rented!")
            return

      print("Vehicle not found!")
        
system = RentalSystem()

car1 = Car("C001", "Fortuner", 2500)
bike1 = Bike("B001", "Activa", 800)

system.add_vehicle(car1)
system.add_vehicle(bike1)

system.show_vehicles()

days = int(input("enter number of days: "))

print("Car rent:", car1.calculate_rent(days))
print("Bike rent:", bike1.calculate_rent(days))

print()

print("\n--- RENT VEHICLE ---")
vehicle_id = input("Enter vehicle ID to rent: ")
system.rent_vehicle(vehicle_id)

print("\n--- VEHICLES AFTER RENTING ---")
system.show_vehicles()

print("\n--- RETURN VEHICLE ---")
vehicle_id = input("Enter vehicle ID to return: ")
system.return_vehicle(vehicle_id)

print("\n--- FINAL VEHICLE LIST ---")
system.show_vehicles()


