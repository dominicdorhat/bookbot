def open_book(path):
    with open(path) as book:
        return book.read()

def count_words(contents):
    text = contents.split()        
    return len(text)

def count_letters(contents):
    letter_count = {}

    # Create new dictionary based on the letter count
    for letter in contents:
        lowered_letter = letter.lower()
        if lowered_letter in letter_count:
            letter_count[lowered_letter] += 1
        else:
            letter_count[lowered_letter] = 1
            
    return letter_count

def generate_report(path, book, letter_count):    
    letter_list = []

    for letter in letter_count:
        if letter.isalpha():
            letter_list.append({'letter': letter, 'count': letter_count[letter]})

    # lambda returns the value of 'count', telling sort() to sort by value of the dict
    letter_list.sort(reverse=True, key=lambda letter: letter['count'])

    # Report generation
    print(f"--- Begin report of {path[1:]} ---")
    print(f"{count_words(book)} words found in the document\n")
    for item in letter_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print("--- End report ---")

# ==============================================================================================================================================        

def main():
    path_to_book = "./books/frankenstein.txt"
    book = open_book(path_to_book)        
    generate_report(path_to_book, book, count_letters(book))

main()