"""
This module contains and exports the BuycoinsGraphqlClient class  and a helper function
"""

from python_graphql_client import GraphqlClient
import base64
from requests import exceptions
from buycoins_sdk.commons import errors, type_to_field
from buycoins_sdk.commons.enums import Cryptocurrency, GetOrdersStatus, BuycoinsType, OrderSide, \
    PriceType
from typing import Any, Dict, List

__all__ = [
    'BuycoinsGraphqlClient',
    '_prepare_graphql_args',
    '_wrap_graphql_call'
]


def _prepare_graphql_args(variables: Dict[str, Any], first: int = None, last: int = None, after: str = None,
                          before: str = None) -> Dict[str, Any]:
    """This function takes in common pagination args for the Connection and prepares them into two variables
    to be used in GraphQL queries

    Args:
        variables: The map of GraphQL variables to be passed to GraphQLClient
        first: For pagination. Returns the first n elements in a list.
        last: For pagination. Returns the last n elements in a list.
        after: A string representing a cursor. Returns the elements in the list that come after the specified
                    cursor.
        before: A string representing a cursor. Returns the elements in the list that come before the specified
                    cursor.

    Returns: A dictionary with keys: connection_arg and arg, which represents the arguments for the Connection and the
            GraphQL query.
    """

    var = variables
    connection_arg = ''
    arg_map = {'first': first, 'last': last, 'after': after, 'before': before}
    arg = ','
    for i in arg_map:
        if arg_map[i] is not None:
            connection_arg = connection_arg + f"{i}:${i},"
            if i == 'first' or i == 'last':
                arg = arg + f"${i}: Int,"
            elif i == 'after' or i == 'before':
                arg = arg + f"${i}: String,"
            var[i] = arg_map[i]
    if connection_arg != '':
        connection_arg = connection_arg[:-1]
        connection_arg = f"({connection_arg})"

    if arg == ',':
        arg = ''
    else:
        arg = arg[:-1]

    return {
        "connection_arg": connection_arg,
        "arg": arg,
        'variables': var
    }

def _wrap_graphql_call(client: GraphqlClient, query: str, variables: dict) -> Any:
    """This function wraps calls to the GraphQL API and raises the appropriate exceptions

    Args:
        client: The GraphqlClient
        query: The GraphQL query string
        variables: The variables used within the GraphQL query

    Returns:
        The GraphQL response is returned

    """
    try:
        data = client.execute(query=query, variables=variables)
    except exceptions.HTTPError as err:
        raise errors.BuycoinsHTTPException(
            response=err.response,
            message=str(err)
        )
    except Exception as err:
        raise errors.BuycoinsException(str(err))
    else:
        if 'errors' in data:
            # for the buy query
            if data['errors'][0]['message'] == 'Your balance is insufficient for this purchase' and 'buy' in data['data']:
                raise errors.InsufficientBalanceToBuyException(cryptocurrency=variables['cryptocurrency'],
                                                               amount_to_buy=variables['coin_amount'])
            # for the cancelWithdrawal mutation
            elif data['errors'][0]['message'] == "This payment has been processed and can not be canceled" \
                    and 'cancelWithdrawal' in data['data']:
                raise errors.WithdrawalCannotBeCanceledException()

            # for the createWithdrawal mutation
            elif data['errors'][0]['message'] == 'Balance is insufficient for this withdrawal' \
                    and 'createWithdrawal' in data['data']:
                raise errors.InsufficientBalanceToWithdrawException(amount_to_withdraw=variables['amount'])

            # for the sell mutation
            elif data['errors'][0]['message'] == 'Your balance is insufficient for this sale' \
                    and 'sell' in data['data']:
                raise errors.InsufficientAmountToSellException(cryptocurrency=variables['cryptocurrency'],
                                                               amount_to_sell=variables['coin_amount'])
            else:
                raise errors.BuycoinsException(data['errors'][0]['message'])
        else:
            return data


