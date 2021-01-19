import json
import difflib                              # Library used to compare text
from difflib import SequenceMatcher         # Checks the ratio that two strings are similar .00 -> 1.00
from difflib import get_close_matches       # Finds other similar strings (ratio 0.6 or greater)

data = json.load(open("data.json", 'r'))

def translate(word):
    # Filter all other variations of typing the word to lower case
    word = word.lower()
    # Check to see if word is within Data
    if word in data:
        return data[word]
    # If users entered "Paris" this will check for "Paris" as well
    elif word.title() in data:
        return data[word.title()]
    # In case the user enters words like USA or NATO
    elif word.upper() in data:
        return data[word.upper()]
    # If there are more than one words that close match
    elif len(get_close_matches(word, data.keys())) > 0:
        YorN = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if YorN.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif YorN.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
# To make the output a bit more user friendly
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)