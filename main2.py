# Task 1
class Discount:
    """
    Default discount.
    """

    def __init__(self, discount=0):
        self.discount = 0
        if discount > 0:
            self.discount = discount


class RegularDiscount(Discount):
    """
    Regular discount for a customer.
    """

    def __init__(self, reg_discount, x):
        super().__init__(discount=0)
        self.reg_discount = x - x * 0.10

    def __str__(self):
        return f'{self.reg_discount}'


class SilverDiscount(Discount):
    """
    Silver discount for a customer.
    """

    def __init__(self, sil_discount, x):
        super().__init__(discount=0)
        self.sil_discount = x - x * 0.30

    def __str__(self):
        return f'{self.sil_discount}'


class GoldDiscount(Discount):
    """
    Gold discount for a customer.
    """

    def __init__(self, gold_discount, x):
        super().__init__(discount=0)
        self.gold_discount = x - x * 0.50

    def __str__(self):
        return f'{self.gold_discount}'


class Client:
    """
    Client's info and discount.
    """

    def __init__(self, name, discount, order):
        self.name = name
        self.discount = discount
        self.order = order

    def get_total_price(self, discount: int | float = 1, order: int | float = 1):
        return order * discount

    def __str__(self):
        return f'{self.name}, {self.discount}, {self.get_total_price}'


if __name__ == '__main__':
    main_order = Client('Mary', 0.3, 100)
    main_order.get_total_price()
    print(main_order)