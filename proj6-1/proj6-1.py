import sys
import nltk
import pandas as pd
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import cdist
from scipy.stats import zscore
from sklearn import preprocessing
import nlpUtils as nlp




'''
Pre: A filename as a string indicating which file to read from
Post: a string contianing the data in the file specified as a string
Opens the indicated file, reads the data into the string, then closes the file before returning
'''
def get_data(fileName):
  fin = open(fileName, 'r')
  
  corpusList = fin.readlines() #read in text as a string

  fin.close()
  
  return corpusList

def getWordsToDelete():
    wordsToDelete = []
    wordsToDelete = stopwords.words("english")
    wordsToDelete.append('<s>')
    wordsToDelete.append('</s>')
    wordsToDelete.append('')
    wordsToDelete.append('-')
    return wordsToDelete

def lemmatization(tokenizedSentences, wordsToDelete):
    newSentences = []
    vocabulary = []
    for sentence in tokenizedSentences:
        newSentence = ''
        sentence = sentence.split()
        for word in sentence:
            if word not in wordsToDelete:
                word = nlp.lemmatize(word)
                if(word != ''):
                    vocabulary.append(word[:-1])
                    newSentence = newSentence+word+' '
        if(newSentence != ''):
            newSentences.append(newSentence[:-1])
    vocabulary = list(set(vocabulary))[1:-1]
    return vocabulary, newSentences

def tfidf_vectorize(doc1, doc2):
    doc1 = ' '.join(doc1)
    doc2 = ' '.join(doc2)

    vectorize = TfidfVectorizer()
    vectors = vectorize.fit_transform([doc1, doc2])
    return pd.DataFrame(vectors.todense().tolist(), columns=vectorize.get_feature_names())
  
def createFinalDictionary(words, vocabulary, ngrams):
    finalDictionary = {}
    print("words:\n\n\n")
    print(words)
    print("vocabulary:\n\n\n")
    print(vocabulary)
    for word in words:
        for w in vocabulary:
           finalDictionary[word] = {}

    for word in words:
        for w in vocabulary:
            finalDictionary[word][w] = 0
    print(finalDictionary)
    print("Creating Final Dict")
    for ngram in ngrams:
        ngram = ngram.split()
        for word in ngram:
            if word in words:
                for w in vocabulary:
                    if w in ngram:
                        print("word: "+word)
                        print("w: "+w)
                        finalDictionary[word][w] = finalDictionary[word][w]+1
    return finalDictionary

def vectorization(finalDictionary, words, vocabulary):
    vectorList = []
    for word in words:
        vec = []
        for w in vocabulary:
            vec.append(finalDictionary[word][w])
        vectorList.append(vec)
    return vectorList

"""
Pre: a list of the sentences in the corpus that has been tokenized
Post: a list of the words in the corpus divided into ngrams
"""
def make_grams(sent_lst, gram_size):
  return [[sent.split(" ")[wordIndex+i] for i in range(0, gram_size)] for sent in sent_lst for wordIndex in range(0, len(sent.split(" "))-int(gram_size))]

def main():
    data = nlp.tokenize(nlp.getData(sys.argv[1]))

    document1 = data[:int(len(data)/2)]
    document2 = data[int(len(data)/2):]

    wordsToDelete = getWordsToDelete()

    vocabulary1, document1 = lemmatization(document1, wordsToDelete)
    vocabulary2, document2 = lemmatization(document2, wordsToDelete)
    newData = document1+document2
    vocabulary = set(vocabulary1+vocabulary2)

    documentFrequency = tfidf_vectorize(document1,document2)

    documentFrequency = documentFrequency[documentFrequency>0]
    documentFrequency.dropna(axis=1,inplace=True)

    words = documentFrequency.sum().sort_values(ascending=False).head(20).index

    grams = nlp.make_grams(newData,4)
    finalDictionary = createFinalDictionary(words,vocabulary, grams)
    vectorDictionary = vectorization(finalDictionary, words, vocabulary)

    distances = cdist(vectorDictionary, vectorDictionary, metric='euclidean')

    docFreq = pd.DataFrame(data=distances, index=words, columns=words)

    x = docFreq.values #returns a numpy array
    print(x)
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    docFreq = pd.DataFrame(x_scaled,index=words, columns=words)
    docFreq.to_csv(r'./data.csv')

main()
