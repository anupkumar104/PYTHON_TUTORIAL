import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def perform_stemming(text):
    stopword = set(stopwords.words('english'))
    tokenized_word = word_tokenize(text)
    stemmer = PorterStemmer()
    stemming_data = []
    for word_1 in tokenized_word:
        stemming_data.append(stemmer.stem(word_1))
    stemming_text = " ".join(stemming_data)
    return stemming_text 
input_text= input("enter a string for stemming:")
print("Original text:",input_text)
print("stemming text:",perform_stemming(input_text) )
