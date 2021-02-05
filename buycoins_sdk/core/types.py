from buycoins_sdk.commons import Cryptocurrency, PriceType, GetOrdersStatus, OrderSide, \
    PostOrderStatus, PaymentStatus, PaymentTypes, BuycoinsPriceStatus, BankAccountTypes, OrderStatus, OnchainTransferRequestStatus

from buycoins_sdk.client import BuycoinsGraphqlClient
import os


# TODO: WRITE AND DOCUMENT METHODS

class Account:
    """
    This class represents the Buycoins Account type
    """

    def __init__(self, node_id: str, cryptocurrency: str, confirmed_balance: str):
        self.id = node_id
        self.cryptocurrency = Cryptocurrency(cryptocurrency)
        self.confirmed_balance = confirmed_balance

    @staticmethod
    def from_dict(fields: dict):
        account = Account(node_id=fields['id'], cryptocurrency=fields['cryptocurrency'],
                          confirmed_balance=fields['confirmedBalance'])
        return account


class BankAccount:
    """
    This class represents the Buycoins BankAccount type
    """

    def __init__(self, node_id: str, account_name: str, account_number: str, account_reference: str,
                 account_type: str, bank_name: str):
        self.id = node_id
        self.account_name = account_name
        self.account_number = account_number
        self.account_reference = account_reference
        self.account_type = BankAccountTypes(account_type)
        self.bank_name = bank_name

    @staticmethod
    def from_dict(fields: dict):
        bank_account = BankAccount(
            node_id=fields['id'],
            account_name=fields['accountName'],
            account_number=fields['accountNumber'],
            account_reference=fields['accountReference'],
            account_type=fields['accountType'],
            bank_name=fields['bankName']
        )
        return bank_account


class PostOrder:
    """
    This class represents the Buycoins PostOrder type
    """

    def __init__(self, node_id: str, coin_amount: str, created_at: str, cryptocurrency: str,
                 dynamic_exchange_rate: str, price_per_coin: str, price_type: str, side: str,
                 static_price: str, status: str):
        """
        This initialises a PostOrder object
        Args:
            node_id:
            coin_amount:
            created_at:
            cryptocurrency:
            dynamic_exchange_rate:
            price_per_coin:
            price_type:
            side:
            static_price:
            status:
        """
        self.status = PostOrderStatus(status)
        self.static_price = static_price
        self.side = OrderSide(side)
        self.price_type = price_type
        self.price_per_coin = price_per_coin
        self.dynamic_exchange_rate = dynamic_exchange_rate
        self.cryptocurrency = Cryptocurrency(cryptocurrency)
        self.created_at = created_at
        self.coin_amount = coin_amount
        self.id = node_id

    @staticmethod
    def from_dict(fields: dict):
        post_order = PostOrder(
            node_id=fields['id'],
            coin_amount=fields['coinAmount'],
            created_at=fields['createdAt'],
            cryptocurrency=fields['cryptocurrency'],
            dynamic_exchange_rate=fields['dynamicExchangeRate'],
            price_per_coin=fields['pricePerCoin'],
            price_type=fields['priceType'],
            side=fields['side'],
            static_price=fields['staticPrice'],
            status=fields['status']
        )
        return post_order


class Payment:
    """
    This class represents the Buycoins Payment type
    """

    def __init__(self, node_id: str, amount: str, created_at: str, fee: str, reference: str, status: str,
                 total_amount: str, payment_type: str):
        self.id = node_id
        self.amount = amount
        self.created_at = created_at
        self.fee = fee
        self.reference = reference
        self.status = PaymentStatus(status)
        self.total_amount = total_amount
        self.payment_type = PaymentTypes(payment_type)

    @staticmethod
    def from_dict(fields: dict):
        payment = Payment(
            node_id=fields['id'],
            amount=fields['amount'],
            created_at=fields['createdAt'],
            fee=fields['fee'],
            reference=fields['reference'],
            status=fields['status'],
            total_amount=fields['totalAmount'],
            payment_type=fields['type']
        )
        return payment


class BuycoinsPrice:
    """
    This class represents the Buycoins BuycoinsPrice type
    """

    def __init__(self, node_id: str, buy_price_per_coin: str, cryptocurrency: str, expires_at: str,
                 max_buy: str, max_sell: str, min_buy: str, min_coin_amount: str, min_sell: str,
                 sell_price_per_coin: str, status: str):
        self.id = node_id
        self.buy_price_per_coin = buy_price_per_coin
        self.cryptocurrency = Cryptocurrency(cryptocurrency)
        self.expires_at = expires_at
        self.max_buy = max_buy
        self.max_sell = max_sell
        self.min_buy = min_buy
        self.min_coin_amount = min_coin_amount
        self.min_sell = min_sell
        self.sell_price_per_coin = sell_price_per_coin
        self.status = BuycoinsPriceStatus(status)

    @staticmethod
    def from_dict(fields: dict):

        if isinstance(fields, list) and len(fields) > 1:
            list_of_prices = []
            for i in fields:
                buycoins_price = BuycoinsPrice(
                    node_id=i['id'],
                    buy_price_per_coin=i['buyPricePerCoin'],
                    cryptocurrency=i['cryptocurrency'],
                    expires_at=i['expiresAt'],
                    max_buy=i['maxBuy'],
                    max_sell=i['maxSell'],
                    min_buy=i['minBuy'],
                    min_coin_amount=i['minCoinAmount'],
                    min_sell=i['minSell'],
                    sell_price_per_coin=i['sellPricePerCoin'],
                    status=i['status']
                )
                list_of_prices.append(buycoins_price)
            return list_of_prices

        else:
            fields = fields[0]
            buycoins_price = BuycoinsPrice(
                node_id=fields['id'],
                buy_price_per_coin=fields['buyPricePerCoin'],
                cryptocurrency=fields['cryptocurrency'],
                expires_at=fields['expiresAt'],
                max_buy=fields['maxBuy'],
                max_sell=fields['maxSell'],
                min_buy=fields['minBuy'],
                min_coin_amount=fields['minCoinAmount'],
                min_sell=fields['minSell'],
                sell_price_per_coin=fields['sellPricePerCoin'],
                status=fields['status']
            )
            return buycoins_price


