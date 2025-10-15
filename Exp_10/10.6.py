import webbrowser
from urllib.parse import quote_plus

query = "lofi beats"
encoded_query = quote_plus(query)
url = "https://www.youtube.com/results?search_query=" + encoded_query
webbrowser.open(url)
