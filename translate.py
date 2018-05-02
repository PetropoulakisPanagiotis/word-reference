import json
from difflib import get_close_matches

# Open file: convert object  to dictionery #
with open("data.json") as data_file:
    data = json.load(data_file)

# Dictionery has words with their definitions #

# Translate:                 #
# Input: string              #
# Output: definition         #

def translate(word):

    if type(word) != str:
        return "Please give a word."

    if not word.islower():
        word = word.lower()

    # Word exists in dictionery #
    if data.has_key(word):
        return data[word]

    # Check if user gave a word that is similar to an existing word #
    else:
        matches = get_close_matches(word, data.keys(),cutoff= 0.8)

        if matches:
            answer = raw_input("Did you mean %s instead? Enter Y for yes or N for no: "% matches[0])

            if answer == "Y" or answer == "y":
                return data[matches[0]]

            elif answer == "N" or answer == "n":
                return "Sorry the word doesn't exists."

            else:
                return "Press Y or N. Please try again."

        # No matches #
        else:
            return "Sorry the word doesn't exists."
