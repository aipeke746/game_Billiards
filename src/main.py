import pygame
import sys

import table
import ball

# スクリーンの大きさ
SCREEN_WIDE = table.OUTER_WIDE + table.OUTER_POS*2
SCREEN_LENGTH = table.OUTER_LENGTH + table.OUTER_POS*2

# フレームレート
FRAME_LATE = 100

# メインループ
def main():
    pygame.init()
    pygame.display.set_caption("BIlliards Game")
    screen = pygame.display.set_mode((SCREEN_WIDE, SCREEN_LENGTH))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((960, 720), pyame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))


        key = pygame.key.get_pressed()

        ball.move()

        table.draw(screen)
        ball.draw(screen)



        pygame.display.update()
        clock.tick(FRAME_LATE)

if __name__ == '__main__':
    main()
