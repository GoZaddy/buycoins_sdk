Types and Enums
=================
An amazing feature of this Buycoins Python SDK is that it comes with many native Python classes and enums that represent the GraphQL types and enums of the Buycoins GraphQL API.
For example, in the Buycoins GraphQL API, there is an Address type which is used to represents cryptocurrency addresses.
Here's what the Address type looks like::

    Address
        id: ID!
        address: String!
        cryptocurrency: Cryptocurrency!
        createdAt: Int!

If you make a query that returns an address type to the Buycoins GraphQL API, you will get a response similar to what we have below::

    >>> response = {
        'data': {
            'someQuery': {
                'id': 'Some ID',
                'address': 'some address',
                'cryptocurrency': 'bitcoin',
                'createdAt': 1689289228
            }
        }
    }

With this response, you can easily use one of the convenience methods available in Buycoins SDK to get a native Python Address object::

    >>> from buycoins_sdk import types
    >>> address = types.Address.from_dict(response['data']['someQuery']) # Now we have our very own address object!

    >>> print(address.address)
        some address

    >>> print(address.cryptocurrency)
        Cryptocurrency.BITCOIN

.. note:: Buycoins SDK also automatically returns GraphQL types as native Python objects so you do not have to use any of the convenience methods directly except you are writing your own queries.

As you may have noticed already, the cryptocurrency of the Address object we created was printed out as `Cryptocurrency.BITCOIN`.
This is an example of one of the enums available in the Buycoins SDK. To use these enums, simply import enums from buycoins_sdk like so::

    >>> from buycoins_sdk import enums
    >>> btc = enums.Cryptocurrency('bitcoin')
    # or
    >>> btc = enums.Cryptocurrency.BITCOIN

    # you can also get the value of an existing enum
    >>> print(btc.value)
    bitcoin

