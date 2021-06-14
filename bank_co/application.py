from uuid import UUID
from bank_co.command import OpenBank, RegisterCustomer, OpenAccount, DepositFunds, WithdrawFunds
from bank_co.query import GetBank, GetCustomer, GetAccount
from bank_co.dto import OpenBankDto, RegisterCustomerDto, OpenAccountDto, TransferFundsDto
from bank_co.entity import Account, Customer, Bank


def open_account(bank_id: UUID, customer_id: UUID, name: str) -> Account:
    #  note the dto is not as input
    command = OpenAccount(OpenAccountDto(bank_id, customer_id, name))
    return command.execute()


def register_customer(bank_id: UUID, name: str) -> Customer:
    command = RegisterCustomer(RegisterCustomerDto(bank_id, name))
    return command.execute()


def open_bank(name: str) -> Bank:
    command = OpenBank(OpenBankDto(name))
    return command.execute()


def deposit_funds(account_id: UUID, amount: int) -> Account:
    command = DepositFunds(TransferFundsDto(account_id, amount))
    return command.execute()


def withdraw_funds(account_id: UUID, amount: int) -> Account:
    command = WithdrawFunds(TransferFundsDto(account_id, amount))
    return command.execute()


def get_bank(bank_id: UUID) -> Bank:
    query = GetBank(bank_id)
    return query.execute()


def get_customer(customer_id: UUID) -> Customer:
    query = GetCustomer(customer_id)
    return query.execute()


def get_account(account_id: UUID) -> Account:
    query = GetAccount(account_id)
    return query.execute()
