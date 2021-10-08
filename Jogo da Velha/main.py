# Prints board
def print_screen(m):
    print('{}|{}|{}'.format(m[0][0], m[0][1], m[0][2]))
    print('------')
    print('{}|{}|{}'.format(m[1][0], m[1][1], m[1][2]))
    print('------')
    print('{}|{}|{}'.format(m[2][0], m[2][1], m[2][2]))


# Modifies the board
def ask_question(player):
    if player == 'p1':
        print('PLAYER 1:')
        print('Type row :')
        row = int(input())
        print('Type column :')
        column = int(input())
        if space_ocupied(row, column):
            print('Space ocuppied')
            print('Try again')
            won = False
            return True, won
        else:
            m[row - 1][column - 1] = 'x'
            won = checks_win(row, column)
            return False, won
    else:
        print('PLAYER 2')
        print('Type row :')
        row = int(input())
        print('Type column :')
        column = int(input())
        if space_ocupied(row, column):
            print('Space ocuppied')
            print('Try again')
            won = False
            return True,won
        else:
            m[row - 1][column - 1] = 'o'
            won = checks_win(row, column)
            return False, won


# Checks if space is already ocuppied
def space_ocupied(row, column):
    if m[row - 1][column - 1] == ' ':
        return False
    else:
        return True


def checks_win(row, column):
    goal = m[row - 1][column - 1]
    if checks_line(row, goal) or checks_columns(column, goal):
        return True
    elif row == column:
        if checks_diag1(goal):
            return True
        else:
            return False
    elif abs(row - column) == 2 or (row == 2 and column == 2):
        if checks_diag2(goal):
            return True
        else:
            return False
    else:
        return False


def checks_line(row, goal):
    equals = True
    for i in range(1, 4):
        if m[row - 1][i - 1] != goal:
            equals = False
    return equals


def checks_columns(column, goal):
    equals = True
    for i in range(1, 4):
        if m[i - 1][column - 1] != goal:
            equals = False
    return equals


def checks_diag1(goal):
    equals = True
    for i in range(1, 4):
        if m[i - 1][i - 1] != goal:
            equals = False
    return equals


def checks_diag2(goal):
    equals = True
    for i in range(1, 4):
        if m[3 - i][i - 1] != goal:
            equals = False
    return equals


# Starts clean board
m = [[' ' for x in range(3)] for y in range(3)]
i = 1
won = False
# Alternate between players
while i < 10 and won == False:
    try_again = True
    if i % 2 == 1:
        player = 'p1'
    else:
        player = 'p2'
    while try_again:
        try_again, won = ask_question(player)
    i += 1
    print_screen(m)
print('End of Game')
if player == 'p1':
    print('Player 1 wins')
else :
    print('Player 2 wins')