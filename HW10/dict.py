# Description: This program print word occurences in a long list
# Name: Cupic, Aleksej
# Date: 12.4.2019

def read_word_list():
    davidC=open('ENGLISH_LIT.txt','r') # use short for debug
    print('OPEN')
    book=davidC.read()
    print('DONE')
    return book.split()

def build_dictionary(book):
    davidDict={}
    for i in range(0,len(book)):
        if book[i] in davidDict:
            davidDict[book[i]]+=1
        else:
            davidDict[book[i]]=1
    return davidDict

def most_frequent(dict_book,frequency_limit):
    tuple_list=[]
    for i in dict_book:
        if dict_book[i]>=frequency_limit:
            tuple_list.append((dict_book[i],i))
    tuple_list.sort(reverse=True)
    return tuple_list


#main

print('\n This programs prints word occurrences in a long list \n')
book=read_word_list()
print('FILE READ')
#print(book)

dict_book=build_dictionary(book)
print('DICTIONARY CREATED')
#print(dict_book)
print('There are ',len(dict_book),' distinct words.')
frequency_limit=int(input('Enter freq: '))
tuple_list=most_frequent(dict_book,frequency_limit)
print('TUPLE LIST')
print(tuple_list)

