import numpy as np
import random

numberOfPieces = int(input("How many puzzle pieces are there? "))

pieces = np.array(list(range(1,numberOfPieces +1)))
attempts = 0

while pieces.size > 1:
    attempts = attempts + 1
    piece1 = random.randint(0, pieces.size - 1)
    piece2 = random.randint(0, pieces.size - 1)
    while (piece2 == piece1):
        piece2 = random.randint(0, pieces.size - 1)
    if (abs(piece2 - piece1) == 1):
        pieces = np.delete(pieces, piece2, 0)
        print("Step:", attempts)
        print(np.transpose(pieces))
print(attempts)