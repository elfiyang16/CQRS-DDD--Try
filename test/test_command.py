import unittest
import uuid
from bank_co.dto import OpenAccountDto, TransferFundsDto, OpenBankDto, RegisterCustomerDto
from bank_co.command import OpenAccount, DepositFunds, WithdrawFunds, OpenBank, RegisterCustomer
from bank_co.repository import BankRepo, CustomerRepo, AccountRepo
from bank_co.entity import Bank, Customer, Account, InsufficientFunds
from bank_co.value_object import Name, Amount


class TestCommands(unittest.TestCase):
    def test_open_account(self):
        bank_id = uuid.uuid4()
        customer_id = uuid.uuid4()
        name = "savings"

        command = OpenAccount(OpenAccountDto(bank_id, customer_id, name))
        account = command.execute()

        self.assertEqual(account.bank_id.value, bank_id)
        self.assertEqual(account.customer_id.value, customer_id)
        self.assertEqual(account.name.value, name)
        self.assertEqual(account.balance.value, 0)

    def test_deposit(self):
        bank = Bank(Name("my bank"))
        customer = Customer(bank.id, Name("alice"))
        account = Account(bank.id, customer.id, Name("savings"))
        BankRepo.save(bank)
        CustomerRepo.save(customer)
        AccountRepo.save(account)

        amount = 100
        command = DepositFunds(TransferFundsDto(account.id.value, amount))
        command.execute()

        self.assertEqual(bank.balance.value, amount)
        self.assertEqual(customer.balance.value, amount)
        self.assertEqual(account.balance.value, amount)

    def test_withdrawl(self):
        bank = Bank(Name("my bank"))
        customer = Customer(bank.id, Name("alice"))
        account = Account(bank.id, customer.id, Name("savings"))
        BankRepo.save(bank)
        CustomerRepo.save(customer)
        AccountRepo.save(account)

        deposit = 100
        withdraw = 90
        command = DepositFunds(TransferFundsDto(account.id.value, deposit))
        command.execute()

        self.assertEqual(bank.balance.value, deposit)
        self.assertEqual(customer.balance.value, deposit)
        self.assertEqual(account.balance.value, deposit)

        command = WithdrawFunds(TransferFundsDto(account.id.value, withdraw))
        command.execute()

        amount = deposit - withdraw
        self.assertEqual(bank.balance.value, amount)
        self.assertEqual(customer.balance.value, amount)
        self.assertEqual(account.balance.value, amount)

        with self.assertRaises(InsufficientFunds):
            command = WithdrawFunds(
                TransferFundsDto(account.id.value, amount + 1))
            command.execute()

    def test_open_bank(self):
        name = "u bank"

        command = OpenBank(OpenBankDto(name))
        bank = command.execute()

        self.assertEqual(bank.name.value, name)
        self.assertEqual(bank.balance.value, 0)

    def test_register_customer(self):
        bank_id = uuid.uuid4()
        name = "Bob"

        command = RegisterCustomer(RegisterCustomerDto(bank_id, name))
        customer = command.execute()

        self.assertEqual(customer.bank_id.value, bank_id)
        self.assertEqual(customer.name.value, name)
        self.assertEqual(customer.balance.value, 0)
