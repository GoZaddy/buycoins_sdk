"""This module contains a single dictionary  which maps GraphQL types from the BuyCoins API to a multi-line string
containing the fields of that type """

from .enums import *


type_to_field = {
    BuycoinsType.ACCOUNT: """
        id
        cryptocurrency
        confirmedBalance
    """,

    BuycoinsType.BANK_ACCOUNT: """
        id
        accountName
        accountNumber
        accountReference
        accountType
        bankName
    """,

    BuycoinsType.POST_ORDER: """
        id
        coinAmount
        createdAt
        cryptocurrency
        dynamicExchangeRate
        pricePerCoin
        priceType
        side
        staticPrice
        status
    """,

    BuycoinsType.PAYMENT: """
        id
        amount
        createdAt
        fee
        reference
        status
        totalAmount
        type
    """,

    BuycoinsType.BUYCOINS_PRICE: """
        id
        buyPricePerCoin
        cryptocurrency
        expiresAt
        maxBuy
        maxSell
        minBuy
        minCoinAmount
        minSell
        sellPricePerCoin
        status
    """,

    BuycoinsType.ADDRESS: """
        id
        address
        createdAt
        cryptocurrency
    """,

    BuycoinsType.DEPOSIT_ACCOUNT: """
        id
        accountName
        accountNumber
        accountReference
        accountType
        bankName
    """,

    BuycoinsType.ORDER: """
        id
        createdAt
        cryptocurrency
        filledCoinAmount
        price {
            id
            buyPricePerCoin
            cryptocurrency
            expiresAt
            maxBuy
            maxSell
            minBuy
            minCoinAmount
            minSell
            sellPricePerCoin
            status
        }
        side
        status
        totalCoinAmount
    """,

    BuycoinsType.ONCHAIN_TRANSFER_REQUEST: """
        id
        address 
        amount
        createdAt
        cryptocurrency
        fee
        status
        transaction{
            id
            address {  
                id
                address
                createdAt
                cryptocurrency     
            }
            amount
            confirmed
            createdAt
            cryptocurrency
            direction
            onchainTransferRequest{
                id
            }
            txhash
        }
    """,

    BuycoinsType.TRANSACTION: """
        id
        address {
            id
            address
            createdAt
            cryptocurrency
        }
        amount
        confirmed
        createdAt
        cryptocurrency
        direction
        onchainTransferRequest{
            id
            address
            amount
            createdAt
            cryptocurrency
            fee
            status
            transaction{
                id
            }
        }
        txhash
    """,

}
