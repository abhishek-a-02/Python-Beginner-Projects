def sum(a, b, c ):
    return a + b + c

def board(xstate,zstate):  
    zero = 'X' if xstate[0] else ('O' if zstate[0] else "")
    one = 'X' if xstate[1] else ('O' if zstate[1] else " ")
    two = 'X' if xstate[2] else ('O' if zstate[2] else " ")
    three = 'X' if xstate[3] else ('O' if zstate[3] else " ")
    four = 'X' if xstate[4] else ('O' if zstate[4] else " ")
    five = 'X' if xstate[5] else ('O' if zstate[5] else " ")
    six = 'X' if xstate[6] else ('O' if zstate[6] else " ")
    seven = 'X' if xstate[7] else ('O' if zstate[7] else " ")
    eight = 'X' if xstate[8] else ('O' if zstate[8] else " ")

    print(f"{zero}  | {one} | {two} ") 
    print("--|---|---")
    print(f"{three} | {four} | {five} ")  
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ")  

def checkwin(xstate,zstate) : 
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
    for win in wins: 
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):   
            print('X WON THE MATCH!')
            return 1 
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):   
            print('O WON THE MATCH!')
            return 0 
    return -1
               
    
xstate = [0,0,0,0,0,0,0,0,0] 
zstate = [0,0,0,0,0,0,0,0,0] 
turn = 1
print("WELCOME TO TIC TAC TOE! ") 
while True:   
    board(xstate,zstate)
    if(turn==1): 
        print("X's chance") 
        value= int( input("Please enter a value: ")) 
        xstate[value]=1 
    else: 
        print("O's chance") 
        value= int(input("Please enter a value: ")) 
        zstate[value]=1 
    cwin= checkwin(xstate , zstate)
    turn = 1 - turn
    if(cwin != -1): 
        print("MATCH OVER")
        break