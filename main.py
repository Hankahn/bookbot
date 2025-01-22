def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print_report(book_path, num_words, char_count)
    # print(f"{char_count} character counts")
    # print(f"{num_words} words found in the document")

def sort_on(dict):
    return dict["count"]

def print_report(book_path, num_words, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the book")
    
    char_count_list = convert_dictionary_to_list(char_count)
    char_count_list.sort(reverse=True, key=sort_on)

    for char in char_count_list:
        print(f"The character '{char['char']}' was found {char['count']} times")

    print("--- End report ---")

def get_char_count(text):
    lc_text = text.lower()
    char_dict = {}

    for char in lc_text:
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 0
            
            char_dict[char] += 1
    
    return char_dict

def convert_dictionary_to_list(dict_to_convert):
    new_list = []

    for key in dict_to_convert.keys():
        new_list.append({ "char": key, "count": dict_to_convert[key] })

    return new_list

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
