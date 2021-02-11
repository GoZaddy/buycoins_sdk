from unittest import TestCase, mock
from buycoins_sdk import BuycoinsSDK, enums, types
from typing import List
from .fixtures import *


class TestMainBuycoinsSDK(TestCase):
    def setUp(self) -> None:
        BuycoinsSDK.__init__ = mock.Mock(side_effect=lambda public_key, secret_key: None)
        self.buycoins_sdk = BuycoinsSDK(public_key='test', secret_key='test')
        self.buycoins_sdk.client = mock.Mock()

    def test_get_balances(self):
        # prepare fixture
        client_result_fixture = {'data': [account_fixture]}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.get_balances.return_value = client_result_fixture
        result = self.buycoins_sdk.get_balances(cryptocurrency=enums.Cryptocurrency.BITCOIN)

        # test for single Account object
        self.assertIsInstance(result, types.Account, 'RESULT SHOULD BE AN ACCOUNT OBJECT')

        # modify fixture
        self.buycoins_sdk.client.get_balances.return_value = {'data': [account_fixture, account_fixture]}
        result = self.buycoins_sdk.get_balances(cryptocurrency=enums.Cryptocurrency.BITCOIN)

        # test for multiple Account objects
        self.assertIsInstance(result, list, 'RESULT SHOULD BE A LIST')
        self.assertTrue(len(result) > 1, 'RESULT SHOULD CONTAIN MORE THAN ONE OBJECT')
        for i in result:
            self.assertIsInstance(i, types.Account, 'RESULT SHOULD CONTAIN ONLY ACCOUNT OBJECTS')


    def test_get_bank_accounts(self):
        pass

    def test_get_estimated_network_fee(self):
        pass

    def test_get_market_book(self):
        pass

    def test_get_orders(self):
        pass

    def test_get_payments(self):
        pass

    def test_get_prices(self):
        pass

    def test_node(self):
        pass

    def test_nodes(self):
        pass

    def test_buy(self):
        pass

    def test_cancel_withdrawal(self):
        pass

    def test_create_address(self):
        pass

    def test_create_deposit_account(self):
        pass

    def test_create_withdrawal(self):
        pass

    def test_post_limit_order(self):
        pass

    def test_post_market_order(self):
        pass

    def test_sell(self):
        pass

    def test_send(self):
        pass

    def test_send_offchain(self):
        pass
