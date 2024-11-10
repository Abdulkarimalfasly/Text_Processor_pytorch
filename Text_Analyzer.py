import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import arabic_reshaper
from bidi.algorithm import get_display

# Download necessary resources in nltk
nltk.download('punkt')

# Text to be analyzed
text = "Place your Arabic text here. It can be long or short as needed."

# Split text into sentences, words, and characters
sentences = sent_tokenize(text)
words = word_tokenize(text)
characters = list(text.replace(" ", ""))  # Removing spaces to count characters only

# Calculate the number of sentences, words, and characters
num_sentences = len(sentences)
num_words = len(words)
num_characters = len(characters)

# Calculate average sentence length in words
average_sentence_length = num_words / num_sentences if num_sentences > 0 else 0

# Calculate word frequency
word_frequency = FreqDist(words)
most_common_words = word_frequency.most_common(10)  # Most common words

# Calculate character frequency
char_frequency = FreqDist(characters)
most_common_characters = char_frequency.most_common(10)  # Most common characters

# Format results for proper Arabic display
reshaped_common_words = [(get_display(arabic_reshaper.reshape(word)), freq) for word, freq in most_common_words]
reshaped_common_characters = [(get_display(arabic_reshaper.reshape(char)), freq) for char, freq in most_common_characters]

# Print results
print("Number of sentences:", num_sentences)
print("Number of words:", num_words)
print("Number of characters:", num_characters)
print("Average sentence length (in words):", round(average_sentence_length, 2))
print("Most frequent words:", reshaped_common_words)
print("Most frequent characters:", reshaped_common_characters)
