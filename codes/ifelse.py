#stock management system
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]
minimum_stock = 10
reorder_list = []
for product,stock in zip(product_names,stock_levels):
    if stock < minimum_stock:
        reorder_list.append(product)
print(reorder_list)
