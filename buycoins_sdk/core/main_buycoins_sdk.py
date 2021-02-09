from buycoins_sdk.client import BuycoinsGraphqlClient
from buycoins_sdk.commons.enums import Cryptocurrency, OrderSide, GetOrdersStatus, BuycoinsType, PriceType
from buycoins_sdk.core.types import Account, BankAccount, EstimatedFee, PostOrders, PaymentConnection, \
    BuycoinsPrice, Order, Payment, DepositAccount, PostOrder, OnchainTransferRequest, Address
from typing import Union, List, Dict


__all__ = [
    'BuycoinsSDK'
]


class BuycoinsSDK:
    """BuycoinsSDK is the entry point of the Buycoins SDK

    All calls to the Buycoins GraphQL API should be done using this class

    Attributes:
        client: A BuycoinsGraphqlClient object where the actual GraphQL queries and mutations are made
    """

    def __init__(self, public_key: str, secret_key: str):
        # TODO: decide whether to remove next 2 lines or not
        self._public_key = public_key
        self._secret_key = secret_key
        self.client = BuycoinsGraphqlClient(public_key=public_key, secret_key=secret_key)

    def get_balances(self, cryptocurrency: Cryptocurrency = None) -> Union[List[Account], Account]:
        """Retrieve supported cryptocurrencies account balance(s)

        Args:
            cryptocurrency: A Cryptocurrency enum representing the cryptocurrency to query.
        Returns:
            An array of Account or a single Account object. An array of Accounts is returned when no cryptocurrency
            is specified
        Raises:
            BuycoinsException: An error occurred
        """
        balances = self.client.get_balances(cryptocurrency)['data']
        if len(balances) > 1:
            result = []

            for balance in balances:
                result.append(Account.from_dict(balance))
            return result
        else:
            return Account.from_dict(balances[0])

    def get_bank_accounts(self, account_number: str = None) -> Union[List[BankAccount], BankAccount]:
        """Retrieve bank accounts

        Args:
            account_number: A string representing the account number to get.
        Returns:
            An array of BankAccount objects or a single BankAccount object. An array of BankAccount objects
            is returned when no account number is specified
        Raises:
            BuycoinsException: An error occurred
        """
        bank_accounts = self.client.get_bank_accounts(account_number)['data']
        if len(bank_accounts) > 1:
            result = []

            for account in bank_accounts:
                result.append(BankAccount.from_dict(account))
            return result
        else:
            return BankAccount.from_dict(bank_accounts[0])

    def get_estimated_network_fee(self, amount: str,
                                  cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> EstimatedFee:
        """Retrieve estimated network fee to send supported cryptocurrencies

        Args:
            amount: A string representing the amount of coins to calculate network fee for
            cryptocurrency: type of cryptocurrency.
        Returns:
            An EstimatedFee object
        Raises:
            BuycoinsException: An error occurred
        """
        estimated_fee = self.client.get_estimated_network_fee(amount=amount, cryptocurrency=cryptocurrency)['data']
        return EstimatedFee.from_dict(estimated_fee)

    def get_market_book(self, first: int = None, last: int = None, after: str = None, before: str = None,
                        cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> PostOrders:
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
        post_orders = self.client.get_market_book(first, last, after, before, cryptocurrency)['data']
        return PostOrders.from_dict(post_orders)

    def get_orders(self, status: GetOrdersStatus, side: OrderSide = None, first: int = None, last: int = None,
                   after: str = None,
                   before: str = None, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> PostOrders:
        """Retrieve open orders

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
                A PostOrders object representing the PostOrders type returned by the GraphQL API
            Raises:
                BuycoinsException: An error occurred
        """
        post_orders = self.client.get_orders(
            side=side,
            first=first,
            last=last,
            after=after,
            before=before,
            cryptocurrency=cryptocurrency,
            status=status
        )['data']
        return PostOrders.from_dict(post_orders)

    def get_payments(self, after: str = None, before: str = None, first: int = None,
                     last: int = None) -> PaymentConnection:
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
        return PaymentConnection.from_dict(self.client.get_payments(
            after=after,
            before=before,
            first=first,
            last=last
        )['data'])

    def get_prices(self, cryptocurrency: Cryptocurrency = None) \
            -> Union[List[BuycoinsPrice], BuycoinsPrice]:
        """Retrieve buy/sell price(s) for supported cryptocurrencies

        Args:
            cryptocurrency: the type of cryptocurrency to query for

        Returns:
            A array of BuycoinsPrice objects or a single BuycoinsPrice object. An array of Buycoins Objects is returned
            when no cryptocurrency is specified
        Raises:
            BuycoinsException: An error occurred

        """
        prices = self.client.get_prices(cryptocurrency)['data']
        if len(prices) > 1:
            result = []

            for price in prices:
                result.append(BuycoinsPrice.from_dict(price))
            return result
        else:
            return BuycoinsPrice.from_dict(prices[0])

    def node(self, node_id: str, gql_type: BuycoinsType) -> dict:
        """Fetches an object given its ID.

        Args:
            node_id: the Global object ID of the node
            gql_type: the GraphQL type of the Graphql node

        Returns:
            A dict representing the GraphQL response
        Raises:
            InvalidGraphQLNodeIDException: You tried to search for a node with the wrong ID or wrong GraphQL type
            BuycoinsException: An unspecified error occurred

        """

        return self.client.node(
            node_id=node_id,
            gql_type=gql_type
        )

    def nodes(self, ids: List[str], gql_types: List[BuycoinsType]) -> dict:
        """Fetches a list of objects given a list of IDs

        Args:
            ids: the list of node IDs
            gql_types: the list of node types

        Returns:
            A dict representing the GraphQL response
        Raises:
            InvalidGraphQLNodeIDException: You tried to search for a node with the wrong ID or wrong GraphQL type
            BuycoinsException: An unspecified error occurred

        """
        return self.client.nodes(
            ids=ids,
            gql_types=gql_types
        )

    def buy(self, price_id: str, coin_amount: str, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> Order:
        """Buy supported cryptocurrencies

        Args:
            price_id: Global ID of a retrieved price
            coin_amount: Amount of coins to buy
            cryptocurrency: type of cryptocurrency

        Returns:
            An Order object representing the GraphQL response

        Raises:
            InsufficientBalanceToBuyException: raised when user has insufficient balance to buy cryptocurrency
            BuycoinsException: An error occurred

        """

        return Order.from_dict(
            self.client.buy(
                price_id=price_id,
                coin_amount=coin_amount,
                cryptocurrency=cryptocurrency
            )['data']
        )

    def cancel_withdrawal(self, payment_id: str) -> Payment:
        """Cancel initiated withdrawal

        Args:
            payment_id: the ID of the Payment node for the withdrawal

        Returns:
            A Payment object representing the GraphQL response

        Raises:
            WithdrawalCannotBeCanceledException: An error occurred because user tried to cancel already processed
             withdrawal
            BuycoinsException: An error occurred
        """
        return Payment.from_dict(
            self.client.cancel_withdrawal(
                payment_id
            )['data']
        )

    def create_address(self, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> Address:
        """Create address to receive supported cryptocurrencies

        Args:
            cryptocurrency: cryptocurrency of address to create

        Returns:
            An Address object representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        return Address.from_dict(
            self.client.create_address(
                cryptocurrency=cryptocurrency
            )['data']
        )

    def create_deposit_account(self, account_name: str) -> DepositAccount:
        """Generate deposit bank accounts to top up your NGNT account with Naira

        Args:
            account_name: name of the account

        Returns:
            A DepositAccount object representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        return DepositAccount.from_dict(
            self.client.create_deposit_account(
                account_name=account_name
            )['data']
        )

    def create_withdrawal(self, bank_account_id: str, amount: str) -> Payment:
        """Create a new withdrawal

        Args:
            bank_account_id: Global object ID of bank account node to withdraw to
            amount: amount to withdraw in naira

        Returns:
            A Payment object representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        return Payment.from_dict(
            self.client.create_withdrawal(
                bank_account_id=bank_account_id,
                amount=amount
            )['data']
        )

    # TODO: test
    def post_limit_order(self, order_side: OrderSide, coin_amount: str, static_price: str, price_type: PriceType,
                         dynamic_exchange_rate: str = None,
                         cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> PostOrder:
        """Create a new limit order

        Args:
            order_side: The order side either buy or sell
            coin_amount: Amount of coins the user wants to trade
            static_price: The static price in naira
            price_type: The type of the price either dynamic or static
            dynamic_exchange_rate: The dynamic exchange rate in naira
            cryptocurrency: type of cryptocurrency

        Returns:
            A PostOrder object representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred

        """
        return PostOrder.from_dict(
            self.client.post_limit_order(
                order_side=order_side,
                coin_amount=coin_amount,
                static_price=static_price,
                price_type=price_type,
                dynamic_exchange_rate=dynamic_exchange_rate,
                cryptocurrency=cryptocurrency
            )['data']
        )


    # TODO: test o
    def post_market_order(self, order_side: OrderSide, coin_amount: str,
                          cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> PostOrder:
        """Create a new market order

        Args:
            order_side: The order side either buy or sell
            coin_amount: Amount of coins the user wants to trade
            cryptocurrency: type of cryptocurrency

        Returns:
            A PostOrder object representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred

        """

        return PostOrder.from_dict(
            self.client.post_market_order(
                order_side=order_side,
                coin_amount=coin_amount,
                cryptocurrency=cryptocurrency
            )['data']
        )

    # TODO: test
    def sell(self, price_id: str, coin_amount: str, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> Order:
        """Sell supported cryptocurrencies

        Args:
            price_id: Global ID of a retrieved price
            coin_amount: Amount of coins to sell
            cryptocurrency: type of cryptocurrency

        Returns:
            An Order object representing the GraphQL response

        Raises:
            InsufficientAmountToSellException: raised when the user has insufficient amount of cryptocurrency to sell
            BuycoinsException: An error occurred

        """

        return Order.from_dict(
            self.client.sell(
                price_id=price_id,
                cryptocurrency=cryptocurrency,
                coin_amount=coin_amount
            )['data']
        )

    # TODO: TEST
    def send(self, address: str, amount: str, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> OnchainTransferRequest:
        """Send supported cryptocurrencies to external address

        Args:
            address: cryptocurrency address of recipient
            amount: amount of cryptocurrency to send
            cryptocurrency: cryptocurrency to send

        Returns:
            An OnchainTransferRequest object representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        return OnchainTransferRequest.from_dict(
            self.client.send(
                address=address,
                amount=amount,
                cryptocurrency=cryptocurrency
            )['data']
        )

    # TODO: TEST
    def send_offchain(self, recipient: str, amount: str,
                      cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> bool:
        """Send supported cryptocurrencies to internal BuyCoins users

        Args:
            recipient: username of recipient
            amount: amount of cryptocurrency to send
            cryptocurrency: cryptocurrency to send

        Returns:
            A boolean indicating whether or not the transfer was successfully initiated

        Raises:
            BuycoinsException: An error occurred
        """
        return self.client.send_offchain(
            recipient=recipient,
            amount=amount,
            cryptocurrency=cryptocurrency
        )['data']['initiated']


