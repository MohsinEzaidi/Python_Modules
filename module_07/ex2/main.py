print('\n=== DataDeck Ability System ===')
try:
    from .EliteCard import EliteCard
    from ex1.SpellCard import SpellCard
    from ex0.CreatureCard import CreatureCard

    print('\nEliteCard capabilities:')
    for key, value in EliteCard.get_capabilities().items():
        print(f'- {key}: {value}')
    game_state = {'mana': 20, 'cards_played': [], 'mana_used': 0}
    arcane = EliteCard('Arcane Warrior', 4, 'Rare', 5, 22, 3, 4)
    target = EliteCard('Enemy', 2, 'Common', 5, 10, 0, 0)

    print(f'\nPlaying {arcane.get_name()} '
          f'({arcane.__class__.__name__.replace("Card", " Card")}):')
    try:
        print('\nCombat phase:')
        arcane.play(game_state)
        target.play(game_state)
        print(f'Attack result: {arcane.attack(target)}')
        print(f'Defense result: {arcane.defend(target.get_attack())}')
    except Exception as e:
        print(e)

    spell = SpellCard('Fireball', 4, 'Rare', 'damage')
    enemy1 = CreatureCard('Enemy1', 2, 'Common', 3, 5)
    enemy2 = CreatureCard('Enemy2', 2, 'Common', 3, 5)
    try:
        print('\nMagic phase:')
        game_state['cards_played'] = []
        game_state['mana_used'] = 0
        spell.play(game_state)
        enemy1.play(game_state)
        enemy2.play(game_state)
        spell_result = arcane.cast_spell(spell.get_name(), [enemy1, enemy2])
        spell_result['mana_used'] = spell.get_cost()
        spell.resolve_effect([enemy1, enemy2])
        print(f'Spell cast: {spell_result}')
        mana_channel = arcane.channel_mana(3)
        print(f'Mana channel: {mana_channel}')
        print('\nMultiple interface implementation successful!')
    except Exception as e:
        print(e)
except (ImportError, AttributeError):
    print(
        'All exercises must be executed from the repository root '
        'using: python3 -m exN.main (where N is the exercise number).\n'
        'Example: python3 -m ex0.main')
except Exception as e:
    print(e)
