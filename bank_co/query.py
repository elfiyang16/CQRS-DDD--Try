from abc import ABC, abstractmethod
from uuid import UUID
from bank_co.repository import BankRepo, CustomerRepo, AccountRepo
from bank_co.entity import Customer, Bank, Aggregate, Account
from bank_co.value_object import UniqueId

"""
query goes into Repo to get the data directly from application layer
"""


class Query(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class GetAccount(Query):
    def __init__(self, account_id: UUID) -> None:
        self._account_id = account_id

    def execute(self) -> None:
        return AccountRepo.find_by_id(UniqueId(self._account_id))


class GetCustomer(Query):
    def __init__(self, customer_id: UUID) -> None:
        self._customer_id = customer_id

    def execute(self) -> None:
        return CustomerRepo.find_by_id(UniqueId(self._customer_id))


class GetBank(Query):
    def __init__(self, bank_id: UUID) -> None:
        self._bank_id = bank_id

    def execute(self) -> None:
        return BankRepo.find_by_id(UniqueId(self._bank_id))
