from math import sqrt


def create_coordinates(coordinates: tuple[int, int, int]
                       ) -> tuple[int, int, int]:
    """
    Create and validate 3D coordinates from an iterable of numbers.
    Ensures exactly 3 integer values are provided.
    """
    coordinates = tuple(int(x) for x in coordinates)
    tuple_len = coordinates.__len__()
    if tuple_len != 3:
        raise Exception(f'Expected 3 elements got {tuple_len}')
    print(f'\nPosition created: {coordinates}')
    return coordinates


def parsing_coordinates(coordinates_str: str) -> tuple[int, int, int]:
    """
    Parse coordinates from a string formatted as 'x,y,z'
    and return a tuple of integers.
    """
    coordinates = tuple(int(x) for x in coordinates_str.split(','))
    tuple_len = coordinates.__len__()
    if tuple_len != 3:
        raise Exception(
            f'Error Parsing coordinates: Expected 3 elements got '
            f'{tuple_len}, your string should look like this "x,y,z"')
    print(f'Parsed position: {coordinates}')
    return coordinates


def calculate_distance(coordinates1: tuple[int, int, int],
                       coordinates2: tuple[int, int, int] = (0, 0, 0)
                       ) -> float:
    """
    Calculate Euclidean distance between two 3D coordinates.
    """
    coordinates1 = tuple(int(x) for x in coordinates1)
    coordinates2 = tuple(int(x) for x in coordinates2)
    tuple1_len = coordinates1.__len__()
    tuple2_len = coordinates2.__len__()
    if tuple1_len != 3 or tuple2_len != 3:
        raise Exception('Error calculating distance: Expected 3 elements'
                        f' on both tuples got {tuple1_len} and {tuple2_len}')
    distance = sqrt(
        (coordinates1[0]-coordinates2[0])**2 +
        (coordinates1[1]-coordinates2[1])**2 +
        (coordinates1[2]-coordinates2[2])**2)
    print(
        f'Distance between {coordinates2} and {coordinates1}: {distance:.2f}')
    return distance


def unpacking_demonstration(coordinates: tuple[int, int, int]) -> None:
    """
    Demonstrate tuple unpacking of 3D coordinates.
    """
    coordinates = tuple(int(x) for x in coordinates)
    tuple_len = coordinates.__len__()
    if tuple_len != 3:
        raise Exception('Error calculating distance: Expected 3'
                        f' elements on the tuple got {tuple_len}')
    x, y, z = coordinates
    print(f'Player at x={x}, y={y}, z={z}')
    print(f'Coordinates: X={x}, Y={y}, Z={z}')


def main() -> None:
    """
    Demonstrate coordinate parsing, creation, distance calculation,
    and unpacking examples with error handling.
    """
    print('=== Game Coordinate System ===')
    try:
        P = create_coordinates((10, 20, 5))
        calculate_distance(P)
    except Exception as e:
        print(f'Error creating coordinates: {e}')
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
    try:
        valid_coordinates = '3,4,0'
        print(f'\nParsing coordinates: "{valid_coordinates}"')
        P = parsing_coordinates(valid_coordinates)
        calculate_distance(P)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
    try:
        invalid_coordinates = "abc,def,ghi"
        print(f'\nParsing invalid coordinates: "{invalid_coordinates}"')
        P = parsing_coordinates(invalid_coordinates)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
    try:
        print('\nUnpacking demonstration:')
        unpacking_demonstration(P)
    except Exception as e:
        print(f"Error unpacking demonstration: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
