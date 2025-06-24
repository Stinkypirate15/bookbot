def get_book_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text

def split_text(returned_getbook):
    total_length=returned_getbook.split()
    max_len=len(total_length)
    return max_len

def characters_amount(returned_getbook):
    char_characters={}
    characters_lowered=returned_getbook.lower()
    for i in characters_lowered:
        character_check=i in char_characters
        if character_check:
            char_characters[i] += 1
        else:
            char_characters[i]= 1
    return char_characters

      
   
    

