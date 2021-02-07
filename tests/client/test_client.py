from unittest import TestCase, main
from unittest.mock import Mock, patch
from buycoins_sdk import BuycoinsGraphqlClient, enums



class TestBuycoinsGraphqlClient(TestCase):
    @patch('buycoins_sdk.BuycoinsGraphqlClient')
    def setUp(self, mock) -> None:
        self.bc_client = BuycoinsGraphqlClient(secret_key="secret_key", public_key="public_key")
        self.bc_client._client = Mock()

    def test_get_balances(self):
        self.bc_client._client.execute.return_value = {
            'data': {
                'getBalances': {
                    'hey': 'hey'
                }
            }
        }

        i = self.bc_client.get_balances(cryptocurrency=enums.Cryptocurrency.BITCOIN)
        print(i)


if __name__ == '__main__':
    main()
