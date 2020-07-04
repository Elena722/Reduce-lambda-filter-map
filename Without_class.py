'''A seller of luxury wrist watches has enlisted your help in performing some difficult tasks.
Combining any of lambda, map, filter or reduce, write a python program to:
The most expensive watch
A new inventory where the watches are sorted according to their price
A dictionary within which each key represents a watch brand and the value is the total
cost of that brand in our inventory (quantity * price)
A list containing all watches with quantity greater than 30
A new inventory with discount prices for items that are not getting sold out. In this new
inventory, if the quantity of a watch from the old inventory is greater than 30, reduce the
price by 50 EUR if the old price is greater than 500 EUR else reduce by 30 EUR'''

import openpyxl
from functools import reduce

class WristWatches:
    def __init__(self, id, item, quantity, unit_price):
        self.id = id
        self.item = item
        self.quantity = quantity
        self.unit_price = unit_price

    def __repr__(self):
        return f'WhristWatch(id={self.id}, name={self.item}, quantity={self.quantity}, unit_price={self.unit_price}'

class Inventory(list):
    def __init__(self, id, item, quantity, unit_price):
        super().__init__()
        self.id = id
        self.item = item
        self.quantity = quantity
        self.unit_price = unit_price

    def __repr__(self):
        for item in self:
            print(item)
        return ''

wb = openpyxl.load_workbook('hm.xlsx')
sheet = wb.active
id =[]
for cell in sheet["B"]:
    if cell.value is not None:
        id.append(cell.value)
item =[]
for cell in sheet["D"]:
    if cell.value is not None:
        cell.value = cell.value.strip()
        item.append(cell.value)
quantity =[]
for cell in sheet["F"]:
    if cell.value is not None:
        quantity.append(cell.value)
unit_price =[]
for cell in sheet["H"]:
    if cell.value is not None:
        unit_price.append(cell.value)
inventory = []

for i, v in enumerate(id):
    if i == 0 or i == 1:
        continue
    inventory.append(WristWatches(id[i], item[i], quantity[i], float(unit_price[i])))

#----------------------------------------------------------------------------------------------------------

# The most expensive watch
print('---The most expensive watch---')
res = reduce(max, map(lambda x: x.unit_price, inventory))
print(f"The most expensive watch: {res}")

res2 = reduce(lambda x, y: max(x, y, key=lambda z: z.unit_price), inventory)
print(f"The most expensive watch: {res2}")

res3 = reduce(
    lambda x, y: x if x.unit_price > y.unit_price else y, inventory
)
print(f"The most expensive watch: {res}")


# A new inventory where the watches are sorted according to their price
print('---Sorted by price---')
s = sorted(inventory, key=lambda x: x.unit_price)
print('price ->', [(s[i].item, s[i].unit_price) for i in range(len(s))])

# A dictionary within which each key represents a watch brand and the value is the total cost of that
# brand in our inventory (quantity * price)
print('---Dictionary---')
d = dict(map(lambda x: [x.item, round(x.quantity*x.unit_price, 2)], inventory))
print('dict ->', d)

# A list containing all watches with quantity greater than 30
print('---Quantity > 30---')
gt = list(filter(lambda x: x.quantity > 30, inventory))
# print(gt)
print('quantity > 30 ->', [(gt[i].item, gt[i].quantity) for i in range(len(gt))])

# A new inventory with discount prices for items that are not getting sold out.
# In this new inventory, if the quantity of a watch from the old inventory is greater than 30,
# reduce the price by 50 EUR if the old price is greater than 500 EUR else reduce by 30 EUR
print('---New inventory---')
inventory2 = inventory
not_sold_out = list(filter(lambda x: x.quantity > 0, inventory))
# new_price = list(map(lambda x: x.unit_price-50 if (x.quantity > 30 and x.unit_price > 500) else (x.unit_price-30
#                                     if x.quantity > 30 and x.unit_price < 500 else x.unit_price), not_sold_out))
#
# for i, v in enumerate(not_sold_out):
#     v.unit_price = new_price[i]
# inventory = not_sold_out
# print('new ->', [(inventory[i].item, inventory[i].unit_price) for i in range(len(inventory))])

# or
def discount(watch):
    if watch.quantity > 30:
        if watch.unit_price > 500:
            watch.unit_price -= 50
        else:
            watch.unit_price -= 30
    return (watch.item, watch.unit_price)
new_price2 = list(map(discount, not_sold_out))
print(new_price2)

# some additional task
# price_and_quantity = reduce(
#         lambda prev_result, next_watch: (prev_result[0] + next_watch.unit_price * next_watch.quantity, prev_result[1] + next_watch.quantity),
#         filter(lambda watch: watch.quantity > 10 and watch.unit_price > 200, inventory),
#         (0, 0)
#     )
# average = round(price_and_quantity[0] / price_and_quantity[1], 2)
# print(f"Average: {average}")

