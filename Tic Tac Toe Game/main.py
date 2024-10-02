def printBoard():
    zero = 'X' if xState[0] else ('O' if yState[0] else 0)
    one = 'X' if xState[1] else ('O' if yState[1] else 1)
    two = 'X' if xState[2] else ('O' if yState[2] else 2)
    three = 'X' if xState[3] else ('O' if yState[3] else 3)
    four = 'X' if xState[4] else ('O' if yState[4] else 4)
    five = 'X' if xState[5] else ('O' if yState[5] else 5)
    six = 'X' if xState[6] else ('O' if yState[6] else 6)
    seven = 'X' if xState[7] else ('O' if yState[7] else 7)
    eight = 'X' if xState[8] else ('O' if yState[8] else 8)
    
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ") 


def win(xState, yState):
    # Winning combinations
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    # Check for X win
    for win in wins:
        if (xState[win[0]] + xState[win[1]] + xState[win[2]] == 3):
            print("X Won the game!")
            return 1
    
    # Check for O win
    for win in wins:
        if (yState[win[0]] + yState[win[1]] + yState[win[2]] == 3):
            print("O Won the game!")
            return 0
    
    # No winner yet
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1

    print("Welcome to Tic Tac Toe game")
    
    while True:
        printBoard()
        if turn == 1:
            print("X's chance")
            value = int(input("Enter a value: "))
            xState[value] = 1
        
        else:
            print("O's chance")
            value = int(input("Enter a value: "))
            yState[value] = 1
        
        pywin = win(xState, yState)
        if pywin != -1:
            print("Game Over!")
            break
        
        turn = 1 - turn

