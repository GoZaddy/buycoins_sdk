from buycoins_sdk.commons.enums import Cryptocurrency, OrderSide, \
    PostOrderStatus, PaymentStatus, PaymentTypes, BuycoinsPriceStatus, BankAccountTypes, OrderStatus, \
    OnchainTransferRequestStatus, EventType


from typing import List

__all__ = [
    'Account',
    'BankAccount',
    'PostOrder',
    'Payment',
    'BuycoinsPrice',
    'Address',
    'DepositAccount',
    'Order',
    'OnchainTransferRequest',
    'Transaction',
    'EstimatedFee',
    'PageInfo',
    'PostOrderEdge',
    'PostOrders',
    'PaymentConnection',
    'PaymentEdge'
]


class Account:
    """This class represents the Buycoins Account type

    Attributes:
        id: a string representing the id of the Account
        cryptocurrency: the cryptocurrency field of the Account type
        confirmed_balance: the confirmed balance field of the Account type
    """

    def __init__(self, node_id: str, cryptocurrency: str, confirmed_balance: str):
        """Create a new Account type

        Args:
            node_id: a string representing the id of the Account
            cryptocurrency: the cryptocurrency field of the Account type
            confirmed_balance: the confirmed balance field of the Account type
        """
        self.id = node_id
        self.cryptocurrency = Cryptocurrency(cryptocurrency)
        self.confirmed_balance = confirmed_balance

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create an Account object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            An Account object
        """
        account = Account(node_id=fields['id'], cryptocurrency=fields['cryptocurrency'],
                          confirmed_balance=fields['confirmedBalance'])
        return account


class BankAccount:
    """This class represents the Buycoins BankAccount type

    Attributes:
        id: the id of the BankAccount
        account_name: the Account name field of the BankAccount type
        account_number: the account number field of the BankAccount type
        account_reference: the account reference field of the BankAccount type
        account_type: the account type field of the BankAccount type
        bank_name: the bank name field of the BankAccount type
    """

    def __init__(self, node_id: str, account_name: str, account_number: str, account_reference: str,
                 account_type: str, bank_name: str):
        """Create a BankAccount type

        Args:
            node_id: the id of the BankAccount
            account_name: the Account name field of the BankAccount type
            account_number: the account number field of the BankAccount type
            account_reference: the account reference field of the BankAccount type
            account_type: the account type field of the BankAccount type
            bank_name: the bank name field of the BankAccount type
        """
        self.id = node_id
        self.account_name = account_name
        self.account_number = account_number
        self.account_reference = account_reference
        self.account_type = BankAccountTypes(account_type)
        self.bank_name = bank_name

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create a BankAccount object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            A BankAccount object
        """
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
    """This class represents the Buycoins PostOrder type
    Attributes:
        id: the id field of the PostOrder type
        coin_amount: the coin amount field of the PostOrder type
        created_at: the createdAt field of the PostOrder type
        cryptocurrency: the cryptocurrency field of the PostOrder type
        dynamic_exchange_rate: the dynamic exchange rate field of the PostOrder type
        price_per_coin: the price per coin field of the PostOrder type
        price_type: the price type field of the PostOrder type
        side: the side field of the PostOrder type
        static_price: the static price field of the PostOrder type
        status: the status field of the PostOrder type
    """

    def __init__(self, node_id: str, coin_amount: str, created_at: int, cryptocurrency: str,
                 dynamic_exchange_rate: str, price_per_coin: str, price_type: str, side: str,
                 static_price: str, status: str):
        """
        This initialises a PostOrder object
        Args:
            node_id: the id field of the PostOrder type
            coin_amount: the coin amount field of the PostOrder type
            created_at: the createdAt field of the PostOrder type
            cryptocurrency: the cryptocurrency field of the PostOrder type
            dynamic_exchange_rate: the dynamic exchange rate field of the PostOrder type
            price_per_coin: the price per coin field of the PostOrder type
            price_type: the price type field of the PostOrder type
            side: the side field of the PostOrder type
            static_price: the static price field of the PostOrder type
            status: the status field of the PostOrder type
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
        """This allows you to create a PostOrder object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods. Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            A PostOrder object
        """
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
    """This class represents the Buycoins Payment type

    Attributes:
        id: the id field of the Payment type
        amount: the amount field of the Payment type
        created_at: the createdAt field of the Payment type
        fee: the fee field of the Payment type
        reference: the reference field of the Payment type
        status: the status field of the Payment type
        total_amount: the total_amount field of the Payment type
        payment_type: the payment_type field of the Payment type
    """

    def __init__(self, node_id: str, amount: str, created_at: int, fee: str, reference: str, status: str,
                 total_amount: str, payment_type: str):
        """Create a new Payment object

        Args:
            node_id: the id field of the Payment type
            amount: the amount field of the Payment type
            created_at: the createdAt field of the Payment type
            fee: the fee field of the Payment type
            reference: the reference field of the Payment type
            status: the status field of the Payment type
            total_amount: the total_amount field of the Payment type
            payment_type: the payment_type field of the Payment type
        """
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
        """This allows you to create a Payment object using the fields in the data attribute of the dicts returned
           from BuycoinsGraphqlClient's methods. Study the methods of BuycoinsSDK to know how this is used

       Args:
           fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
       Returns:
           A Payment object
       """
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
    """This class represents the Buycoins BuycoinsPrice type

    Attributes:
        id: the id field of the BuycoinsPrice type
        buy_price_per_coin: the buyPricePerCoin field of the BuycoinsPrice type
        cryptocurrency: the cryptocurrency field of the BuycoinsPrice type
        expires_at: the expiresAt field of the BuycoinsPrice type
        max_buy: the maxBuy field of the BuycoinsPrice type
        max_sell: the maxSel field of the BuycoinsPrice type
        min_buy: the minBuy field of the BuycoinsPrice type
        min_coin_amount: the minCoinAmount field of the BuycoinsPrice type
        min_sell: the minSell field of the BuycoinsPrice type
        sell_price_per_coin: the sellPricePerCoin field of the BuycoinsPrice type
        status: the status field of the BuycoinsPrice type
    """

    def __init__(self, node_id: str, buy_price_per_coin: str, cryptocurrency: str, expires_at: int,
                 max_buy: str, max_sell: str, min_buy: str, min_coin_amount: str, min_sell: str,
                 sell_price_per_coin: str, status: str):
        """Create a new BuycoinsPrice object

        Args:
            node_id: the id field of the BuycoinsPrice type
            buy_price_per_coin: the buyPricePerCoin field of the BuycoinsPrice type
            cryptocurrency: the cryptocurrency field of the BuycoinsPrice type
            expires_at: the expiresAt field of the BuycoinsPrice type
            max_buy: the maxBuy field of the BuycoinsPrice type
            max_sell: the maxSel field of the BuycoinsPrice type
            min_buy: the minBuy field of the BuycoinsPrice type
            min_coin_amount: the minCoinAmount field of the BuycoinsPrice type
            min_sell: the minSell field of the BuycoinsPrice type
            sell_price_per_coin: the sellPricePerCoin field of the BuycoinsPrice type
            status: the status field of the BuycoinsPrice type
        """
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
        """This allows you to create a BuycoinsPrice object using the fields in the data attribute of the dicts returned
           from BuycoinsGraphqlClient's methods. Study the methods of BuycoinsSDK to know how this is used

       Args:
           fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
       Returns:
           A BuycoinsPrice object
       """
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
    """This class represents the Buycoins Address type

    Attributes:
        id: the id field of the Address object
        address: the address field of the Address object
        created_at: the createdAt field of the Address object
        cryptocurrency: the cryptocurrency field of the Address object
    """

    def __init__(self, node_id: str, address: str, created_at: int, cryptocurrency: str):
        """Create a new Address object

        Args:
            node_id: the id field of the Address object
            address: the address field of the Address object
            created_at: the createdAt field of the Address object
            cryptocurrency: the cryptocurrency field of the Address object
        """
        self.id = node_id
        self.address = address
        self.created_at = created_at
        self.cryptocurrency = Cryptocurrency(cryptocurrency)

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create an Address object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            An Address object
        """
        address = Address(
            node_id=fields['id'],
            address=fields['address'],
            created_at=fields['createdAt'],
            cryptocurrency=fields['cryptocurrency']
        )
        return address


