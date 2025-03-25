def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    result = {}
    for i in range(len(text)):
                   char = text[i].lower()
                   if char.isalpha():
                        if char not in result:
                            result[char] = 1
                        else:
                            result[char] += 1
    return result

def sort_on(dict):
      return dict["value"]

# transform dictionary to a sorted list of dictionaries
def get_characters_sorted(text):
    dict = get_num_characters(text)
    sorted_list = []
    for key in dict:
          sorted_list.append({"key": f"{key}", "value": dict[key]})
          
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def format_char_message(list):
    message = ""

    for i in list:
        message += f"{i['key']}: {i['value']}\n"
    return message
    