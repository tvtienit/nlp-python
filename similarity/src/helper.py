import io
import numpy as np

def levenshtein(seq1, seq2):  
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])

def log_w(ctext):
	print('[INFO] ' + ctext, end='\n')

def read_data(filename):
	data = None
	with io.open(filename, 'r', encoding='utf8') as f:
		data = f.readlines()
		f.close()
	return data

def write_data(filename, data):
	with io.open(filename, 'w', encoding='utf8') as f:
		for element in data:
			f.write(element)
		f.close()

def enquiry(arr):
    if not arr:
        return 1
    else:
        return 0
