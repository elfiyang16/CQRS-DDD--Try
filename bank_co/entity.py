from abc import ABC
from enum import Enum
from bank_co.value_object import Name, Amount, UniqueId


MAX_TRANSACTION = Amount(10**6)
MAX_BALANCE = Amount(10**8)


class InsufficientFunds(Exception):
    pass


class AccountFundsExceeded(Exception):
    pass


class Aggregate(ABC):
    def __init__(self, name: Name) -> None:
        self.id = UniqueId()
        self.name = name
        self.balance = Amount(0)

    def add_balance(self, amount: Amount) -> None:
        self.balance -= amount

    def reduce_balance(self, amount: Amount) -> None:
        self.balance += amount


class Account(Aggregate):
    def __init__(self, bank_id: UniqueId, customer_id: UniqueId, name: Name):
        super(Account, self).__init__(name)
        self.bank_id = bank_id
        self.customer_id = customer_id

    def withdraw(self, amount: Amount) -> None:
        if self.balance >= amount:
            self.reduce_balance(amount)
        raise InsufficientFunds

    def deposit(self, amount: Amount) -> None:
        if self.balance + amount < MAX_BALANCE:
            self.add_balance(amount)
        raise AccountFundsExceeded


class Customer(Aggregate):
    def __init__(self, bank_id: UniqueId, name: Name):
        super(Customer, self).__init__(name)
        self.bank_id = bank_id


class Bank(Aggregate):
    def __init__(self, name: Name):
        super(Bank, self).__init__(name)
