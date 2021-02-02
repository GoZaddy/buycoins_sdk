"""
This module contains and exports the BuycoinsGraphqlClient class  and a helper function
"""

from python_graphql_client import GraphqlClient
from dotenv import load_dotenv
import base64
import os
from buycoins_sdk.commons import errors, gql_fields, Cryptocurrency, GetOrdersStatus, BuycoinsType
import pprint
from typing import Union, Any

load_dotenv()


def _prepare_graphql_args(variables: dict[str, Any], first: int = None, last: int = None, after: str = None,
                          before: str = None) -> dict[str, Any]:
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
            variables[i] = arg_map[i]
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
    }


# TODO: write and documents BuycoinsGraphqlClient's methods
class BuycoinsGraphqlClient:
    """The BuycoinsGraphqlClient is a wrapper around GraphqlClient which takes in the user's public and secret keys
    for making GraphQL queries.
    """

    def __init__(self, public_key: str, secret_key: str):
        """Initialise a BuycoinsGraphqlClient

        Args:
            public_key: your BuyCoins public key as a string
            secret_key: your BuyCoins secret key as a string
        """
        b64_key = base64.b64encode(f"{public_key}:{secret_key}".encode()).decode()
        self._client = GraphqlClient(os.getenv("BUYCOINS_GRAPHQL_ENDPOINT"), headers={
            'authorization': f"Basic {b64_key}"
        })

    def get_balances(self, cryptocurrency: Cryptocurrency) -> dict:
        """Executes the getBalances query

        Args:
            cryptocurrency: A Cryptocurrency enum representing the cryptocurrency to query.
        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred
        """
        query = """
            query getBalances($cryptocurrency: Cryptocurrency){
                getBalances(cryptocurrency: $cryptocurrency){
                    id
                    cryptocurrency
                    confirmedBalance
                }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value}
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
                return {'data': data['data']['getBalances']}

    def get_bank_accounts(self, account_number: str) -> dict:
        """Executes the getBankAccounts query

        Args:
            account_number: A string representing the account number to get.
        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred
        """
        query = """
            query getBankAccounts($accountNumber: String){
                getBankAccounts(accountNumber: $accountNumber){
                    accountName
                    accountNumber
                    accountReference
                    accountType
                    bankName
                    id
                }
            }
        """
        variables = {'accountNumber': account_number}
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
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
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
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
                      id
                      coinAmount
                      createdAt
                      cryptocurrency
                      dynamicExchangeRate
                      pricePerCoin
                      priceType
                      side
                      staticPrice
                      status
                    }
                  }
                }  
              }
            }
        """
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
                return {'data': data['data']['getMarketBook']}

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
        variables = {'cryptocurrency': cryptocurrency.value, 'status': status.value}

        # get arguments for the GraphQL query and that of the orders query
        arg_and_order_arg = _prepare_graphql_args(variables, first, last, after, before)
        connection_arg = arg_and_order_arg['connection_arg']
        arg = arg_and_order_arg['arg']

        # get the arguments for the getOrders query
        get_orders_args = ""
        if side is not None:
            get_orders_args = "side: $side"
            arg = arg + ", $side: OrderSide"
            variables['side'] = side
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
                      id
                      coinAmount
                      createdAt
                      cryptocurrency
                      dynamicExchangeRate
                      pricePerCoin
                      priceType
                      side
                      staticPrice
                      status
                    }
                  }
                }  
              }
            }
        """
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
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
                      """ + gql_fields.type_to_field[BuycoinsType.PAYMENT] + """
                    }
                }
              }
            }
        """
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
                return {'data': data['data']['getPayments']}

    def get_prices(self, cryptocurrency: Cryptocurrency = Cryptocurrency.BITCOIN) -> dict:
        """Executes the getPrices query

        Args:
            cryptocurrency: the type of cryptocurrency to query for

        Returns:
            A dict representing the GraphQL response
        Raises:
            BuycoinsException: An error occurred

        """
        query = """
            query getPrices($cryptocurrency: Cryptocurrency){
              getPrices(cryptocurrency: $cryptocurrency){
                id
                cryptocurrency
                buyPricePerCoin
                expiresAt
                maxBuy
                maxSell
                minBuy
                minCoinAmount
                minSell
                sellPricePerCoin
                status 
              }
            }
        """
        variables = {'cryptocurrency': cryptocurrency.value}

        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
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


        fields = gql_fields.type_to_field[gql_type]


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

        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            elif data['data']['node'] == {}:
                raise errors.InvalidGraphQLNodeIDException(gql_type=gql_type, node_id=node_id)
            else:
                return {'data': data['data']['node']}

    # TODO:
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
        on_part_of_query = """"""
        for i in gql_types:
            on_part_of_query = on_part_of_query + "\n" + """
                ... on """ + i.value + """{
                    """ + gql_fields.type_to_field[i] + """
                }
            """
        query = """
            query nodes($ids: [ID!]!){
                nodes(ids: $ids){
                    """+on_part_of_query+"""
                }
            }
        """

        variables = {'ids': ids}

        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise errors.BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise errors.BuycoinsException(data['errors'][0]['message'])
            else:
                if {} in data['data']['nodes']:
                    raise errors.InvalidGraphQLNodeIDException(message="One of your nodes could not looked up. Please "
                                                                       "check your Node IDs or GraphQL types")
                else:
                    return {'data': data['data']['nodes']}


# bc = BuycoinsGraphqlClient(public_key=os.getenv("BUYCOINS_PUBLIC_KEY"), secret_key=os.getenv("BUYCOINS_SECRET_KEY"))

# pprint.pprint( bc.nodes(gql_types=[BuycoinsType.PAYMENT, BuycoinsType.ADDRESS],
# ids=["UGF5bWVudC1jYWQyOGU1MC04ZGZlLTQ2ZDMtOGNjMS0xNzM4N2YxNDM0ODI=",
# "UGF5bWVudC1mOWFhMmE1Ni00MmYzLTQ1YTYtYThlYS0yZmQyMjZkZmY2NzY=",
# "QWRkcmVzcy0yOTkwNWQzOC01NjhjLTQwOTMtYWNjOS1iZTc3YjNhZmZiN2M=" ]))
