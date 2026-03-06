from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable
from typing import Dict, Union


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 card_id: str, rating: int, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self._card_id = card_id
        self._rating = rating if rating > 0 else 0
        self._attack = attack if attack > 0 else 0
        self._health = health if health > 0 else 0
        self._wins = 0
        self._losses = 0

    def get_card_id(self) -> str:
        return self._card_id

    def get_rating(self) -> int:
        return self._rating

    def get_attack(self) -> int:
        return self._attack

    def set_card_id(self, card_id: str) -> None:
        self._card_id = card_id

    def set_rating(self, rating) -> None:
        self._rating = rating

    def set_attack(self, attack: int) -> None:
        if attack < 0:
            self._attack = 0
            return
        self._attack = attack

    def set_health(self, health: int) -> None:
        if health < 0:
            self._health = 0
            return
        self._health = health

    def set_wins(self, wins: int) -> None:
        if wins < 0:
            self._wins = 0
            return
        self._wins = wins

    def set_losses(self, losses: int) -> None:
        if losses < 0:
            self._losses = 0
            return
        self._losses = losses

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self._cost:
            raise ValueError(
                f'You don\'t have enough mana to play "{self._name}"')
        game_state['mana'] -= self._cost
        game_state['cards_played'].append(self)
        game_state['mana_used'] += self._cost
        result: Dict[str, Union[str, int]] = {
            'card_played': self.get_name(),
            'mana_used': self.get_cost(),
            'effect': 'Tournament Card summoned to battlefield'
        }
        return result

    def attack(self, target) -> dict:
        if self._attack >= target._health:
            target._health = 0
        else:
            self.set_health(target._health - self._attack)
        result: Dict[str, Union[str, int]] = {
            'attacker': self._name,
            'target': target._name,
            'damage': self._attack,
            'combat_type': 'melee'}
        return result

    def defend(self, incoming_damage: int) -> dict:
        self.set_health(self._health - incoming_damage)
        result: Dict[str, Union[str, int]] = {
            'defender': self._name,
            'damage_taken': incoming_damage
        }
        return result

    def get_combat_stats(self) -> dict:
        return {
            'attack': self._attack,
            'health': self._health,
            'still_alive': self._health > 0
        }

    def calculate_rating(self) -> int:
        if self._wins > self._losses:
            self.set_rating(self._rating + 16)
        elif self._wins < self._losses:
            self.set_rating(self._rating - 16)
        return self._rating

    def update_wins(self, wins: int) -> None:
        self.set_wins(self._wins + wins)

    def update_losses(self, losses: int) -> None:
        self.set_losses(self._losses + losses)

    def get_rank_info(self) -> dict:
        return {
            'rating': self._rating,
            'record': f"{self._wins}-{self._losses}"
        }

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.get_name(),
            'card_id': self.get_card_id(),
            'rating': self.get_rating()
        }
