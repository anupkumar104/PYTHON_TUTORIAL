def sort_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sentence = " ".join(words)
    return sorted_sentence
sentence = input("Enter a sentence: ")
print("Original Sentence:", sentence)
print("Sorted Sentence:", sort_sentence(sentence))
