from dataclasses import dataclass, field
from functools import total_ordering
import uuid


class InvalidNameError(Exception):
    """Invalid name attribute"""
    pass


class InvalidAmountError(Exception):
    """Invalid amount attribute"""
    pass


@dataclass(frozen=True)
class UniqueId:
    value: uuid.UUID = uuid.uuid4()


@dataclass(fronzen=True)
class Name:
    value: str

    def __post_init__(self):
        if len(self.value) == 0:
            raise InvalidNameError


@total_ordering
@dataclass(fronzen=True)
class Amount:
    value: float

    def __post_init__(self):
        if self.value < 0:
            raise InvalidAmountError

    def __add__(self, other):
        return Amount(self.value + other.value)

    def __sub__(self, other):
        if self.value >= other.value:
            return Amount(self.value - other.value)
        raise InvalidAmountError

    def __ge__(self, other):
        return self.value >= other.value

    # def __eq__(self, other):
    #     return self.value == other.value

    # def __le__(self, other):
    #     return self.value <= other.value
