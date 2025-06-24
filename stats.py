def get_book_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text

def split_text(returned_getbook):
    total_length=returned_getbook.split()
    max_len=len(total_length)
    return max_len

def characters_amount(returned_getbook):
    char_characters={}#creates empty dict
    characters_lowered=returned_getbook.lower()#makes every letter in book lwoer case
    for i in characters_lowered:
        character_check=i in char_characters
        if character_check:#if character is detected in list adds count to it
            char_characters[i] += 1
        else:
            char_characters[i]= 1#if character is not detected in list adds it to list
    return char_characters

def sort_characters(char_characters):
    def sort_on(dict_Def):#creates function allowing for sorting
        return dict_Def["num"]
    
    arrangement=[]#Creates empty list
   
    
    
    for char,count in char_characters.items():#defines what were looking for in dict
    
        
        dict_Def={"char":char,"num": count}#creates format for dict
        arrangement.append(dict_Def)#appends dict to list
    arrangement.sort(reverse=True, key=sort_on)#sorts from highest to lowest
        
    return arrangement

      
   
    

