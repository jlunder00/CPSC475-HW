'''
Class: CPSC 475-01
Team Member 1: Jason Lunder
Submitted By: Jason Lunder
GU Username: jlunder
File Name: nlpUtils.py
Program contains functions to be used in a driver program. These can read a corpus from a passed filename line by line and return a list of lines,
take a list of lines and tokenize it, returning a list of tokenized lines
take a list of lines and a ngram size and develop and return a flattened list of all the ngrams in the sentence list
To use: import nlpUtils in a driver program. This should be run with python3
'''

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


'''
Pre: A filename as a string indicating which file to read from
Post: a string contianing the data in the file specified as a string
Opens the indicated file, reads the data into the string, then closes the file before returning
'''
def getData(fileName):
  fin = open(fileName, 'r')
  
  corpusList = fin.readlines() #read in text as a string

  fin.close()
  
  return corpusList

'''
Pre: An untokenized and unnormalized string corpus
Post: A list containing all of the elements of the corpus, as found, seperated, and filtered using various techniques:
    first, all non ascii numbers are found, and are concatenated with all of the digits and punctuation possible
    in a string. Then a list of blank whitespace elements of the same length as the previously created
    string is created. These are used to replace all of the instances of an invalid character for our
    normalization with whitespace. Then, the string is split along whitespace into a list
    This list is processed to be made lowercase, remove all empty indexes and all indexes contianing single letters
    that are neither 'a' nor 'i'. Also removes all words containing < or >
'''
def tokenize(corpusList):
  corpusList = [line for line in corpusList if line[0] != '\n']
  corpusList = [line.strip() for line in corpusList]
  corpusList = ["<s> "+line[0:len(line)-1]+" </s> " for line in corpusList]
  corpusList = [''.join([c for c in line if ord(c) < 127 and c != '\n']) for line in corpusList]
  return corpusList

"""
Pre: a list of the sentences in the corpus that has been tokenized
Post: a list of the words in the corpus divided into ngrams
"""
def make_grams(sent_lst, gram_size):
  #print([sent for sent in sent_lst])
  unflattenedList = [[sent.split(" ")[wordIndex+i] for i in range(0, gram_size)] for sent in sent_lst for wordIndex in range(0, len(sent.split(" "))-int(gram_size))]
  flattenedList = [nGram[i] for nGram in unflattenedList for i in range(0, gram_size)]
  return flattenedList

def getFreq(ngrams):
    dictionary = {}
    for w in ngrams:
        if w in dictionary:
            dictionary[w] = dictionary[w]+1
        else:
            dictionary[w] = 1
    return dictionary

def lemmatize(word):
    return WordNetLemmatizer().lemmatize(word)
