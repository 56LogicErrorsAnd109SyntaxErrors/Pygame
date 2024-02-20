import pygame
import random
import os
#Initialize the pygame
pygame.init()

window = pygame.display.set_mode((900, 700))
screen_width = 900
screen_height = 700
#Title and Icon
pygame.display.set_caption("Tetris, but there's mines")
# icon = pygame.image.load("")
# pygame.display.set_icon(icon)

#Constants
TETRIS_NOTATION = ['T', 'S', 'Z', 'L', 'J', 'I', 'O']
TETRIMINO_COLOR = {'T' : (221, 10, 178), 'S' : (83, 218, 63), 'Z' : (253, 63, 89), 'L' : (255, 145, 12), 'J' : (0, 119, 211), 'I' : (1, 237, 250), 'O' : (254, 251, 52)}
BOARDSIZE = 200
MINES = 31

class TetrisBoard:
    def __init__(self) -> None:
        self.board = []
        self.pieces = ['T', 'S', 'Z', 'L', 'J', 'I', 'O']
        for i in range(BOARDSIZE):
            self.board.append({'X' : 300 + 30 * (i % 10), 'Y' : 50 + 30 * (i // 10), 'block' : None})
        self.current_piece = self.generate_next_piece()
        self.next_piece = self.generate_next_piece()
        #First Index is the center piece
        self.tetrimino_position = {'T' : [{'X' : 450, 'Y' : 80}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 480, 'Y' : 80}],
                                    'S' : [{'X' : 450, 'Y' : 80}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 480, 'Y' : 50}],
                                    'Z' : [{'X' : 450, 'Y' : 80}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 50}, {'X' : 480, 'Y' : 80}],
                                    'L' : [{'X' : 450, 'Y' : 80}, {'X' : 480, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 480, 'Y' : 80}],
                                    'J' : [{'X' : 450, 'Y' : 80}, {'X' : 420, 'Y' : 80}, {'X' : 420, 'Y' : 50}, {'X' : 480, 'Y' : 80}],
                                    'I' : [{'X' : 390, 'Y' : 50}, {'X' : 420, 'Y' : 50}, {'X' : 450, 'Y' : 50}, {'X' : 480, 'Y' : 50}, [None, [0, 1], None, None, None, [1, 1], None, None, None, [2, 1], None, None, None, [3, 1], None, None]],
                                    'O' : [{'X' : 420, 'Y' : 50}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 450, 'Y' : 80}]}
        
        self.lines_cleared = 0
        self.score = 0
        self.level = 1
        #{level : frames per grid}
        self.speed = {'1' : 13, '2' : 11, '3' : 9, '4' : 8, '5' : 7, '6' : 7, '7' : 6, '8' : 6, '9' : 6, '10' : 5, '11' : 5, '12' : 5, '13' : 4, '14' : 4, '15' : 4, '16' : 3, '17' : 3, '18' : 3, '19' : 2}
    def draw_tetris_board(self):
        for i in range(BOARDSIZE):
            if self.board[i]['block'] != None:
                pygame.draw.rect(window, self.board[i]['block'], pygame.Rect(self.board[i]['X'], self.board[i]['Y'], 30, 30))
    
    def display_current_piece(self):
        for i in range(4):
            pygame.draw.rect(window, TETRIMINO_COLOR[self.current_piece], pygame.Rect(self.tetrimino_position[self.current_piece][i]['X'], self.tetrimino_position[self.current_piece][i]['Y'], 30, 30), 100)


    def generate_next_piece(self):
        if len(self.pieces) == 0:
            self.pieces = ['T', 'S', 'Z', 'L', 'J', 'I', 'O']
        next_piece = random.choice(self.pieces)
        self.pieces.remove(next_piece)
        return next_piece
    
    def display_next_piece(self):
        if self.next_piece == 'T':
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(635, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(695, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 85, 30, 30), 100)
        if self.next_piece == 'S':
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(635, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 85, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(695, 85, 30, 30), 100)
        if self.next_piece == 'Z':
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(695, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 85, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(635, 85, 30, 30), 100)
        if self.next_piece == 'L':
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(635, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(695, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(695, 85, 30, 30), 100)
        if self.next_piece == 'J':
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(635, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(665, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(695, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(635, 85, 30, 30), 100)        
        if self.next_piece == 'I':        
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(709, 100, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(679, 100, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(649, 100, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(619, 100, 30, 30), 100)
        if self.next_piece == 'O':
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(679, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(649, 115, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(649, 85, 30, 30), 100)
            pygame.draw.rect(window, TETRIMINO_COLOR[self.next_piece], pygame.Rect(679, 85, 30, 30), 100)

    def is_border(self, direction):
        if direction == 'left':
            for i in range(4):
                if self.tetrimino_position[self.current_piece][i]['X'] == 300:
                    return True
                corr_x = self.tetrimino_position[self.current_piece][i]['X'] - 30
                corr_y = self.tetrimino_position[self.current_piece][i]['Y']
                row_num = int((corr_y - 50) / 30)
                column_num = int((corr_x - 300) / 30)
                if self.board[row_num * 10 + column_num]['block'] != None:
                    return True
        elif direction == 'right':
            for i in range(4):
                if self.tetrimino_position[self.current_piece][i]['X'] == 570:
                    return True
                corr_x = self.tetrimino_position[self.current_piece][i]['X'] + 30
                corr_y = self.tetrimino_position[self.current_piece][i]['Y']
                row_num = int((corr_y - 50) / 30)
                column_num = int((corr_x - 300) / 30)
                if self.board[row_num * 10 + column_num]['block'] != None:
                    return True
        return False
    
    def is_stop_falling(self):
        for i in range(4):
            if self.tetrimino_position[self.current_piece][i]['Y'] == 620:
                return True
            temp_y = self.tetrimino_position[self.current_piece][i]['Y'] + 30
            temp_x = self.tetrimino_position[self.current_piece][i]['X']
            row_num = int((temp_y - 50) / 30)
            column_num = int((temp_x - 300) / 30)
            if self.board[row_num * 10 + column_num]['block'] != None:
                return True
        return False
    
    def move(self, direction):
        if direction == 'left':
            if not self.is_border(direction):
                for i in range(4):
                    self.tetrimino_position[self.current_piece][i]['X'] -=  30
        elif direction == 'right':
            if not self.is_border(direction):
                for i in range(4):
                    self.tetrimino_position[self.current_piece][i]['X'] +=  30
        elif direction == 'down':
            if not self.is_stop_falling():
                for i in range(4):
                    self.tetrimino_position[self.current_piece][i]['Y'] +=  30

    def rotate(self, direction):
        if self.current_piece == 'O':
            return
        if self.current_piece == 'I':
            original_orientation = self.tetrimino_position[self.current_piece][4]
            min_x = self.tetrimino_position[self.current_piece][0]['X']
            min_y = self.tetrimino_position[self.current_piece][0]['Y']
            #Find minimum x and y coordinates
            for i in range(len(original_orientation)):
                if original_orientation[i] != None:
                    corr_y = original_orientation[i][1]
                    corr_x = original_orientation[i][0]
                    break

            if min_x == self.tetrimino_position[self.current_piece][1]['X']:
                min_x -= corr_x * 30
            if min_y == self.tetrimino_position[self.current_piece][1]['Y']:
                min_y -= corr_y * 30

            if direction == 'clockwise':
                new_orientation = [None, None, None, None,
                                None, None, None, None,
                                None, None, None, None,
                                None, None, None, None]
                #Invert x and y coordinates
                for i in range(len(original_orientation)):
                    if original_orientation[i] != None:
                        new_orientation[(original_orientation[i][0] * 4) + original_orientation[i][1]] = [original_orientation[i][1], original_orientation[i][0]]
                final_orientation = [None, None, None, None,
                                    None, None, None, None,
                                    None, None, None, None,
                                    None, None, None, None]
                # Mirror along y-axis
                for i in range(len(new_orientation)):
                    if new_orientation[i] != None:
                        mirrored_x = 3 - new_orientation[i][1]
                        mirrored_y = new_orientation[i][0]
                        final_orientation[(mirrored_x * 4) + mirrored_y] = [mirrored_y, mirrored_x]
                #Shift I piece at border
                x_shift = 0
                y_shift = 0
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        temp_x = min_x + final_orientation[i][0] * 30 
                        temp_y = min_y + final_orientation[i][1] * 30
                        if temp_x > 570:
                            x_shift -= 1
                        elif temp_x < 300:
                            x_shift += 1
                        if temp_y > 620:
                            y_shift -= 1
                        elif temp_y < 50:
                            y_shift += 1
                # Check if rotation is possible
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        temp_x = min_x + final_orientation[i][0] * 30 + x_shift * 30
                        temp_y = min_y + final_orientation[i][1] * 30 + y_shift * 30
                        row_num = int((temp_y - 50) / 30)
                        column_num = int((temp_x - 300) / 30)
                        if self.board[row_num * 10 + column_num]['block'] != None:
                            return
                #Update Coordinates
                index = 0
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        self.tetrimino_position[self.current_piece][index]['X'] = min_x + final_orientation[i][0] * 30 + x_shift * 30
                        self.tetrimino_position[self.current_piece][index]['Y'] = min_y + final_orientation[i][1] * 30 + y_shift * 30
                        index += 1
            elif direction == 'anti-clockwise':
                new_orientation = [None, None, None, None,
                                None, None, None, None,
                                None, None, None, None,
                                None, None, None, None]
                #Mirror along y-axis
                for i in range(len(original_orientation)):
                    if original_orientation[i] != None:
                        mirrored_x = 3 - original_orientation[i][1]
                        mirrored_y = original_orientation[i][0]
                        new_orientation[(mirrored_x * 4) + mirrored_y] = [mirrored_y, mirrored_x]

                final_orientation = [None, None, None, None,
                                    None, None, None, None,
                                    None, None, None, None,
                                    None, None, None, None]
                #Invert x and y coordiantes
                for i in range(len(new_orientation)):
                    if new_orientation[i] != None:
                        final_orientation[(new_orientation[i][0] * 4) + new_orientation[i][1]] = [new_orientation[i][1], new_orientation[i][0]]
                #Shift piece at border
                x_shift = 0
                y_shift = 0
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        temp_x = min_x + final_orientation[i][0] * 30 
                        temp_y = min_y + final_orientation[i][1] * 30
                        if temp_x > 570:
                            x_shift -= 1
                        elif temp_x < 300:
                            x_shift += 1
                        if temp_y > 620:
                            y_shift -= 1
                        elif temp_y < 50:
                            y_shift += 1
                #Check if rotation is possible          
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        temp_x = min_x + final_orientation[i][0] * 30 + x_shift * 30
                        temp_y = min_y + final_orientation[i][1] * 30 + y_shift * 30
                        row_num = int((temp_y - 50) / 30)
                        column_num = int((temp_x - 300) / 30)
                        if self.board[row_num * 10 + column_num]['block'] != None:
                            return
                #Update coordinates
                index = 0
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        self.tetrimino_position[self.current_piece][index]['X'] = min_x + final_orientation[i][0] * 30 + x_shift * 30
                        self.tetrimino_position[self.current_piece][index]['Y'] = min_y + final_orientation[i][1] * 30 + y_shift * 30
                        index += 1
            self.tetrimino_position[self.current_piece][4] = final_orientation
        else:
            mid_x = self.tetrimino_position[self.current_piece][0]['X']
            mid_y = self.tetrimino_position[self.current_piece][0]['Y']
            original_orientation = [None, None, None,
                                    None, None, None,
                                    None, None, None]
            #Add the blocks into the board to prepare rotation
            for i in range(4):
                x = self.tetrimino_position[self.current_piece][i]['X']
                corr_x = int((x - mid_x + 30) / 30)
                y = self.tetrimino_position[self.current_piece][i]['Y']
                corr_y = int((y - mid_y + 30) / 30)
                original_orientation[corr_y + (corr_x * 3)] = [corr_y, corr_x]
            if direction == 'clockwise':
                #Invert the x and y coordinates
                new_orientation = [None, None, None,
                                None, None, None,
                                None, None, None]
                for i in range(len(original_orientation)):
                    if original_orientation[i] != None:
                        new_orientation[(original_orientation[i][0] * 3) + original_orientation[i][1]] = [original_orientation[i][1], original_orientation[i][0]]

                #Mirror along y-axis
                final_orientation = [None, None, None,
                                    None, None, None,
                                    None, None, None]
                for i in range(len(new_orientation)):
                    if new_orientation[i] != None:
                        mirrored_x = 2 - new_orientation[i][1]
                        mirrored_y = new_orientation[i][0]
                        final_orientation[(mirrored_x * 3) + mirrored_y] = [mirrored_y, mirrored_x]
                #Shift piece at border
                x_shift = 0
                y_shift = 0
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        temp_x = mid_x + final_orientation[i][0] * 30 - 30
                        temp_y = mid_y + final_orientation[i][1] * 30 - 30
                        if temp_x > 570:
                            x_shift -= 1
                        elif temp_x < 300:
                            x_shift += 1
                        if temp_y > 620:
                            y_shift -= 1
                        elif temp_y < 50:
                            y_shift += 1
                #Check if rotation is possible
                for i in range(len(final_orientation)):
                    if final_orientation[i] == [1, 1]:
                        continue
                    if final_orientation[i] != None:
                        temp_x = mid_x + final_orientation[i][0] * 30 - 30 + x_shift * 30
                        temp_y = mid_y + final_orientation[i][1] * 30 - 30 + y_shift * 30
                        row_num = int((temp_y - 50) / 30)
                        column_num = int((temp_x - 300) / 30)
                        if self.board[row_num * 10 + column_num]['block'] != None:
                            return
                #Update terimino position
                index = 1
                for i in range(len(final_orientation)):
                    if final_orientation[i] == [1, 1]:
                        self.tetrimino_position[self.current_piece][0]['X'] += x_shift * 30
                        self.tetrimino_position[self.current_piece][0]['Y'] += y_shift * 30
                        continue
                    if final_orientation[i] != None:
                        self.tetrimino_position[self.current_piece][index]['X'] = mid_x + final_orientation[i][1] * 30 - 30 + x_shift * 30
                        self.tetrimino_position[self.current_piece][index]['Y'] = mid_y + final_orientation[i][0] * 30 - 30 + y_shift * 30
                        index += 1
            elif direction == 'anti-clockwise':
                new_orientation = [None, None, None,
                                None, None, None,
                                None, None, None]
                #Mirror along y-axis
                for i in range(len(original_orientation)):
                    if original_orientation[i] != None:
                        mirrored_x = 2 - original_orientation[i][1]
                        mirrored_y = original_orientation[i][0]
                        new_orientation[(mirrored_x * 3) + mirrored_y] = [mirrored_y, mirrored_x]
                #Invert the x and y coordinates
                final_orientation = [None, None, None,
                                    None, None, None,
                                    None, None, None]
                for i in range(len(new_orientation)):
                    if new_orientation[i] != None:
                        final_orientation[(new_orientation[i][0] * 3) + new_orientation[i][1]] = [new_orientation[i][1], new_orientation[i][0]]
                #Shift piece at border
                x_shift = 0
                y_shift = 0
                for i in range(len(final_orientation)):
                    if final_orientation[i] != None:
                        temp_x = mid_x + final_orientation[i][0] * 30 - 30
                        temp_y = mid_y + final_orientation[i][1] * 30 - 30
                        if temp_x > 570:
                            x_shift -= 1
                        elif temp_x < 300:
                            x_shift += 1
                        if temp_y > 620:
                            y_shift -= 1
                        elif temp_y < 50:
                            y_shift += 1
                #Check if rotation is possible
                for i in range(len(final_orientation)):
                    if final_orientation[i] == [1, 1]:
                        continue
                    if final_orientation[i] != None:
                        temp_x = mid_x + final_orientation[i][1] * 30 - 30 + x_shift * 30
                        temp_y = mid_y + final_orientation[i][0] * 30 - 30 + y_shift * 30
                        row_num = int((temp_y - 50) / 30)
                        column_num = int((temp_x - 300) / 30)
                        if self.board[row_num * 10 + column_num]['block'] != None:
                            return
                #Update terimino position
                index = 1
                for i in range(len(final_orientation)):
                    if final_orientation[i] == [1, 1]:
                        self.tetrimino_position[self.current_piece][0]['X'] += x_shift * 30
                        self.tetrimino_position[self.current_piece][0]['Y'] += y_shift * 30
                        continue
                    if final_orientation[i] != None:
                        self.tetrimino_position[self.current_piece][index]['X'] = mid_x + final_orientation[i][1] * 30 - 30 + x_shift * 30
                        self.tetrimino_position[self.current_piece][index]['Y'] = mid_y + final_orientation[i][0] * 30 - 30 + y_shift * 30
                        index += 1
    
    def clear_line(self):
        count = 0
        rows_cleared = []
        for row_num in reversed(range(20)):
            for column_num in range(10):
                if self.board[row_num* 10 + column_num]['block'] != None:
                    count += 1
            if count == 10:
                for column_num in range(10):
                    self.board[row_num* 10 + column_num]['block'] = None
                rows_cleared.append(row_num)
            count = 0
        self.lines_cleared += len(rows_cleared)
        old_row = 19
        new_row = 19
        new_board = []
        for i in range(BOARDSIZE):
            new_board.append({'X' : 300 + 30 * (i % 10), 'Y' : 50 + 30 * (i // 10), 'block' : None})
        while old_row > 0:
            if old_row in rows_cleared:
                old_row -= 1
            else:
                for column_num in range(10):
                    new_board[column_num + new_row * 10]['block'] = self.board[column_num + old_row * 10]['block']
                new_row -= 1 
                old_row -= 1
        self.board = new_board

    def calculate_score(self):
        count = 0
        rows_cleared = []
        for row_num in reversed(range(20)):
            for column_num in range(10):
                if self.board[row_num * 10 + column_num]['block'] != None:
                    count += 1
            if count == 10:
                rows_cleared.append(row_num)
            count = 0
        if len(rows_cleared) == 1:
            self.score += self.level * 100
        elif len(rows_cleared) == 2:
            self.score += self.level * 200
        elif len(rows_cleared) == 3:
            self.score += self.level * 300
        elif len(rows_cleared) == 4:
            self.score += self.level * 800
        else:
            self.score += 0

    def is_next_level(self):
        if self.lines_cleared >= 10:
            self.lines_cleared -= 10
            self.level += 1
            return True
        return False

    def is_lose(self):
        spawn_position = {'T' : [{'X' : 450, 'Y' : 80},  {'X' : 450, 'Y' : 50},  {'X' : 420, 'Y' : 80},  {'X' : 480, 'Y' : 80}],
                        'S' : [{'X' : 450, 'Y' : 80},  {'X' : 450, 'Y' : 50},  {'X' : 420, 'Y' : 80},  {'X' : 480, 'Y' : 50}],
                        'Z' : [{'X' : 450, 'Y' : 80},  {'X' : 450, 'Y' : 50},  {'X' : 420, 'Y' : 50},  {'X' : 480, 'Y' : 80}],
                        'L' : [{'X' : 450, 'Y' : 80},  {'X' : 480, 'Y' : 50},  {'X' : 420, 'Y' : 80},  {'X' : 480, 'Y' : 80}],
                        'J' : [{'X' : 450, 'Y' : 80},  {'X' : 420, 'Y' : 80},  {'X' : 420, 'Y' : 50},  {'X' : 480, 'Y' : 80}],
                        'I' : [{'X' : 390, 'Y' : 50},  {'X' : 420, 'Y' : 50},  {'X' : 450, 'Y' : 50},  {'X' : 480, 'Y' : 50}, [None, [1, 0], None, None, None, [1, 1], None, None, None, [1, 2], None, None, None, [1, 3], None, None]],
                        'O' : [{'X' : 420, 'Y' : 50},  {'X' : 450, 'Y' : 50},  {'X' : 420, 'Y' : 80},  {'X' : 450, 'Y' : 80}]}
        for i in range(4):
            column_num = int((spawn_position[self.current_piece][i]['X'] - 300) / 30)
            row_num = int((spawn_position[self.current_piece][i]['Y'] - 50) / 30)
            if self.board[row_num * 10 + column_num]['block'] != None:
                return True
        return False
    
class MinesweeperBoard:
    def __init__(self) -> None:
        self.board = []
        for i in range(BOARDSIZE):
            self.board.append({'X' : 300 + 30 * (i % 10), 'Y' : 50 + 30 * (i // 10), 'has_mine' : False, 'nearby_mines' : 0, 'discovered' : False, 'has_flag' : False})
        self.mines_coordinates = []
        self.started = False

    def start_minesweeper(self, start_position):
        count = 0
        leave_empty_coordinates = [start_position]
        matrix = [[-1, -1], [-1, 0], [-1, 1],
                    [0, -1], [0, 1],
                    [1, -1], [1, 0], [1, 1]]
        for adjacent in matrix:
            leave_empty_coordinates.append(start_position + adjacent[0] * 10 + adjacent[1])
        while count != MINES:
            temp = random.randint(0, 199)
            if temp not in self.mines_coordinates and temp not in leave_empty_coordinates:
                self.mines_coordinates.append(temp)
                count += 1
        for coord in self.mines_coordinates:
            row_num = int(coord // 10)
            column_num = int(coord % 10)
            self.board[row_num * 10 + column_num]['has_mine'] = True
        for i in range(BOARDSIZE):
            row_num = i // 10
            column_num = i % 10
            mines_adjacent = 0
            for adjacent in matrix:
                if column_num + adjacent[0] < 0 or column_num + adjacent[0] > 9 or row_num + adjacent[1] < 0 or row_num + adjacent[1] > 19:
                    continue
                else:
                    adjacent_row_num = row_num + adjacent[1]
                    adjacent_column_num = column_num + adjacent[0]
                    if self.board[adjacent_row_num * 10 + adjacent_column_num]['has_mine'] == True:
                        mines_adjacent += 1
            self.board[row_num * 10 + column_num]['nearby_mines'] = mines_adjacent
    
    def clear_empty_adjacent_tiles(self, start_position, visited_coordinates):
        matrix = [[-1, -1], [-1, 0], [-1, 1],
                    [0, -1], [0, 1],
                    [1, -1], [1, 0], [1, 1]]
        new_matrix = []
        row_num = start_position // 10
        column_num = start_position % 10
        for adjacent in matrix:
            if row_num + adjacent[0] >= 0 and row_num + adjacent[0] <= 19 and column_num + adjacent[1] >= 0 and column_num + adjacent[1] <= 9:
                new_matrix.append(adjacent)
        #Base Case
        self.board[row_num * 10 + column_num]['discovered'] = True
        if self.board[row_num * 10 + column_num]['nearby_mines'] != 0 or self.board[row_num * 10 + column_num]['has_mine']:
            return
        else:
            for adjacent in new_matrix:
                if (start_position + adjacent[0] * 10 + adjacent[1]) in visited_coordinates:
                    continue
                visited_coordinates.append(start_position)
                self.clear_empty_adjacent_tiles(start_position + adjacent[0] * 10 + adjacent[1], visited_coordinates)

    def draw_minesweeper_board(self):
        font = pygame.font.Font(('mine-sweeper.ttf'), 20)
        number_colours = {'0' : (255, 165, 0), #Orange
                            '1' : (0, 0, 255), #Blue
                            '2' : (0, 255, 0), #Green
                            '3' : (255, 0, 0), #Red
                            '4' : (75, 0 , 130), #Indigo
                            '5' : (128, 0, 0), #Maroon
                            '6' : (0, 255, 255), #Cyan
                            '7' : (255, 255, 0), #Yellow
                            '8' : (211, 211, 211), #Light Gray
                            '*' : (0, 0, 0), #Black
                            '`' : (255, 0, 0)} #Red

        for i in range(BOARDSIZE):
            text = None
            shift = 0
            row_num = int((i // 10))
            column_num = int((i % 10))
            if self.board[i]['has_flag']:
                text = '`'
                shift += 3
            if self.board[i]['discovered']:
                shift = 0
                if self.board[i]['has_mine']:
                    text = '*'
                else:
                    text = self.board[i]['nearby_mines']
            if text == 1:
                shift += 4
            if text == '*':
                shift -= 3
            if text != None:
                image = font.render(str(text), True, number_colours[str(text)])
                window.blit(image, (column_num * 30 + 306 + shift, row_num * 30 + 53))

    def is_lose(self):
        for i in range(BOARDSIZE):
            if self.board[i]['has_mine'] and self.board[i]['discovered']:
                return True
        return False

    def is_win(self):
        for i in range(BOARDSIZE):
            if not self.board[i]['discovered'] and not self.board[i]['has_mine']:
                return False
        return True

class Game:
    def __init__(self) -> None:
        self.running = True
        self.started = False
        self.changing_controls = False
        self.tetris_board = TetrisBoard()
        self.minesweeper_board = MinesweeperBoard()
        #Movement
        self.move_cooldown = 0
        self.moving = False
        self.left = False
        self.right = False
        self.down = False
        #List follows [left, down, right]
        self.direction = ['left', 'down', 'right']
        self.priority = [0, 0, 0]
        #Rotate
        self.rotating = False
        self.rotate_direction = None
        #Click
        self.clicking = False
        self.clear_tile = False
        self.place_flag = False
        #Timer
        self.clock = None
        self.speed = self.tetris_board.speed[str(self.tetris_board.level)] * 1/24
        self.block_drop_timer = self.speed
        self.dt = 0 
    
    def outline_menu(self):
        window.fill((128, 128, 128))
        font = pygame.font.Font(('HunDIN1451.ttf'), 70)
        font.set_bold(False)
        img = font.render('tetris:egyptian    difficulty', True, (255, 255, 255))
        window.blit(img, (screen_width // 2 - img.get_width() // 2, 50))

        font = pygame.font.Font(('HunDIN1451.ttf'), 50)
        font.set_bold(False)
        img = font.render('your board is safe,or is it?', True, (255, 255, 255))
        window.blit(img, (screen_width // 2 - img.get_width() // 2, 150))

        font = pygame.font.Font(('HunDIN1451.ttf'), 70)
        font.set_bold(True)
        img = font.render('START', True, (255, 255, 255))
        window.blit(img, (screen_width // 2 - img.get_width() // 2, 275))
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(250, 250, 400, 100), 10)

        font = pygame.font.Font(('HunDIN1451.ttf'), 70)
        font.set_bold(True)
        img = font.render('CONTROLS', True, (255, 255, 255))
        window.blit(img, (screen_width // 2 - img.get_width() // 2, 405))
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(250, 380, 400, 100), 10)
        pygame.display.update()

    def outline_board(self):
        #Board Outline
        pygame.draw.rect(window, (255,255,255), pygame.Rect(290, 40, 320, 620), 10)
        #Vertical Lines
        for i in range(10):
            pygame.draw.rect(window, (255,255,255), pygame.Rect(300 + i * 30, 40, 1, 620))
        #Horizontal Lines
        for i in range(20):
            pygame.draw.rect(window, (255,255,255), pygame.Rect(290, 50 + i * 30, 320, 1))
        #Next Box
        pygame.draw.rect(window, (255,255,255), pygame.Rect(600, 40, 150, 30), 100)
        pygame.draw.rect(window, (255,255,255), pygame.Rect(749, 70, 1, 90))
        pygame.draw.rect(window, (255,255,255), pygame.Rect(600, 160, 149, 1))
        font = pygame.font.Font(('HunDIN1451.ttf'), 30)
        img = font.render('NEXT', True, (255, 255, 255))
        window.blit(img, (610, 45))
        #Scoreboard
        img = font.render(str(self.tetris_board.score), 20, (255, 255, 255))
        window.blit(img, (445, 665))

    def display_gameOver(self, has_won):
        window.fill((128, 128, 128))
        #Board Outline
        pygame.draw.rect(window, (255,255,255), pygame.Rect(40, 40, 320, 620), 10)
        #Vertical Lines
        for i in range(10):
            pygame.draw.rect(window, (255,255,255), pygame.Rect(50 + i * 30, 40, 1, 620))
        #Horizontal Lines
        for i in range(20):
            pygame.draw.rect(window, (255,255,255), pygame.Rect(40, 50 + i * 30, 320, 1))
        font = pygame.font.Font(('mine-sweeper.ttf'), 50)
        if has_won:
            text = 'VICTORY'
            image = font.render(str(text), True, (255, 255, 255))
            window.blit(image, (450, 90))
        else:
            text = 'DEFEAT'
            image = font.render(str(text), True, (255, 255, 255))
            window.blit(image, (470, 90))

        font = pygame.font.Font(('mine-sweeper.ttf'), 20)

        text = 'score:'
        image = font.render(str(text), True, (255, 255, 255))
        window.blit(image, (400, 220))

        text = str(self.tetris_board.score)
        image = font.render(str(text), True, (255, 255, 255))
        window.blit(image, (400, 270))

        text = 'lines Cleared:'
        image = font.render(str(text), True, (255, 255, 255))
        window.blit(image, (400, 320))
            
        text = str(self.tetris_board.lines_cleared)
        image = font.render(str(text), True, (255, 255, 255))
        window.blit(image, (400, 370))

        tiles_cleared = 0
        for i in range(BOARDSIZE):
            if self.minesweeper_board.board[i]['discovered']:
                tiles_cleared += 1      

        text = 'tiles left:'
        image = font.render(str(text), True, (255, 255, 255))
        window.blit(image, (400, 420))

        text = str(200 - tiles_cleared)
        image = font.render(str(text), True, (255, 255, 255))
        window.blit(image, (400, 470))

        pygame.draw.rect(window, (255,255,255), pygame.Rect(480, 560, 290, 75), 10)
        
        font = pygame.font.Font(('mine-sweeper.ttf'), 25)

        text = 'play again'
        image = font.render(str(text), True, (255, 255, 255))
        window.blit(image, (500, 580))
    
        #Display tetris board
        for i in range(BOARDSIZE):
            if self.tetris_board.board[i]['block'] != None:
                pygame.draw.rect(window, self.tetris_board.board[i]['block'], (self.tetris_board.board[i]['X'] - 250, self.tetris_board.board[i]['Y'], 30, 30))
       
        #Display minesweeper board
            font = pygame.font.Font(('mine-sweeper.ttf'), 20)
            number_colours = {'0' : (255, 165, 0), #Orange
                            '1' : (0, 0, 255), #Blue
                            '2' : (0, 255, 0), #Green
                            '3' : (255, 0, 0), #Red
                            '4' : (75, 0 , 130), #Indigo
                            '5' : (128, 0, 0), #Maroon
                            '6' : (0, 255, 255), #Cyan
                            '7' : (255, 255, 0), #Yellow
                            '8' : (211, 211, 211), #Light Gray
                            '*' : (0, 0, 0), #Black
                            '`' : (255, 0, 0)} #Red

            for i in range(BOARDSIZE):
                text = None
                shift = 0
                if self.minesweeper_board.board[i]['has_flag']:
                    text = '`'
                    shift += 3
                if self.minesweeper_board.board[i]['discovered']:
                    shift = 0
                    if self.minesweeper_board.board[i]['has_mine']:
                        text = '*'
                    else:
                        text = self.minesweeper_board.board[i]['nearby_mines']
                if text == 1:
                    shift += 4
                if text == '*':
                    shift -= 3
                if text != None:
                    image = font.render(str(text), True, number_colours[str(text)])
                    window.blit(image, (self.minesweeper_board.board[i]['X'] - 244 + shift, self.minesweeper_board.board[i]['Y'] + 3))
        pygame.display.update()
    def outline_controls(self):
        window.fill((128, 128, 128))
        font = pygame.font.Font(('HunDIN1451.ttf'), 70)
        font.set_bold(True)
        img = font.render('CONTROLS', True, (255, 255, 255))
        window.blit(img, (screen_width // 2 - img.get_width() // 2, 50))
        
        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('move  left', True, (255, 255, 255))
        window.blit(img, (25, 150))

        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('move  right', True, (255, 255, 255))
        window.blit(img, (25, 250))

        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('soft  drop', True, (255, 255, 255))
        window.blit(img, (25, 350))

        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('rotate  reft', True, (255, 255, 255))
        window.blit(img, (25, 450))

        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('rotate  right', True, (255, 255, 255))
        window.blit(img, (25, 550))

        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('place  flag', True, (255, 255, 255))
        window.blit(img, (450, 150))

        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('clear  square', True, (255, 255, 255))
        window.blit(img, (450, 250))
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(285, 140, 150, 50), 5)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(285, 240, 150, 50), 5)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(285, 340, 150, 50), 5)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(285, 440, 150, 50), 5)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(285, 540, 150, 50), 5)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(710 , 140, 150, 50), 5)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(710 , 240, 150, 50), 5)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(35, 40, 110, 50), 5)

        font = pygame.font.Font(('HunDIN1451.ttf'), 20)
        font.set_bold(False)
        img = font.render('arrow left', True, (255, 255, 255))
        window.blit(img, (310, 155))

        font = pygame.font.Font(('HunDIN1451.ttf'), 20)
        font.set_bold(False)
        img = font.render('arrow right', True, (255, 255, 255))
        window.blit(img, (310, 255))
        
        font = pygame.font.Font(('HunDIN1451.ttf'), 20)
        font.set_bold(False)
        img = font.render('arrow down', True, (255, 255, 255))
        window.blit(img, (310, 355))

        font = pygame.font.Font(('HunDIN1451.ttf'), 20)
        font.set_bold(False)
        img = font.render('A', True, (255, 255, 255))
        window.blit(img, (355, 455))

        font = pygame.font.Font(('HunDIN1451.ttf'), 20)
        font.set_bold(False)
        img = font.render('D', True, (255, 255, 255))
        window.blit(img, (355, 555))

        font = pygame.font.Font(('HunDIN1451.ttf'), 20)
        font.set_bold(False)
        img = font.render('left click', True, (255, 255, 255))
        window.blit(img, (740, 155))

        font = pygame.font.Font(('HunDIN1451.ttf'), 20)
        font.set_bold(False)
        img = font.render('right click', True, (255, 255, 255))
        window.blit(img, (740, 255))

        font = pygame.font.Font(('HunDIN1451.ttf'), 40)
        font.set_bold(False)
        img = font.render('back', True, (255, 255, 255))
        window.blit(img, (50, 50))
        pygame.display.update()
    def handle_event_start_menu(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = list(pygame.mouse.get_pos())
                if cursor_pos[0] > 260 and cursor_pos[1] > 260 and cursor_pos[0] < 640 and cursor_pos[1] < 350:
                    self.started = True
                if cursor_pos[0] > 260 and cursor_pos[1] > 390 and cursor_pos[0] < 640 and cursor_pos[1] < 770:
                    self.changing_controls = True
    def handle_event_control_menu(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.changing_controls = False
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = list(pygame.mouse.get_pos())
                if cursor_pos[0] > 30 and cursor_pos[1] > 35 and cursor_pos[0] < 140 and cursor_pos[1] < 85:
                    self.changing_controls = False
            
    def handle_event_main_game(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.moving and self.left:
                        continue
                    self.moving = True
                    self.move_cooldown = 0
                    self.left = True
                    if self.priority == [0, 0, 0]:
                        self.priority[0] = 1
                    else:
                        self.priority[0] = max(self.priority) + 1
                if event.key == pygame.K_RIGHT:
                    if self.moving and self.right:
                        continue
                    self.moving = True
                    self.move_cooldown = 0
                    self.right = True
                    if self.priority == [0, 0, 0]:
                        self.priority[2] = 1
                    else:
                        self.priority[2] = max(self.priority) + 1
                if event.key == pygame.K_DOWN:
                    if self.moving and self.down:
                        continue
                    self.down = True
                    self.moving = True
                    self.move_cooldown = 0
                    if self.priority == [0, 0, 0]:
                        self.priority[1] = 1
                    else:
                        self.priority[1] = max(self.priority) + 1
                if event.key == pygame.K_a:
                    self.rotating = True
                    self.rotate_direction = 'anti-clockwise'
                if event.key == pygame.K_d:
                    self.rotating = True
                    self.rotate_direction = 'clockwise'
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    if event.key == pygame.K_DOWN:
                        if self.priority[0] > self.priority[1]:
                            self.priority[0] -= 1
                        if self.priority[2] > self.priority[1]:
                            self.priority[2] -= 1
                        self.down = False
                        self.priority[1] = 0
                    if event.key == pygame.K_LEFT:
                        if self.priority[1] > self.priority[0]:
                            self.priority[1] -= 1
                        if self.priority[2] > self.priority[0]:
                            self.priority[2] -= 1
                        self.left = False
                        self.priority[0] = 0
                    if event.key == pygame.K_RIGHT:
                        if self.priority[0] > self.priority[2]:
                            self.priority[0] -= 1
                        if self.priority[1] > self.priority[2]:
                            self.priority[1] -= 1
                        self.priority[2] = 0
                        self.right = False
                    self.move_cooldown = 0
                    if self.priority == [0, 0, 0]:
                        self.moving = False
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicking = True
                if event.button == 1:
                    self.clear_tile = True
                if event.button == 3:
                    self.place_flag = True
    
    def handle_event_game_over(self):
        events= pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = list(pygame.mouse.get_pos())
                if cursor_pos[0] > 480 and cursor_pos[1] > 560 and cursor_pos[0] < 770 and cursor_pos[1] < 635:
                    self.tetris_board = TetrisBoard()
                    self.minesweeper_board = MinesweeperBoard()
                    #Movement
                    self.move_cooldown = 0
                    self.moving = False
                    self.left = False
                    self.right = False
                    self.down = False
                    #List follows [left, down, right]
                    self.direction = ['left', 'down', 'right']
                    self.priority = [0, 0, 0]
                    #Rotate
                    self.rotating = False
                    self.rotate_direction = None
                    #Click
                    self.clicking = False
                    self.clear_tile = False
                    self.place_flag = False
                    #Timer
                    self.clock = pygame.time.Clock()
                    self.block_drop_timer = 0
                    self.dt = 0 
    
    def update_cooldown(self):
        self.move_cooldown -= self.dt

    def run(self):
        while self.running:
            if self.started:
                break
            self.outline_menu()
            self.handle_event_start_menu()
            while self.changing_controls:
                self.outline_controls()
                self.handle_event_control_menu()
        self.clock = pygame.time.Clock()
        window.fill((128, 128, 128))
        self.outline_board
        next = self.tetris_board.next_piece
        piece = self.tetris_board.current_piece
        pygame.display.update()
        while self.running:
            if self.minesweeper_board.is_lose() or self.tetris_board.is_lose():
                self.display_gameOver(False)
                self.handle_event_game_over()
            elif self.minesweeper_board.is_win():
                self.display_gameOver(True)
                self.handle_event_game_over()
            else:
                self.handle_event_main_game()
                if self.moving:
                    self.update_cooldown()
                    if self.move_cooldown <= 0:
                        direction = self.direction[self.priority.index(max(self.priority))]
                        self.tetris_board.move(direction)
                        self.move_cooldown = 0.2
                if self.rotating:
                    self.tetris_board.rotate(self.rotate_direction)
                    self.rotate_direction = None
                    self.rotating = False
                if self.clicking:
                    cursor_pos = list(pygame.mouse.get_pos())
                    column_num = (cursor_pos[0] - 300) // 30 
                    row_num = (cursor_pos[1] - 50) // 30 
                    mouse_position = (column_num) + ((row_num) * 10)
                    if cursor_pos[0] >= 300 and cursor_pos[0] <= 600 and cursor_pos[1] <= 650 and cursor_pos[1] >= 50 and self.tetris_board.board[mouse_position]['block'] == None:
                        if not self.minesweeper_board.started:
                            self.minesweeper_board.start_minesweeper(mouse_position)
                            self.minesweeper_board.started = True
                        if self.clear_tile:
                            self.minesweeper_board.clear_empty_adjacent_tiles(mouse_position, [mouse_position])
                            self.minesweeper_board.board[mouse_position]['discovered'] = True
                            self.clear_tile = False
                        if self.place_flag:
                            if self.minesweeper_board.board[mouse_position]['has_flag'] == True:
                                self.minesweeper_board.board[mouse_position]['has_flag'] = False
                            else:
                                self.minesweeper_board.board[mouse_position]['has_flag'] = True
                            self.place_flag = False
                    self.clicking = False


                self.block_drop_timer -= self.dt
                if self.block_drop_timer <= 0:
                    self.block_drop_timer = self.speed
                    if not self.tetris_board.is_stop_falling():
                        for i in range(4):
                            self.tetris_board.tetrimino_position[self.tetris_board.current_piece][i]['Y'] += 30
                    else:
                        for i in range(4):
                            row_num = int((self.tetris_board.tetrimino_position[self.tetris_board.current_piece][i]['Y'] - 50) / 30)
                            column_num = int((self.tetris_board.tetrimino_position[self.tetris_board.current_piece][i]['X'] - 300) / 30)
                            self.tetris_board.board[row_num * 10 + column_num]['block'] = TETRIMINO_COLOR[self.tetris_board.current_piece]
                        self.tetris_board.tetrimino_position = {'T' : [{'X' : 450, 'Y' : 80}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 480, 'Y' : 80}],
                                                                'S' : [{'X' : 450, 'Y' : 80}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 480, 'Y' : 50}],
                                                                'Z' : [{'X' : 450, 'Y' : 80}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 50}, {'X' : 480, 'Y' : 80}],
                                                                'L' : [{'X' : 450, 'Y' : 80}, {'X' : 480, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 480, 'Y' : 80}],
                                                                'J' : [{'X' : 450, 'Y' : 80}, {'X' : 420, 'Y' : 80}, {'X' : 420, 'Y' : 50}, {'X' : 480, 'Y' : 80}],
                                                                'I' : [{'X' : 390, 'Y' : 50}, {'X' : 420, 'Y' : 50}, {'X' : 450, 'Y' : 50}, {'X' : 480, 'Y' : 50}, [None, [0, 1], None, None, None, [1, 1], None, None, None, [2, 1], None, None, None, [3, 1], None, None]],
                                                                'O' : [{'X' : 420, 'Y' : 50}, {'X' : 450, 'Y' : 50}, {'X' : 420, 'Y' : 80}, {'X' : 450, 'Y' : 80}]}
                        self.tetris_board.current_piece = self.tetris_board.next_piece 
                        self.tetris_board.next_piece = self.tetris_board.generate_next_piece()
                        self.tetris_board.calculate_score()
                        self.tetris_board.clear_line()
                        if self.tetris_board.is_next_level():
                            if self.tetris_board.level > 19:
                                self.speed = 2 * 1/24
                                self.block_drop_timer = self.speed
                            if self.tetris_board.level >= 29:
                                self.speed = 1 * 1/24
                                self.block_drop_timer = self.speed
                            else:
                                self.speed = self.tetris_board.speed[str(self.tetris_board.level)] * 1/24
                                self.block_drop_timer = self.speed
                #Display Shit
                window.fill((128, 128, 128))
                self.outline_board()
                self.minesweeper_board.draw_minesweeper_board()
                self.tetris_board.draw_tetris_board()
                self.tetris_board.display_next_piece()
                self.tetris_board.display_current_piece()
                pygame.display.update()
                self.dt = self.clock.tick(60)/1000

game = Game()
game.run()
                
