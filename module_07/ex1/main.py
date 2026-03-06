print('\n=== DataDeck Deck Builder ===')
game_state = {'mana': 20, 'cards_played': [], 'mana_used': 0}
try:
    from .SpellCard import SpellCard
    from .Deck import Deck
    from .ArtifactCard import ArtifactCard
    from ex0.CreatureCard import CreatureCard

    print('\nBuilding deck with different card types...')
    deck = Deck()
    cards = [
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        ArtifactCard("Mana Crystal", 2,
                     "Common", 5, "Permanent: +1 mana per turn"),
        SpellCard("Lightning Bolt", 3, "Common", "damage")
    ]
    for card in cards:
        try:
            deck.add_card(card)
        except Exception as e:
            print(e)
    deck.shuffle()
    deck_stats = deck.get_deck_stats()
    print(f'Deck stats: {deck_stats}')

    print('\nDrawing and playing cards:')
    try:
        for _ in range(deck_stats['total_cards']):
            card = deck.draw_card()
            print(f'\nDrew: {card.get_name()} '
                  f'({card.__class__.__name__.replace("Card", "")})')
            print(f'Play result: {card.play(game_state)}')
    except Exception as e:
        print(e)
    print(
        '\nPolymorphism in action: Same interface, different card behaviors!')
except (ImportError, AttributeError):
    print(
        'All exercises must be executed from the repository root '
        'using: python3 -m exN.main (where N is the exercise number).\n'
        'Example: python3 -m ex0.main')
except Exception as e:
    print(e)
