from typing import List


class Checkout(object):
    def __init__(self):
        self.items: List[dict] = []

    def add_item(self, item: str, price: float):
        self.items.append({"name": item, "price": price})

    def total(self) -> float:
        total = 0
        for item in self.items:
            total = total + float(item["price"])

        return total

    def discount_item(self, item_name: str, discount: float):
        for item in self.items:
            if item["name"] == item_name:
                new_total = float(item["price"] - discount)

                if new_total < 0:
                    raise DiscountError()

                item["price"] = new_total
                return


class DiscountError(Exception):
    pass
