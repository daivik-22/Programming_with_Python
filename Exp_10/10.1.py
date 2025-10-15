import sys, webbrowser
from urllib.parse import quote_plus

address = "Vijaya Mall"
encoded_address = quote_plus(address)
url = "https://www.openstreetmap.org/search?query=" + encoded_address
webbrowser.open(url)
