def move_piece_right(to_button, from_button):
    from view.Board import BoardWidget
    to_button.setText(from_button.text()) 
    to_button.setProperty('color', from_button.property('color'))
    to_button.setProperty('piece_type', from_button.property('piece_type'))
    from_button.setText("") 
    from_button.setProperty('color', None)
    from_button.setProperty('piece_type', None)
    if BoardWidget.current_color == 'white':
        BoardWidget.current_color = 'black'
    else:
        BoardWidget.current_color = 'white'

def catch_piece(to_button, from_button):
    print("захват!")
    return None

def logic_pawn(color, from_pos, to_pos, from_button, to_button):
    if(color == 'white'):
        if from_pos[0] == 6 and (to_pos[0] == 5 or to_pos[0] == 4):
            print(to_button.text(), to_pos[1] == from_pos[1] + 1, to_pos[1] == from_pos[1] - 1)
            if to_button.text() and (to_pos[1] == from_pos[1] + 1 or to_pos[1] == from_pos[1] - 1):
                catch_piece(to_button, from_button)
            elif(to_pos[1] == from_pos[1]) and not to_button.text():
                move_piece_right(to_button, from_button)
        elif(to_pos[0] == from_pos[0]-1):
            if not to_button.text() and to_pos[1] == from_pos[1]:
                move_piece_right(to_button, from_button)
            elif to_button.text() and (to_pos[1] == from_pos[1] + 1 or to_pos[1] == from_pos[1] - 1):
                catch_piece(to_button, from_button)
    else:
        if from_pos[0] == 1 and (to_pos[0] == 2 or to_pos[0] == 3):
            if to_button.text() and (to_pos[1] == from_pos[1] + 1 or to_pos[1] == from_pos[1] - 1):
                catch_piece(to_button, from_button)
            elif(to_pos[1] == from_pos[1]) and not to_button.text():
                move_piece_right(to_button, from_button)
        elif(to_pos[0] == from_pos[0]+1):
            if not to_button.text() and to_pos[1] == from_pos[1]:
                move_piece_right(to_button, from_button)
            elif to_button.text() and (to_pos[1] == from_pos[1] + 1 or to_pos[1] == from_pos[1] - 1):
                catch_piece(to_button, from_button)
    return None

def logic_king(from_pos, to_pos, from_button, to_button):
    from view.Board import BoardWidget
    if (to_pos[0] == from_pos[0]+1 or to_pos[0] == from_pos[0]-1 or to_pos[0] == from_pos[0]) and (to_pos[1] == from_pos[1]+1 or to_pos[1] == from_pos[1]-1 or to_pos[1] == from_pos[1]):
        if not to_button.text():
            move_piece_right(to_button, from_button)
        elif to_button.text() and to_button.property('color') != BoardWidget.current_color:
            catch_piece(to_button, from_button)
    return None

def logic_knight(from_pos, to_pos, from_button, to_button):
    from view.Board import BoardWidget
    if (to_pos[0] == from_pos[0]+2 and (to_pos[1] == from_pos[1]+1 or to_pos[1] == from_pos[1]-1)) or (to_pos[0] == from_pos[0]-2 and (to_pos[1] == from_pos[1]+1 or to_pos[1] == from_pos[1]-1)) or (to_pos[0] == from_pos[0]+1 and (to_pos[1] == from_pos[1]+2 or to_pos[1] == from_pos[1]-2)) or (to_pos[0] == from_pos[0]-1 and (to_pos[1] == from_pos[1]+2 or to_pos[1] == from_pos[1]-2)):
        if not to_button.text():
            move_piece_right(to_button, from_button)
        elif to_button.text() and to_button.property('color') != BoardWidget.current_color:
            catch_piece(to_button, from_button)
    return None

# ПОЧИНИТЬ
def logic_rook(from_pos, to_pos, from_button, to_button, board):
    if(to_pos[0] == from_pos[0] and to_pos[1] > from_pos[1]):
        for step in range(1, to_pos[1]-from_pos[1]+1):
            current_pos = (from_pos[0], from_pos[1]+step)
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break

    elif(to_pos[1] == from_pos[1] and to_pos[0] < from_pos[0]):
        for step in range(1, from_pos[0]-to_pos[0]+1):
            current_pos = (from_pos[0]-step, from_pos[1])
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break

    elif(to_pos[0] == from_pos[0] and to_pos[1] < from_pos[1]):
        for step in range(1, from_pos[1]-to_pos[1]+1):
            current_pos = (from_pos[0], from_pos[1]-step)
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break
            
    elif(to_pos[1] == from_pos[1] and to_pos[0] > from_pos[0]):
        for step in range(1, to_pos[0]-from_pos[0]+1):
            current_pos = (from_pos[0]+step, from_pos[1])
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break


def validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
    if square.text():
        if current_pos[0] == to_pos[0] and current_pos[1] == to_pos[1] and square.property('color') != from_button.property('color'):
            catch_piece(to_button, from_button)
        return False
    if not square.text():
        if current_pos[0] == to_pos[0] and current_pos[1] == to_pos[1]:
            move_piece_right(to_button, from_button)
        return True
    
def logic_bishop(from_pos, to_pos, from_button, to_button, board):
    if(to_pos[0] < from_pos[0] and to_pos[1] > from_pos[1]):
        for step in range(1, from_pos[0]-to_pos[0]+1):
            current_pos = (from_pos[0]-step, from_pos[1]+step)
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break

    elif(to_pos[0] > from_pos[0] and to_pos[1] > from_pos[1]):
        for step in range(1, to_pos[0]-from_pos[0]+1):
            current_pos = (from_pos[0]+step, from_pos[1]+step)
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break

    elif(to_pos[0] < from_pos[0] and to_pos[1] < from_pos[1]):
        for step in range(1, from_pos[0]-to_pos[0]+1):
            current_pos = (from_pos[0]-step, from_pos[1]-step)
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break

    elif(to_pos[0] > from_pos[0] and to_pos[1] < from_pos[1]):
        for step in range(1, to_pos[0]-from_pos[0]+1):
            current_pos = (from_pos[0]+step, from_pos[1]-step)
            square = board[current_pos[0]][current_pos[1]]
            if not validate_one_square_move(current_pos, to_pos, square, from_button, to_button):
                break

def logic_queen(from_pos, to_pos, from_button, to_button, board):
    logic_bishop(from_pos, to_pos, from_button, to_button, board)
    logic_rook(from_pos, to_pos, from_button, to_button, board)

""" 
   for i in range(8):
        print(i)
        if i+from_pos[0] or i+from_pos[1] > 7:
            return None
        if board[i+from_pos[0]][i-from_pos[1]] is None:
            return None
        else: 
            if i-from_pos[0] == to_pos[0] and i-from_pos[1] == to_pos[1]:
                move_piece_right(to_button, from_button) """

    # if to_pos[0] > from_pos[0]:
    #     if to_pos[1] > from_pos[1]:
    #         return None
    #     elif to_pos[1] < from_pos[1]:
    #         return None
    # elif to_pos[0] < from_pos[0]:
    #     if to_pos[1] > from_pos[1]:
    #         return None
    #     elif to_pos[1] < from_pos[1]:
    #         for i in range(from_pos[])