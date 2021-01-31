from python_graphql_client import GraphqlClient
from dotenv import load_dotenv
import base64
import os
import buycoins_sdk.commons.constants as constants
from buycoins_sdk.commons.errors import BuycoinsException
import pprint
from typing import Union

load_dotenv()


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
        print(b64_key)
        self._client = GraphqlClient(os.getenv("BUYCOINS_GRAPHQL_ENDPOINT"), headers={
            'authorization': f"Basic {b64_key}"
        })

    def get_balances(self, cryptocurrency: str) -> dict:
        """Executes the getBalances query

        Args:
            cryptocurrency: A string representing the cryptocurrency to query.
                You can and should use the constants available in buycoins_sdk.constants
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
        variables = {'cryptocurrency': cryptocurrency}
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise BuycoinsException(data['errors'][0]['message'])
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
            raise BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise BuycoinsException(data['errors'][0]['message'])
            else:
                return {'data': data['data']['getBankAccounts']}

    def get_estimated_network_fee(self, amount: str, cryptocurrency: str = constants.BITCOIN) -> dict:
        """Executes the getEstimatedNetworkFee query

        Args:
            amount: A string representing the amount of coins to calculate network fee for
            cryptocurrency: type of cryptocurrency. You can and should use the constants available in buycoins_sdk.constants
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
        variables = {'cryptocurrency': cryptocurrency, 'amount': amount}
        try:
            data = self._client.execute(query=query, variables=variables)
        except Exception as err:
            raise BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise BuycoinsException(data['errors'][0]['message'])
            else:
                return {'data': data['data']['getEstimatedNetworkFee']}

    def get_market_book(self, first: int = None, last: int = None, after: str = None, before: str = None,
                        cryptocurrency: str = constants.BITCOIN) -> dict:
        """Executes the getMarketBook query

            Args:
                first: For pagination. Returns the first n elements in a list.
                last: For pagination. Returns the last n elements in a list.
                after: A string representing a cursor. Returns the elements in the list that come after the specified cursor.
                before: A string representing a cursor. Returns the elements in the list that come before the specified cursor.
                cryptocurrency: type of cryptocurrency. You can and should use the constants available in buycoins_sdk.constants
            Returns:
                A dict representing the GraphQL response
            Raises:
                BuycoinsException: An error occurred
        """

        # The code just before the query is used to format the build the graphql query just by taking in the parameters
        # passed to the method and assigning certain parts to variables which will later form part of the graphql query
        orders_arg = ""
        arg_map = {'first': first, 'last': last, 'after': after, 'before': before}
        arg = ','
        variables = {'cryptocurrency': cryptocurrency, 'after': after,
                     'before': before}
        for i in arg_map:
            if arg_map[i] is not None:
                orders_arg = orders_arg + f"{i}:${i},"
                if i == 'first' or i == 'last':
                    arg = arg + f"${i}: Int,"
                    variables[i] = arg_map[i]
                elif i == 'after' or i == 'before':
                    arg = arg + f"${i}: String,"
        if len(orders_arg) != 0:
            if orders_arg[len(orders_arg) - 1] == ',':
                orders_arg = orders_arg[:-1]
                orders_arg = f"({orders_arg})"

        if arg == ',':
            arg = ''
        else:
            arg = arg[:-1]

        query = """
            query getMarketBook($cryptocurrency: Cryptocurrency""" + arg + """){                           
              getMarketBook(cryptocurrency: $cryptocurrency){
                dynamicPriceExpiry
                orders""" + orders_arg + """{
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
            raise BuycoinsException(str(err))
        else:
            if 'errors' in data:
                raise BuycoinsException(data['errors'][0]['message'])
            else:
                return {'data': data['data']['getMarketBook']}

    def get_orders(self, status: dict, side: dict, cryptocurrency: str = constants.BITCOIN) -> dict:
        return {}

    def get_payments(self) -> dict:
        return {}

    def get_prices(self, side: dict, cryptocurrency: str = constants.BITCOIN) -> dict:
        return {}

    def node(self, id: str) -> dict:
        return {}

    def nodes(self, ids: [str]) -> dict:
        return {}


bc = BuycoinsGraphqlClient(public_key=os.getenv("BUYCOINS_PUBLIC_KEY"), secret_key=os.getenv("BUYCOINS_SECRET_KEY"))

pprint.pprint(bc.get_market_book(cryptocurrency=constants.BITCOIN, last=1))
