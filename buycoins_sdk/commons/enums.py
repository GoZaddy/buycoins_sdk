"""This module contains various constants(mostly in the form of enums) that act as native python versions of similar
constants in the GraphQL API """

from enum import Enum


class BuycoinsType(Enum):
    """This contains enums for all the types in the Buycoins GraphQL API

    """
    ACCOUNT = 'Account'
    BANK_ACCOUNT = 'BankAccount'
    POST_ORDER = 'PostOrder'
    PAYMENT = 'Payment'
    BUYCOINS_PRICE = 'BuycoinsPrice'
    ADDRESS = 'Address'
    DEPOSIT_ACCOUNT = 'DepositAccount'
    ORDER = 'Order'
    ONCHAIN_TRANSFER_REQUEST = 'OnchainTransferRequest'
    TRANSACTION = 'Transaction'


class Cryptocurrency(Enum):
    """The Cryptocurrency enum represents the Cryptocurrency enum in the GraphQL API

    """
    LITECOIN = 'litecoin'
    BITCOIN = 'bitcoin'
    ETHEREUM = 'ethereum'
    USD_COIN = 'usd_coin'
    USD_TETHER = 'usd_tether'
    NAIRA_TOKEN = 'naira_token'


class OrderSide(Enum):
    """The OrderSide enum represents the OrderSide enum in the GraphQL API

    """
    BUY = 'buy'
    SELL = 'sell'


class BuycoinsPriceStatus(Enum):
    """The BuycoinsPriceStatus enum represents the BuycoinsPriceStatus enum in the GraphQL API

    """
    EXPIRED = 'expired'
    ACTIVE = 'active'


class GetOrdersStatus(Enum):
    """The GetOrdersStatus enum represents the GetOrdersStatus enum in the GraphQL API

    """
    OPEN = 'open'
    COMPLETED = 'completed'


class PriceType(Enum):
    """The PriceType enum represents the PriceType enum in the GraphQL API

    """
    STATIC = 'static'
    DYNAMIC = 'dynamic'


class PostOrderStatus(Enum):
    """The PostOrderStatus enum represents the PostOrderStatus enum in the GraphQL API

    """
    INACTIVE = 'inactive'
    ACTIVE = 'active'
    PENDING_DEACTIVATION = 'pending_deactivation'
    PAYMENT_PENDING = 'payment_pending'
    PAYMENT_PROCESSING = 'payment_processing'
    CANCELLED = 'cancelled'
    EXPIRED = 'expired'
    COMPLETED = 'completed'
    OPEN = 'open'
    DONE = 'done'


class PaymentStatus(Enum):
    """The PaymentStatus enum represents the PaymentStatus enum in the GraphQL API

    """
    SUCCESS = 'success'
    PENDING = 'pending'
    FAILED = 'failed'
    RETRIED = 'retried'
    INITIATED = 'initiated'
    READY_FOR_PROCESSING = 'ready_for_processing'
    CANCELED = 'canceled'
    FLAGGED = 'flagged'
    RETURNED = 'returned'


class PaymentTypes(Enum):
    """The PaymentTypes enum represents the PaymentTypes enum in the GraphQL API

    """
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'


class OnchainTransferRequestStatus(Enum):
    """The OnchainTransferRequestStatus enum represents the OnchainTransferRequestStatus enum in the GraphQL API

    """
    UNCONFIRMED = 'unconfirmed'
    CONFIRMED = 'confirmed'
    FLAGGED = 'flagged'
    FAILED = 'failed'
    EXPIRED = 'expired'
    PROCESSED = 'processed'
    READY_FOR_PROCESSING = 'ready_for_processing'
    PROCESSING = 'processing'


class BankAccountTypes(Enum):
    """The BankAccountTypes enum represents the BankAccountTypes enum in the GraphQL API

    """
    WITHDRAWAL = 'withdrawal'
    DEPOSIT = 'deposit'


class OrderStatus(Enum):
    """The OrderStatus enum represents the OrderStatus enum in the GraphQL API

    """
    PENDING = 'pending'
    CANCELED = 'canceled'
    DONE = 'done'
    FAILED = 'failed'


class EventType(Enum):
    """The EventType enum represents the types of events that can be fired by Buycoins

    """
    COINS_INCOMING = 'coins.incoming'
    BANK_DEPOSIT_INCOMING = 'bank_deposit.incoming'
    ORDER_SUCCEEDED = 'order.succeeded'
    ORDER_FAILED = 'order.failed'
