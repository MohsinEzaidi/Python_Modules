def test_error_types() -> None:
    try:
        print('\nTesting ValueError...')
        int('8')
    except ValueError:
        print('Caught ValueError: invalid literal for int()')
    else:
        print('No ValueError caught :)')

    try:
        print('\nTesting ZeroDivisionError...')
        3/0
    except ZeroDivisionError:
        print('Caught ZeroDivisionError: division by zero')
    else:
        print('No ZeroDivisionError caught :)')

    try:
        print('\nTesting FileNotFoundError...')
        x = 'tests.py'
        open(x)
        print('\nTesting FileNotFoundError...')
    except FileNotFoundError:
        print(f'Caught FileNotFoundError: No such file \'{x}\'')
    else:
        print('No FileNotFoundError caught :)')

    try:
        print('\nTesting KeyError...')
        garden_data = {'rose': 10, 'carrot': 30}
        missing_plant = 'missing_plant'
        garden_data[missing_plant]
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    else:
        print('No KeyError caught :)')

    try:
        print("\nTesting multiple errors together...")
        int('8')
    except (ZeroDivisionError, KeyError, ValueError, FileNotFoundError):
        print('Caught an error, but program continues!')
    else:
        print('No ValueError caught :)')


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print('\nAll error types tested successfully!')


if __name__ == '__main__':
    main()
