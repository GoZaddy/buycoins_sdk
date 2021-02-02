from enum import Enum


class Cryptocurrency(Enum):
    """The Cryptocurrency enum represents the Cryptocurrency enum in the GraphQL API

    """
    LITECOIN = 'litecoin'
    BITCOIN = 'bitcoin'
    ETHEREUM = 'ethereum'
    USD_COIN = 'usd_coin'
    USD_TETHER = 'usd_tether'


class OrderSide(Enum):
    """The OrderSide enum represents the OrderSide enum in the GraphQL API

    """
    BUY = 'buy'
    SELL = 'sell'


class BuycoinsPriceStatus(Enum):
    """The BuycoinsPriceStatus enum represents the BuycoinsPriceStatus enum in the GraphQL API

    """
    EXPIRED = 'expired'
    ACTIVE = 'status'


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
