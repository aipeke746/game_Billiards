import pygame

# ==================== 定数 ====================
# ビリヤードテーブルの位置
OUTER_POS = 100
INNER_POS = 150
# ビリヤードテーブルの寸法
OUTER_WIDE = 1370
OUTER_LENGTH = 735
INNER_WIDE = 1270
INNER_LENGTH = 635
# 色
OUTER_COLOR = (115, 66, 41)
INNER_COLOR = (0, 92, 76)


# ==================== 関数 ====================
# ビリヤードテーブルの描画
def draw(sc):
    pygame.draw.rect(sc, OUTER_COLOR, [OUTER_POS, OUTER_POS, OUTER_WIDE, OUTER_LENGTH])
    pygame.draw.rect(sc, INNER_COLOR, [INNER_POS, INNER_POS, INNER_WIDE, INNER_LENGTH])
