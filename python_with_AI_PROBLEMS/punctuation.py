import string
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)
input_text = input("Enter a string: ")
result = remove_punctuation(input_text)
print("Original String:", input_text)
print("String without Punctuations:", result)