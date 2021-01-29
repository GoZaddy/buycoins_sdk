from python_graphql_client import GraphqlClient
from dotenv import load_dotenv
import base64
import os
import buycoins_sdk.commons.constants as constants
from decimal import *

load_dotenv()


# TODO: write and documents BuycoinsGraphqlClient's methods
class BuycoinsGraphqlClient:
    """The BuycoinsGraphqlClient is a wrapper around GraphqlClient which takes in the user's public and secret keys
    for making GraphQL queries.
    """

    def __init__(self, public_key: str, secret_key: str):
        b64_key = base64.b64encode(f"{public_key}:{secret_key}".encode()).decode()
        print(b64_key)
        self._client = GraphqlClient(os.getenv("BUYCOINS_GRAPHQL_ENDPOINT"), headers={
            'authorization': f"Basic {b64_key}"
        })

    def get_balances(self, cryptocurrency: str) -> dict:
        """Retrieve supported cryptocurrencies account balance(s)

        Args:
            cryptocurrency: A string representing the cryptocurrency to query.
                You can and should use the constants available in buycoins_sdk.constants
        Returns:
            A dict representing the GraphQL response

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
            print(err)
        else:
            return {'data': data['data']['getBalances']}

    def get_bank_account(self, account_number: str) -> dict:
        return {}

    def get_estimated_network_fee(self, amount: Decimal, cryptocurrency: str = constants.BITCOIN) -> dict:
        return {}

    def get_market_book(self, coin_amount: Decimal, cryptocurrency: str = constants.BITCOIN) -> dict:
        return {}

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

print(bc.get_balances(constants.LITECOIN))
