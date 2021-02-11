from unittest import TestCase
from buycoins_sdk import types, errors
from .fixtures import *


class TestTypes(TestCase):

    def test_account(self):
        result = types.Account.from_dict(account_fixture)

        self.assertIsInstance(result, types.Account, 'should be an Account object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = account_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.Account.from_dict(modified_fixture)

    def test_bank_account(self):
        result = types.BankAccount.from_dict(bank_account_fixture)

        self.assertIsInstance(result, types.BankAccount, 'should be a BankAccount object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = bank_account_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.BankAccount.from_dict(modified_fixture)

    def test_post_order(self):
        result = types.PostOrder.from_dict(post_order_fixture)

        self.assertIsInstance(result, types.PostOrder, 'should be a PostOrder object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = post_order_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.PostOrder.from_dict(modified_fixture)

    def test_payment(self):
        result = types.Payment.from_dict(payment_fixture)

        self.assertIsInstance(result, types.Payment, 'should be a Payment object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = payment_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.Payment.from_dict(modified_fixture)

    def test_buycoins_price(self):
        result = types.BuycoinsPrice.from_dict(buycoins_price_fixture)

        self.assertIsInstance(result, types.BuycoinsPrice, 'should be a BuycoinsPrice object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = buycoins_price_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.BuycoinsPrice.from_dict(modified_fixture)

    def test_address(self):
        result = types.Address.from_dict(address_fixture)

        self.assertIsInstance(result, types.Address, 'should be an Address object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = address_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.Address.from_dict(modified_fixture)

    def test_deposit_account(self):
        result = types.DepositAccount.from_dict(deposit_account_fixture)

        self.assertIsInstance(result, types.DepositAccount, 'should be a DepositAccount object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = deposit_account_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.DepositAccount.from_dict(modified_fixture)

    def test_order(self):
        result = types.Order.from_dict(order_fixture)

        self.assertIsInstance(result, types.Order, 'should be an Order object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = order_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.Order.from_dict(modified_fixture)

    def test_onchain_transfer_request(self):
        result = types.OnchainTransferRequest.from_dict(onchain_transfer_request_fixture)

        self.assertIsInstance(result, types.OnchainTransferRequest, 'should be an OnchainTransferRequest object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = onchain_transfer_request_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.OnchainTransferRequest.from_dict(modified_fixture)

    def test_transaction(self):
        result = types.Transaction.from_dict(transaction_fixture)

        self.assertIsInstance(result, types.Transaction, 'should be a Transaction object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = transaction_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.Transaction.from_dict(modified_fixture)

    def test_estimated_fee(self):
        result = types.EstimatedFee.from_dict(estimated_fee_fixture)

        self.assertIsInstance(result, types.EstimatedFee, 'should be an EstimatedFee object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = estimated_fee_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.EstimatedFee.from_dict(modified_fixture)

    def test_page_info(self):
        result = types.PageInfo.from_dict(page_info_fixture)

        self.assertIsInstance(result, types.PageInfo, 'should be a PageInfo object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = page_info_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.PageInfo.from_dict(modified_fixture)

    def test_post_orders(self):
        result = types.PostOrders.from_dict(post_orders_fixture)

        self.assertIsInstance(result, types.PostOrders, 'should be a PostOrders object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = post_orders_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.PostOrders.from_dict(modified_fixture)

    def test_payment_connection(self):
        result = types.PaymentConnection.from_dict(payment_connection_fixture)

        self.assertIsInstance(result, types.PaymentConnection, 'should be a PaymentConnection object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = payment_connection_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.PaymentConnection.from_dict(modified_fixture)

    def test_event(self):
        result = types.Event.from_request_body(event_fixture)

        self.assertIsInstance(result, types.Event, 'should be a PaymentConnection object')
        # test for fields equality

        # test for error - MissingFieldException
        modified_fixture = event_fixture
        modified_fixture.popitem()

        with self.assertRaises(errors.MissingFieldException):
            result = types.Event.from_request_body(modified_fixture)
