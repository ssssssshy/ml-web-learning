from backend.services import analyze_sentiment


def test_positive_sentiment():
    text = "I love this movie"
    result = analyze_sentiment(text)
    assert result == "positive"


def test_negative_sentiment(text="This is awful"):
    text = "This is awful"
    result = analyze_sentiment(text)
    assert result == "negative"


def test_neutral_sentiment(text="This is a movie"):
    text = "This is a movie"
    result = analyze_sentiment(text)
    assert result == "neutral"
