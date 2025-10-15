import webbrowser
from urllib.parse import quote_plus

query = "Python programming tutorials"
encoded_query = quote_plus(query)
url = "https://www.google.com/search?q=" + encoded_query
webbrowser.open(url)
