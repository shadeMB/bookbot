def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    low_case_text = text.lower()
    char_count = {}

    for char in low_case_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