class DepositAccount:
    """This class represents the Buycoins DepositAccount type

    Attributes:
        id: the id field of the DepositAccount object
        account_name: the accountName field of the DepositAccount object
        account_number: the accountNumber field of the DepositAccount object
        account_reference: the accountReference field of the DepositAccount object
        account_type: the accountType field of the DepositAccount object
        bank_name: the bankName field of the DepositAccount object
    """

    def __init__(self, node_id: str, account_name: str, account_number: str, account_reference: str,
                 account_type: str, bank_name: str):
        """Create a new DepositAccount object

        Args:
            node_id: the id field of the DepositAccount object
            account_name: the accountName field of the DepositAccount object
            account_number: the accountNumber field of the DepositAccount object
            account_reference: the accountReference field of the DepositAccount object
            account_type: the accountType field of the DepositAccount object
            bank_name: the bankName field of the DepositAccount object
        """
        self.id = node_id
        self.account_name = account_name
        self.account_number = account_number
        self.account_reference = account_reference
        self.account_type = BankAccountTypes(account_type)
        self.bank_name = bank_name

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create a DepositAccount object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            A DepositAccount object
        """
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
    """This class represents the Buycoins Order type

    Attributes:
        id: the id field of the Order object
        created_at: the createdAt field of the Order object
        cryptocurrency: the cryptocurrency field of the Order object
        filled_coin_amount: the filledCoinAmount field of the Order object
        price: the price field of the Order object
        side: the side field of the Order object
        status: the status field of the Order object
        total_coin_amount: the totalCoinAmount field of the Order object
    """

    def __init__(self, node_id: str, created_at: int, cryptocurrency: str, filled_coin_amount: str,
                 price: BuycoinsPrice,
                 side: str, status: str, total_coin_amount: str):
        """

        Args:
            node_id: the id field of the Order object
            created_at: the createdAt field of the Order object
            cryptocurrency: the cryptocurrency field of the Order object
            filled_coin_amount: the filledCoinAmount field of the Order object
            price: the price field of the Order object
            side: the side field of the Order object
            status: the status field of the Order object
            total_coin_amount: the totalCoinAmount field of the Order object
        """
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
        """This allows you to create an Order object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            An Order object
        """
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
    """This class represents the Buycoins OnchainTransferRequest type

    Attributes:
        id: the id field of the OnchainTransferRequest type
        address: the address field of the OnchainTransferRequest type
        amount: the amount field of the OnchainTransferRequest type
        created_at: the createdAt field of the OnchainTransferRequest type
        cryptocurrency: the cryptocurrency field of the OnchainTransferRequest type
        fee: the fee field of the OnchainTransferRequest type
        status: the status field of the OnchainTransferRequest type
        transaction_id: the id of the transaction of the OnchainTransferRequest type
    """

    def __init__(self, node_id: str, address: str, amount: str, created_at: int, cryptocurrency: str, fee: str,
                 status: str, transaction_id: str):
        """Create a new OnchainTransferRequest type

        Args:
            node_id: the id field of the OnchainTransferRequest type
            address: the address field of the OnchainTransferRequest type
            amount: the amount field of the OnchainTransferRequest type
            created_at: the createdAt field of the OnchainTransferRequest type
            cryptocurrency: the cryptocurrency field of the OnchainTransferRequest type
            fee: the fee field of the OnchainTransferRequest type
            status: the status field of the OnchainTransferRequest type
            transaction_id: the id of the transaction of the OnchainTransferRequest type
        """
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
        """This allows you to create an OnchainTransferRequest object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            An OnchainTransferRequest object
        """
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
    """This class represents the Buycoins Transaction type

    Attributes:
        node_id: the id field of the Transaction type
        address: the address field of the Transaction type
        amount: the amount field of the Transaction type
        confirmed: the confirmed field of the Transaction type
        created_at: the createdAt field of the Transaction type
        cryptocurrency: the cryptocurrency field of the Transaction type
        direction: the direction field of the Transaction type
        onchain_transfer_request_id: the id field of the onchainTransferRequest field of the Transaction type
        tx_hash: the txHash field of the Transaction type
    """

    def __init__(self, node_id: str, address: Address, amount: str, confirmed: bool, created_at: int,
                 cryptocurrency: str, direction: str, onchain_transfer_request_id: str, tx_hash: str):
        """Create a new Transaction object

        Args:
            node_id: the id field of the Transaction type
            address: the address field of the Transaction type
            amount: the amount field of the Transaction type
            confirmed: the confirmed field of the Transaction type
            created_at: the createdAt field of the Transaction type
            cryptocurrency: the cryptocurrency field of the Transaction type
            direction: the direction field of the Transaction type
            onchain_transfer_request_id: the id field of the onchainTransferRequest field of the Transaction type
            tx_hash: the txHash field of the Transaction type
        """
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
        """This allows you to create a Transaction object using the fields in the data attribute of the dicts returned
            from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

        Args:
            fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
        Returns:
            A Transaction object
        """
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


class EstimatedFee:
    """This class represents the Buycoins EstimatedFee type

    Attributes:
        estimated_fee: Estimated network fee for send
        total: Sum of amount and estimated network fee
    """

    def __init__(self, estimated_fee: str, total: str):
        """Initialise a new EstimatedFee object

        Args:
            estimated_fee: a string representing estimated fee
            total: a string representing sum of estimated fee and amount of coins to be sent
        """
        self.estimated_fee = estimated_fee
        self.total = total

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create an EstimatedFee object using the fields in the data attribute of the dicts returned
           from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

       Args:
           fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
       Returns:
           An EstimatedFee object
       """
        es_fee = EstimatedFee(
            estimated_fee=fields['estimatedFee'],
            total=fields['total']
        )
        return es_fee


