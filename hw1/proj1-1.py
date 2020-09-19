'''
Class: CPSC 475-01
Team Member 1: Jason Lunder
Submitted By: Jason Lunder
GU Username: jlunder
File Name: proj1-1.py
Program counts the number of instances of a substring within a string,
Using a user inputted substring and the contents of a user specified
file as the string to search.
To Build and Execute: python proj1-1.py (or python3 proj1-1.py)
'''

import sys

def main():
  # Open a file and save its content as a string
  openedFile = openFile()
  fileAsString = readFileString(openedFile)

  # Get a substring from the user and count how many times
  # it appears in the string saved previously
  substring = input("Enter a substring: ")
  instances = countInstances(fileAsString, substring)
  
  print(instances)

'''
Pre: No preconditions, happens at the very beginning of the program
Post: outputs a variable containing the opened file
'''
def openFile():
  while(True):
    fileIn = input("Enter a filename: ")
    try:
      fileIn = open(fileIn, 'r')
      break
    except:
      print("Invalid file: Does not exist.")
  return fileIn

'''
Pre: fileIn contains a opened file
Post: outputs a variable containing the content of the file as a string
'''
def readFileString(fileIn):
  return fileIn.read()

'''
Pre: text contains the content of a file as a string,
     sub is the substring to be searched for within text
Post: outputs a variable containing the number of instances
     of sub within text
'''
def countInstances(text, sub):
  count = 0
  subLength = len(sub)

  # loops from 0 to the index at which there is only len(sub)
  # characters left in text before the end of text
  for i in range(len(text)-subLength):
    
    # increments the counter if the segment of text starting at i
    # and extending for the length of the substring is the same
    # content as the substring
    if text[i:i+subLength] == sub:
      count += 1
  return count

main()
