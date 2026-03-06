from .TournamentCard import TournamentCard
from ex0.Card import Card
from typing import Dict, Union, List


class TournamentPlatform:
    def __init__(self):
        self._cards: List[Card] = []
        self._matches: int = 0
        self._platform_status: str = 'active'

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError('Card should be of type TournamentCard')
        self._cards.append(card)
        rank_info = card.get_rank_info()
        return (f"\n{card.get_name()} (ID: {card.get_card_id()}):\n"
                f"- Interfaces: [Card, Combatable, Rankable]\n"
                f"- Rating: {rank_info['rating']}\n"
                f"- Record: {rank_info['record']}")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if not self._cards:
            raise ValueError('You have to register cards first')
        result = {
            'winner': 'No winner',
            'loser': 'No loser',
        }
        card1 = [c for c in self._cards if c.get_card_id() == card1_id][0]
        card2 = [c for c in self._cards if c.get_card_id() == card2_id][0]
        card1.attack(card2)
        card2.defend(card1.get_attack())
        self._matches += 1

        if not card1.get_combat_stats()['still_alive']:
            card2.update_wins(1)
            card1.update_losses(1)
            result['winner'] = card2.get_card_id()
            result['loser'] = card1.get_card_id()
            result['winner_rating'] = card2.calculate_rating()
            result['loser_rating'] = card1.calculate_rating()
            return result

        elif not card2.get_combat_stats()['still_alive']:
            result: Dict[str, Union[str, int]] = {
                'winner': 'No winner',
                'loser': 'No loser',
                'winner_rating': 0,
                'loser_rating': 0
            }
            card1.update_wins(1)
            card2.update_losses(1)
            result['winner'] = card1.get_card_id()
            result['loser'] = card2.get_card_id()
            result['winner_rating'] = card1.calculate_rating()
            result['loser_rating'] = card2.calculate_rating()
            return result
        return result

    def get_leaderboard(self) -> list:
        if not self._cards:
            raise ValueError('You have to register cards first')
        result: List[str] = []
        for i in range(0, len(self._cards)):
            card = self._cards[i]
            result.append(f'{i+1}. {card.get_name()} - Rating: '
                          f'{card.get_rating()} '
                          f'({card.get_rank_info()["record"]})')
        return result

    def generate_tournament_report(self) -> dict:
        if not self._cards:
            raise ValueError('You have to register cards first')
        return {
            'total_cards': len(self._cards),
            'matches_played': self._matches,
            'avg_rating': sum([
                c.get_rating()
                for c in self._cards])//len(self._cards),
            'platform_status': self._platform_status
            }
