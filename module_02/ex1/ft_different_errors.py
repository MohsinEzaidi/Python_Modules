def garden_operations(error_type: str) -> None:
    """
    Demonstrates one of these errors
    (ValueError, ZeroDivisionError, FileNotFoundError, KeyError)
    """
    if error_type == 'ValueError':
        int('abc')
    elif error_type == 'ZeroDivisionError':
        10/0
    elif error_type == 'FileNotFoundError':
        open('missing.txt')
    elif error_type == 'KeyError':
        x = {'1': 1, '2': 2}
        print(x['8'])
    else:
        print(f'{error_type} is not a valid error\n'
              'Please enter one of these errors'
              ' (ValueError, ZeroDivisionError, FileNotFoundError, KeyError)')


def test_error_types() -> None:
    """
    Demonstrate how different Python exception types are raised and caught.
    """
    print("=== Garden Error Types Demo ===")
    try:
        print('\nTesting ValueError...')
        garden_operations('ValueError')
    except ValueError:
        print('Caught ValueError: invalid literal for int()')
    else:
        print('No ValueError caught :)')

    try:
        print('\nTesting ZeroDivisionError...')
        garden_operations('ZeroDivisionError')
    except ZeroDivisionError:
        print('Caught ZeroDivisionError: division by zero')
    else:
        print('No ZeroDivisionError caught :)')

    try:
        print('\nTesting FileNotFoundError...')
        garden_operations('FileNotFoundError')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: No such file \'{e.filename}\'')
    else:
        print('No FileNotFoundError caught :)')

    try:
        print('\nTesting KeyError...')
        garden_operations('KeyError')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    else:
        print('No KeyError caught :)')

    try:
        print("\nTesting multiple errors together...")
        garden_operations('ValueError')
        garden_operations('ZeroDivisionError')
        garden_operations('FileNotFoundError')
        garden_operations('KeyError')
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, KeyError):
        print('Caught an error, but program continues!')
    else:
        print('No Error caught :)')
    print('\nAll error types tested successfully!')


if __name__ == '__main__':
    try:
        test_error_types()
    except Exception as e:
        print(
            f'\nCaught {e.__class__.__name__}, PLEASE stick to the normal'
            ' tests INSIDE try blocks')
