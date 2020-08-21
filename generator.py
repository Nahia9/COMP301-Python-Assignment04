"""
Name:Nahia Akter
Student#: 301106956
Program: generator.py

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
    x = random.randint(0,1)
    if  x == 0:
        return nounPhrase() + " " + verbPhrase()
    else:
        return nounPhrase() + " " + verbPhrase() + " " +  conjunctionPhrase() + " " + nounPhrase() + " " + verbPhrase() 


def nounPhrase():
    """Builds and returns a noun phrase."""

    x = random.randint(0,1)
    if  x == 0:
        return random.choice(articles) + " " + random.choice(nouns)
    else:    
        return random.choice(articles) + " " + adjectivePhrase() + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    x = random.randint(0,1)
    if x == 0:
        return random.choice(verbs) + " " + nounPhrase() + " "
    else:
        return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    prephrase = ""
    prechance = random.randrange(100) + 1
    if (prechance > 50):
        prephrase = prepositionalPhrase()
    return random.choice(prepositions) + " " + nounPhrase()

def adjectivePhrase():
    """Builds and returns a adjective phrase."""
    adjphrase = ""
    adjchance = random.randrange(100)+1
    if (adjchance > 60):
        adjphrase = adjectivePhrase()
    return random.choice(adjectives) + " " +  nounPhrase()

def conjunctionPhrase():
    conjphrase = ""
    conjchance = random.randrange(100)+1
    if (conjchance > 70):
        conjphrase = conjunctionPhrase()
    return random.choice(conjunctions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

main()