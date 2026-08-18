orders = [
    {"order_id": 101, "customer_id": 1, "amount": 500},
    {"order_id": 102, "customer_id": 2, "amount": 1200},
    {"order_id": 103, "customer_id": 1, "amount": 750},
    {"order_id": 104, "customer_id": 3, "amount": 300},
]
Revenue = 0
MaxVal = 0
CountG700 = 0
for x in orders:
    Revenue += x["amount"]
    MaxVal = max(MaxVal, x["amount"])
    if x["amount"] > 700:
        CountG700 += 1

AvgOrderVal = Revenue / len(orders)

print("Total Orders:", len(orders))
print("Total Revenue:", Revenue)
print("Average Order Value:", AvgOrderVal)
print("Highest Order:", MaxVal)
print("Orders above 700:", CountG700)