# TODO 1. Create a dictionary from the NATO Alphabet: 
import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {letter:code for (letter,code) in nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs. 

user_input = list(input("Input a series of letter to have translated into phonetic code: ").upper()) 

print(nato_dict.index(user_input))
