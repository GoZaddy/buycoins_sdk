"""
This module contains errors that can be raised during the use of the SDK
"""


class BuycoinsException(Exception):
    """
    BuycoinsException is a generic exception which all represents all exceptions thrown by the Graphql API. All other
    exceptions must inherit from this
    """

    def __init__(self, error_message: str):
        """Create a new BuycoinsException

        Args:
            error_message: the error message thrown by the Buycoins API
        """
        super().__init__(error_message)


class InsufficientAmountToSellException(BuycoinsException):
    """InsufficientAmountToSellException is raised when a user tries to sell more cryptocurrency than they have

    """
    def __init__(self, cryptocurrency: str, amount_to_sell: str):
        """Create a new InsufficientAmountToSellException

        Args:
            cryptocurrency: a string representing the cryptocurrency the user tried to sell
            amount_to_sell: the amount of coins the user tried to sell
        """
        self.cryptocurrency = cryptocurrency
        self.amount_to_sell = amount_to_sell
        super().__init__(f"Your balance is insufficient for this sale\nCryptocurrency: {cryptocurrency}, Amount to "
                         f"sell: {amount_to_sell}")
