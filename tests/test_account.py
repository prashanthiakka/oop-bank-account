import pytest
from src.bank_account.account import BankAccount


def test_initial_balance():
    account = BankAccount("Alice")
    assert account.get_balance() == 0.0


def test_deposit_success():
    account = BankAccount("Bob")
    account.deposit(100)
    assert account.get_balance() == 100.0


def test_deposit_negative_amount():
    account = BankAccount("Charlie")
    with pytest.raises(ValueError):
        account.deposit(-50)


def test_withdraw_success():
    account = BankAccount("Dana", 200)
    account.withdraw(50)
    assert account.get_balance() == 150.0


def test_withdraw_insufficient_balance():
    account = BankAccount("Eve", 50)
    with pytest.raises(ValueError):
        account.withdraw(100)


def test_withdraw_negative_amount():
    account = BankAccount("Frank", 100)
    with pytest.raises(ValueError):
        account.withdraw(-20)


def test_owner_attribute():
    account = BankAccount("Grace", 75)
    assert account.owner == "Grace"
