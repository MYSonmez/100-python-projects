PLACEHOLDER = "[name]"

with open("project-023/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
with open("project-023/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(
            f"project-023/Output/ReadyToSend/letter_for_{stripped_name}.txt",
            "w",
        ) as new_file:
            new_file.write(new_letter)