class BuycoinsGraphqlClient:
    """The BuycoinsGraphqlClient is a wrapper around GraphqlClient which takes in the user's public and secret keys
    for making GraphQL queries.

    Attributes:
        _client: A GraphqlClient used to make queries and mutations directly. Only use this when you want to write your
                    own queries and mutations. Most times, you won't need to do that yourself.
    """

    def __init__(self, public_key: str, secret_key: str):
        """Initialise a BuycoinsGraphqlClient

        Args:
            public_key: your BuyCoins public key as a string
            secret_key: your BuyCoins secret key as a string
        """
        b64_key = base64.b64encode(f"{public_key}:{secret_key}".encode()).decode()
        self._client = GraphqlClient("https://backend.buycoins.tech/api/graphql", headers={
            'authorization': f"Basic {b64_key}"
        })

    def get_balances(self, cryptocurrency: Cryptocurrency) -> dict:
        """Executes the getBalances query

        Args:
            cryptocurrency: A Cryptocurrency enum representing the cryptocurrency to query.
        Returns:
            A dict representing the GraphQL response
        Raises:
            AuthenticationException: User provided wrong on invalid BuyCoins API credentials
            BuycoinsException: An error occurred
        """
        if cryptocurrency is None:
            query = """
                query getBalances{
                    getBalances{
                        """ + type_to_field[BuycoinsType.ACCOUNT] + """
                    }
                }
            """
            variables = {}
        else:
            query = """
                query getBalances($cryptocurrency: Cryptocurrency){
                    getBalances(cryptocurrency: $cryptocurrency){
                        """ + type_to_field[BuycoinsType.ACCOUNT] + """
                    }
                }
            """
            variables = {'cryptocurrency': cryptocurrency.value}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['getBalances']}

    def get_bank_accounts(self, account_number=None) -> dict:
        """Executes the getBankAccounts query

        Args:
            account_number: A string representing the account number to get.
        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred
        """
        if account_number is None:
            query = """
                query getBankAccounts{
                    getBankAccounts{
                        """ + type_to_field[BuycoinsType.BANK_ACCOUNT] + """
                    }
                }
            """
            variables = {}
        else:
            query = """
                query getBankAccounts($accountNumber: String){
                    getBankAccounts(accountNumber: $accountNumber){
                        """ + type_to_field[BuycoinsType.BANK_ACCOUNT] + """
                    }
                }
            """
            variables = {'accountNumber': account_number}
        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['getBankAccounts']}

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
        query = """
            query getEstimatedNetworkFee($cryptocurrency: Cryptocurrency, $amount: BigDecimal!){
                getEstimatedNetworkFee(cryptocurrency: $cryptocurrency, amount: $amount){
                    estimatedFee
                    total
                }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value, 'amount': amount}
        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['getEstimatedNetworkFee']}

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
        variables = {'cryptocurrency': cryptocurrency.value}

        # get arguments for the GraphQL query and that of the orders query
        arg_and_order_arg = _prepare_graphql_args(variables, first, last, after, before)
        connection_arg = arg_and_order_arg['connection_arg']
        arg = arg_and_order_arg['arg']
        variables = arg_and_order_arg['variables']

        query = """
            query getMarketBook($cryptocurrency: Cryptocurrency""" + arg + """){                           
              getMarketBook(cryptocurrency: $cryptocurrency){
                dynamicPriceExpiry
                orders""" + connection_arg + """{
                  pageInfo{
                    endCursor
                    hasNextPage
                    hasPreviousPage
                    startCursor
                  }
                  edges{
                    cursor
                    node{
                      """ + type_to_field[BuycoinsType.POST_ORDER] + """
                    }
                  }
                }  
              }
            }
        """
        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['getMarketBook']}

    def get_orders(self, status: GetOrdersStatus, side: OrderSide = None, first: int = None, last: int = None,
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
        variables = {'cryptocurrency': cryptocurrency.value, 'status': status.value}

        # get arguments for the GraphQL query and that of the orders query
        arg_and_order_arg = _prepare_graphql_args(variables, first, last, after, before)
        connection_arg = arg_and_order_arg['connection_arg']
        arg = arg_and_order_arg['arg']
        variables = arg_and_order_arg['variables']

        # get the arguments for the getOrders query
        get_orders_args = ""
        if side is not None:
            get_orders_args = "side: $side"
            arg = arg + ", $side: OrderSide"
            variables['side'] = side.value
        query = """
            query getOrders($cryptocurrency: Cryptocurrency, $status: GetOrdersStatus!""" + arg + """){                           
              getOrders(cryptocurrency: $cryptocurrency, status: $status, """ + get_orders_args + """ ){
                dynamicPriceExpiry
                orders""" + connection_arg + """{
                  pageInfo{
                    endCursor
                    hasNextPage
                    hasPreviousPage
                    startCursor
                  }
                  edges{
                    cursor
                    node{
                      """ + type_to_field[BuycoinsType.POST_ORDER] + """
                    }
                  }
                }  
              }
            }
        """
        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['getOrders']}

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
        variables = {}
        args_and_get_payments_args = _prepare_graphql_args(variables, first, last, after, before)
        arg = args_and_get_payments_args['arg']
        connection_arg = args_and_get_payments_args['connection_arg']
        variables = args_and_get_payments_args['variables']

        if arg != "":
            arg = arg[1:]
            arg = f"({arg})"

        query = """
            query getPayments""" + arg + """{                           
              getPayments""" + connection_arg + """{
                pageInfo{
                    endCursor
                    hasNextPage
                    hasPreviousPage
                    startCursor
                }
                edges{
                    cursor
                    node{
                      """ + type_to_field[BuycoinsType.PAYMENT] + """
                    }
                }
              }
            }
        """
        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['getPayments']}

    def get_prices(self, cryptocurrency: Cryptocurrency = None) -> dict:
        """Executes the getPrices query

        Args:
            cryptocurrency: the type of cryptocurrency to query for

        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred

        """
        if cryptocurrency is None:
            query = """
                        query getPrices{
                          getPrices{
                            """ + type_to_field[BuycoinsType.BUYCOINS_PRICE] + """ 
                          }
                        }
                    """
            variables = {}
        else:
            query = """
                query getPrices($cryptocurrency: Cryptocurrency){
                  getPrices(cryptocurrency: $cryptocurrency){
                    """ + type_to_field[BuycoinsType.BUYCOINS_PRICE] + """ 
                  }
                }
            """
            variables = {'cryptocurrency': cryptocurrency.value}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['getPrices']}

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

        fields = type_to_field[gql_type]

        query = """
            query node($id: ID!){
                node(id: $id){
                     ... on """ + gql_type.value + """ {
                        """ + fields + """
                    }
                }
            }
        """

        variables = {'id': node_id}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        if data['data']['node'] == {}:
            raise errors.InvalidGraphQLNodeIDException(gql_type=gql_type, node_id=node_id)
        else:
            return {'data': data['data']['node']}

    def nodes(self, ids: List[str], gql_types: List[BuycoinsType]) -> dict:
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
        on_part_of_query = """"""
        for i in gql_types:
            on_part_of_query = on_part_of_query + "\n" + """
                ... on """ + i.value + """{
                    """ + type_to_field[i] + """
                }
            """
        query = """
            query nodes($ids: [ID!]!){
                nodes(ids: $ids){
                    """ + on_part_of_query + """
                }
            }
        """

        variables = {'ids': ids}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        if {} in data['data']['nodes']:
            raise errors.InvalidGraphQLNodeIDException(message="One of your nodes could not looked up. Please "
                                                               "check your Node IDs or GraphQL types")
        else:
            return {'data': data['data']['nodes']}

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

        query = """
            mutation buy($cryptocurrency: Cryptocurrency, $price: ID!, $coin_amount: BigDecimal!){
                buy(cryptocurrency: $cryptocurrency, price: $price, coin_amount: $coin_amount){
                   """ + type_to_field[BuycoinsType.ORDER] + """
                }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value, 'price': price_id, 'coin_amount': coin_amount}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['buy']}

    def cancel_withdrawal(self, payment_id: str) -> dict:
        """Executes the cancelWithdrawal mutation

        Args:
            payment_id: the ID of the Payment node for the withdrawal

        Returns:
            A dict representing the GraphQL response

        Raises:
            WithdrawalCannotBeCanceledException: An error occurred because user tried to cancel already processed
             withdrawal
            BuycoinsException: An error occurred
        """
        query = """
            mutation cancelWithdrawal($payment: ID!){
                cancelWithdrawal(payment: $payment){
                   """ + type_to_field[BuycoinsType.PAYMENT] + """
                }
            }
        """
        variables = {'payment': payment_id}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['cancelWithdrawal']}

    def create_address(self, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the createAddress mutation

        Args:
            cryptocurrency: cryptocurrency of address to create

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        query = """
            mutation createAddress($cryptocurrency: Cryptocurrency){
                createAddress(cryptocurrency: $cryptocurrency){
                    """ + type_to_field[BuycoinsType.ADDRESS] + """
                }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['createAddress']}

    def create_deposit_account(self, account_name: str) -> dict:
        """Executes the createDepositAccount mutation

        Args:
            account_name: name of the account

        Returns:
            A dict representing the GraphQL response

        Raises:
            BuycoinsException: An error occurred
        """
        query = """
            mutation createDepositAccount($account_name: String!){
                createDepositAccount(accountName: $account_name){
                   """ + type_to_field[BuycoinsType.DEPOSIT_ACCOUNT] + """
                }
            }
        """
        variables = {'account_name': account_name}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['createDepositAccount']}

    def create_withdrawal(self, bank_account_id: str, amount: str):
        """Executes the createWithdrawal mutation

        Args:
            bank_account_id: Global object ID of bank account node to withdraw to
            amount: amount to withdraw in naira

        Returns:
            A dict representing the GraphQL response

        Raises:
            InsufficientBalanceToWithdrawException: This is raised when a user tries withdrawing more naira than they have
            BuycoinsException: An error occurred
        """
        query = """
            mutation createWithdrawal($bank_account: ID!, $amount: BigDecimal!){
                createWithdrawal(bankAccount: $bank_account, amount: $amount){
                   """ + type_to_field[BuycoinsType.PAYMENT] + """
                }
            }
        """
        variables = {'bank_account': bank_account_id, 'amount': amount}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['createWithdrawal']}

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
        dynamic_exchange_rate_query_slices = ["", ""]
        if dynamic_exchange_rate is not None:
            dynamic_exchange_rate_query_slices = [", $dynamic_exchange_rate: BigDecimal", ", dynamicExchangeRate: "
                                                                                          "$dynamic_exchange_rate"]
        static_price_query_slices = ["", ""]
        if static_price_query_slices is not None:
            static_price_query_slices = [", $static_price: BigDecimal", ", staticPrice: $static_price"]
        query = """
            mutation postLimitOrder($cryptocurrency: Cryptocurrency, $order_side: OrderSide!, $coin_amount: BigDecimal!,
            $price_type: PriceType!""" + dynamic_exchange_rate_query_slices[0] + static_price_query_slices[0] + """){
                postLimitOrder(cryptocurrency: $cryptocurrency, orderSide: $order_side, coinAmount: $coin_amount, 
                priceType: $price_type""" + dynamic_exchange_rate_query_slices[1] + \
                static_price_query_slices[1] + """){
                   """ + type_to_field[BuycoinsType.POST_ORDER] + """
                }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value, 'order_side': order_side.value, 'coin_amount': coin_amount,
                     'static_price': static_price, 'price_type': price_type.value,
                     'dynamic_exchange_rate': dynamic_exchange_rate}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['postLimitOrder']}

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

        query = """
            mutation postMarketOrder($cryptocurrency: Cryptocurrency, $order_side: OrderSide!, $coin_amount: BigDecimal!){
                postMarketOrder(cryptocurrency: $cryptocurrency, orderSide: $order_side, coinAmount: $coin_amount){
                   """ + type_to_field[BuycoinsType.POST_ORDER] + """
                }
            }
        """

        variables = {'cryptocurrency': cryptocurrency.value, 'order_side': order_side.value, 'coin_amount': coin_amount}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['postMarketOrder']}

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

        query = """
            mutation sell($cryptocurrency: Cryptocurrency, $price: ID!, $coin_amount: BigDecimal!){
                sell(cryptocurrency: $cryptocurrency, price: $price, coin_amount: $coin_amount){
                   """ + type_to_field[BuycoinsType.ORDER] + """
                }
            }
        """

        variables = {'cryptocurrency': cryptocurrency.value, 'price': price_id, 'coin_amount': coin_amount}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['sell']}

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
        query = """
            mutation send($cryptocurrency: Cryptocurrency, $address: String!, $amount: BigDecimal!){
                send(cryptocurrency: $cryptocurrency, address: $address, amount: $amount){
                   """ + type_to_field[BuycoinsType.ONCHAIN_TRANSFER_REQUEST] + """
                }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value, 'address': address, 'amount': amount}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['send']}

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
        query = """
            mutation sendOffchain($cryptocurrency: Cryptocurrency, $recipient: String!, $amount: BigDecimal!){
                sendOffchain(cryptocurrency: $cryptocurrency, recipient: $recipient, amount: $amount){
                   initiated
                }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value, 'recipient': recipient, 'amount': amount}

        data = _wrap_graphql_call(self._client, query=query, variables=variables)
        return {'data': data['data']['sendOffchain']}

