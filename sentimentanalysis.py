# import NLTK library
import nltk

# download necessary NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')

# import SentimentIntensityAnalyzer class from NLTK
from nltk.sentiment import SentimentIntensityAnalyzer

# create SentimentIntensityAnalyzer object
analyzer = SentimentIntensityAnalyzer()

# To get user input
user_input = input("Enter some text: ")

# calculate sentiment scores using polarity Return a float for sentiment strength based on the input text. Positive values are positive valence, negative value are negative valence.
scores = analyzer.polarity_scores(user_input)

# determine emotional tone
if scores['compound'] > 0:
    tone = "positive"
elif scores['compound'] < 0:
    tone = "negative"
else:
    tone = "neutral"

# To print emotional tone
print("The emotional tone of the user's writing is:", tone)
