"""sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def sushi(orders):
    receipt = {}
    
    for order in orders:
        order['count'] = 1
        if order['name'] in receipt:
            receipt[order['name']]['quantity'] += 1
        elif order['name'] not in receipt:
            receipt[order['name']] = {
                "price": order['price'],
                "quantity": 1
            }
    for name, qt in receipt.items():
        print(f"{name} x {qt['quantity']} ... ${ qt['quantity'] * qt['price'] }")

sushi(sushi_orders)"""

wards = {
    "Cardiology": ["Alice", "Bob", "Carol"],
    "Neurology": ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology": ["Ivy", "Bob"]
}

staff = {}

for ward, name in wards.items():
    for ppl in name:
        if ppl not in staff:
            staff[ppl] = []
        staff[ppl].append(ward)

print(staff)