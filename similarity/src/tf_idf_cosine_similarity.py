import tensorflow as tf
import collections
import zipfile
import numpy as np
import math
# https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/
def read_data(filename):
    """Extract the first file enclosed in a zip file as a list of words."""
    with zipfile.ZipFile(filename) as f:
        data = tf.compat.as_str(f.read(f.namelist()[0])).split()
    return data

def counter(vocabularys,vocabulary_size=500000):
    words = []
    words.extend(collections.Counter(vocabularys).most_common(vocabulary_size - 1))
    return words

def getAllVocab(filePath,vocabulary_size=50000):
    vocabularys = read_data(filePath)
    dictionary = dict()
    words = counter(vocabularys)
    for word, _ in words:
      dictionary[word] = 0
    return dictionary

def calTF(filePathDic,filePathIDF):
    dicVocab = getAllVocab(filePathDic)
    countDocument = 0
    with open(filePathIDF, encoding='utf-8') as f:
      for line in f:
          words = list(set(tf.compat.as_str(line).split()))
          for word in words:
              dicVocab[word] = dicVocab[word] + 1
          countDocument+=1
    return dicVocab,countDocument

def calDicIDF(zipPath,dataPath):
    dicTF,countDocument = calTF(zipPath,dataPath)
    dicIDF = dict()
    for word in dicTF.keys():
        dicIDF[word] = 1 +  np.log(countDocument/dicTF[word])
    return dicIDF

def tryDic(dictionary,key):
  try:
    return dictionary[key]
  except:
    return 0

def tfSentence(setence):
  dicTF = dict()
  words = setence.split()
  size = len(words)
  freqWords = counter(words)
  for word, freqWord in freqWords:
    dicTF[word] = freqWord/size
  return dicTF

def dotProduct(query,document,idf):
    tfQuery = tfSentence(query)
    tfDocument = tfSentence(document)
    wordsQuery = query.split(" ")
    dotProduct = 0
    for word in wordsQuery:
        idfWord = tryDic(idf,word)
        dotProduct += (tfQuery[word] * idfWord * tryDic(tfDocument,word) * idfWord)
    return dotProduct

def sqrQuery(query,idf):
  tfQuery = tfSentence(query)
  wordsQuery = query.split(" ")
  sqr_query = 0
  for word in wordsQuery:
    idfWord = tryDic(idf,word)
    tf_idf = tfQuery[word] * idfWord
    sqr_query +=  tf_idf * tf_idf
  return math.sqrt(sqr_query)

def sqrDocument(query,document,idf):
  tfDocument = tfSentence(document)
  wordsQuery = query.split(" ")
  sqr_document = 0
  for word in wordsQuery:
    idfWord = tryDic(idf,word)
    tfWord = tryDic(tfDocument,word)
    sqr_document += (tfWord * idfWord ) * (tfWord * idfWord )
  return math.sqrt(sqr_document)

def CosineSimilarity(query,document,idf):
    query = query.strip()
    document= document.strip()
    under = ( sqrQuery(query,idf)* sqrDocument(query,document,idf)) 
    if under <= 0:
       return 0
    return dotProduct(query,document,idf) / under 

