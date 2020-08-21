"""
Name      :Nahia Akter
Student#  : 301106956
Program   : generator.py

Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""

import random

def getWords(filename):
    files = open(filename)
    temp_list = list()
    for each_line in files:
        each_line = each_line.strip()
        temp_list.append(each_line)

    words = tuple(temp_list)
    files.close()

    return words

"""Getting words from the text files."""

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')
conjunctions = getWords('conjunctions.txt')
adjectives = getWords('adjectives.txt')

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
main()