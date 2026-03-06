print('\n=== DataDeck Card Foundation ===')
game_state = {'mana': 6, 'cards_played': [], 'mana_used': 0}

try:
    from .CreatureCard import CreatureCard

    print('\nTesting Abstract Base Class Design:')
    print('\nCreatureCard Info:')
    creature = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    print(creature.get_card_info())

    try:
        print(f'\nPlaying {creature.get_name()} with '
              f'{game_state["mana"]} mana available:')
        playable = creature.is_playable(game_state['mana'])

        print('Playable:', playable)
        if playable:
            print(f'Play result: {creature.play(game_state)}')

            try:
                goblin = CreatureCard('Goblin Warrior', 3, 'Common', 2, 4)
                print(f'\n{creature.get_name()} attacks {goblin.get_name()}:')
                print(f'Attack result: {creature.attack_target(goblin)}')
            except Exception as e:
                print('Error:', e)

        game_state['mana'] = 3
        print(f'\nTesting insufficient mana ({game_state["mana"]} available):')

        playable = creature.is_playable(game_state['mana'])
        print('Playable:', playable)
        if playable:
            print(f'Play result: {creature.play(game_state)}')
        print('\nAbstract pattern successfully demonstrated!')
    except Exception as e:
        print('Error:', e)
except (ImportError, AttributeError):
    print(
        'All exercises must be executed from the repository root '
        'using: python3 -m exN.main (where N is the exercise number).\n'
        'Example: python3 -m ex0.main')
except Exception as e:
    print('Error:', e)

