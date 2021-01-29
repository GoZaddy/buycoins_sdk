class InsufficientAmountToSellException(Exception):
    def __init__(self, cryptocurrency: str, amount_to_sell: float):
        self.cryptocurrency = cryptocurrency
        self.amount_to_sell = amount_to_sell
        super().__init__(f"Your balance is insufficient for this sale\nCryptocurrency: {cryptocurrency}, Amount to sell: {amount_to_sell}")




