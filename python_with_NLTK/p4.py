import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
sia=SentimentIntensityAnalyzer()
print(sia.polarity_scores("program is fun"))
print(sia.polarity_scores("my name is anup"))