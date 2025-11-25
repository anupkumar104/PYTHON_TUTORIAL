import nltk
# nltk.download("stopwords")
text="""Artificial Intelligence,especially Natural Language Processing, enables machines to analyze, understand,and generate human language, allowing applications like chatbots,translators,and voice assistants to communicate naturally with users across the world"""
from nltk.tokenize import word_tokenize,sent_tokenize
word_tokenized=word_tokenize(text)
print("word_tokenized:",word_tokenized)
from nltk.corpus import stopwords
stopword=set(stopwords.words('english'))
# print("the colletion of stopwords in english::",stopword)
word_tokenized_without_stopwords=[]
for word in word_tokenized:
    if word not in stopword:
        word_tokenized_without_stopwords.append(word)
print("word_tokenized_without_stopwords :",set(word_tokenized_without_stopwords))
print("the stopword which is removed from tokenized words:",set(word_tokenized)-set(word_tokenized_without_stopwords))
