# TODO 1. Create a dictionary from the NATO Alphabet: 
import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index,row) in nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs. 

def generate_phonetic():
    user_input = list(input("Input a series of letter to have translated into phonetic code: ").upper()) 
    try:
        code_list = [nato_dict[letter] for letter in user_input ]
    except KeyError: 
        print("Sorry. Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_list)

generate_phonetic()