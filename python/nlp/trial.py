import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences # used for pad the sequence 

sentences = [
	'I love my dog',
	'i love my cat',
	'You love my dog!',
	'do you think my dog is amazing?'
]

tokenizer = Tokenizer(num_words = 100, oov_token= "<OOV>") # out of vocabulary word, if not present in the train set
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences) # prints the index of word occurance
padded = pad_sequences(sequences, padding = 'post')
print(word_index)
#print(sequences)
#print(padded)  # comapres with the longest word, and appends with extra 0.

