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


class InvalidGraphQLNodeIDException(BuycoinsException):
    """InvalidGraphQLNodeIDException is raised when a user tries to get a node with an invalid Global Object ID(one
    that points to no node) or with a wrong GraphQL type

    """

    def __init__(self, node_id=None, gql_type=None,
                 message="The ID or GraphQL type you passed in was invalid or wrong"):
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

        """

    def __init__(self, amount_to_buy, cryptocurrency):
        """Create a new InvalidGraphQLNodeIDException

        Args:
            amount_to_buy: amount of coins the user tried to buy
            cryptocurrency: the type of the cryptocurrency the user tried to buy
        """
        self.cryptocurrency = cryptocurrency
        self.amount_to_buy = amount_to_buy
        super().__init__(f'Your balance is insufficient for this purchase\nCryptocurrency: {cryptocurrency}, Amount to buy: {amount_to_buy}')