class PageInfo:
    """This class represents the Buycoins PageInfo type

    Attributes:
        end_cursor: a string representing the last cursor of the PageInfo
        has_next_page: boolean stating whether or not a next page exists
        has_previous_page: boolean stating whether or not a previous page exists
        start_cursor: start cursor of PageInfo object
    """

    def __init__(self, end_cursor: str, has_next_page: bool, has_previous_page: bool, start_cursor: str):
        """Initialise a new PageInfo object

        Args:
            end_cursor: end cursor of PageInfo object
            has_next_page: boolean stating whether or not a next page exists
            has_previous_page: boolean stating whether or not a previous page exists
            start_cursor: start cursor of PageInfo object
        """
        self.end_cursor = end_cursor
        self.has_next_page = has_next_page
        self.has_previous_page = has_previous_page
        self.start_cursor = start_cursor

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create a PageInfo object using the fields in the data attribute of the dicts returned
           from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

       Args:
           fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
       Returns:
           A PageInfo object
       """
        return PageInfo(
            end_cursor=fields['endCursor'],
            start_cursor=fields['startCursor'],
            has_next_page=fields['hasNextPage'],
            has_previous_page=fields['hasPreviousPage']
        )


class PostOrderEdge:
    """This class represents the Buycoins PostOrderEdge type

   Attributes:
        cursor: a string representing the cursor for the PostOrderEdge object
        post_order: a PostOrder object representing the PostOrder node
    """

    def __init__(self, cursor: str, post_order: PostOrder):
        """Initialise new PostOrderEdge object

        Args:
            cursor: cursor for the PostOrderEdge object
            post_order: a PostOrder object representing the PostOrder node
        """
        self.cursor = cursor
        self.post_order = post_order


class PostOrders:
    """This class represents the Buycoins PostOrders type

    Attributes:
        dynamic_price_expiry:
        page_info: a PageInfo object containing pagination details about the post_order_edges attribute
        post_order_edges: a list of PostOrderEdge objects
    """

    def __init__(self, dynamic_price_expiry: str, page_info: PageInfo, post_order_edges: List[PostOrderEdge]):
        self.dynamic_price_expiry = dynamic_price_expiry
        self.page_info = page_info
        self.post_order_edges = post_order_edges

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create a PostOrders object using the fields in the data attribute of the dicts returned
           from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

       Args:
           fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
       Returns:
           A PostOrders object
       """
        po_edges = []
        post_order_edges_dict = fields['orders']['edges']
        for i in post_order_edges_dict:
            post_order = PostOrder.from_dict(i['node'])
            po_edges.append(PostOrderEdge(cursor=i['cursor'], post_order=post_order))
        return PostOrders(
            dynamic_price_expiry=fields['dynamicPriceExpiry'],
            page_info=PageInfo.from_dict(fields['orders']['pageInfo']),
            post_order_edges=po_edges
        )


