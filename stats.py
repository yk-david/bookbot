def count_number_of_words(book):
    number_of_words = len(book.split())

    return number_of_words

def count_number_of_characters(book):
    character_dic = {}
    
    for word in book.lower():
        if word in character_dic:
            character_dic[word] += 1
        else:
            character_dic[word] = 1 # If word appears first time, set it to 1 not 0
    
    return character_dic

def get_report(dict):
    dict_list = []
    
    for key in dict: # It would be better filter out non alphabet here
        if key.isalpha():
            dict_list.append({ "char": key, "num": dict[key] }) # Append only if `char` is alphabet
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

def sort_on(dict):
    return dict["num"]
