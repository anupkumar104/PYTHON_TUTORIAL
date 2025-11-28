import nltk
from nltk.tokenize import word_tokenize
#ltk.download('averaged_perceptron_tagger_eng')
sentence = "The leaves are falling from the trees and the boys were playing games while running and studies are continuing."
words = word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print("Parts of Speech Tagging:")
for word, tag in pos_tags:
    print(f"{word} --> {tag}")
