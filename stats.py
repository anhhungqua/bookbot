def get_num_words(book_text):
    return len(book_text.split())
def get_num_unique_words(book_text):
    unique_characters = {}
    lower_key_text = book_text.lower()
    for i in lower_key_text:
        if i not in unique_characters:
            unique_characters[i] = 1
        else:
            unique_characters[i] += 1
    return unique_characters
def sort_on(d):
    return d["num"]
def get_unique_characters_list_sort(unique_characters):
    unique_characters_list = []
    for i in unique_characters:
        num = unique_characters[i]
        if i.isalpha() == True:
            unique_characters_list.append({"char": i, "num": num})
    unique_characters_list.sort(reverse=True, key=sort_on) 
    return unique_characters_list
