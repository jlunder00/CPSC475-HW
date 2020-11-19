'''
Class: CPSC 475-01
Team Member 1: Jason Lunder
Submitted By: Jason Lunder
GU Username: jlunder
File Name: proj3-1.py
Program uses nlpUtils to generate a list of ngrams of user specified size from a user specified file that contains a corpus
nd prints out the ngrams generated from that corpus, as many ngrams as specified by the user in an organized manner
To Build and Execute: python proj2-3.py </directory name> <1-4> or python3 proj3-1.py <filename> <number greater than 1> <number of grams to display>
Be careful not to exceed the number of ngrams you can display given the size of ngrams youre choosing and the length of your corpus
(If your PATH and python bin are set up so python maps to python2, this program must be run with a version of python 3)
'''


import nlpUtils
import sys

def display(fname, gram_size, num_grams):
    grams = nlpUtils.make_grams(nlpUtils.tokenize(nlpUtils.get_data(fname)), gram_size)
    #print(grams)
    for i in range(0, len(grams)-gram_size, gram_size):
      print(', '.join([grams[i+j] for j in range(0, gram_size)]))

    #print(''.join([''.join([grams[i+j*gram_size] for i in range(0, gram_size)])+'\n' for j in range(0, num_grams)]))

def main():
    fname = sys.argv[1]
    gram_size = int(sys.argv[2])
    num_grams = int(sys.argv[3])
    display(fname, gram_size, num_grams)

main()
