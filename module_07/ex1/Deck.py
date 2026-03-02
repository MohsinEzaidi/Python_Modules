from ex0 import Card, CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import shuffle


class Deck():
    def __init__(self) -> None:
        self._deck: list[Card] = []

    def get_deck(self) -> list:
        return self._deck

    def set_deck(self, new_deck: list[Card]) -> None:
        self._deck = new_deck

    def add_card(self, card: Card) -> None:
        self._deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self._deck:
            if card.name == card_name:
                self._deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self._deck)

    def draw_card(self) -> Card:
        if not self._deck:
            raise ValueError('Deck is empty, couldn\'t draw a card')
        return self._deck.pop(0)

    def get_deck_stats(self) -> dict:
        deck_stats = {
            'total_cards' : 0,
            'creatures' : 0,
            'spells' : 0,
            'artifacts' : 0,
            'avg_cost' : 0
            }
        if not self._deck:
            return deck_stats
        costs = []
        for card in self._deck:
            if isinstance(card, CreatureCard):
                deck_stats['creatures'] += 1
            elif isinstance(card, SpellCard):
                deck_stats['spells'] += 1
            elif isinstance(card, ArtifactCard):
                deck_stats['artifacts'] += 1
            else:
                self._deck.remove(card)
            costs.append(card.get_cost())
            deck_stats['total_cards'] += 1
        deck_stats['avg_cost'] = sum(costs)/len(costs)
        return deck_stats
