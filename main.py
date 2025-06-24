from stats import get_book_text, split_text,characters_amount
def main():
    
    filepath="books/frankenstein.txt"
    returned_getbook = ( get_book_text(filepath))
    print(get_book_text(filepath))
    
    
    
    print(f"{split_text(returned_getbook)} words found in the document")
    print(characters_amount(returned_getbook))
    
    
    



    
   

if __name__ == "__main__":
    main()


