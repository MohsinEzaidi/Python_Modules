def water_plants(plant_list: str) -> None:
    print('Opening watering system')
    for plant in plant_list:
        if plant.__class__.__name__ != 'str':
            raise Exception(f'Error: Cannot water "{plant.__str__()}" - invalid plant!')
        else:
            print(f'Watering {plant}')
    print('Watering completed successfully!')

def test_watering_system() -> None:
    try:
        print('\nTesting normal watering...')
        water_plants(['warda', 'tefa7a', 'banana'])
    except Exception as e:
        print(e)
    finally:
        print('Closing watering system (cleanup)')
    try:
        print('\nTesting with error...')
        water_plants(['warda', 'tefa7a', 'banana', 635])
    except Exception as e:
        print(e)
    finally:
        print('Closing watering system (cleanup)')

def main() -> None:
    print('=== Garden Watering System ===')
    test_watering_system()
    print('\nCleanup always happens, even with errors!')


if __name__ == '__main__':
    main()