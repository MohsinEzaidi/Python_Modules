def check_temperature(temp_str: str) -> int:
    """Validate a temperature string and return it if safe for plants."""
    print(f'\nTesting temperature: {temp_str}')
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f'Error: \'{temp_str}\' is not a valid number')
    if temp < 0:
        raise ValueError(f'Error: {temp}°C is too cold for plants (min 0°C)')
    elif temp > 40:
        raise ValueError(f'Error: {temp}°C is too hot for plants (max 40°C)')
    else:
        print(f'Temperature {temp}°C is perfect for plants!')
        return temp


def main() -> None:
    """Run sample tests for the garden temperature checker."""
    tests = ['25', 'abc', '100', '-50']
    print('=== Garden Temperature Checker ===')
    for test in tests:
        try:
            check_temperature(test)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(
                f'Caught {e.__class__.__name__}, PLEASE stick to the normal'
                ' tests INSIDE try blocks')
    print('\nAll tests completed - program didn\'t crash!')


if __name__ == '__main__':
    main()
