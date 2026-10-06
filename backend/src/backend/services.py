def analyze_sentiment(text: str) -> str:
    text = text.lower()
    words = text.split()
    positive_words = {"good", "great", "excellent", "love"}
    negative_words = {"bad", "terrible", "awful", "hate"}

    for word in words:
        word = word.strip(".,!?;:")
        if word in positive_words:
            return "positive"
        elif word in negative_words:
            return "negative"

    return "neutral"
