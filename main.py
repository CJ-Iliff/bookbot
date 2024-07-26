#open and read Frankenstein
import string
def main():
    charcount={}
    bookpath = "/home/cjiliff/workspace/github.com/CJ-Iliff/bookbot/books/frankenstein.txt"
    text = getbook(bookpath)
    word_count = countwords(text)
    charcount = countchars(text)
    print (f"There are {word_count} words in Frankenstein!")
    print ("The character breakdown is as follows:")
    print (charcount)

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
  
main()