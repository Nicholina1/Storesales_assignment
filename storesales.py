# Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

# The owner wants you to do some calculations on the data with these criteria's:

#     -calculate the total price average for all products

#     -create a new price list that reduces the old prices by $ 5

#     -calculate the total revenue generated from the products

#     -calculate the average daily revenue generated from the products

#     -based on the new prices, which products are less than $ 30 

# Below is the data you are to use for the problem :

# products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

# prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

# last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]


#Calculate the total price average
total_price = sum(prices)
price_average = total_price / len(prices)

#Create a new price list that reduces the old prices by $5
new_price = [price-5 for price in prices]
#print(new_price)

#Calculate the total revenue generated from the products
total_revenue = 0
index = 0

for price in prices:
    product_totalrevenue = price * last_week[index]
    total_revenue = total_revenue + product_totalrevenue
    index = index + 1
#print(total_revenue)


#Calculate average daily revenue
average_dailyrevenue = total_revenue/7
#print(average_dailyrevenue)

#Products less than $30
prices_lessthan30 = list(enumerate(new_price))

products_lessthan30 = []

for index, price in prices_lessthan30:
    if(price < 30):
        product = products[index]
        products_lessthan30.append(product)
#print(products_lessthan30)
        
print(f"Total Price Average: ${total_price:.2f}")
print(f"New Prices: {new_price}")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Daily Revenue: ${average_dailyrevenue:.2f}")
print(f"Products Less Than $30: {products_lessthan30}")
