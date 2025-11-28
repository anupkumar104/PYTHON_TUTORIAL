# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()
sentence = "The leaves are falling from the trees and the boys were playing games while running and studies are continuing."
words = word_tokenize(sentence)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]#list comprehention
print("Original Sentence:")
print(words)
print("\nAfter Lemmatization:")
print(lemmatized_words)
