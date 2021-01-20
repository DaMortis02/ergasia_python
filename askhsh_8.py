import urllib.request
import json

#Create a string that will contain the user's file 
user_input=input("Enter your file name: ")

# Open file and read data
with open(user_input) as f:
    data = f.read()

 # Create dictionary from file data using JSON 
js = json.loads(data)

# Create an empty list for the cryptocurrencies
crypto=[]

# Add the cryptocurrencies in the list 
for keys in js.keys():
    crypto.append(keys)

# Create an empty list for the cryptocurrencies's quantity
crypto_quantity=[]

# Add the quantities in the list 
for values in js.values():
    crypto_quantity.append(values)

# Initialize the value of all cryptocurrencies
sum_of_crypto_value = 0

# Open URL,read data from URL and create dictionary with these data
# Calculate value of each cryptocurrency and calculate the sum of those values 
# Print those values

for i in range(len(crypto)):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms="+crypto[i]+"&tsyms=EUR"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    dict1=json.loads(html)
    current_total_crypto_value=round(dict1[crypto[i]]["EUR"]*crypto_quantity[i],2)
    sum_of_crypto_value+=current_total_crypto_value
    print("Your " + crypto[i] + " quantity is " + str(crypto_quantity[i]) + " and the value in euros is: " + str(current_total_crypto_value) + " euros")

print("Your portfolio value in cryptocurrencies is: " + str(round(sum_of_crypto_value,2)) + " euros") # Print portfolio value