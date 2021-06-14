import unittest
from bank_co.repository import AccountRepo, CustomerRepo, BankRepo
from bank_co.entity import Account, Customer, Bank
from bank_co.value_object import Name, UniqueId


class TestRepos(unittest.TestCase):
    def test_account_repo(self):
        repo = AccountRepo()
        account = Account(UniqueId(), UniqueId(), Name("Savings"))
        repo.save(account)

        test_account = AccountRepo().findById(account.id)
        self.assertEqual(account, test_account)

    def test_customer_repo(self):
        repo = CustomerRepo()
        customer = Customer(UniqueId(), Name("Alice"))
        repo.save(customer)

        test_customer = CustomerRepo().findById(customer.id)
        self.assertEqual(customer, test_customer)

    def test_bank_repo(self):
        repo = BankRepo()
        bank = Bank(Name("Simple Bank"))
        repo.save(bank)

        test_bank = BankRepo().findById(bank.id)
        self.assertEqual(bank, test_bank)
