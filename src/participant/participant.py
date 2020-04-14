from dataclasses import dataclass


@dataclass(frozen=True)
class Participant:
    first_name: str
    last_name: str
    weight: int = 1