class Address:
    """
    This class represents the Buycoins Address type
    """

    def __init__(self, node_id: str, address: str, created_at: str, cryptocurrency: str):
        self.id = node_id
        self.address = address
        self.created_at = created_at
        self.cryptocurrency = Cryptocurrency(cryptocurrency)

    @staticmethod
    def from_dict(fields: dict):
        address = Address(
            node_id=fields['id'],
            address=fields['address'],
            created_at=fields['createdAt'],
            cryptocurrency=fields['cryptocurrency']
        )
        return address


class DepositAccount:
    """
    This class represents the Buycoins DepositAccount type
    """

    def __init__(self, node_id: str, account_name: str, account_number: str, account_reference: str,
                 account_type: str, bank_name: str):
        self.id = node_id
        self.account_name = account_name
        self.account_number = account_number
        self.account_reference = account_reference
        self.account_type = BankAccountTypes(account_type)
        self.bank_name = bank_name

    @staticmethod
    def from_dict(fields: dict):
        deposit_account = DepositAccount(
            node_id=fields['id'],
            account_name=fields['accountName'],
            account_number=fields['accountNumber'],
            account_reference=fields['accountReference'],
            account_type=fields['accountType'],
            bank_name=fields['bankName']
        )
        return deposit_account


class Order:
    """
    This class represents the Buycoins Order type
    """

    def __init__(self, node_id: str, created_at: str, cryptocurrency: str, filled_coin_amount: str, price: BuycoinsPrice,
                 side: str, status: str, total_coin_amount: str):
        self.id = node_id
        self.created_at = created_at
        self.cryptocurrency = Cryptocurrency(cryptocurrency)
        self.filled_coin_amount = filled_coin_amount
        self.price = price
        self.side = OrderSide(side)
        self.status = OrderStatus(status)
        self.total_coin_amount = total_coin_amount

    @staticmethod
    def from_dict(fields: dict):
        order = Order(
            node_id=fields['id'],
            created_at=fields['createdAt'],
            cryptocurrency=fields['cryptocurrency'],
            filled_coin_amount=fields['filledCoinAmount'],
            price=BuycoinsPrice.from_dict(fields['price']),
            side=fields['side'],
            status=fields['status'],
            total_coin_amount=fields['totalCoinAmount']
        )
        return order


class OnchainTransferRequest:
    """
    This class represents the Buycoins OnchainTransferRequest type
    """

    def __init__(self, node_id: str, address: str, amount: str, created_at: str, cryptocurrency: str, fee: str,
                 status: str, transaction_id: str):
        self.id = node_id
        self.address = address
        self.amount = amount
        self.created_at = created_at
        self.cryptocurrency = Cryptocurrency(cryptocurrency)
        self.fee = fee
        self.status = OnchainTransferRequestStatus(status)
        self.transaction_id = transaction_id

    @staticmethod
    def from_dict(fields: dict):
        onchain_transfer_request = OnchainTransferRequest(
            node_id=fields['id'],
            address=fields['address'],
            amount=fields['amount'],
            cryptocurrency=fields['cryptocurrency'],
            created_at=fields['createdAt'],
            fee=fields['fee'],
            status=fields['status'],
            transaction_id=fields['transaction']['id']
        )
        return onchain_transfer_request


class Transaction:
    """
    This class represents the Buycoins Transaction type
    """

    def __init__(self, node_id: str, address: Address, amount: str, confirmed: bool, created_at: str,
                 cryptocurrency: str, direction: str, onchain_transfer_request_id: str, tx_hash: str):
        self.id = node_id
        self.address = address
        self.amount = amount
        self.confirmed = confirmed
        self.created_at = created_at
        self.cryptocurrency = Cryptocurrency(cryptocurrency)
        self.direction = direction
        self.onchain_transfer_request_id = onchain_transfer_request_id
        self.tx_hash = tx_hash

    @staticmethod
    def from_dict(fields: dict):
        tx = Transaction(
            node_id=fields['id'],
            address=Address.from_dict(fields['address']),
            amount=fields['amount'],
            confirmed=fields['confirmed'],
            created_at=fields['createdAt'],
            cryptocurrency=fields['cryptocurrency'],
            direction=fields['direction'],
            onchain_transfer_request_id=fields['onchainTransferRequest']['id'],
            tx_hash=fields['txhash']
        )
        return tx



bc = BuycoinsGraphqlClient(public_key=os.getenv('BUYCOINS_PUBLIC_KEY'), secret_key=os.getenv('BUYCOINS_SECRET_KEY'))
print(bc.get_prices(Cryptocurrency.BITCOIN)['data'])

