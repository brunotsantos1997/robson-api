from dataclasses import dataclass


@dataclass
class Objective:
    id: int
    user_id: int
    name: str
    initial_date: str
    final_date: str
    initial_investment: str
    recurring_investment: str
    goal_value: str


@dataclass
class Users:
    user_id: int
    name: str
    email: str
