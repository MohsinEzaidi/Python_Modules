def create_player_achievement(name: str, achievements: list) -> set:
    achievements_set = set(achievements)
    print(f'Player {name} achievements: {achievements_set}')
    return achievements_set

def all_unique_achievements(players: list[set]) -> set:
    return set().union(*players)


def all_common_achievements(players: list[set]) -> set:
    return players[0].intersection(*players[1:])


def all_rare_achievements(players: list[set]) -> set:
    rare_achievements = players[0].difference(*players[1:])
    unique_achievements = all_unique_achievements()
    
    print("\n------------------------------------------------")
    print((players[1].difference(players[2])))
    print("------------------------------------------------\n")
    counter = 0
    for player in players:
        for achievement in rare_achievements:
            if achievement in player:
                counter += 1
    print(f'Rare achievements ({players.__len__() - counter} player): {rare_achievements}\n')
    return rare_achievements

def main() -> None:
    print('=== Achievement Tracker System ===\n')
    alice = create_player_achievement('alice', ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = create_player_achievement('bob', ['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = create_player_achievement('charlie', ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'])
    players = [alice, bob, charlie]
    # print('\n=== Achievement Analytics ===')
    # unique_achievements = all_unique_achievements(players)
    # print(f'All unique achievements: {unique_achievements}\n'
    #       f'Total unique achievements: {unique_achievements.__len__()}\n')
    # common_achievements = all_common_achievements(players)
    # print(f'Common to all players: {common_achievements}')
    all_rare_achievements(players)
    # print(f'Alice vs Bob common: {all_common_achievements([alice, bob])}')
    # print(f'Alice unique: {all_unique_achievements([alice, bob, charlie])}')
    # print(f'Bob unique: {all_unique_achievements([bob, alice, charlie])}')


if __name__ == '__main__':
    main()