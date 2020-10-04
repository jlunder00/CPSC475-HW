'''
Class: CPSC 475-01
Team Member 1: Jason Lunder
Submitted By: Jason Lunder
GU Username: jlunder
File Name: proj2-3.py
Program tokenizes/normalizes a corpus generated from all the text files in a user specified directory
according to a user specified method, then plots the log(rank) vs the log(frequency) of the elements in the corpus
To Build and Execute: python proj2-3.py </directory name> <1-4> or python3 proj2-3.py </directory name> <1-4>
(If your PATH and python bin are set up so python maps to python2, this program must be run with a version of python 3)
'''

import matplotlib.pyplot as plt
import string
import sys
from nltk.tokenize import word_tokenize
import porter
import math
import os
import re

'''
Pre: The name for a directory containing text files
Post: A list of all of the text files in that directory
'''
def collectFileNames(directoryName):
  targetDirectory = os.getcwd()+directoryName
  return [fileName.path for fileName in os.scandir(targetDirectory) if fileName.path.endswith('.txt')]
  
'''
Pre: A list of all the text files in a directory that are to be concatenated together into one file
Post: All of the files contents written to a single file, concatenated together. Returned is a the name of this file
'''
def writeManyToOne(filePaths, outputFile='BSC.txt'):
  fout = open(outputFile, 'w')
  for path in filePaths:
    fin = open(path, 'r')
    fout.writelines(fin.readlines())
  fout.close()
  return outputFile 

'''
Pre: A filename as a string indicating which file to read from
Post: a string contianing the data in the file specified as a string
Opens the indicated file, reads the data into the string, then closes the file before returning
'''
def readData(fileName):
  fin = open(fileName, 'r')
    
  corpusAsString = fin.read()  #read in text as a string
  fin.close()
  return corpusAsString

'''
Pre: An untokenized or normalized string corpus
Post: a list containing all of the elements of the corpus, as seperated by whitespaces
'''
def basicTokenize(corpusString):
  return corpusString.split()

'''
Pre: An untokenized and unnormalized string corpus
Post: A list containing all of the elements of the corpus, as found and seperated using the nltk word_tokenize(string) function
'''
def NLTKTokenizeNormalize(corpusString):
  return word_tokenize(corpusString)

'''
Pre: An untokenized and unnormalized string corpus
Post: a list containing all of the elements of the corpus, as found, seperated, and normalized using the porter stemmer for tokenizing and normalization
'''
def porterTokenizer(corpusString):
  p = porter.PorterStemmer()
  output = ''
  word = ''
  lines = corpusString.split('\n')
  for line in lines:
    for c in line:
      if c.isalpha():
        word += c.lower()
      else:
        if word:
          output += p.stem(word, 0,len(word)-1)
          word = ''
        output += c.lower()
  return output.split()

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
def bestTokenizer(corpusString):

  #find all the non-ascii characters
  nonAsciiDict = {ord(ch) : ch for ch in corpusString if ord(ch) > 127}
  nonAscii = ''.join(list(nonAsciiDict.values()))

  #characters to be removed from the corpusString
  remove = string.digits + string.punctuation + nonAscii

  remove = remove.replace('<', '')
  remove = remove.replace('>', '')
    
  #replace each character to be removed with a blank space
  #first create a list of the same length as remove filled with spaces
  blank = ''.join([' ' for ch in remove])
    
  #make a table to use translate with which replaces each character in remove found in 
  #the string being translated with the corresponding character in blank
  table = str.maketrans(remove, blank)
    
  #use transate to replace chars from remove that existin corpusString with spaces
  corpusString = corpusString.translate(table)
    
  #split on the whitespace
  wordList = corpusString.split()

  #Remove empty words from the list. length of None is 0
  wordList = [word for word in wordList if len(word) > 0]
  
  wordList = [word.lower() for word in wordList]

  wordList = [word for word in wordList if re.search('<', word) == None and re.search('>', word) == None]
  
  #Remove invalid single letter words from list:
  wordList = [word for word in wordList if len(word) > 1 or
                      word == 'i' or word == 'a']

  return wordList


'''
Pre: A tokenized and normalized list of the elements in a corpus
Post: A dictionary contianing unique keys that are each element of the corpus, mapped to the number
    of instances of that element
'''
def getCounts(wordList):
  wordDict = {}
  for word in wordList:
    if word in wordDict:
      wordDict[word] = wordDict[word] + 1
    else:
      wordDict[word] = 1
  return wordDict

def main():
  dirName = sys.argv[1]
  
  while dirName[0] != '/':
    dirName = input('Please enter a directory name. Make sure that a \'/\' precedes it: ')

  fname = writeManyToOne(collectFileNames(dirName))

  text = readData(fname)
  tokenizer = int(sys.argv[2])
    
  wordList = []
  if tokenizer == 1:
    wordList = basicTokenize(text)
  elif tokenizer == 2:
    wordList = NLTKTokenizeNormalize(text)
  elif tokenizer == 3:
    wordList = porterTokenizer(text)
  elif tokenizer == 4:
    wordList = bestTokenizer(text)

  #map elements of a corpus to their frequency
  frequencies = getCounts(wordList)

  #sort the dictionary in reverse order so the highest frequency comes first
  frequencies = {key: value for key, value in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}
    
  i = 1
  rankAndFrequency = {}

  #map the rank to the frequency in a new dictionary, starting at 1
  for value in frequencies.values():
    rankAndFrequency[i] = value
    i += 1

  x = []
  y = []
  #adds the key of the rank and frequency dictionary to x and the number of instances to y,
  #but with the distinction that the natural log of x is added for x and the natural log of y is added for y
  for key, value in rankAndFrequency.items():
    x.append(math.log(key))
    y.append(math.log(value))
    
  #plot the log log graph of rank vs frequency
  plt.plot(x,y)
  plt.show()

  outName = 'output'+str(tokenizer)
  fout = open(outName, 'w')
  fout.write(" ".join(wordList))




main()
