import webbrowser
from urllib.parse import quote_plus

topic = "OpenStreetMap"
encoded_topic = quote_plus(topic)
url = "https://en.wikipedia.org/wiki/" + encoded_topic
webbrowser.open(url)
