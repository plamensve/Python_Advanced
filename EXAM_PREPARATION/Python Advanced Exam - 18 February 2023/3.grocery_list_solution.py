def shop_from_grocery_list(budget, grocery_list, *products_and_prices):
    bought_products = []
    for product, price in products_and_prices:
        if product not in grocery_list:
            continue
        if budget - float(price) < 0:
            break
        else:
            bought_products.append(product)
            grocery_list.remove(product)
            budget -= float(price)
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."