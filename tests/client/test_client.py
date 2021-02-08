from unittest import TestCase, main
from unittest.mock import Mock, patch
from buycoins_sdk import BuycoinsGraphqlClient, enums


class TestBuycoinsGraphqlClient(TestCase):
    @patch('buycoins_sdk.BuycoinsGraphqlClient')
    def setUp(self, mock) -> None:
        self.bc_client = BuycoinsGraphqlClient(secret_key="secret_key", public_key="public_key")
        self.bc_client._client = Mock()

    def test_get_balances(self):
        val = {
            'data': {
                'getBalances': [
                    {
                        'confirmedBalance': '0.0',
                        'cryptocurrency': 'bitcoin',
                        'id': 'QWNjb3VudC0='
                    }
                ]
            }
        }
        self.bc_client._client.execute.return_value = val

        balances = self.bc_client.get_balances(cryptocurrency=enums.Cryptocurrency.BITCOIN)

        self.assertEqual(val['data']['getBalances'], balances['data'], "should be Equal")


if __name__ == '__main__':
    main()
