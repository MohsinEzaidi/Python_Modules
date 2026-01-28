def create_player_achievement(name: str, achievements: list) -> set:
    achievements_set = set(achievements)
    print(f'Player {name} achievements: {achievements_set}')
    return achievements_set


def all_unique_achievements(players: list[set]) -> set:
    return set().union(*players)


def all_common_achievements(players: list[set]) -> set:
    return players[0].intersection(*players[1:])


def all_rare_achievements(players: list[set]) -> set:
    unique_achievements = all_unique_achievements(players)
    rare_achievements = set()
    players_len = players.__len__()
    for i in range(players_len):
        for j in range(i + 1, players_len):
            rare_achievements = rare_achievements.union(players[i].intersection(players[j]))
    rare_achievements = unique_achievements.difference(rare_achievements)
    return rare_achievements


def main() -> None:
    print('=== Achievement Tracker System ===\n')
    alice = create_player_achievement('alice', ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = create_player_achievement('bob', ['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = create_player_achievement('charlie', ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'])
    players = [alice, bob, charlie]
    print('\n=== Achievement Analytics ===')
    unique_achievements = all_unique_achievements(players)
    print(f'All unique achievements: {unique_achievements}\n'
          f'Total unique achievements: {unique_achievements.__len__()}\n')
    common_achievements = all_common_achievements(players)
    print(f'Common to all players: {common_achievements}')
    rare_achievements = all_rare_achievements(players)
    print(f'Rare achievements (1 player): {rare_achievements}\n')
    print(f'Alice vs Bob common: {all_common_achievements([alice, bob])}')
    print(f'Alice unique: {alice.difference(bob)}')
    print(f'Bob unique: {bob.difference(alice)}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)