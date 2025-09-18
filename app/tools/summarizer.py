# Summarization tool
def summarize_articles(articles):
    # Ensure torch is imported for transformers
    try:
        import torch  # noqa: F401
    except ImportError:
        pass
    from transformers import pipeline
    import os
    summarizer = pipeline("summarization", model=os.getenv("HF_SUMMARIZER_MODEL", "sshleifer/distilbart-cnn-12-6"))
    summaries = []
    for article in articles:
        text = article.get("summary") or article.get("title")
        if not text:
            continue
        try:
            summary = summarizer(text, max_length=60, min_length=15, do_sample=False)[0]["summary_text"]
        except Exception:
            summary = text[:200] + ("..." if len(text) > 200 else "")
        summaries.append({"title": article.get("title", ""), "summary": summary, "link": article.get("link", "")})
    return summaries
