
from abc import ABC, abstractmethod
from bank_co.entity import Bank, Customer, Account, Aggregate
from bank_co.event import FundsDeposited, FundsWithdrawn
from bank_co.value_object import Amount, UniqueId, Name
from bank_co.dto import OpenAccountDto, TransferFundsDto, RegisterCustomerDto, OpenBankDto
from bank_co.repository import AccountRepo, CustomerRepo, BankRepo

"""
Command -- Aggregate Root 
1 --- 1 
use DTO to move data around
Entity independent of Repo, and vice versa
Repo is simply lifting the data access burden away from Entity
it's for storing and fetching data
"""


class Command(ABC):
    @abstractmethod
    def execute(self) -> Aggregate:
        pass


class OpenAccount(Command):
    def __init__(self, request: OpenAccountDto) -> None:
        self._request = request

    def execute(self) -> Account:
        account = Account(UniqueId(self._request.bank_id),
                          UniqueId(self._request.customer_id),
                          Name(self._request.name))
        AccountRepo.save(account)
        return account


class RegisterCustomer(Command):
    def __init__(self, request: RegisterCustomerDto) -> None:
        self._request = request

    def execute(self) -> Customer:
        customer = Customer(UniqueId(self._request.bank_id),
                            Name(self._request.name))
        CustomerRepo.save(customer)
        return customer


class OpenBank(Command):
    def __init__(self, request: OpenBankDto) -> None:
        self._request = request

    def execute(self) -> Bank:
        bank = Bank(Name(self._request.name))
        BankRepo.save(bank)
        return bank


"""
use event to fire side effects alongside the primary AR operation
"""


class DepositFunds(Command):
    def __init__(self, request: TransferFundsDto) -> None:
        self._request = request

    def execute(self) -> Account:
        account = AccountRepo.find_by_id(self._request.id)
        account.deposit(self._request.amount)

        event = FundsDeposited(
            account.bank_id, account.customer_id, Amount(self._request.amount))
        event.trigger()

        return account


class WithdrawFunds(Command):
    def __init__(self, request: TransferFundsDto) -> None:
        self._request = request

    def execute(self) -> Account:
        account = AccountRepo.find_by_id(self._request.id)
        account.deposit(self._request.amount)

        event = FundsWithdrawn(
            account.bank_id, account.customer_id, Amount(self._request.amount))
        event.trigger()

        return account
