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
        result = self.buycoins_sdk.get_balances()

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
        # prepare fixture
        client_result_fixture = {'data': [bank_account_fixture]}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.get_bank_accounts.return_value = client_result_fixture
        result = self.buycoins_sdk.get_bank_accounts('000000000000')  # random bank account

        # test for single BankAccount object
        self.assertIsInstance(result, types.BankAccount, 'RESULT SHOULD BE A BankAccount OBJECT')

        # modify fixture
        self.buycoins_sdk.client.get_bank_accounts.return_value = {'data': [bank_account_fixture, bank_account_fixture]}
        result = self.buycoins_sdk.get_bank_accounts()

        # test for multiple BankAccount objects
        self.assertIsInstance(result, list, 'RESULT SHOULD BE A LIST')
        self.assertTrue(len(result) > 1, 'RESULT SHOULD CONTAIN MORE THAN ONE OBJECT')
        for i in result:
            self.assertIsInstance(i, types.BankAccount, 'RESULT SHOULD CONTAIN ONLY BankAccount OBJECTS')

    def test_get_estimated_network_fee(self):
        # prepare fixture
        client_result_fixture = {'data': estimated_fee_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.get_estimated_network_fee.return_value = client_result_fixture
        result = self.buycoins_sdk.get_estimated_network_fee(cryptocurrency=enums.Cryptocurrency.BITCOIN, amount='1000')

        # test for EstimatedFee object
        self.assertIsInstance(result, types.EstimatedFee, 'RESULT SHOULD BE An EstimatedFee OBJECT')
        self.assertEqual(client_result_fixture['data']['estimatedFee'], result.estimated_fee, 'should be equal')
        self.assertEqual(client_result_fixture['data']['total'], result.total, 'should be equal')

    def test_get_market_book(self):
        # prepare fixture
        client_result_fixture = {'data': post_orders_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.get_market_book.return_value = client_result_fixture
        result = self.buycoins_sdk.get_market_book()

        # test for PostOrder object
        self.assertIsInstance(result, types.PostOrders, 'RESULT SHOULD BE A PostOrders OBJECT')

    def test_get_orders(self):
        # prepare fixture
        client_result_fixture = {'data': post_orders_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.get_orders.return_value = client_result_fixture
        result = self.buycoins_sdk.get_orders(status=enums.GetOrdersStatus.OPEN)

        # test for PostOrder object
        self.assertIsInstance(result, types.PostOrders, 'RESULT SHOULD BE A PostOrders OBJECT')

    def test_get_payments(self):
        # prepare fixture
        client_result_fixture = {'data': payment_connection_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.get_payments.return_value = client_result_fixture
        result = self.buycoins_sdk.get_payments()

        # test for PostOrder object
        self.assertIsInstance(result, types.PaymentConnection, 'RESULT SHOULD BE A PaymentConnection OBJECT')

    def test_get_prices(self):
        # prepare fixture
        client_result_fixture = {'data': [buycoins_price_fixture]}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.get_prices.return_value = client_result_fixture
        result = self.buycoins_sdk.get_prices()

        # test for single BuycoinsPrice object
        self.assertIsInstance(result, types.BuycoinsPrice, 'RESULT SHOULD BE A BuycoinsPrice OBJECT')

        # modify fixture
        self.buycoins_sdk.client.get_prices.return_value = {'data': [buycoins_price_fixture, buycoins_price_fixture]}
        result = self.buycoins_sdk.get_prices(cryptocurrency=enums.Cryptocurrency.BITCOIN)

        # test for multiple BuycoinsPrice objects
        self.assertIsInstance(result, list, 'RESULT SHOULD BE A LIST')
        self.assertTrue(len(result) > 1, 'RESULT SHOULD CONTAIN MORE THAN ONE OBJECT')
        for i in result:
            self.assertIsInstance(i, types.BuycoinsPrice, 'RESULT SHOULD CONTAIN ONLY BuycoinsPrice OBJECTS')

    def test_node(self):
        # prepare fixture
        client_result_fixture = {'data': address_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.node.return_value = client_result_fixture
        result = self.buycoins_sdk.node(node_id='random_id', gql_type=enums.BuycoinsType.ADDRESS)

        # test for correct response object
        self.assertIsInstance(result, dict, 'RESULT SHOULD BE A DICT')
        self.assertDictEqual(result, client_result_fixture, 'SHOULD RETURN RESULT FROM BuycoinsGraphqlClient')

    def test_nodes(self):
        # prepare fixture
        client_result_fixture = {'data': [address_fixture, address_fixture]}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.nodes.return_value = client_result_fixture
        result = self.buycoins_sdk.nodes(ids=['random_id', 'another random id'], gql_types=[enums.BuycoinsType.ADDRESS])

        # test for list of nodes object
        self.assertIsInstance(result['data'], list, 'RESULT SHOULD BE A LIST')
        self.assertDictEqual(result, client_result_fixture, 'SHOULD RETURN RESULT FROM BuycoinsGraphqlClient')

    def test_buy(self):
        # prepare fixture
        client_result_fixture = {'data': order_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.buy.return_value = client_result_fixture
        result = self.buycoins_sdk.buy(
            price_id='random price id',
            coin_amount='1',
        )

        # test for Order object
        self.assertIsInstance(result, types.Order, 'RESULT SHOULD BE AN ORDER OBJECT')

    def test_cancel_withdrawal(self):
        # prepare fixture
        client_result_fixture = {'data': payment_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.cancel_withdrawal.return_value = client_result_fixture
        result = self.buycoins_sdk.cancel_withdrawal(
            payment_id='random price id',
        )

        # test for Payment object
        self.assertIsInstance(result, types.Payment, 'RESULT SHOULD BE A PAYMENT OBJECT')

    def test_create_address(self):
        # prepare fixture
        client_result_fixture = {'data': address_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.create_address.return_value = client_result_fixture
        result = self.buycoins_sdk.create_address()

        # test for Address object
        self.assertIsInstance(result, types.Address, 'RESULT SHOULD BE A ADDRESS OBJECT')
        self.assertEqual(result.id, client_result_fixture['data']['id'], 'should be Equal')
        self.assertEqual(result.address, client_result_fixture['data']['address'], 'should be Equal')
        self.assertEqual(result.cryptocurrency, types.Cryptocurrency(client_result_fixture['data']['cryptocurrency']),
                         'should be Equal')
        self.assertEqual(result.created_at, client_result_fixture['data']['createdAt'], 'should be Equal')

    def test_create_deposit_account(self):
        # prepare fixture
        client_result_fixture = {'data': deposit_account_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.create_deposit_account.return_value = client_result_fixture
        result = self.buycoins_sdk.create_deposit_account(
            account_name='random name'
        )

        # test for Payment object
        self.assertIsInstance(result, types.DepositAccount, 'RESULT SHOULD BE A DepositAccount OBJECT')

    def test_create_withdrawal(self):
        # prepare fixture
        client_result_fixture = {'data': payment_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.create_withdrawal.return_value = client_result_fixture
        result = self.buycoins_sdk.create_withdrawal(
            bank_account_id='random bank account id',
            amount='10000'
        )

        # test for Payment object
        self.assertIsInstance(result, types.Payment, 'RESULT SHOULD BE A PAYMENT OBJECT')

    def test_post_limit_order(self):
        # prepare fixture
        client_result_fixture = {'data': post_order_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.post_limit_order.return_value = client_result_fixture
        result = self.buycoins_sdk.post_limit_order(
            static_price='random price id',
            coin_amount='1',
            price_type=enums.PriceType.STATIC,
            order_side=enums.OrderSide.SELL,
            cryptocurrency=enums.Cryptocurrency.BITCOIN
        )

        # test for PostOrder object
        self.assertIsInstance(result, types.PostOrder, 'RESULT SHOULD BE A PostOrder OBJECT')

    def test_post_market_order(self):
        # prepare fixture
        client_result_fixture = {'data': post_order_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.post_market_order.return_value = client_result_fixture
        result = self.buycoins_sdk.post_market_order(
            coin_amount='1',
            order_side=enums.OrderSide.SELL,
            cryptocurrency=enums.Cryptocurrency.BITCOIN
        )

        # test for PostOrder object
        self.assertIsInstance(result, types.PostOrder, 'RESULT SHOULD BE A PostOrder OBJECT')

    def test_sell(self):
        # prepare fixture
        client_result_fixture = {'data': order_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.sell.return_value = client_result_fixture
        result = self.buycoins_sdk.sell(
            price_id='random price id',
            coin_amount='1',
        )

        # test for Order object
        self.assertIsInstance(result, types.Order, 'RESULT SHOULD BE AN ORDER OBJECT')

    def test_send(self):
        # prepare fixture
        client_result_fixture = {'data': onchain_transfer_request_fixture}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.send.return_value = client_result_fixture
        result = self.buycoins_sdk.send(
            amount='random price id',
            cryptocurrency=enums.Cryptocurrency.BITCOIN,
            address='random address'
        )

        # test for OnchainTransferRequest object
        self.assertIsInstance(result, types.OnchainTransferRequest, 'should be an OnchainTransferRequest object')

    def test_send_offchain(self):
        # prepare fixture
        client_result_fixture = {'data': {'initiated': True}}

        # mock the buycoins_sdk's client
        self.buycoins_sdk.client.send_offchain.return_value = client_result_fixture
        result = self.buycoins_sdk.send_offchain(
            amount='random price id',
            cryptocurrency=enums.Cryptocurrency.BITCOIN,
            recipient='random recipient'
        )

        # test for Payment object
        self.assertTrue(result, 'should be True as is in fixture')