class PaymentEdge:
    """This class represents the Buycoins PaymentEdge type

       Attributes:
            cursor: a string representing the cursor for the PaymentEdge object
            payment: a Payment object representing the Payment node
        """

    def __init__(self, cursor: str, payment: Payment):
        """Initialise new PaymentEdge object

        Args:
            cursor: a string representing the cursor for the PaymentEdge object
            payment: a Payment object representing the Payment node
        """
        self.cursor = cursor
        self.payment = payment


class PaymentConnection:
    """This class represents the connection type for Buycoins Payment type.

    Attributes:
        payment_edges: a list of PaymentEdge objects
        page_info: a PageInfo object containing pagination details about the payment_edges attribute
    """

    def __init__(self, payment_edges: List[PaymentEdge], page_info: PageInfo):
        """Initialise a new PaymentConnection object

        Args:
            payment_edges: a list of PaymentEdge objects
            page_info: a PageInfo object containing pagination details about the payment_edges attribute
        """
        self.payment_edges = payment_edges
        self.page_info = page_info

    @staticmethod
    def from_dict(fields: dict):
        """This allows you to create a PaymentConnection object using the fields in the data attribute of the dicts returned
           from BuycoinsGraphqlClient's methods.Study the methods of BuycoinsSDK to know how this is used

       Args:
           fields: the fields of the data property of a dict returned from a BuycoinsGraphqlClient method
       Returns:
           A PaymentConnection object
       """
        p_edges = []
        payment_edges_dict = fields['edges']
        for i in payment_edges_dict:
            payment = Payment.from_dict(i['node'])
            p_edges.append(PaymentEdge(cursor=i['cursor'], payment=payment))
        return PaymentConnection(
            page_info=PageInfo.from_dict(fields['pageInfo']),
            payment_edges=p_edges
        )


