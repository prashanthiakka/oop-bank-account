class BankAccount:
    """Represents a simple bank account."""

    def __init__(self, owner: str, balance: float = 0.0):
        """
        Initialize a bank account.

        Args:
            owner (str): The name of the account owner.
            balance (float, optional): Starting balance. Defaults to 0.0.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw. Must be positive and
                            not exceed the current balance.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Get the current account balance.

        Returns:
            float: The current balance.
        """
        return self.balance
