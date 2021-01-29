class BuycoinsException(Exception):
    def __init__(self, error_message:str):
        super().__init__(error_message)


class InsufficientAmountToSellException(BuycoinsException):
    def __init__(self, cryptocurrency: str, amount_to_sell: float):
        self.cryptocurrency = cryptocurrency
        self.amount_to_sell = amount_to_sell
        super().__init__(f"Your balance is insufficient for this sale\nCryptocurrency: {cryptocurrency}, Amount to "
                         f"sell: {amount_to_sell}")


