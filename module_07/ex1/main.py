from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex0 import CreatureCard


print('\n=== DataDeck Deck Builder ===')
print('\nBuilding deck with different card types...')
game_state = {'mana': 20}
try:
    deck = Deck()
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    artifact = ArtifactCard("Mana Crystal", 2, "Common", 5, "Permanent: +1 mana per turn")
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")

    deck.add_card(creature)
    deck.add_card(artifact)
    deck.add_card(spell)

    deck.shuffle()
    deck_stats = deck.get_deck_stats()

    try:
        for _ in range(deck_stats['total_cards']):
            card = deck.draw_card()
            print(f'\nDrew: {card.get_name()} ({card.__class__.__name__.replace("Card", "")})')
            print(f'Play result: {card.play(game_state)}')
    except Exception as e:
        print(e)
except Exception as e:
    print(e)
print('\nPolymorphism in action: Same interface, different card behaviors!')