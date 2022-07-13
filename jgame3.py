#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:06:46 2022

@author: blaubaer
"""

import pygame
import math
import configparser
import random

#get Symboles
config = configparser.ConfigParser()
config.read('spiel.ini')
bild1 = config['DEFAULT']['bild1']
bild2 = config['DEFAULT']['bild2']


# Initializing Pygame
pygame.init()

# Screen
WIDTH = 500
ROWS = 3
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Jana's TicTacToe Spiel")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Images
X_IMAGE = pygame.transform.scale(pygame.image.load(bild1), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load(bild2), (150, 150))
#Startbild
initiating_window = pygame.image.load("Jana_logo.gif")


	
global random_dec

random_dec ='a1'

# Fonts
END_FONT = pygame.font.SysFont('courier', 30)


def draw_grid():
    
    
    gap = WIDTH // ROWS

    # Starting points
    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap

        pygame.draw.line(win, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(win, GRAY, (0, x), (WIDTH, x), 3)


def initialize_grid():
    
    
    dis_to_cen = WIDTH // ROWS // 2

    # Initializing the array
    game_array = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            game_array[i][j] = (x, y, "", True)

    return game_array


def engine_easy(game_array):
    global x_turn, o_turn, images, random_dec
    
    
# =============================================================================
#     for i in range(len(game_array)):
#         for j in range(len(game_array[i])):
#             x, y, char, can_play = game_array[i][j]
#             print (x, y, char)
# 
# =============================================================================
    
    
    
    if random_dec =='a1':
        images.append((83, 83, O_IMAGE))
        x_turn = True
        o_turn = False
    
        game_array[0][0] = (83, 83, 'Spieler2', False)

    elif random_dec =='a2':
        images.append((249, 83, O_IMAGE))
        x_turn = True
        o_turn = False
    
        game_array[0][1] = (249, 83, 'Spieler2', False)
    elif random_dec =='a3':
        
        images.append((415, 83, O_IMAGE))
        x_turn = True
        o_turn = False
    
        game_array[0][2] = (415, 83, 'Spieler2', False)
    
    elif random_dec =='b1':
        images.append((83, 249, O_IMAGE))
        x_turn = True
        o_turn = False
    
        game_array[1][0] = (83, 249, 'Spieler2', False)
    elif random_dec =='b2':
        images.append((249, 249, O_IMAGE))
        x_turn = True
        o_turn = False
    
        game_array[1][1] = (249, 249, 'Spieler2', False)
    
    elif random_dec =='b3':
        images.append((415, 249, O_IMAGE))
        x_turn = True
        o_turn = False
    
        
        game_array[1][2] = (415, 249, 'Spieler2', False)
    
    
    elif random_dec =='c1':
        images.append((83, 415, O_IMAGE))
        x_turn = True
        o_turn = False
    
        
        game_array[2][0] = (83, 415, 'Spieler2', False)
    elif random_dec =='c2':
        images.append((249, 415, O_IMAGE))
        x_turn = True
        o_turn = False
    
        game_array[2][1] = (249, 415, 'Spieler2', False)
    elif random_dec =='c3':
        images.append((415, 415, O_IMAGE))
        x_turn = True
        o_turn = False
    
        
        game_array[2][2] = (415, 415, 'Spieler2', False)
    



def click(game_array):
    global x_turn, o_turn, images, random_dec

    # Mouse position
    m_x, m_y = pygame.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]

            # Distance between mouse and the centre of the square
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

            # If it's inside the square
            if dis < WIDTH // ROWS // 2 and can_play:
                if x_turn:  # If it's X's turn
                    images.append((x, y, X_IMAGE))
                    x_turn = False
                    o_turn = True
                    game_array[i][j] = (x, y, 'Spieler1', False)
                    still_free(game_array)
                    #computer
                    
                #elif o_turn:  # If it's O's turn
                    engine_easy(game_array)        
                    
                        
                    
                    
# =============================================================================
#                 elif o_turn:  # If it's O's turn
#                     
#                 
#                     images.append((x, y, O_IMAGE))    # Mouse position
   
#                     x_turn = True
#                     o_turn = False
#                     game_array[i][j] = (x, y, 'Spieler2', False)
# 
# =============================================================================

def still_free(game_array):
    
    global random_dec
    
    empty_array = list()
    array_values = list()
    
    a1 = game_array[0][0]
    a1_player = a1[2]
    a1_value = a1[3]
    
    print(a1_value)
    print(str(a1_value))
    
    array_values.append(a1_value)
    if a1_value == True:
        empty_array.append('a1')
    
    a2 = game_array[0][1]
    a2_player = a2[2]
    a2_value = a2[3]
    array_values.append(a2_value)
    if a2_value == True:
        empty_array.append('a2')
    
    a3 = game_array[0][2]   
    a3_player = a3[2]
    a3_value = a3[3]
    array_values.append(a3_value)
    if a3_value == True:
        empty_array.append('a3')
    
    
    b1 = game_array[1][0]
    b1_player = b1[2]
    b1_value = b1[3]
    array_values.append(b1_value)
    if b1_value == True:
        empty_array.append('b1')
    
    b2 = game_array[1][1]
    b2_player = b2[2]
    b2_value = b2[3]
    array_values.append(b2_value)
    if b2_value == True:
        empty_array.append('b2')
    
    b3 = game_array[1][2]
    b3_player = b3[2]
    b3_value = b3[3]
    array_values.append(b3_value)
    if b3_value == True:
        empty_array.append('b3')
    
    c1 = game_array[2][0]
    c1_player = c1[2]
    c1_value = c1[3]
    array_values.append(c1_value)
    if c1_value == True:
        empty_array.append('c1')
    
    c2 = game_array[2][1]
    c2_player = c2[2]
    c2_value = c2[3]
    array_values.append(c2_value)
    if c2_value == True:
        empty_array.append('c2')
    
    c3 = game_array[2][2]
    c3_player = c3[2]
    c3_value = c3[3]
    array_values.append(c3_value)
    if c3_value == True:
        empty_array.append('c3')
        
    print(empty_array)
    print(array_values)
    
    if len(empty_array)>=1:
        random_dec = random.choice(empty_array)
        print(random_dec)
    else:
        if len (empty_array)==0:
            print('Array empty')
        else:
            random_dec = empty_array[0]
            print(random_dec)
    

# Checking if someone has won
def has_won(game_array):
    # Checking rows
    for row in range(0,3):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            display_message(game_array[row][0][2].upper() + " hat gewonnen!")
            return True

    # Checking columns
    for col in range(0, 3):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper() + " hat gewonnen!")
            return True

    # Checking main diagonal
    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " hat gewonnen!")
        return True

    # Checking reverse diagonal
    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " hat gewonnen!")
        return True

    return False


def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    display_message("Ist ein schönes Bild!")
    return True


def display_message(content):
    pygame.time.delay(500)
    win.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def render():
    win.fill(WHITE)
    draw_grid()

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def main():
    global x_turn, o_turn, images, draw
    
    
    images = []
    draw = False

    run = True

    x_turn = True
    o_turn = False

    game_array = initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)
                #still_free(game_array)

        render()

        if has_won(game_array) or has_drawn(game_array):
            run = False


while True:
    if __name__ == '__main__':
        main()