account_fixture = {
    'confirmedBalance': '0.0',
    'cryptocurrency': 'bitcoin',
    'id': 'QWNjb3VudC0='
}


bank_account_fixture = {
    'accountName': 'Some random name',
    'accountNumber': '2119851388',
    'accountReference': None,
    'accountType': 'withdrawal',
    'bankName': 'GTB',
    'id': 'some_random_node_id'
}

post_order_fixture = {
    'id': 'random id',
    'coinAmount': '137392302.892',
    'createdAt': 1612759118,
    'cryptocurrency': 'bitcoin',
    'dynamicExchangeRate': '1673822.8292',
    'pricePerCoin': '237920.73839',
    'priceType': 'static',
    'side': 'buy',
    'staticPrice': '378320.2893',
    'status': 'active'
}

payment_fixture = {
    'amount': '2859.0',
    'createdAt': 1611182392,
    'fee': '0.0',
    'id': 'random_id',
    'reference': 'random_ref',
    'status': 'success',
    'totalAmount': '2859.0',
    'type': 'withdrawal'
}

buycoins_price_fixture = {
    'buyPricePerCoin': '17779805.68',
    'cryptocurrency': 'bitcoin',
    'expiresAt': 1612759034,
    'id': 'QnV5Y29pbnNQcmljZS03NWY3ZGIwMy1hNDk1LTQ0NjAtOGJjYi01ZGMwMTYzYjU5MDg=',
    'maxBuy': '0.00768501',
    'maxSell': '4.98935757',
    'minBuy': '0.001',
    'minCoinAmount': '0.001',
    'minSell': '0.001',
    'sellPricePerCoin': '17427685.275',
    'status': 'active'
}

address_fixture = {
    'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
    'createdAt': 1612759118,
    'cryptocurrency': 'litecoin',
    'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
}

deposit_account_fixture = {
    'id': 'random id',
    'accountName': 'foo',
    'accountNumber': '123',
    'accountReference': '123',
    'accountType': 'deposit',
    'bankName': 'bar'
}

order_fixture = {
    'createdAt': 1612759118,
    'cryptocurrency': 'bitcoin',
    'filledCoinAmount': '1202020302',
    'id': 'some random id',
    'price': {
        'buyPricePerCoin': '17779805.68',
        'cryptocurrency': 'bitcoin',
        'expiresAt': 1612759034,
        'id': 'QnV5Y29pbnNQcmljZS03NWY3ZGIwMy1hNDk1LTQ0NjAtOGJjYi01ZGMwMTYzYjU5MDg=',
        'maxBuy': '0.00768501',
        'maxSell': '4.98935757',
        'minBuy': '0.001',
        'minCoinAmount': '0.001',
        'minSell': '0.001',
        'sellPricePerCoin': '17427685.275',
        'status': 'active'
    },
    'side': 'sell',
    'status': 'done',
    'totalCoinAmount': '123039230'
}

onchain_transfer_request_fixture = {
    'id': 'random id',
    'address': 'random address',
    'amount': '1626378.7829',
    'createdAt': 1673839222,
    'cryptocurrency': 'bitcoin',
    'fee': '13789.27829',
    'status': 'confirmed',
    'transaction': {
        'id': 'random id',
        'address': {
            'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
            'createdAt': 1612759118,
            'cryptocurrency': 'litecoin',
            'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
        },
        'amount': '1638920.82902',
        'confirmed': True,
        'createdAt': 1673839222,
        'cryptocurrency': 'bitcoin',
        'direction': 'incoming',
        'onchainTransferRequest': {
            'id': 'random id'
        },
        'txhash': 'tx hash '
    }
}

transaction_fixture = {
    'id': 'random id',
    'address': {
        'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
        'createdAt': 1612759118,
        'cryptocurrency': 'litecoin',
        'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
    },
    'amount': '1638920.82902',
    'confirmed': True,
    'createdAt': 1673839222,
    'cryptocurrency': 'bitcoin',
    'direction': 'incoming',
    'onchainTransferRequest': {
        'id': 'random id'
    },
    'txhash': 'tx hash '
}

estimated_fee_fixture = {'estimatedFee': '0.00038', 'total': '100.00038'}

page_info_fixture = {
    'endCursor': 'Mg',
    'hasNextPage': True,
    'hasPreviousPage': True,
    'startCursor': 'MQ'
}

post_orders_fixture = {
    'dynamicPriceExpiry': 1612756694,
    'orders': {
        'edges': [
            {
                'cursor': 'MQ',
                'node': {
                    'coinAmount': '0.00963874',
                    'createdAt': 1612716031,
                    'cryptocurrency': 'bitcoin',
                    'dynamicExchangeRate': None,
                    'id': 'UG9zdE9yZGVyLThjMzRjZThiLTNlM2MtNDI4My04Yzg4LWVhYzE4MGRkNjQ4Mw==',
                    'pricePerCoin': '17990000.0',
                    'priceType': 'static',
                    'side': 'sell',
                    'staticPrice': '1799000000',
                    'status': 'active'
                }
            },
        ],
        'pageInfo': {
            'endCursor': 'Mg',
            'hasNextPage': True,
            'hasPreviousPage': True,
            'startCursor': 'MQ'
        }
    }
}

payment_connection_fixture = {
    'edges': [
        {
            'cursor': 'MQ',
            'node': {
                'amount': '2859.0',
                'createdAt': 1611182392,
                'fee': '0.0',
                'id': 'random_id',
                'reference': 'random_ref',
                'status': 'success',
                'totalAmount': '2859.0',
                'type': 'withdrawal'
            }
        }
    ],
    'pageInfo': {
        'endCursor': 'MQ',
        'hasNextPage': True,
        'hasPreviousPage': False,
        'startCursor': 'MQ'
    }
}

event_fixture = {
    "hook_id": 36,
    "hook_key": "6a622fda-f696-4f5c-9eab-d09f59f17366",
    "hook_time": 1579626696,
    "hook_signature": "X-Webhook-Signature",
    "payload": {
        "event": "coins.incoming",
        "data": {
            "transactionId": "VHlwZXM6OlB1YmxpY0FwaTo6QWRkcmVzcy1mOGRmNGZlYy1iZTJmLTQ1YjktOWJjMy04YjMwMGNhZTg5Y2I=",
            "cryptocurrency": "naira_token",
            "transactionHash": "00c49d94c2c7ed92d7f166a4499a27e1bc2c3b9b",
            "amount": 25985,
            "type": "onchain",
            "confirmed": False,
            "address": "1f6d648ccdfc13e55050e24727421d5dca2eed95"
        }
    }
}