class Event:
    """Event represents the request body of a webhook request sent from Buycoins

    Attributes:
        hook_id: hook id of webhook event
        hook_key: hook key of webhook event
        hook_time: hook time of webhook event
        hook_signature: hook signature of webhook event
        event_type: type of event
        data: data in payload
    """

    def __init__(self, hook_id: int, hook_key: str, hook_time: int, hook_signature: str, event_type: EventType, data: dict):
        """Create a new Event

        Args:
            hook_id: hook id of webhook event
            hook_key: hook key of webhook event
            hook_time: hook time of webhook event
            hook_signature: hook signature of webhook event
            event_type: type of event
            data: data in payload
        """

        self.hook_id = hook_id
        self.hook_key = hook_key
        self.hook_time = hook_time
        self.hook_signature = hook_signature
        self.event_type = event_type
        self.data = data

    @staticmethod
    def from_request_body(request_body: dict):
        """This allows you to create an Event object using the request body of a request from Buycoins

       Args:
           request_body: the request body from buycoins
       Returns:
           An Event object
       """
        event = Event(
            hook_id=request_body['hook_id'],
            hook_key=request_body['hook_key'],
            hook_time=request_body['hook_time'],
            hook_signature=request_body['hook_signature'],
            event_type=EventType(request_body['payload']['event']),
            data=request_body['payload']['data']
        )
        return event


if __name__ == '__main__':
    pass