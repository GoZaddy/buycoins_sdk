Writing your own GraphQL queries
===================================
| Although the Buycoins SDK provides most, if not all, of the functionality that you will need in your apps, there are sometimes where you might want to write your own GraphQL queries

| Here's a simple guide on how to do that!

Steps
-------
    * Create a *BuycoinsGraphqlClient* object with your Buycoins API keys ::

        >>> from buycoins_sdk import BuycoinsGraphqlClient

        >>> bc_client = BuycoinsGraphqlClient(
            public_key=os.getenv('BUYCOINS_PUBLIC_KEY'),
            secret_key=os.getenv('BUYCOINS_SECRET_KEY')
        )

    * Use the *client* attribute of your *BuycoinsGraphqlClient* instance to write your queries manually.
      The Buycoins SDK makes use of `python_graphql_client <https://pypi.org/project/python-graphql-client/>`_ to query the Buycoins API so you might want to check out the documentation for that ::

        >>> query = """
                query getEstimatedNetworkFee($cryptocurrency: Cryptocurrency, $amount: BigDecimal!){
                    getEstimatedNetworkFee(cryptocurrency: $cryptocurrency, amount: $amount){
                        estimatedFee
                        total
                    }
                }
            """
        >>> variables = {'cryptocurrency': enums.Cryptocurrency.BITCOIN.value, 'amount': '100'}
        >>> res = bc_client.client.execute(query=query, variables=variables)
