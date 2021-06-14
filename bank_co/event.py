from abc import ABC, abstractmethod
from bank_co.repository import BankRepo, CustomerRepo
from bank_co.value_object import Amount, UniqueId
"""
event to perform side effect across multiple aggregates
can call repo from infra
and entity from domain 
"""


class DomainEvent(ABC):
    @abstractmethod
    def trigger(self) -> None:
        pass


class FundsDeposited(DomainEvent):
    def __init__(self, bank_id: UniqueId, customer_id: UniqueId, amount: Amount) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> None:
        bank = BankRepo.find_by_id(self._bank_id)
        customer = CustomerRepo.find_by_id(self._customer_id)
        customer.add_balance(self._amount)
        bank.add_balance(self._amount)
        CustomerRepo.save(customer)
        BankRepo.save(bank)


class FundsWithdrawn(DomainEvent):
    def __init__(self, bank_id: UniqueId, customer_id: UniqueId, amount: Amount) -> None:
        self._bank_id = bank_id
        self._customer_id = customer_id
        self._amount = amount

    def trigger(self) -> None:
        bank = BankRepo.find_by_id(self._bank_id)
        customer = CustomerRepo.find_by_id(self._customer_id)
        customer.reduce_balance(self._amount)
        bank.reduce_balance(self._amount)
        CustomerRepo.save(customer)
        BankRepo.save(bank)
