from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    id: int
    name: str
    gamerTag: str
    mains: list[str]
    activeSince: str
    isRetired: bool = False
   