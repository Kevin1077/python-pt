import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter:row.code for(index, row) in df.iterrows()}
print(letter_dict)
name = input("Enter your Name!!!\n").upper()
letter_list = [letter_dict.get(letter) for letter in name]
print(letter_list)
