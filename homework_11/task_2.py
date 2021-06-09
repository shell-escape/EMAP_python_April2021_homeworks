"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


from typing import Callable


class Order:
    """A class that stores the price and calculates the final price
    after the discount program is applied.

    Args:
        price: initial price.
        discount: a function that represents discount program.

    Attributes:
        price: initial price.
        _discount: a function that represents discount program.
    """

    def __init__(self, price: float, discount: Callable):
        self.price = price
        self._discount = discount

    def final_price(self) -> float:
        """Returns the price after the discount program is applied"""
        return self.price - self.price * self._discount()
