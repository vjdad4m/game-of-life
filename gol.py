import time

def print_board(board):
    for e in board:
        for f in e:
            print(f, end=" ")
        print()

def get_neighbour_count(board,y,x):
    c = 0
    for a in range(y-1,y+2,1):
        for b in range(x-1,x+2,1):
            if not (a==y and b==x):
                try:
                    if board[a][b] == 1:
                        c+=1
                except: pass
    return c

def should_change(state, neighbours):
    if state == 1:
        if n < 2:
            return True
        if n == 2 or n == 3:
            return False
        if n > 3:
            return True
    else:
        if n == 3:
            return True
    return False

def change(board, lst):
    for e in lst:
        tmp = board[e[0]][e[1]]
        if tmp == 1:
            board[e[0]][e[1]] = 0
        else:
            board[e[0]][e[1]] = 1
    return board

def game_over(board):
    if sum(x.count(0) for x in board) == len(board)*len(board[0]):
        return True
    return False

if __name__ == '__main__':
    board= [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0],
            [0,0,0,0,1,0,0,1,0,0],
            [0,0,0,0,1,1,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    
    h = len(board)
    w = len(board[0])

    while not game_over(board):
        print('--'*w)
        print_board(board)
        change_lst = []
        for y in range(h):
            for x in range(w):
                n = get_neighbour_count(board,y,x)
                if should_change(board[y][x],n):
                    change_lst.append([y,x])
        board = change(board, change_lst)
        time.sleep(0.5)

    print_board(board)