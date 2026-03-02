from ex2.EliteCard import EliteCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


print('\n=== DataDeck Ability System ===')
print('\nEliteCard capabilities:')
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

try:
    game_state = {'mana': 20, 'cards_played': [], 'mana_used': 0}
    arcane = EliteCard('Arcane Warrior', 4, 'Rare', 5, 22, 3, 4)
    target = EliteCard('Enemy', 2, 'Common', 5, 10, 0, 0)

    print(f'\nPlaying {arcane.get_name()} ({arcane.__class__.__name__.replace("Card", " Card")}):')
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

    except Exception as e:
        print(e)
except Exception as e:
    print(e)

print('\nMultiple interface implementation successful!')