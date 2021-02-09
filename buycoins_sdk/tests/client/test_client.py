from unittest import TestCase, main
from unittest.mock import Mock
from buycoins_sdk import BuycoinsGraphqlClient, enums, errors, client
from .fixtures import *


def _add_error_to_result(result: dict, message: str = 'random error message'):
    res = result
    res['errors'] = [{
        'message': message
    }]

    return res


class TestClient(TestCase):
    """This is the TestCase for the BuycoinsGraphqlClient Class and some utility functions

    """

    def setUp(self) -> None:
        BuycoinsGraphqlClient.__init__ = Mock(side_effect=lambda public_key, secret_key: None)
        self.bc_client = BuycoinsGraphqlClient(secret_key="secret_key", public_key="public_key")
        self.bc_client._client = Mock()

    def test_prepare_graphql_args(self):
        res = client._prepare_graphql_args(variables={}, first=2, last=2, after='ma', before='mb')
        result = {
            'connection_arg': '(first:$first,last:$last,after:$after,before:$before)',
            'arg': ',$first: Int,$last: Int,$after: String,$before: String',
            'variables': {'first': 2, 'last': 2, 'after': 'ma', 'before': 'mb'}
        }
        self.assertEqual(res, result, 'SHOULD BE EQUAL')

        res = client._prepare_graphql_args(variables={})
        result = {
            'connection_arg': '',
            'arg': '',
            'variables': {}
        }
        self.assertEqual(res, result, 'SHOULD BE EQUAL')

    def test_get_balances(self):
        # testing success state
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

        # testing failure state
        val = {
            'data': {
                'getBalances': None,
            },
            'errors': [
                {
                    'message': 'Test error'
                }
            ]
        }

        self.bc_client._client.execute.return_value = val
        # balances = self.bc_client.get_balances(cryptocurrency=enums.Cryptocurrency.BITCOIN)
        with self.assertRaises(errors.BuycoinsException):
            print(self.bc_client.get_balances(cryptocurrency=enums.Cryptocurrency.BITCOIN))

    def test_get_bank_accounts(self):
        # testing success state
        val = {
            'data': {
                'getBankAccounts': [
                    {
                        'accountName': 'Some random name',
                        'accountNumber': '2119851388',
                        'accountReference': None,
                        'accountType': 'withdrawal',
                        'bankName': 'GTB',
                        'id': 'some_random_node_id'
                    }
                ]
            }
        }
        self.bc_client._client.execute.return_value = val
        bank_accounts = self.bc_client.get_bank_accounts()
        self.assertEqual(val['data']['getBankAccounts'], bank_accounts['data'], "should be Equal")

        # testing failure state
        val = {
            'data': {
                'getBankAccounts': None,
            },
            'errors': [
                {
                    'message': 'Test error'
                }
            ]
        }
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.get_bank_accounts()

    def test_get_estimated_network_fee(self):
        val = {
            'data': {'getEstimatedNetworkFee': {
                'estimatedFee': '0.00036',
                'total': '500.00036'
            }}
        }

        self.bc_client._client.execute.return_value = val
        estimated_fee = self.bc_client.get_estimated_network_fee(amount='random_amount')

        self.assertEqual(val['data']['getEstimatedNetworkFee'], estimated_fee['data'])

        val = {
            'data': {
                'getEstimatedNetworkFee': None
            },
        }
        val = _add_error_to_result(val, 'a random error')

        self.bc_client._client.execute.return_value = val

        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.get_estimated_network_fee(amount='a random amount')

    def test_get_market_book(self):
        # test for success
        val = get_market_book_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.get_market_book()
        self.assertEqual(val['data']['getMarketBook'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            client_result = self.bc_client.get_market_book()

    def test_get_orders(self):
        # test for success
        val = get_orders_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.get_orders(status=enums.GetOrdersStatus.OPEN)
        self.assertEqual(val['data']['getOrders'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            client_result = self.bc_client.get_orders(status=enums.GetOrdersStatus.OPEN)

    def test_get_payments(self):
        # test for success
        val = get_payments_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.get_payments()
        self.assertEqual(val['data']['getPayments'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            client_result = self.bc_client.get_payments()

    def test_get_prices(self):
        # test for success
        val = get_prices_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.get_prices()
        self.assertEqual(val['data']['getPrices'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            client_result = self.bc_client.get_prices()

    def test_node(self):
        # test for success
        val = node_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.node(
            node_id='random id',
            gql_type=enums.BuycoinsType.ADDRESS  # random type
        )
        self.assertEqual(val['data']['node'], client_result['data'], "should be Equal")

        # test for InvalidGraphQLNodeIDException - 1
        val['data']['node'] = {}
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.InvalidGraphQLNodeIDException):
            self.bc_client.node(
                node_id='random id',
                gql_type=enums.BuycoinsType.ADDRESS  # random type
            )

    def test_nodes(self):
        # test for success
        val = nodes_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.nodes(
            ids=['random id'],
            gql_types=[enums.BuycoinsType.ADDRESS]  # random type
        )
        self.assertEqual(val['data']['nodes'], client_result['data'], "should be Equal")

        # test for InvalidGraphQLNodeIDException - 1
        val['data']['nodes'][0] = {}
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.InvalidGraphQLNodeIDException):
            self.bc_client.nodes(
                ids=['random id'],
                gql_types=[enums.BuycoinsType.ADDRESS]  # random type
            )

    def test_buy(self):
        # test for success
        val = buy_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.buy(
            price_id='random id',
            coin_amount='10',
            cryptocurrency=enums.Cryptocurrency.BITCOIN
        )
        self.assertEqual(val['data']['buy'], client_result['data'], "should be Equal")

        # test for error - InsufficientBalanceToBuyException
        val = _add_error_to_result(val, message='Your balance is insufficient for this purchase')
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.InsufficientBalanceToBuyException):
            self.bc_client.buy(
                price_id='random id',
                coin_amount='10',
                cryptocurrency=enums.Cryptocurrency.BITCOIN
            )
        # test for error - BuycoinsException
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.buy(
                price_id='random id',
                coin_amount='10',
                cryptocurrency=enums.Cryptocurrency.BITCOIN
            )

    def test_cancel_withdrawal(self):
        val = cancel_withdrawal_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.cancel_withdrawal(
            payment_id='random_id'
        )
        self.assertEqual(val['data']['cancelWithdrawal'], client_result['data'], "should be Equal")

        # test for error - WithdrawalCannotBeCanceledException
        val = _add_error_to_result(val, message="This payment has been processed and can not be canceled")
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.WithdrawalCannotBeCanceledException):
            self.bc_client.cancel_withdrawal(
                payment_id='random_id'
            )
        # test for error - BuycoinsException
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.cancel_withdrawal(
                payment_id='random_id'
            )

    def test_create_address(self):
        val = create_address_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.create_address()
        self.assertEqual(val['data']['createAddress'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            client_result = self.bc_client.create_address()

    def test_create_deposit_account(self):
        val = create_deposit_account_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.create_deposit_account(account_name='test')
        self.assertEqual(val['data']['createDepositAccount'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            client_result = self.bc_client.create_deposit_account(account_name='test')

    def test_create_withdrawal(self):
        val = create_withdrawal_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.create_withdrawal(bank_account_id='id', amount='123')
        self.assertEqual(val['data']['createWithdrawal'], client_result['data'], "should be Equal")

        # test for error - InsufficientBalanceToWithdrawException

        val = _add_error_to_result(val, message='Balance is insufficient for this withdrawal')
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.InsufficientBalanceToWithdrawException):
            client_result = self.bc_client.create_withdrawal(bank_account_id='id', amount='123')

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            client_result = self.bc_client.create_withdrawal(bank_account_id='id', amount='123')

    def test_post_limit_order(self):
        val = post_limit_order_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.post_limit_order(coin_amount='10', order_side=enums.OrderSide.SELL,
                                                        static_price='1000', price_type=enums.PriceType.STATIC)
        self.assertEqual(val['data']['postLimitOrder'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.post_limit_order(coin_amount='10', order_side=enums.OrderSide.SELL,
                                            static_price='1000', price_type=enums.PriceType.STATIC)

    def test_post_market_order(self):
        val = post_market_order_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.post_market_order(
            order_side=enums.OrderSide.SELL,
            coin_amount='100'
        )
        self.assertEqual(val['data']['postMarketOrder'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.post_market_order(
                order_side=enums.OrderSide.SELL,
                coin_amount='100'
            )

    def test_sell(self):
        val = sell_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.sell(
            price_id='id',
            coin_amount='1',
            cryptocurrency=enums.Cryptocurrency.BITCOIN
        )
        self.assertEqual(val['data']['sell'], client_result['data'], "should be Equal")

        # test for error - InsufficientAmountToSellException

        val = _add_error_to_result(val, message='Your balance is insufficient for this sale')
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.InsufficientAmountToSellException):
            self.bc_client.sell(
                price_id='id',
                coin_amount='1',
                cryptocurrency=enums.Cryptocurrency.BITCOIN
            )

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.sell(
                price_id='id',
                coin_amount='1',
                cryptocurrency=enums.Cryptocurrency.BITCOIN
            )

    def test_send(self):
        val = send_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.send(
            address='address',
            amount='1892.920',
            cryptocurrency=enums.Cryptocurrency.BITCOIN
        )
        self.assertEqual(val['data']['send'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.send(
                address='address',
                amount='1892.920',
                cryptocurrency=enums.Cryptocurrency.BITCOIN
            )

    def test_send_offchain(self):
        val = send_offchain_success
        self.bc_client._client.execute.return_value = val
        client_result = self.bc_client.send_offchain(
            recipient='random person',
            amount='1892.920',
            cryptocurrency=enums.Cryptocurrency.BITCOIN
        )
        self.assertEqual(val['data']['sendOffchain'], client_result['data'], "should be Equal")

        # test for error
        val = _add_error_to_result(val)
        self.bc_client._client.execute.return_value = val
        with self.assertRaises(errors.BuycoinsException):
            self.bc_client.send_offchain(
                recipient='random person',
                amount='1892.920',
                cryptocurrency=enums.Cryptocurrency.BITCOIN
            )


if __name__ == '__main__':
    main()
