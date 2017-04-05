import random

vowels = "aeiou"

word_format = input ("What is your name: ")
count = 0

for each in word_format:
    if each in vowels:
        count += 1

print("Out of {} letters, {} has {} vowels".format(len(word_format), word_format, count))
