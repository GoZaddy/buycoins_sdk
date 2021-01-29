class BuycoinsSDK:
    """BuycoinsSDK is the entry point of the Buycoins SDK

    more stuff here.

    """
    def __init__(self, public_key: str, secret_key: str):
        self._public_key = public_key
        self._secret_key = secret_key

    def get_balances(self, cryptocurrency: str):
        pass