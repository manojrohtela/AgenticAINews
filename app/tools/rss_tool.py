# RSS fetching tool (to be implemented)
def fetch_rss(category: str):
    import feedparser
    feeds = {
        "latest": "https://news.google.com/rss",
        "stock": "https://www.moneycontrol.com/rss/markets.xml",
        "sports": "https://www.espn.com/espn/rss/news"
    }
    url = feeds.get(category, feeds["latest"])
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.get("title", ""),
            "summary": entry.get("summary", ""),
            "link": entry.get("link", "")
        })
    return articles
