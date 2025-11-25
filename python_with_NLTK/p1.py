import nltk
import matplotlib.pyplot as plt
# nltk.download("punkt_tab")
#text="""my name is anup. i am nineteen years old. i am from lucknow."""
text2="""Artificial Intelligence,especially Natural Language Processing, enables machines to analyze, understand,and generate human language, allowing applications like chatbots,translators,and voice assistants to communicate naturally with users across the world"""
# from nltk.tokenize import word_tokenize
# print(word_tokenize(text))
# from nltk.tokenize import sent_tokenize
# print(sent_tokenize(text))
from nltk.tokenize import word_tokenize
word_tokenized=word_tokenize(text2)
from nltk.probability import FreqDist
fd=FreqDist(word_tokenized)
print(fd)
print(fd.most_common(3))
fd.plot(20,cumulative=False)
plt.show()