def test_error_types() -> None:
    try:
        int('kg')
    except ValueError:
        print('Testing ValueError...')
        print('Caught ValueError: invalid literal for int()\n')

    try:
        3/0
    except ZeroDivisionError:
        print('Testing ZeroDivisionError...')
        print('Caught ZeroDivisionError: division by zero\n')

    try:
        x = 'missing.txt'
        open(x)
    except FileNotFoundError:
        print('Testing FileNotFoundError...')
        print(f'Caught FileNotFoundError: No such file \'{x}\'\n')

    try:
        missing_plant = 'missing_plant'
        garden_data = {'rose': 10}
        garden_data['missing_plant']
    except KeyError as e:
        print('Testing KeyError...')
        print(f'Caught KeyError: {e}\n')

    try:
        int('jd')

    except (ZeroDivisionError, KeyError, ValueError, FileNotFoundError):
        print("Testing multiple errors together...")
        print('Caught an error, but program continues!\n')


def main() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print('All error types tested successfully!')


if __name__ == '__main__':
    main()
