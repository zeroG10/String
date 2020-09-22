def number_of_characters(some_text):
    letter_in_text = 0
    for letter in some_text:
        if letter == "і":
            letter_in_text += 1
    print(letter_in_text)


number_of_characters('Секрет успіху – в тому, щоб викликати обурення\n'
                     ' у якомога більшої кількості людей.')