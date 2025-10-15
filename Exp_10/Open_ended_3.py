import webbrowser
from urllib.parse import quote_plus

product = "samsung galaxy s24 ultra"
encoded_product = quote_plus(product)
url = "https://www.amazon.in/s?k=" + encoded_product
webbrowser.open(url)
