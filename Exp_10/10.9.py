import webbrowser
from urllib.parse import quote_plus

word = "ubiquitous"
encoded_word = quote_plus(word)
url = "https://www.dictionary.com/browse/" + encoded_word
webbrowser.open(url)
