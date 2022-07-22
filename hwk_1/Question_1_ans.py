import random

class CashRegister:

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.discount = 0

    def add_item(self, item_price):
        self.total_items.update(item_price)

    def check_price(self, __key):
        price = self.total_items.get(__key)
        print(f"The price is £{price:.2f}")

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, money_off):
        self.discount += money_off
        print(f"£{money_off:.2f} voucher discount applied")

    def use_gift_card(self):
        money_on_card = round(random.uniform(0.00, 100.00), 2)
        self.discount += money_on_card
        print(f"you have used your £{money_on_card} gift card balance")

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        total = total_before_discount - self.discount
        if total > 0:
            print("\n total = £ {:.2f}".format(total))
        else:
            print("Total to pay = £0.00")



    def show_items(self):
        for item, price in self.total_items.items():
            print(f" {item:20s} £{price:.2f}")

    def reset_register(self):
        self.total_items = {}
        self.discount = 0


register_1 = CashRegister()
register_2 = CashRegister()
register_3 = CashRegister()


register_1.add_item({'Microwave': 49.99})
register_1.add_item({'Fan': 10.00})

register_1.check_price('Fan')

register_1.add_item({'Dog Bowl': 6.00})
register_1.add_item({'Dog Toy': 3.50})
register_1.add_item({'Scooter': 29.99})
register_1.add_item({'Dumbbells': 30.00})

register_1.remove_item('Dumbbells')

register_1.show_items()

register_1.apply_discount(3.00)
register_1.use_gift_card()

register_1.get_total()
