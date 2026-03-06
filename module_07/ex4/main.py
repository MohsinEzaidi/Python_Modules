print('\n=== DataDeck Tournament Platform ===')
try:
    from .TournamentPlatform import TournamentPlatform
    from .TournamentCard import TournamentCard

    card1 = TournamentCard("Fire Dragon", 5, "Legendary",
                           "dragon_001", 1200, 7, 5)
    card2 = TournamentCard("Ice Wizard", 4, "Rare", "wizard_001", 1150, 3, 4)
    platform = TournamentPlatform()

    try:
        print('\nRegistering Tournament Cards...')
        print(platform.register_card(card1))
        print(platform.register_card(card2))
    except Exception as e:
        print(e)

    try:
        print('\nCreating tournament match...')
        card1_id = card1.get_card_id()
        card2_id = card2.get_card_id()
        print('Match result: '
              f'{platform.create_match(card1_id, card2_id)}')
    except Exception as e:
        print(e)

    try:
        print('\nTournament Leaderboard: ')
        for message in platform.get_leaderboard():
            print(message)
    except Exception as e:
        print(e)

    try:
        print('\nPlatform Report:')
        print(platform.generate_tournament_report())
    except Exception as e:
        print(e)
    print('\n=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!')
except (ImportError, AttributeError):
    print(
        'All exercises must be executed from the repository root '
        'using: python3 -m exN.main (where N is the exercise number).\n'
        'Example: python3 -m ex0.main')
except Exception as e:
    print(e)
