def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Validate plant health conditions and raise errors if invalid."""
    if plant_name == '':
        raise ValueError('Error: Plant name cannot be empty!')
    if water_level > 10:
        raise ValueError(f'Error: Water level {water_level}',
                         'is too high (max 10)')
    if water_level < 1:
        raise ValueError(f'Error: Water level {water_level}',
                         'is too low (min 1)')
    if sunlight_hours > 12:
        raise ValueError(f'Error: Sunlight hours {sunlight_hours}',
                         'is too high (min 12)')
    if sunlight_hours < 2:
        raise ValueError(f'Error: Sunlight hours {sunlight_hours}',
                         'is too low (min 2)')
    print(f'Plant \'{plant_name}\' is healthy!')


def test_plant_checks() -> None:
    """Run multiple tests to validate plant health checks."""
    try:
        print('\nTesting good values...')
        check_plant_health('tomato', 4, 4)
    except Exception as e:
        print(e)

    try:
        print('\nTesting empty plant name...')
        check_plant_health('', 4, 4)
    except Exception as e:
        print(e)

    try:
        print('\nTesting bad water level...')
        check_plant_health('tomato', -66, 4)
    except Exception as e:
        print(e)

    try:
        print('\nTesting bad sunlight hours...')
        check_plant_health('tomato', 4, -55)
    except Exception as e:
        print(e)

    print('\nAll error raising tests completed!')


def main() -> None:
    """Program entry point for plant health validation."""
    print('=== Garden Plant Health Checker ===')
    test_plant_checks()


if __name__ == '__main__':
    try:
        main()
        0/0
    except Exception as e:
        print(
            f'Caught {e.__class__.__name__}, PLEASE stick to the normal'
            ' tests INSIDE try blocks')
