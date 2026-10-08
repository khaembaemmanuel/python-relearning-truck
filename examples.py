import gc
import sys

class MatatuRoute:
    def __init__(self, name):
        self.name = name
        self.vehicle = None

class MatatuVehicle:
    def __init__(self, plate):
        self.plate = plate
        self.route = None

# 1. Create our objects
route = MatatuRoute("Pipeline Route")
vehicle = MatatuVehicle("KDA 123Z")

# 2. Tie them together, creating a reference cycle
route.vehicle = vehicle
vehicle.route = route

# 3. Delete our direct pointers to the variables
del route
del vehicle

# 4. Force the background garbage collector to find and clear the trapped loop
collected_count = gc.collect()
print(f"The cleanup crew successfully cleared {collected_count} trapped items from memory!")