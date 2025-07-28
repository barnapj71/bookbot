def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
      
    return file_contents

def count_char_nums(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    lowercase_contents = file_contents.lower()
    
    my_list=[]
    my_dict={}
    
    for char in lowercase_contents:
        if char not in my_list:
            my_list.append(char)
            
    for item in my_list:
        my_dict[item]=lowercase_contents.count(item)

    return my_dict

def sort_on(items):
    return items["num"]

def sort_my_dict(dict_to_sort:dict):
    
    my_dict =[]

    for item in dict_to_sort:
        if item.isalpha():
            my_dict.append({"char":item,"num":dict_to_sort[item]})




    my_dict.sort(reverse=True, key=sort_on)

    
    return my_dict
        

    
    