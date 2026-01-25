class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant-related operation fails."""
    pass


class Plant:
    """Represents a plant with water and sunlight properties."""
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        """Initialize plant data with basic validation."""
        self._name = name if name.__class__.__name__ == 'str' else ''
        self._water_level = water_level if water_level > 0 else 0
        self._sunlight_hours = sunlight_hours if sunlight_hours > 0 else 0

    def get_name(self) -> str:
        """Return the plant name."""
        return self._name

    def get_water_level(self) -> int:
        """Return the current water level."""
        return self._water_level

    def set_water_level(self, new_water_level: int) -> None:
        """Update the plant water level."""
        self._water_level = new_water_level

    def get_sunlight_hours(self) -> int:
        """Return the sunlight hours."""
        return self._sunlight_hours


class GardeMannager:
    """Manages plants and watering operations in a garden."""
    def __init__(self, name: str, water_tank: int) -> None:
        """Initialize garden manager with a water tank."""
        self.name = name
        self._water_tank = water_tank
        self._plants_list = []

    def get_plants_list(self) -> list[Plant]:
        """Return the list of plants."""
        return self._plants_list

    def get_water_tank(self) -> int:
        """Return the available water amount."""
        return self._water_tank

    def set_water_tank(self, new_water_tank) -> None:
        """Update the water tank level."""
        self._water_tank = new_water_tank

    def add_plant(self, new_plant: Plant) -> None:
        """Add a plant to the garden or raise PlantError."""
        if new_plant.get_name() == '':
            raise PlantError('Error adding plant: Plant name cannot be empty!')
        else:
            self.get_plants_list().append(new_plant)
            print(f'Added {new_plant.get_name()} successfully')

    def water_plants(self) -> None:
        """Water all plants if enough water is available."""
        print('Opening watering system')
        total_plants = self.get_plants_list().__len__()
        if total_plants == 0:
            raise GardenError('Error: There are no plants in the garden')
        if total_plants > self.get_water_tank():
            raise GardenError('Caught GardenError: Not enough water in tank')
        for plant in self.get_plants_list():
            print(f'Watering {plant.get_name()} - success')
            plant.set_water_level(plant.get_water_level() + 1)
            self.set_water_tank(self.get_water_tank() - 1)

    def check_plants_health(self) -> None:
        """Check health conditions for all plants."""
        if self.get_plants_list().__len__() == 0:
            raise GardenError('Error: There are no plants in the garden')
        for plant in self.get_plants_list():
            name = plant.get_name()
            water_level = plant.get_water_level()
            sunlight_hours = plant.get_sunlight_hours()
            if plant.get_water_level() > 10:
                raise GardenError(f'Error checking {name}: Water level '
                                  f'{water_level} is too high (max 10)')
            if water_level < 1:
                raise GardenError(f'Error checking {name}: Water level '
                                  f'{water_level} is too low (min 1)')
            if sunlight_hours > 12:
                raise GardenError(f'Error checking {name}: Sunlight hours '
                                  f'{sunlight_hours} is too high (min 12)')
            if sunlight_hours < 2:
                raise GardenError(f'Error checking {name}: Sunlight hours '
                                  f'{sunlight_hours} is too low (min 2)')
            print(f'{plant.get_name()}: healthy (water: {water_level}, '
                  f'sun: {sunlight_hours})')


def test_garden_management() -> None:
    """Run multiple tests on the garden management system."""
    garden = GardeMannager('my garden', 10)
    print('\nAdding plants to garden...')
    try:
        garden.add_plant(Plant('tomato', 4, 4))
        garden.add_plant(Plant('lettuce', 15, 4))
        garden.add_plant(Plant('', 4, 4))
    except PlantError as e:
        print(e)
    try:
        print('\nWatering plants...')
        garden.water_plants()
    except GardenError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    try:
        print('\nChecking plant health...')
        garden.check_plants_health()
    except GardenError as e:
        print(e)
    try:
        print('\nTesting error recovery...')
        garden.set_water_tank(0)
        garden.water_plants()
    except GardenError as e:
        print(e)
    print('System recovered and continuing...')


def main() -> None:
    """Program entry point."""
    print('=== Garden Management System ===')
    try:
        test_garden_management()
    except Exception as e:
        print(f'\nCaught {e.__class__.__name__}')
    print('\nGarden management system test complete!')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(
            f'Caught {e.__class__.__name__}, PLEASE stick to the normal'
            ' tests INSIDE try blocks')
