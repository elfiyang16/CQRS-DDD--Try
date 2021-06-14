from dataclasses import dataclass
from uuid import UUID


@dataclass
class OpenAccountDto:
    bank_id: UUID
    customer_id: UUID
    name: str


@dataclass
class TransferFundsDto:
    amount: int
    account_id: UUID


@dataclass
class OpenBankDto:
    name: str


@dataclass
class RegisterCustomerDto:
    bank_id: UUID
    name: str
