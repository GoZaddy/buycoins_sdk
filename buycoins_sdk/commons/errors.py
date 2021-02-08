"""
This module contains errors that can be raised during the use of the SDK
"""

from .enums import BuycoinsType
from requests import Response

__all__ = [
    'BuycoinsException',
    'InsufficientAmountToSellException',
    'InvalidGraphQLNodeIDException',
    'InsufficientBalanceToBuyException',
    'InsufficientBalanceToWithdrawException',
    'WithdrawalCannotBeCanceledException',
    'BuycoinsHTTPException'
]


class BuycoinsException(Exception):
    """BuycoinsException is a generic exception which all represents all exceptions thrown by the Graphql API. All other
    exceptions must inherit from this

    Attributes:
        error_message: This is a string containing the error message thrown by buycoins
    """

    def __init__(self, error_message: str):
        """Create a new BuycoinsException

        Args:
            error_message: the error message thrown by the Buycoins API
        """
        super().__init__(error_message)


class BuycoinsHTTPException(BuycoinsException):
    """BuycoinsHTTPException is raised when a call to the BuyCoins API raises an HTTPError

    Attributes:
        status_code [int]: an integer representing the status code of the HTTPError
        response [requests.Response]: the HTTP Response from the HTTPError
        error_message: the error message from the HTTPError
    """

    def __init__(self, response: Response, message: str):
        """Create a new BuycoinsHTTPException

            Args:
                response: This is the HTTP Response from the HTTPError
                message: This is error message from the HTTPError
        """
        self.status_code = response.status_code
        self.response = response
        self.error_message = message
        super().__init__(error_message=message)


class InsufficientAmountToSellException(BuycoinsException):
    """InsufficientAmountToSellException is raised when a user tries to sell more cryptocurrency than they have

    Attributes:
        cryptocurrency: a string representing the cryptocurrency the user tried to sell
        amount_to_sell: a string representing the amount of coins the user tried to sell
    """

    def __init__(self, cryptocurrency: str, amount_to_sell: str):
        """Create a new InsufficientAmountToSellException

        Args:
            cryptocurrency: a string representing the cryptocurrency the user tried to sell
            amount_to_sell: the amount of coins the user tried to sell
        """
        self.cryptocurrency = cryptocurrency
        self.amount_to_sell = amount_to_sell
        super().__init__("Your balance is insufficient for this sale")


class InvalidGraphQLNodeIDException(BuycoinsException):
    """InvalidGraphQLNodeIDException is raised when a user tries to get a node with an invalid Global Object ID(one
    that points to no node) or with a wrong GraphQL type

    Attributes:
         node_id: a string representing the Global Object ID that passed by the user
        gql_type: a BuycoinsType enum representing the GraphQL type passed by the user
    """

    def __init__(self, node_id: str = None, gql_type: BuycoinsType = None,
                 message: str = "The ID or GraphQL type you passed in was invalid or wrong"):
        """Create a new InvalidGraphQLNodeIDException

        Args:
            node_id: a string representing the Global Object ID that passed by the user
            gql_type: a BuycoinsType enum representing the GraphQL type passed by the user
        """

        self.node_id = node_id
        self.gql_type = gql_type
        super().__init__(message)


class InsufficientBalanceToBuyException(BuycoinsException):
    """InsufficientBalanceToBuyException is raised when a user tries to buy cryptocurrency with insufficient balance

    Attributes:
        amount_to_buy: a string representing the amount of coins the user tried to buy
        cryptocurrency: a string representing the type of the cryptocurrency the user tried to buy
    """

    def __init__(self, amount_to_buy: str, cryptocurrency: str):
        """Create a new InsufficientBalanceToBuyException

        Args:
            amount_to_buy: amount of coins the user tried to buy
            cryptocurrency: the type of the cryptocurrency the user tried to buy
        """
        self.cryptocurrency = cryptocurrency
        self.amount_to_buy = amount_to_buy
        super().__init__(
            f'Your balance is insufficient for this purchase\nCryptocurrency: {cryptocurrency}, Amount to buy: {amount_to_buy}')


class InsufficientBalanceToWithdrawException(BuycoinsException):
    """InsufficientBalanceToWithdrawException is raised when a user tries to withdraw more than they have

    Attributes:
        amount_to_withdraw: a string representing amount of naira the user tried to withdraw
    """

    def __init__(self, amount_to_withdraw):
        """Create a new InsufficientBalanceToWithdrawException

        Args:
            amount_to_withdraw: amount of naira the user tried to withdraw
        """
        self.amount_to_withdraw = amount_to_withdraw
        super().__init__('Balance is insufficient for this withdrawal')


class WithdrawalCannotBeCanceledException(BuycoinsException):
    """WithdrawalCannotBeCanceledException is raised when a user tries to cancel an already processed withdrawal

    """

    def __init__(self):
        """Create a new WithdrawalCannotBeCanceledException

        """
        super().__init__("This payment has been processed and can not be canceled")
