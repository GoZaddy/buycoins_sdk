Quickstart
===========


* :ref:`installation`
* :ref:`using_buycoins_sdk`
    * :ref:`pre_req`
    * :ref:`steps`


.. _installation:

Installation
-------------
Install the Buycoins SDK using pip::

    $ pip install buycoins_sdk

.. _using_buycoins_sdk:

Using the Buycoins SDK
-----------------------
.. _pre_req:

Prerequisites
^^^^^^^^^^^^^^
You must have access to the Buycoins API and must have generated a pair of public and private keys after gaining access.
To apply for API access, please send an email to support@buycoins.africa from your email account registered on BuyCoins.

.. _steps:

Steps
^^^^^^

* Initialise a BuycoinsSDK object
    To initialise a BuycoinsSDK object, use the BuycoinsSDK class and pass your public and secret keys as arguments.
    It is not advisable to pass in your public and private keys directly due to security reasons. A better option would be to use
    environment variables ::

        >>> from buycoins_sdk import BuycoinsSDK
        >>> buycoins_sdk = BuycoinsSDK(
            public_key=os.getenv('BUYCOINS_PUBLIC_KEY'),
            secret_key=os.getenv('BUYCOINS_SECRET_KEY')
        )

* Get to work!
    You can now make use of the BuycoinsSDK object to access all of the Buycoins API's functionality. Here's an example showing how to get current prices of cryptocurrencies::

        >>> from buycoins_sdk import enums
        >>> prices = buycoins_sdk.get_prices(enums.Cryptocurrency.BITCOIN)

        >>> print(prices.cryptocurrency)
        Cryptocurrency.BITCOIN

        >>> print(prices.status)
        BuycoinsPriceStatus.ACTIVE

        >>> print(prices.sell_price_per_coin)
        17233901.685

        >>> print(prices.buy_price_per_coin)
        17582107.27




