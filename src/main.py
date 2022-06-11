import pygame
import sys

import table
import ball

# ==================== 定数 ====================
# スクリーンの大きさ
SCREEN_WIDE = table.OUTER_WIDE + table.OUTER_POS*2
SCREEN_LENGTH = table.OUTER_LENGTH + table.OUTER_POS*2
# フレームレート
FRAME_LATE = 100

# ==================== 変数 ====================
tmr = 0

# ==================== メイン処理 ====================
# メインループ
def main():
    global tmr

    pygame.init()
    pygame.display.set_caption("BIlliards Game")
    screen = pygame.display.set_mode((SCREEN_WIDE, SCREEN_LENGTH))
    clock = pygame.time.Clock()

    while True:
        tmr += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((960, 720), pyame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))

        # キー入力
        key = pygame.key.get_pressed()
        # マウス入座標／入力
        mouseX, mouseY = pygame.mouse.get_pos()
        mBtn1, mBtn2, mBtn3 = pygame.mouse.get_pressed()

        # ボールの処理
        if tmr == 1:
            ball.init_pos()

        ball.shot(mBtn1, mouseX, mouseY)
        ball.move()

        # 描画
        table.draw(screen)
        ball.draw(screen)

        pygame.display.update()
        clock.tick(FRAME_LATE)

if __name__ == '__main__':
    main()
