import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

terminal_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
terminal_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)


class Discount:
    def discount(self):
        raise NotImplementedError


class DiscountLimit(Exception):
    def init(self, limit_discount, message='Invalid discount'):
        self.limit_discount = limit_discount
        self.message = message
        super().__init__()

    def str(self):
        return f'Limit of discount is {self.limit_discount}\n. {self.message}'


class RegularDiscount(Discount):
    def discount(self):
        return 0.7


class SilverDiscount(Discount):
    def discount(self):
        return 0.05


class GoldDiscount(Discount):
    def discount(self):
        return 0.1


class PlatinumDiscount(Discount):
    def discount(self):
        return 0.15


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price}'


class Customer:
    def __init__(self, name: str, discount: Discount):
        self.name = name
        self.discount = discount


class Order:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int):
        self.products.append(product)
        self.quantities.append(quantity)

    def total_price(self, customer: Customer = None):
        discount = customer.discount.discount() if customer else 0
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.price * quantity
        return total * (1 - discount)

    def __str__(self):
        return '\n'.join(map(str, self.products))


discounts = {
    'regular': RegularDiscount(),
    'silver': SilverDiscount(),
    'gold': GoldDiscount(),
    'platinum': PlatinumDiscount(),
}

if __name__ == '__main__':
    print('Welcome to our shop!')
    print('Available discounts:')
    for discount in discounts:
        try:
            discounts
        except DiscountLimit:
            raise DiscountLimit(0.4)
    discount = input('Please choose discount: ')
    customer = Customer('John', discounts[discount])

    product1 = Product('banana', 100)
    product2 = Product('apple', 200)
    order = Order()
    order.add_product(product1, 2)
    order.add_product(product2, 1)

    print(order.total_price(customer))

