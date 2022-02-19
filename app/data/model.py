from dataclasses import dataclass
from typing import Optional


@dataclass
class Objective:
    id: Optional[int]
    user_id: int
    name: str
    initial_date: str
    final_date: str
    initial_investment: str
    recurring_investment: str
    goal_value: str


@dataclass
class User:
    user_id: Optional[int]
    name: str
    email: str
