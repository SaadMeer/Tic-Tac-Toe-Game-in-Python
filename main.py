def printTable(xAxis, yAxis):
    zero = 'X' if xAxis[0] else('O' if yAxis[0] else 0)
    one = 'X' if xAxis[1] else('O' if yAxis[1] else 1)
    two = 'X' if xAxis[2] else('O' if yAxis[2] else 2)
    three = 'X' if xAxis[3] else('O' if yAxis[3] else 3)
    four = 'X' if xAxis[4] else('O' if yAxis[4] else 4)
    five = 'X' if xAxis[5] else('O' if yAxis[5] else 5)
    six = 'X' if xAxis[6] else('O' if yAxis[6] else 6)
    seven = 'X' if xAxis[7] else('O' if yAxis[7] else 7)
    eight = 'X' if xAxis[8] else('O' if yAxis[8] else 8)
    
    print(f" {zero}  | {one} |  {two}  ")
    print(f" ---|---|--- ")
    print(f" {three}  | {four} |  {five}  ")
    print(f" ---|---|--- ")
    print(f" {six}  | {seven} |  {eight}  ")

def sum(a,b,c):
    return a + b + c;    

def checkWin(xAxis, yAxis):
    winner = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],
              [2,5,8],[0,4,8],[2,4,6]]
    for win in winner:
        if(sum(xAxis[win[0]], xAxis[win[1]], xAxis[win[2]]) == 3):
            print("X Won the Game")
            return 1
        if(sum(yAxis[win[0]], yAxis[win[1]], yAxis[win[2]]) == 3):
            print("O Won the Game")
            return 0
    return -1


if __name__ == "__main__": 
    xAxis = [0,0,0,0,0,0,0,0,0]
    yAxis = [0,0,0,0,0,0,0,0,0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while(True):
        printTable(xAxis, yAxis)
        if(turn == 1):
            print("Player X Chance")
            value = int(input("Please Enter X Position: "))
            xAxis[value] = 1
        else:
            print("Player O Chance")
            value = int(input("Please Enter O Position: "))
            yAxis[value] = 1
            
        winner = checkWin(xAxis, yAxis)
        if(winner != -1):
            print("Match Over")
            break
        
        turn = 1 - turn
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        