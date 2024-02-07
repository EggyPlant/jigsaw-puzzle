import random

def connectPieces(piecesConnected, piece1, piece2):
  piecesConnected[piece1] = True
  piecesConnected[piece2] = True



def main():
  solved = False
  steps = 0
  piece1 = 0
  piece2 = 0
  numberOfPieces = 100
  piecesConnected = {}


  while not solved:

    piece1 = random.randint(1,numberOfPieces)
    piece2 = random.randint(1,numberOfPieces)
    while piece2 == piece1:
      piece2 = random.randint(1,numberOfPieces)
      print("piece 2 changed")
  

    if abs(piece1 - piece2) == 1:
      connectPieces(piece1, piece2)

    


    #Find the connecting numbers on piece 1 and 2, and then do mathematical comparissons on those it would be much easier
    
    #If piece 1 and 2 are connected, compare which one is the higher number, and sort through there. 
    # if (piecesConnected[piece1] == True and piecesConnected[piece2] == True):
    #   if piecesConnected[piece1] > piecesConnected[piece2]:
    #     print()
    #   else:
    #     print()

    if (piece1 == (piece2 + 1)) or (piece1 == (piece2 - 1)):
      print('pieces can connect')
      print(piece1)
      print(piece2)
      connectPieces(piecesConnected, piece1, piece2)
      # piecesConnected[piece1] = True
      # piecesConnected[piece2] = True
    
    # if (piecesConnected[piece1] == True) or (piecesConnected[piece2] == True):
    #   piece2 = True

    # if piece2 > piece1:

    #   #start to go down the chain
    #   while piecesConnected[i] != True:
    #     i = piece1 - 1
    #   print()
    # elif piece2 < piece1:
    #   #start to up the chain
  
      #Connect piece1 and 2 and track the numbers
      #What is the best way to track these numbers?
      # piecesConnected[piece1] = True
      # piecesConnected[piece2] = True

      print(piecesConnected[piece1])
      print(piecesConnected[piece2])

    solved = True
    print('This is the number of steps', steps)

    steps += 1

    #while piece2 != piece1 keep picking,
    # but what if we have a long piece 250 - 490 and we keep picking two pieces in those range
    # print(piece1)
    # print(piece2)
    # if steps == 5:
main()
