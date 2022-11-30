# CREATE GAMEBOARD / INITIAL REPRESENTATION OF THE WORLD
    # 0 empty cell, 1 inhabitant 

# CHECK IF NEIGHBOR IS IN ARRAY / BORDER
    # check horizontally
    # check vertically 
    # check diagonally 

# ASSIGN NEW VALUES 
    
# CREATE DENSITY MAP 




# 1. this are our given values of the initial representation of the world; 0= empty cell; 1= inhabitant
# this is the input board
board= [
    ["0" ,"1" ,"0" ],
    ["0" ,"1" ,"0" ],
    ["0", "1", "0"]    
]
# this is the outpot board / heatmap 
board2= [
    ["-" ,"-" ,"-" ],
    ["-" ,"-" ,"-" ],
    ["-", "-", "-"]    
]

# 2. Try to make a graphic interface "lookalike", (vertical lines done with alt + 7) 
def printBoard():
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---------")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---------")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])



# 3. Check for neighbors

def checkneighbors(row, col):
    # check above 
    count = 0 
    if row - 1 >= 0 and board[row -1][col] == "1":
        board2[row][col] = count + 1 
       
    # check below 
    if row +1 <= 2 and board[row +1][col] == "1":
        board2[row][col] = count + 1
        
    # check left 
    if col - 1 >= 0 and board[row][col -1] == "1":
        board2[row][col] = count + 1 
    
    # check right 
    if col + 1 >= 2 and board[row][col + 1] == "1":
        board2[row][col] = count + 1 
    
    #check diagonal up right 
    if col +1 <=2 and board[row +1][col] <=2 == "1":
        board2[row][col] = count + 1  
    
    #check diagonal up left
    if col -1 >= 0 and board[row +1][col] <=2 == "1": 
        board2[row][col] = count + 1  
        
    #check diagonal down right  
    if col +1 <= 2 and board[row + 1][col] <=2 == "1":
        board2[row][col] = count +1 
    
    # check diagonal down left 
    if col -1 >= 0 and board[row + 1][col] <= 2 == "1":
        board2[row][col] = count + 1 



#MASTERFUNCTION
checkneighbors(0,0) #-> here loop / . 2 loops to right/left and down 
printBoard(board2)


#loop outside 
#for i in x 





    