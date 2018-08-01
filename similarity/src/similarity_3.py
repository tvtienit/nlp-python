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
    print (matrix)
    return (matrix[size_x - 1, size_y - 1])
print(levenshtein("Harry ran all the way to the south room to find the invisibility cloak and map of the bandits in the chest ; It made it so fast that Ron and Ron were ready to go for at least five minutes to see Hermione return from the girl's bedroom after wrapping the towel , wearing gloves and carrying one of the capped caps .","Harry sprinted up to the boys'dormitories to fetch the Invisibility Cloak and the Marauder's Map from his trunk ; he was so quick that he and Ron were ready to leave at least five minutes before Hermione hurried back down from the girls'dormitories , wearing scarf , gloves and one of her own knobbly elf hats ."))