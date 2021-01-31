"""This module contains a single dictionary which maps GraphQL types from the BuyCoins API to a multi-line string
containing the fields of that type """

type_to_field = {
    "Account": """
        id
        cryptocurrency
        confirmedBalance
    """,

    "BankAccount": """
        id
        accountName
        accountNumber
        accountReference
        accountType
        bankName
    """,

    "PostOrder": """
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

    "Payment": """
        id
        amount
        createdAt
        fee
        reference
        status
        totalAmount
        type
    """,

    "BuycoinsPrice": """
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

    "Address": """
        id
        address
        createdAt
        cryptocurrency
    """,

    "DepositAccount": """
        id
        accountName
        accountNumber
        accountReference
        accountType
        bankName
    """,

    "Order": """
        id
        createdAt
        cryptocurrency
        filledCoinAmount
        price
        side
        status
        totalCoinAmount
    """,

    "OnchainTransferRequest": """
        id
        address
        amount
        createdAt
        cryptocurrency
        fee
        status
        transaction
    """,

    "Transaction": """
        id
        address
        amount
        confirmed
        createdAt
        cryptocurrency
        direction
        onchainTransferRequest
        txhash
    """,

}
