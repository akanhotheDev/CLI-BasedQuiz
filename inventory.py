
products = [{"name": "book", "price": 400, "quantity": 12},{"name": "shoe", "price": 1600, "quantity": 4},{"name": "shirt", "price": 8000, "quantity": 8},{"name": "track", "price": 7000, "quantity": 6}]
total_value = 0
final_total = 0
for product in products:
    total_value = product["price"] * product["quantity"]
    print(f"{product['name']}: {product['quantity']} units at {product['price']} = {total_value}")
    if product["quantity"] <= 5:
        print(f"low stock!")
        final_total += total_value

print(f"ALl products total is : {final_total}")