from dataclasses import dataclass
from enum import Enum
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
    user_id: Optional[str]
    name: str
    email: str


class InvestmentClass(Enum):
    UNKNOWN = 0
    VARIABLE_INCOME = 1
    POST_FIXED = 2
    MULTI_MARKET = 3
    GLOBAL = 4
    INFLATION = 5


@dataclass
class Investment:
    identity: str
    bankId: str
    description: str
    type: str
    classification: InvestmentClass
    value: float
    dueDate: Optional[str]
    profitability: Optional[float]
    risk: int
    acquisitionDate: str


@dataclass
class Transaction:
    amount: float
    description: str
    date: str


@dataclass
class UserTransactions:
    user_id: str
    suitability: float
    transactions: list[Transaction]
