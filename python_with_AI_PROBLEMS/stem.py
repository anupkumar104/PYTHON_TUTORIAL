import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stopword=set(stopwords.words('english'))
text=input("enter a string for stemming:")
#text="The leaves are falling from the trees and the boys were playing games while running and studies are continuing."
tokenized_word=word_tokenize(text)
tokenized_word_without_stopwords=[]
#for word in tokenized_word:
  #  if word not in stopword:
   #     tokenized_word_without_stopwords.append(word)
#print("tokenized_word_without_stopwords :",tokenized_word_without_stopwords)
stemmer=PorterStemmer()
stemming_data=[]
for word_1 in tokenized_word:
    stemming_data.append(stemmer.stem(word_1))
#print(stemming_data)
stemming_text=" ".join(stemming_data)
print(stemming_text)