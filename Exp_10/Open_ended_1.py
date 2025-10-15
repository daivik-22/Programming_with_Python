import webbrowser
from urllib.parse import quote_plus

query = "Python webbrowser module"
encoded_query = quote_plus(query)
url = "https://stackoverflow.com/search?q=" + encoded_query
webbrowser.open(url)
