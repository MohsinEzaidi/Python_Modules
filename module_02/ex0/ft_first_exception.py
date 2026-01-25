def check_temperature(temp_str: str) -> int | None:
    """Validate a temperature string and return it if safe for plants."""
    try:
        print(f'Testing temperature: {temp_str}')
        temp = int(temp_str)
        if temp < 0:
            print(f'Error: {temp}°C is too cold for plants (min 0°C)\n')
            return None
        elif temp > 40:
            print(f'Error: {temp}°C is too hot for plants (max 40°C)\n')
            return None
        else:
            print(f'Temperature {temp}°C is perfect for plants!\n')
            return temp
    except ValueError:
        print(f'Error: \'{temp_str}\' is not a valid number\n')
    return None


def main() -> None:
    """Run sample tests for the garden temperature checker."""
    print('=== Garden Temperature Checker ===\n')
    check_temperature('25')
    check_temperature('abc')
    check_temperature('100')
    check_temperature('-50')
    print('All tests completed - program didn\'t crash!')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Caught {e.__class__.__name__}')
