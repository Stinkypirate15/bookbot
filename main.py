from stats import get_book_text, split_text,characters_amount,sort_characters
def main():
    
    filepath="books/frankenstein.txt"
    returned_getbook = ( get_book_text(filepath))
    print(f"============ BOOKBOT ============\n")
    print(f"Analyzing book found at {filepath}...\n")
    print("----------- Word Count ----------\n")
    #print(get_book_text(filepath))
    print(f"Found {split_text(returned_getbook)} total words\n")
    print("--------- Character Count -------")
    
    #print(characters_amount(returned_getbook))
    sorted_chars = sort_characters(characters_amount(returned_getbook))
    for char_dict in sorted_chars:
         if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
           
        

   
    
    




    
   

if __name__ == "__main__":
    main()


