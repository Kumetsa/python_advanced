def grocery_store(**products):
    sorted_products = sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    return '\n'.join([f"{product}: {quantity}" for product, quantity in sorted_products])


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))