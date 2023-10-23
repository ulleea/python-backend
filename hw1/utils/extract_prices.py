def extract_prices(products):
    prices = []
    for product in products:
        if product.price not in prices:
            prices.append(product.price)
    return prices
