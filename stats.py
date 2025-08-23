def get_num_words(text):
    # takes a string
    # returns the number of words in the given string

    words = text.split()
    return len(words)

def get_num_characters(text):
    # takes a string
    # returns a dictionary containing each character and 
    # the number of times it appears in the string

    low_case_text = text.lower()
    char_count = {}

    for char in low_case_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_dict(dict):
    # takes a dictionary of characters and their count
    # returns a sorted list of dictionaries

    sorted_list = []

    # create list of dictionaries based on the given dictionary
    for key in dict:
        num = dict[key]
        sorted_list.append({"char": key, "num": num})

    # function used to sort the list of dictionaries
    def sort_on(sorted_dict):
        return sorted_dict["num"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list