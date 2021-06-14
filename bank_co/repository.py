from typing import Dict
from uuid import UUID
from bank_co.entity import Account, Customer, Bank, Aggregate
from bank_co.value_object import UniqueId


account_db: Dict[UUID, Aggregate] = {}
customer_db: Dict[UUID, Aggregate] = {}
bank_db: Dict[UUID, Aggregate] = {}


class AccountRepo(object):
    @classmethod
    def save(cls, account: Account):
        account_db[account.id] = account

    @classmethod
    def find_by_id(cls, id: UUID):
        return account_db[id]


class CustomerRepo(object):
    @classmethod
    def save(cls, customer: Customer):
        customer_db[customer.id] = customer

    @classmethod
    def find_by_id(cls, id: UUID):
        return customer_db[id]


class BankRepo(object):
    @classmethod
    def save(cls, bank: Bank):
        bank_db[bank.id] = bank

    @classmethod
    def find_by_id(cls, id: UUID):
        return bank_db[id]
