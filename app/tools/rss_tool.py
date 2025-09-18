# RSS fetching tool (to be implemented)
def fetch_rss(category: str):
    import feedparser
    feeds = {
        "latest": "https://news.google.com/rss",
        "stock": "https://www.moneycontrol.com/rss/markets.xml",
        "sports": "https://www.espn.com/espn/rss/news"
    }
    # If category is known, use mapped feed. Otherwise, use Google News topic search RSS
    if category in feeds:
        url = feeds[category]
    else:
        # Google News topic search RSS (e.g., cricket, bollywood, technology, etc.)
        from urllib.parse import quote_plus
        topic = quote_plus(category)
        url = f"https://news.google.com/rss/search?q={topic}"
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.get("title", ""),
            "summary": entry.get("summary", ""),
            "link": entry.get("link", "")
        })
    return articles
