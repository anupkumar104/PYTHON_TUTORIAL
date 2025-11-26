import nltk
#nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer,PorterStemmer
demoword=['good','better','doing','programming','program','programs','code','codes','coding']
lematizer=WordNetLemmatizer()
stemmer=PorterStemmer()
for word in demoword:
    print(word,stemmer.stem(word),lematizer.lemmatize(word,"v"))
