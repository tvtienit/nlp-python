import numpy as np
import re, math
from collections import Counter
WORD = re.compile(r'\w+')
from sklearn.metrics.pairwise import cosine_similarity

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def calculator(setence_1,setence_2):
    input_1 = text_to_vector(setence_1)
    input_2 = text_to_vector(setence_2)
    #tf df .. 
    # cosine simitary. <- 
    cosine = get_cosine(input_1,input_2)
    return cosine

