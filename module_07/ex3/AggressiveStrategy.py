from .GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        playable_cards = sorted(hand, key=lambda card: card.get_cost())
        targets = self.prioritize_targets(battlefield)
        for card in playable_cards:
            if card.get_cost() < 4:
                cards_played.append(card)
        return{
            'cards_played': [card.get_name() for card in cards_played],
            'mana_used': sum([card.get_cost() for card in cards_played]),
            'targets_attacked': ['Enemy Player'] + [card.get_name() for card in targets if isinstance(card, CreatureCard)],
            'damage_dealt': sum([card.get_attack() for card in cards_played if isinstance(card, CreatureCard)])
        }


    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda enemy: enemy.get_health() if isinstance(enemy, CreatureCard) else None)