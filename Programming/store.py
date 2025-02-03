'''
Milk, 2.50
Bread, 1.20
Eggs, 3.00
done
Sample Output

Milk: 2.5
Bread: 1.2
Eggs: 3.0

Python (3.8.1)
Dark

language

1234567
# TODO: Prompt the user to enter product names and prices, and store them in product_prices

# TODO: Allow the user to enter multiple entries until they type 'done'

# TODO: Print each product's name along with its price



Run Code
Submit Code


'''

d = {}
while True:
    user_input = input()
    if user_input == 'done':
        break
    product_name, price = user_input.split(',')
    product_name = product_name.strip()
    price = float(price.strip())
    d[product_name] = price

for product_name, price in d.items():
    print(f"{product_name}: {price}")    




