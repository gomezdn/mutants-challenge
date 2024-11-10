def found_horizontal_sequence(letter, dna, current_row_index, current_letter_index):
    letters_left_to_check = 3

    try:
        dna[current_row_index][current_letter_index + letters_left_to_check]
    except:
        return False
        
    while (letters_left_to_check > 0):
        if (letter != dna[current_row_index][current_letter_index + 1]):
            break
        current_letter_index += 1
        letters_left_to_check -=1

    return letters_left_to_check == 0

def found_vertical_sequence(letter, dna, current_row_index, current_letter_index):
    letters_left_to_check = 3

    try:
        dna[current_row_index + letters_left_to_check][current_letter_index]
    except:
        return False

    while (letters_left_to_check > 0):
        if (letter != dna[current_row_index + 1][current_letter_index]):
            break

        current_row_index += 1
        letters_left_to_check -=1

    return letters_left_to_check == 0

def found_diagonal_sequence(letter, dna, current_row_index, current_letter_index):
    letters_left_to_check = 3

    try:
        dna[current_row_index + letters_left_to_check][current_letter_index + letters_left_to_check]
    except:
        return False

    while (letters_left_to_check > 0):
        if (letter != dna[current_row_index + 1][current_letter_index + 1]):
            break
        
        current_letter_index += 1
        current_row_index += 1
        letters_left_to_check -=1

    return letters_left_to_check == 0

def found_sequence_for_letter(letter, dna, current_row_index, current_letter_index):
    return (
        found_diagonal_sequence(letter, dna, current_row_index, current_letter_index)
        or found_vertical_sequence(letter, dna, current_row_index, current_letter_index)
        or found_horizontal_sequence(letter, dna, current_row_index, current_letter_index)
    )

def is_mutant(dna):
    # PRECONDITION: there isn't any sequence longer than 4 letters.
    total_sequences_found = 0
    current_row_index = 0

    while total_sequences_found < 2 and current_row_index < len(dna) - 1:
        current_letter_index = 0

        while total_sequences_found < 2 and current_letter_index < len(dna):
            letter = dna[current_row_index][current_letter_index]

            if found_sequence_for_letter(letter, dna, current_row_index, current_letter_index):
                total_sequences_found += 1

            current_letter_index += 1

        current_row_index += 1

    return total_sequences_found > 1