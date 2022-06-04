import pygame
import math

import table
import calc

# ==================== 定数 ====================
# 大きさ（半径）
BALL_RADIUS = 28.4 / 2
# 色
COLOR_0 = (255, 255, 255)
BLACK = (0, 0, 0)
# 初期セット位置
INIT_XPOS = table.INNER_POS + 158.75
INIT_YPOS = table.INNER_POS + table.INNER_LENGTH/2
# 移動範囲（ビリヤードテーブル）
FIELD_TOP = table.INNER_POS + BALL_RADIUS
FIELD_LEFT = table.INNER_POS + BALL_RADIUS
FIELD_BOTTOM = table.INNER_POS + table.INNER_LENGTH - BALL_RADIUS
FIELD_RIGHT = table.INNER_POS + table.INNER_WIDE - BALL_RADIUS

# ==================== 変数 ====================
# 位置
ball_x = INIT_XPOS
ball_y = INIT_YPOS
# 速度
ball_vx = 0
ball_vy = 0
# ショット
shot_trigger = False
shot_x = 0
shot_y = 0

# ==================== 関数 ====================
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


# ボールが止まったかの判定
def judge_stop():
    global ball_vx, ball_vy

    if abs(ball_vx) < 0.01:
        ball_vx = 0
    if abs(ball_vy) < 0.01:
        ball_vy = 0


# ボールを打つ
def shot(mb, mx, my):
    global shot_trigger, shot_x, shot_y, ball_vx, ball_vy

    # 引く
    if mb == True and shot_trigger == False and ball_vx == 0 and ball_vy == 0:
        if calc.judge_shot(mx, my, ball_x, ball_y, BALL_RADIUS):
            shot_x = mx
            shot_y = my
            shot_trigger = True
    # 打つ
    elif mb == False and shot_trigger == True:
        ball_vx = (shot_x - mx) * 0.3
        ball_vy = (shot_y - my) * 0.3
        shot_trigger = False

# ボールの描画
def draw(sc):
    global ball_x, ball_y

    pygame.draw.circle(sc, COLOR_0, [ball_x, ball_y], BALL_RADIUS)
