GraphQL Global object Nodes
=============================
| The Buycoins GraphQL API implements the `GraphQL Global Object Identification Specification <https://relay.dev/graphql/objectidentification.htm>`_ which basically allows GraphQL objects called nodes to be fetched by GraphQL clients via a unique ID.
| Most native Python Buycoins classes available in the Buycoins SDK have an **id** field which points to the ID for that object.

Now that you know what a Global Object ID is, how do you use it to fetch GraphQL object?
In the BuycoinsSDK class, there are two methods available for node fetching - **node** and **nodes**.

.. note:: You can find these methods and the BuycoinsSDK class in :doc:`buycoins_sdk.core`

**node** is used to retrieve a single GraphQL object. To use **node**, you must know the type of the GraphQL object you are planning to retrieve and of course, its Global Object ID or just ID.
Here's an example of how to use this::

    >>> from buycoins_sdk import enums, BuycoinsSDK

    # initialise the Buycoins SDK
    >>> buycoins_sdk = BuycoinsSDK(
        public_key='pubic_key',
        secret_key='secret_key'
    )

    >>> address_node = buycoins_sdk.node(
        gql_type=enums.BuycoinsType.ADDRESS,
        node_id='QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk='
    )

    >>> print(address_node)
    {
        'data': {
            'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk=',
            'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
            'createdAt': 1612759118,
            'cryptocurrency': 'litecoin'
        }
    }

*Voila!*

Also, unlike other methods of the BuycoinsSDK class, the **node** and **nodes** methods return their responses in a dictionary format so it is your job to convert those responses to native Python objects if you want.
We can easily do that::

    >>> from buycoins_sdk import types
    >>> address = types.Address.from_dict(address_node['data'])

    >>> print(address.cryptocurrency)
    Cryptocurrency.LITECOIN

| The **nodes** method, on the other hand is used for fetching more than one node at the same time.

Like the **node** method, it returns the fetched nodes in a dictionary format so you will need to convert them to native Python objects if that's what you want::


    >>> from buycoins_sdk import types
    >>> fetched_nodes = buycoins_sdk.nodes(
        ids=['QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk=', 'QWRkcmVzcy1mM2YzOGQ4OS02OWFjLTQwOWQtOWM5Zi1hMDM4YTM0YTExMTg='],
        gql_types=[enums.BuycoinsType.ADDRESS]  # pass in all the types of all the IDs. No need to repeat types.
    )

    >>> print(fetched_nodes)
    {
        'data': [
            {
                'id': 'QWRkcmVzcy1iOWM1NWZiNy01ODc2LTQ2NjMtOTc0OS0zODIwZjI5MGZlZTk=',
                'address': 'MNjTVmqy5a9mjUShT8XsWgJQFasgHpr1ML',
                'createdAt': 1612759118,
                'cryptocurrency': 'litecoin'
            },
            {
                'id': 'QWRkcmVzcy1mM2YzOGQ4OS02OWFjLTQwOWQtOWM5Zi1hMDM4YTM0YTExMTg=',
                'address': '0x680dd813a5fdcd2f69e9b5edaa4a8dd6b098d759',
                'createdAt': 1612819781,
                'cryptocurrency': 'naira_token'
            }
        ]
    }


