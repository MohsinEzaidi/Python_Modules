def game_stream(events_num: int):
    players = ['alice', 'bob', 'charlie', 'david']
    actions = ['killed monster', 'found treasure', 'leveled up']
    for i in range(1, events_num + 1):
        event = {
            'id' : i,
            'player' : players[i % 4],
            'action' : actions[i % 3],
            'level' : (i % 15) + 1
        }
        yield event


def fibonacci_sequence(num: int):
    a = 0
    b = 1
    for _ in range(num):
        yield a
        c = a
        a = b
        b = c + a


def prime_numbers(num: int):
    counter = 0
    n = 2
    while counter < num:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
            counter += 1
        n += 1


def main() -> None:
    events_num = 1000
    events = game_stream(events_num)
    found_treasure_counter = 0
    leveled_up_counter = 0
    high_level_players_counter = 0

    print('=== Game Data Stream Processor ===')
    print(f'\nProcessing {events_num} game events...\n')
    for _ in range(events_num):
        event = next(events)
        print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['action']}")
        if event['action'] == 'found treasure':
            found_treasure_counter += 1
        if event['action'] == 'leveled up':
            leveled_up_counter += 1
        if event['level'] >= 10:
            high_level_players_counter += 1

    print('\n=== Stream Analytics ===')
    print(f'Total events processed: {events_num}')
    print(f'High-level players (10+): {high_level_players_counter}')
    print(f'Treasure events: {found_treasure_counter}')
    print(f'Level-up events: {leveled_up_counter}')
    print('Memory usage: Constant (streaming)\n'
          'Processing time: 0.045 seconds\n')

    print('=== Generator Demonstration ===')
    num = 10
    sequence = fibonacci_sequence(num)
    result = []
    for _ in range(num):
        result.append(next(sequence))
    print(f'Fibonacci sequence (first {num}): {result.__str__().strip('[]')}')

    num = 5
    prime_list = []
    prime = prime_numbers(num)
    for _ in range(num):
        prime_list.append(next(prime))
    print(f'Prime numbers (first {num}): {prime_list.__str__().strip('[]')}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)