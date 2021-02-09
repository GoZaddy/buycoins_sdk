Overview
==========
The purpose of this page is to give you a quick rundown of some of the contents of the Buycoins SDK package and some of the things you can do with it.

Subpackages
------------
The Buycoins SDK has three subpackages: client, core and commons

    * :doc:`client <buycoins_sdk.client>` - this package contains BuycoinsGraphqlClient and some other private helper functions.
    * :doc:`commons <buycoins_sdk.commons>` - this package contains the exceptions and enums that are used throughout the Buycoins SDK
    * :doc:`core <buycoins_sdk.core>` - this package contains the native Python representations for the Buycoins GraphQL API types, and the BuycoinsSDK class


BuycoinsSDK and BuycoinsGraphqlClient
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
BuycoinsSDK is the entry point of the Buycoins SDK. It gives you full access to all the functionality of the Buycoins public API.
BuycoinsGraphqlClient, on the other hand, is a class that wraps a standard GraphQL client and makes the queries and mutations to the Buycoins API on behalf of the BuycoinsSDK.
You can use the BuycoinsGraphqlClient on its own, although there's almost no reason for you to.

.. note:: BuycoinsSDK's methods mostly return responses as native Python objects while those of the BuycoinsClient return responses as dictionaries in the form of `{'data': graphql_response}`.

Here's how to use BuycoinsSDK and BuycoinsGraphqlClient::

    >>> from buycoins_sdk import BuycoinsSDK, BuycoinsGraphqlClient

    >>> bc_sdk = BuycoinsSDK(
            public_key=os.getenv('BUYCOINS_PUBLIC_KEY'),
            secret_key=os.getenv('BUYCOINS_SECRET_KEY')
        )

    >>> fetched_nodes = bc_sdk.nodes(
            ids=['QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk=', 'QWRkcmVzcy1mM2YzOGQ4OS02OWFjLTQwOWQtOWM5Zi1hMDM4YTM0YTExMTg='],
            gql_types=[enums.BuycoinsType.ADDRESS]
        )

    >>> bc_client = BuycoinsGraphqlClient(
            public_key=os.getenv('BUYCOINS_PUBLIC_KEY'),
            secret_key=os.getenv('BUYCOINS_SECRET_KEY')
        )

    >>> prices = bc_client.get_prices(enums.Cryptocurrency.BITCOIN)

Exceptions
^^^^^^^^^^^^
To use exceptions from the Buycoins SDK, simply import them like so::

    >>> from buycoins_sdk import errors

    >>> try:
            # buycoins related code
        except errors.BuycoinsException:
            # handle error

Native Buycoins Classes
^^^^^^^^^^^^^^^^^^^^^^^^
To use the native Buycoins related classes, import them like so::

    >>> from buycoins_sdk import types

    >>> address = types.Address(...)

Enums
^^^^^^^^
To use the enums available in the Buycoins SDK, import them like so::

    >>> from buycoins_sdk import enums

    >>> btc = enums.Cryptocurrency.BITCOIN



Indices and tables
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`