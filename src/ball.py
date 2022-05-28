import pygame
import math

import table

# 大きさ（半径）
BALL_RADIUS = 28.4 * 1

# 色
COLOR_0 = (255, 255, 255)
BLACK = (0, 0, 0)

# 位置
INIT_XPOS = table.INNER_POS + 158.75
INIT_YPOS = table.INNER_POS + table.INNER_LENGTH/2
ball_x = INIT_XPOS
ball_y = INIT_YPOS

# 速度
ball_vx = 30
ball_vy = 30

# 移動範囲（ビリヤードテーブル）
FIELD_TOP = table.INNER_POS + BALL_RADIUS
FIELD_LEFT = table.INNER_POS + BALL_RADIUS
FIELD_BOTTOM = table.INNER_POS + table.INNER_LENGTH - BALL_RADIUS
FIELD_RIGHT = table.INNER_POS + table.INNER_WIDE - BALL_RADIUS

# ボールの移動
def move():
    global ball_x, ball_y, ball_vx, ball_vy

    ball_x += ball_vx
    if ball_x < FIELD_LEFT:
        ball_x = FIELD_LEFT
        ball_vx *= -1
    elif ball_x > FIELD_RIGHT:
        ball_x = FIELD_RIGHT
        ball_vx *= -1

    ball_y += ball_vy
    if ball_y < FIELD_TOP:
        ball_y = FIELD_TOP
        ball_vy *= -1
    elif ball_y > FIELD_BOTTOM:
        ball_y = FIELD_BOTTOM
        ball_vy *= -1

    ball_vx *= 0.99
    ball_vy *= 0.99

    judge_stop()



def judge_stop():
    global ball_vx, ball_vy

    if abs(ball_vx) < 0.001:
        ball_vx = 0
    if abs(ball_vy) < 0.001:
        ball_vy = 0

    print(ball_vx, ball_vy)




def draw(sc):
    global ball_x, ball_y

    pygame.draw.circle(sc, COLOR_0, [ball_x, ball_y], BALL_RADIUS)
