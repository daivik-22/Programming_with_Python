import webbrowser
from urllib.parse import quote_plus

city = "Chennai"
encoded_city = quote_plus(city)
url = "https://www.google.com/search?q=" + encoded_city + "+weather"
webbrowser.open(url)
