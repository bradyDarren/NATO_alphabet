# TODO 1. Create a dictionary from the NATO Alphabet: 
import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (_,row) in nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs. 

user_input = list(input("Input a series of letter to have translated into phonetic code: ").upper()) 

code_list = [nato_dict[letter] for letter in user_input ]

print(code_list)