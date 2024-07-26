#open and read Frankenstein
import string
def main():
    bookpath = "/home/cjiliff/workspace/github.com/CJ-Iliff/bookbot/books/frankenstein.txt"
    text = getbook(bookpath)
    word_count = countwords(text)
    charcount = countchars(text)
    print (f"There are {word_count} words in Frankenstein!")
    print ("---Begin Report of books/frankenstein.txt ---")
    list_dict_charcount = dict_list(charcount)
    sorted_charcount = characteraggregated(list_dict_charcount)
    for key in sorted_charcount:
        character = key["Character"]
        number = key["Number"]
        print (f"The {character} was found {number} times")
    
    

def getbook(path):
    with open(path) as f:
        return f.read()

def countwords(book):
    book_split = book.split()
    wordcount = len(book_split)
    return wordcount

def countchars(book):
    char_dict={}
    #Method is to get the "book" string to lower case -> list out the characters -> sort -> iterate
    lower_book = book.lower()
    char_split = list(lower_book)
    char_split.sort()

    for char in char_split:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] +=1
            else:
                char_dict[char] = 1
    return char_dict

def dict_list(matrix):
    listed_matrix=[]
    for char in matrix:
        dict_row={}
        dict_row["Character"] = char
        dict_row["Number"] = matrix[char]
        listed_matrix.append(dict_row)

    return listed_matrix

def characteraggregated(list):
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["Number"]
   
main()