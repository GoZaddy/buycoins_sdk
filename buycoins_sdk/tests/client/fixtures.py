get_market_book_success = {
    'data': {
        'getMarketBook': {
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
    }
}

get_orders_success = {
    'data': {
        'getOrders': {
            'dynamicPriceExpiry': 1612758374,
            'orders': {
                'edges': [],
                'pageInfo': {
                    'endCursor': None,
                    'hasNextPage': False,
                    'hasPreviousPage': False,
                    'startCursor': None
                }
            }
        }
    }
}

get_payments_success = {
    'data': {
        'getPayments': {
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
    }
}

get_prices_success = {
    'data': {
        'getPrices': [
            {
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
        ]
    }
}

node_success = {
    'data': {
        'node': {
            'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
            'createdAt': 1612759118,
            'cryptocurrency': 'litecoin',
            'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
        }
    }
}

nodes_success = {
    'data': {
        'nodes': [{
            'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
            'createdAt': 1612759118,
            'cryptocurrency': 'litecoin',
            'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
        },
            {
                'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
                'createdAt': 1612759118,
                'cryptocurrency': 'litecoin',
                'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
            }
        ]
    }
}

buy_success = {
    'data': {
        'buy': {
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
            'side': 'buy',
            'status': 'done',
            'totalCoinAmount': '123039230'
        }
    }
}

cancel_withdrawal_success = {
    'data': {
        'cancelWithdrawal': {
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
}

create_address_success = {
    'data': {
        'createAddress': {
            'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
            'createdAt': 1612759118,
            'cryptocurrency': 'litecoin',
            'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
        }
    }
}



create_deposit_account_success = {
    'data': {
        'createDepositAccount': {
            'id': 'random id',
            'accountName': 'foo',
            'accountNumber': '123',
            'accountReference': '123',
            'accountType': 'deposit',
            'bankName': 'bar'
        }
    }
}

create_withdrawal_success = {
    'data': {
        'createWithdrawal': {
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
}

post_limit_order_success = {
    'data': {
        'postLimitOrder': {
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
    }
}

post_market_order_success = {
    'data': {
        'postMarketOrder': {
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
    }
}

sell_success = {
    'data': {
        'sell': {
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
    }
}

send_success = {
    'data': {
        'send': {
            'id': 'random id',
            'address': 'random address',
            'amount': '1626378.7829',
            'createdAt': 1673839222,
            'cryptocurrency': 'bitcoin',
            'fee': '13789.27829',
            'status': 'confirmed',
            'transaction': {
                'id': 'random id',
                'address': 'random address',
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
    }
}

send_offchain_success = {
    'data': {
        'sendOffchain': {
            'initiated': True
        }
    }
}
