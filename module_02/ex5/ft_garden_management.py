"""
Create a GardenManager class that:
    • Has methods to add plants, water plants, and check plant health
    • Uses your custom error types from previous exercises
    • Handles different types of errors appropriately
    • Uses try/except/finally blocks where needed
    • Raises its own errors when something is wrong
    • Keeps working even when some operations fail

Your garden manager should:
    • Handle bad input gracefully
    • Use custom exceptions for garden-specific problems
    • Always clean up resources (use finally blocks)
    • Provide helpful error messages to users
    • Demonstrate all the error handling concepts from this project

Create a test_garden_management() function that demonstrates:
    • Adding plants with both valid and invalid inputs
    • Watering plants with proper cleanup (using finally)
    • Checking plant health and handling validation errors
    • Error recovery - showing the system continues working after errors
    • Integration of all error handling techniques learned

Example:
$> python3 ft_garden_management.py
=== Garden Management System ===

Adding plants to garden...
Added tomato successfully
Added lettuce successfully
Error adding plant: Plant name cannot be empty!

Watering plants...
Opening watering system
Watering tomato - success
Watering lettuce - success
Closing watering system (cleanup)

Checking plant health...
tomato: healthy (water: 5, sun: 8)
Error checking lettuce: Water level 15 is too high (max 10)

Testing error recovery...
Caught GardenError: Not enough water in tank
System recovered and continuing...

Garden management system test complete!
"""
class GardenManagerError(Exception):
    pass

class PlantError(GardenManagerError):
    pass

class WaterError(GardenManagerError):
    pass

class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int) -> None:
        self._name = name
        self._water_level = water_level
        self._sunlight_hours = sunlight_hours

    def get_name(self) -> str:
        return self._name

    def get_water_level(self) -> int:
        return self._water_level

    def get_sunlight_hours(self) -> int:
        return self._sunlight_hours


class GardeMannager:
    def __init__(self, name: str, water_tank: int) -> None:
        self.name = name
        self._plants_list = []

    # def get_plants_list(self) -> list[Plant]:
    #     return self._plants_list

    def add_plant(self, new_plant: Plant) -> None:
        if new_plant.get_name() == '':
            raise PlantError('Error adding plant: Plant name cannot be empty!')
        else:
            self._plants_list.append(new_plant)
            print(f'Added {new_plant.get_name()} successfully')

    def water_plants(self) -> None:
        print('Opening watering system')
        if self._plants_list.__len__() == 0:
            raise GardenManagerError('Error: There are no plants in the garden')
        for plant in self._plants_list:
            print(f'Watering {plant.get_name()} - success')
            plant.get_water_level() += 1

    def check_plants_health(self) -> None:
        if self._plants_list.__len__() == 0:
            raise GardenManagerError('Error: There are no plants in the garden')
        for plant in self._plants_list:
            if plant.get_water_level() > 10:
                raise GardenManagerError(f'Error checking {plant.get_name()}: Water level {plant.get_water_level()} is too high (max 10)')
            if plant.get_water_level() < 1:
                raise GardenManagerError(f'Error checking {plant.get_name()}: Water level {plant.get_water_level()} is too low (min 1)')
            if plant.get_sunlight_hours() > 12:
                raise GardenManagerError(f'Error checking {plant.get_name()}: Sunlight hours {plant.get_sunlight_hours()} is too high (min 12)')
            if plant.get_sunlight_hours() < 2:
                raise GardenManagerError(f'Error checking {plant.get_name()}: Sunlight hours {plant.get_sunlight_hours()} is too low (min 2)')
            print(f'{plant.get_name()}: healthy (water: {plant.get_water_level()}, sun: {plant.get_sunlight_hours()})')


def test_garden_management() -> None:
    garden = GardeMannager('my garden')
    print('\nAdding plants to garden...')
    try:
        garden.add_plant(Plant('tomato', 4, 4))
        garden.add_plant(Plant('lettuce', 4, 4))
        garden.add_plant(Plant('', 4, 4))
    except GardeMannager as e:
        print(e)
    try:
        print('\nWatering plants...')
        garden.water_plants()
    except GardenManagerError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    try:
        print('\nChecking plant health...')
        garden.check_plants_health()
    except GardenManagerError as e:
        print(e)