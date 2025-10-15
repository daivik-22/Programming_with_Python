import webbrowser

news_sites = [
    "https://www.bbc.com/news",
    "https://www.cnn.com",
    "https://www.reuters.com",
    "https://www.thehindu.com"
]

for site in news_sites:
    webbrowser.open(site)
