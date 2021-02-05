from buycoins_sdk.client import BuycoinsGraphqlClient
from buycoins_sdk.commons import Cryptocurrency, OrderSide, GetOrdersStatus, BuycoinsType, PriceType


class BuycoinsSDK:
    """BuycoinsSDK is the entry point of the Buycoins SDK

    All calls to the Buycoins GraphQL API should be done using this class

    """

    def __init__(self, public_key: str, secret_key: str):
        # TODO: decide whether to remove next 2 lines or not
        self._public_key = public_key
        self._secret_key = secret_key
        self.client = BuycoinsGraphqlClient(public_key=public_key, secret_key=secret_key)

    def get_balances(self, cryptocurrency: Cryptocurrency) -> dict:
        """Executes the getBalances query

        Args:
            cryptocurrency: A Cryptocurrency enum representing the cryptocurrency to query.
        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def get_bank_accounts(self, account_number: str) -> dict:
        """Executes the getBankAccounts query

        Args:
            account_number: A string representing the account number to get.
        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def get_estimated_network_fee(self, amount: str, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the getEstimatedNetworkFee query

        Args:
            amount: A string representing the amount of coins to calculate network fee for
            cryptocurrency: type of cryptocurrency.
        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def get_market_book(self, first: int = None, last: int = None, after: str = None, before: str = None,
                        cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the getMarketBook query

            Args:
                first: For pagination. Returns the first n elements in a list.
                last: For pagination. Returns the last n elements in a list.
                after: A string representing a cursor. Returns the elements in the list that come after the specified
                    cursor.
                before: A string representing a cursor. Returns the elements in the list that come before the specified
                    cursor.
                cryptocurrency: type of cryptocurrency.
            Returns:
                A dict representing the GraphQL response
            Raises:
                BuycoinsException: An error occurred
        """
        pass

    def get_orders(self, status: GetOrdersStatus, side: str = None, first: int = None, last: int = None,
                   after: str = None,
                   before: str = None, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the getOrders query

            Args:
                status: the status of the orders to get
                side: the side of the orders to get
                first: For pagination. Returns the first n elements in a list.
                last: For pagination. Returns the last n elements in a list.
                after: A string representing a cursor. Returns the elements in the list that come after the specified
                    cursor.
                before: A string representing a cursor. Returns the elements in the list that come before the specified
                    cursor.
                cryptocurrency: type of cryptocurrency.
            Returns:
                A dict representing the GraphQL response
            Raises:
                BuycoinsException: An error occurred
        """
        pass

    def get_payments(self, after: str = None, before: str = None, first: int = None, last: int = None) -> dict:
        """Executes the getPayments GraphQL query

        Args:
            first: For pagination. Returns the first n elements in a list.
            last: For pagination. Returns the last n elements in a list.
            after: A string representing a cursor. Returns the elements in the list that come after the specified
                cursor.
            before: A string representing a cursor. Returns the elements in the list that come before the specified
                cursor.
        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred

        """
        pass

    def get_prices(self, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the getPrices query

        Args:
            cryptocurrency: the type of cryptocurrency to query for

        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred

        """
        pass

    def node(self, node_id: str, gql_type: BuycoinsType) -> dict:
        """Executes the node Graphql query

        Args:
            node_id: the Global object ID of the node
            gql_type: the GraphQL type of the Graphql node

        Returns:
            A dict representing the GraphQL response
        Raises:
            InvalidGraphQLNodeIDException: You tried to search for a node with the wrong ID or wrong GraphQL type
            BuycoinsException: An unspecified error occurred

        """

        pass

    def nodes(self, ids: list[str], gql_types=list[BuycoinsType]) -> dict:
        """Executes the nodes GraphQL query

        Args:
            ids: the list of node IDs
            gql_types: the list of node types

        Returns:
            A dict representing the GraphQL response
        Raises:
            InvalidGraphQLNodeIDException: You tried to search for a node with the wrong ID or wrong GraphQL type
            BuycoinsException: An unspecified error occurred

        """
        pass

    def buy(self, price_id: str, coin_amount: str, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Execute the buy mutation

        Args:
            price_id: Global ID of a retrieved price
            coin_amount: Amount of coins to buy
            cryptocurrency: type of cryptocurrency

        Returns:
            A dict representing the GraphQL response

        Raises:
            InsufficientBalanceToBuyException: raised when user has insufficient balance to buy cryptocurrency
            BuycoinsException: An error occurred

        """

        pass

    def cancel_withdrawal(self, payment_id: str) -> dict:
        """Executes the cancelWithdrawal mutation

        Args:
            payment_id: the ID of the Payment node for the withdrawal

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def create_address(self, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the createAddress mutation

        Args:
            cryptocurrency: cryptocurrency of address to create

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def create_deposit_account(self, account_name: str) -> dict:
        """Executes the createDepositAccount mutation

        Args:
            account_name: name of the account

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def create_withdrawal(self, bank_account_id: str, amount: str):
        """Executes the createWithdrawal mutation

        Args:
            bank_account_id: Global object ID of bank account node to withdraw to
            amount: amount to withdraw in naira

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def post_limit_order(self, order_side: OrderSide, coin_amount: str, static_price: str, price_type: PriceType,
                         dynamic_exchange_rate: str = None,
                         cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Execute the postLimitOrder mutation

        Args:
            order_side: The order side either buy or sell
            coin_amount: Amount of coins the user wants to trade
            static_price: The static price in naira
            price_type: The type of the price either dynamic or static
            dynamic_exchange_rate: The dynamic exchange rate in naira
            cryptocurrency: type of cryptocurrency

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred

        """
        pass

    def post_market_order(self, order_side: OrderSide, coin_amount: str,
                          cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Execute the postMarketOrder mutation

        Args:
            order_side: The order side either buy or sell
            coin_amount: Amount of coins the user wants to trade
            cryptocurrency: type of cryptocurrency

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred

        """

        pass

    def sell(self, price_id: str, coin_amount: str, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Execute the sell mutation

        Args:
            price_id: Global ID of a retrieved price
            coin_amount: Amount of coins to sell
            cryptocurrency: type of cryptocurrency

        Returns:
            A dict representing the GraphQL response

        Raises:
            InsufficientAmountToSellException: raised when the user has insufficient amount of cryptocurrency to sell
            BuycoinsException: An error occurred

        """

        pass

    def send(self, address: str, amount: str, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the send mutation

        Args:
            address: cryptocurrency address of recipient
            amount: amount of cryptocurrency to send
            cryptocurrency: cryptocurrency to send

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        pass

    def send_offchain(self, recipient: str, amount: str,
                      cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the sendOffchain mutation

        Args:
            recipient: username of recipient
            amount: amount of cryptocurrency to send
            cryptocurrency: cryptocurrency to send

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        pass
