import time


class Product:
    """
    Product class.
    """
    def __init__(self, name: str, price: float | int):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


class Cart:
    """
    Cart class.
    """
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Add product to cart.
        """
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            raise TypeError("Invalid type.")
        self.products.append(product)
        self.quantities.append(quantity)

    def remove_product(self, product: Product, quantity: int | float = 1):
        """
        Remove product from cart.
        """
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            raise TypeError("Invalid type.")
        if product not in self.products:
            raise ValueError("Product not in cart.")

        index = self.products.index(product)
        if self.quantities[index] < quantity:
            raise ValueError("Not enough quantity.")
        self.quantities[index] -= quantity
        if self.quantities[index] == 0:
            del self.products[index]
            del self.quantities[index]
        return None

    def total(self):
        """
        Calculate total price.
        """
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __len__(self):
        return len(self.products)

    def __iadd__(self, other):
        self.Cart += other.Cart
        return self

    def __str__(self):
        res = f'{time.ctime()}: Items {len(self)}\n'
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product.name} - {product.price} x {quantity} = {product.price * quantity} UAH\n'
        res += f'Total: {self.total()} UAH'
        return res


if __name__ == '__main__':
    product_1 = Product('Milk', 20)
    product_2 = Product('Bread', 10)
    product_3 = Product('Meat', 100)
    product_4 = Product('Apples', 15)
    product_5 = Product('Cucumbers', 20)
    product_6 = Product('Cheese', 120)

    cart1 = Cart()
    cart1.add_product(product_1, 2)
    cart1.add_product(product_2)
    cart1.add_product(product_3, 1.5)

    cart2 = Cart()
    cart2.add_product(product_4, 1.5)
    cart2.add_product(product_5)
    cart2.add_product(product_6, 0.5)

    print(cart1)
    print(cart2)

#Task 3
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def common_denominator(self, other):
        if self.b != other.b:
            self.a = self.a * other.b
            other.a = other.a * self.b
            self.b = self.b * other.b
            other.b = self.b
        return self, other

    def __eq__(self, other):
        self.common_denominator(other)
        return self.a == other.a

    def __gt__(self, other):
        self.common_denominator(other)
        return self.a > other.a

    def __add__(self, other):
        self.common_denominator(other)
        summary = self.a + other.a
        res = Fraction(summary, self.b)
        return res

    def __sub__(self, other):
        self.common_denominator(other)
        b = self.a - other.a
        res = Fraction(b, self.b)
        return res

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        mul = Fraction(a, b)
        return mul

    def __str__(self):
        if self.a >= self.b:
            return "Improper fraction: " + str(self.a) + " / " + str(self.b) + ""
        else:
            return "Proper fraction:  " + str(self.a) + " / " + str(self.b) + " "

frac_1 = Fraction(3, 5)
frac_2 = Fraction(4, 6)

print(frac_1)
print(frac_2)
print(frac_1 == frac_2)
print(frac_1 > frac_2)
print(frac_1 + frac_2)
print(frac_1 - frac_2)
print(frac_1 * frac_2)