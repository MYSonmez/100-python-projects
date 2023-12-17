import pandas

nato_alphabet = pandas.read_csv("project-025/project/nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

word = input("Enter the word: ").upper()

coded_letter_list = [alphabet_dict[letter] for letter in word]
print(coded_letter_list)
