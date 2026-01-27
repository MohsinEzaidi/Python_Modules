from sys import argv as av


def command_quest() -> None:
    try:
        ac = av.__len__()
        if ac < 2:
            print('No arguments provided!')
        print(f'Program name: {av[0]}')
        if ac > 1:
            print(f'Arguments received: {ac - 1}')
            for i in range(1, ac):
                print(f'Argument {i}: {av[i]}')
        print(f'Total arguments: {ac}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print('=== Command Quest ===')
    command_quest()
