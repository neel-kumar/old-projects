from difflib import get_close_matches
import json
d = json.load(open("data.json"))

def find_def (w):
    w = w.lower()
    if w in d:
        return d[w]
    elif w.upper() in d:
        return d[word]
    elif w.title() in d:
        return d[w.title()]
    elif len(get_close_matches(w, d.keys()))> 0:
        user = input("Did you mean %s instead. Enter Y if yes, or N if no: " % get_close_matches(w, d.keys())[0])
        if user == "Y":
            return d[get_close_matches(w, d.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "This word doesn't exist. Please double check."

word = input("Enter word: ")
output = find_def(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
