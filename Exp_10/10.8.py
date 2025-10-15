import webbrowser
from urllib.parse import quote_plus

address = "SRM Institute of Science and Technology"
encoded_address = quote_plus(address)
url = "https://www.google.com/maps/place/" + encoded_address
webbrowser.open(url)
