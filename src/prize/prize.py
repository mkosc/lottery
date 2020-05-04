"""
Prize data class
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Prize:
    prize_id: int
    name: str
    amount: int
