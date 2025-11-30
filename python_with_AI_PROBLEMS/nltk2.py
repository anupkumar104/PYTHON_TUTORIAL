# read text file
file = open("nltk.txt", "r")
data = file.read()
file.close()
# perform tokenization on .txt file data
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
tokenized_data = word_tokenize(data)
# function to remove stopwords
def remove_stopwords(tokenized_data):
    stopword = set(stopwords.words('english'))
    tokenized_data_without_stopwords = []
    for word in tokenized_data:
        if word not in stopword:
            tokenized_data_without_stopwords.append(word)
    return tokenized_data_without_stopwords
tokenized_data_without_stopwords = remove_stopwords(tokenized_data)
print("the stopword which is removed from tokenized data:", set(tokenized_data) - set(tokenized_data_without_stopwords))
data1 = ' '.join(tokenized_data_without_stopwords)
print("filtered_data:", data1)
