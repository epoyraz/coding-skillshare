import requests
from bs4 import BeautifulSoup

# Define the URL of the travel booking website and the search parameters
url = 'https://www.expedia.com/Flights-Search'
params = {'flight-type': 'on', 'starDate': '2022/03/01', 'endDate': '2022/03/10', 'mode': 'search', 'trip': 'roundtrip',
          'leg1': 'from:Larnaca,%20Cyprus%20(LCA-Larnaca%20Intl.),to:Zurich,%20Switzerland%20(ZRH)', 'leg2': 'from:Zurich,%20Switzerland%20(ZRH),to:Larnaca,%20Cyprus%20(LCA-Larnaca%20Intl.)',
          'passengers': 'adults:1,children:0,seniors:0,infantinlap:Y'}

# Send a GET request to the website with the search parameters
response = requests.get(url, params=params)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element that contains the flight price and extract the price
price_elem = soup.find('span', {'data-test-id': 'listing-price-dollars'})
price = price_elem.text if price_elem else 'Price not found'

# Print the flight price
print('The price of a roundtrip flight from Larnaca to Zurich is', price)