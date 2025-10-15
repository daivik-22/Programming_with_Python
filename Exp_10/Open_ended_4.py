import webbrowser
from urllib.parse import quote_plus

text = "¿Cómo estás?"
encoded_text = quote_plus(text)
url = "https://translate.google.com/?sl=auto&tl=en&text=" + encoded_text + "&op=translate"
webbrowser.open(url)
