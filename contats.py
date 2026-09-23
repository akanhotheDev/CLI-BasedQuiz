contacts = [{"name": "Ada", "age": 20},{"name": "Instep", "age": 16},{"name": "Akanho", "age": 40}]

for info in contacts:
    print(f"{info['name']} is {info['age']}")
    if info["age"] > 29:
        print("Adult")
    elif info["age"] > 17:
        print("Young Adult")
    else:
        print("Minor")

print(f"total contacs is {len(contacts)}")