# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_true=True
while is_true:
    ask = input("Enter a word: ").upper()
    try:
        word = [data_dict[letter] for letter in ask]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(word)
        is_true=False
