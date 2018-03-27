#The tic tac toe board
import random

board  =  [0,1,2,
            3,4,5,
            6,7,8]

#show function to format the board

def show():
    
    
    print(board[0], board[1], board[2])
    
    print(board[3], board[4], board[5])

    print(board[6], board[7], board[8])
    print() 
show()


while True:

        input = raw_input('select a spot:')
        input = int(input)

if board[input] != 'x' and board[input] = !'o':
     board[input] = 'x'

     random.seed()  #gives a random generator
     opponent = random.randint = (0,8)

            else:
                print 'This spot is taken'
                show()
    