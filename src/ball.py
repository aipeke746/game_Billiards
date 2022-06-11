import pygame
import math

import table
import calc

# ==================== 定数 ====================
# 大きさ（半径）
BALL_DIAMETER = 28.4
BALL_RADIUS = BALL_DIAMETER / 2
# 色
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)
BROWN = (165, 42, 42)
BLACK = (0, 0, 0)
BALL_COLOR = [WHITE, YELLOW, BLUE, RED, PURPLE, ORANGE, GREEN, BROWN, BLACK, YELLOW, BLUE, RED, PURPLE, ORANGE, GREEN, BLACK]
# 初期セット位置
INIT_PLAYER_XPOS = table.INNER_POS + 158.75
INIT_PLAYER_YPOS = table.INNER_POS + table.INNER_LENGTH/2
INIT_BALL_BASE_XPOS = table.INNER_POS + table.INNER_WIDE - 158.75
INIT_BALL_BASE_YPOS = table.INNER_POS + table.INNER_LENGTH/2
# 移動範囲（ビリヤードテーブル）
FIELD_TOP = table.INNER_POS + BALL_RADIUS
FIELD_LEFT = table.INNER_POS + BALL_RADIUS
FIELD_BOTTOM = table.INNER_POS + table.INNER_LENGTH - BALL_RADIUS
FIELD_RIGHT = table.INNER_POS + table.INNER_WIDE - BALL_RADIUS
# ボールの数
BALL_MAX = 16
# プレイヤーのボール
PLAYER = 0

# ==================== 変数 ====================
# フラグ／位置／速度
ball_f = [False] * BALL_MAX
ball_x = [0] * BALL_MAX
ball_y = [0] * BALL_MAX
ball_vx = [0] * BALL_MAX
ball_vy = [0] * BALL_MAX

# ショット
shot_trigger = False
shot_x = 0
shot_y = 0


# ==================== 関数 ====================
# ボールの初期位置
def init_pos():
    # プレイヤーのボール
    ball_f[PLAYER] = True
    ball_f[PLAYER] = True
    ball_x[PLAYER] = INIT_PLAYER_XPOS
    ball_y[PLAYER] = INIT_PLAYER_YPOS

    # 色付きボールの位置
    for x in range(1, 6):
        num = int((x**2 - x + 2) / 2)

        for y in range(x):
            ball_f[num+y] = True
            ball_x[num+y] = INIT_BALL_BASE_XPOS + BALL_DIAMETER * math.sqrt(3) / 2 * x
            ball_y[num+y] = INIT_BALL_BASE_YPOS - BALL_DIAMETER / 2 * x + BALL_DIAMETER * y


# ボールの移動
def move():

    for num in range(BALL_MAX):
        if ball_f[num] == False:
            continue
        if ball_vx[num] == 0 and ball_vy[num] == 0:
            continue

        judge_collision(num)

    for num in range(BALL_MAX):
        if ball_f[num] == False:
            continue
        if ball_vx[num] == 0 and ball_vy[num] == 0:
            continue

        ball_x[num] += ball_vx[num]
        if ball_x[num] < FIELD_LEFT:
            ball_x[num] = FIELD_LEFT
            ball_vx[num] *= -1
        elif ball_x[num] > FIELD_RIGHT:
            ball_x[num] = FIELD_RIGHT
            ball_vx[num] *= -1

        ball_y[num] += ball_vy[num]
        if ball_y[num] < FIELD_TOP:
            ball_y[num] = FIELD_TOP
            ball_vy[num] *= -1
        elif ball_y[num] > FIELD_BOTTOM:
            ball_y[num] = FIELD_BOTTOM
            ball_vy[num] *= -1

        ball_vx[num] *= 0.99
        ball_vy[num] *= 0.99


        judge_stop(num)



# ボールの衝突処理判定
def judge_collision(target):

    for num in range(BALL_MAX):
        if num == target:
            continue

        distance = math.sqrt((ball_x[target] - ball_x[num])**2 + (ball_y[target] - ball_y[num])**2)

        # 衝突判定
        if distance <= BALL_DIAMETER:
            overlapping = abs(BALL_DIAMETER - distance)

            # ボールが重なる場合
            if overlapping > 0:
                dis_x = ball_x[target] - ball_x[num]
                dis_y = ball_y[target] - ball_y[num]
                # 衝突した位置に戻す
                if dis_x > 0:   ball_x[target] += overlapping * (distance / dis_x)
                if dis_y > 0:   ball_y[target] += overlapping * (distance / dis_y)

            ball_vx[target] = ball_vx[target] * 0.95
            ball_vy[target] = ball_vy[target] * 0.95
            ball_vx[num] = ball_vx[target] * 0.99
            ball_vy[num] = ball_vy[target] * 0.99


#ボールが止まったかの判定
def judge_stop(target):

    if abs(ball_vx[target]) < 0.01:
        ball_vx[target] = 0
    if abs(ball_vy[target]) < 0.01:
        ball_vy[target] = 0


# ボールを打つ
def shot(mb, mx, my):
    global shot_trigger, shot_x, shot_y

    # 引く
    if mb == True and shot_trigger == False and ball_vx[PLAYER] == 0 and ball_vy[PLAYER] == 0:
        if judge_shot(mx, my):
            shot_x = mx
            shot_y = my
            shot_trigger = True
    # 打つ
    elif mb == False and shot_trigger == True:
        ball_vx[PLAYER] = (shot_x - mx) * 0.3
        ball_vy[PLAYER] = (shot_y - my) * 0.3
        shot_trigger = False


def judge_shot(mx, my):
    if (mx - ball_x[PLAYER])**2 + (my - ball_y[PLAYER])**2 <= BALL_RADIUS**2:
        return True
    return False


# ボールの描画
def draw(sc):

    for num in range(BALL_MAX):
        if ball_f[num] == True:
            pygame.draw.circle(sc, BALL_COLOR[num], [ball_x[num], ball_y[num]], BALL_RADIUS)

            if num >= 9:
                pygame.draw.circle(sc, BALL_COLOR[0], [ball_x[num], ball_y[num]], BALL_RADIUS)
                pygame.draw.rect(sc, BALL_COLOR[num], [ball_x[num]-BALL_RADIUS*math.sqrt(3)/2, ball_y[num]-BALL_RADIUS/2, BALL_RADIUS*math.sqrt(3), BALL_RADIUS])
                pygame.draw.arc(sc, BALL_COLOR[num] ,[ball_x[num]-BALL_RADIUS, ball_y[num]-BALL_RADIUS, BALL_DIAMETER, BALL_DIAMETER], 3*math.pi/4, 5*math.pi/4, width=3)
                pygame.draw.arc(sc, BALL_COLOR[num] ,[ball_x[num]-BALL_RADIUS, ball_y[num]-BALL_RADIUS, BALL_DIAMETER, BALL_DIAMETER], -1*math.pi/4, math.pi/4, width=3)
