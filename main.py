# @TIME:2018.06.24
# @AUTHOR: Iiwll
import sys
import pygame
from setting import *
from piece import Piece
def main () :
    pygame.init() #初始化pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT+100))
    pygame.display.set_caption('俄罗斯方块')
    piece = Piece('Z', screen)
    while True: #游戏主循环
        check_event(piece)
        screen.fill(BG_COLOR)
        draw_game_area(screen)
        Piece.paint(piece)
        pygame.display.flip()


def draw_game_area(screen):
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT, GAME_AREA_TOP),
                     (GAME_AREA_LEFT + GAME_AREA_WIDTH,GAME_AREA_TOP)) #绘制顶部
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT, GAME_AREA_TOP + 20* CELL_WIDTH),
                     (GAME_AREA_LEFT + GAME_AREA_WIDTH,GAME_AREA_TOP + 20* CELL_WIDTH))
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP),
                     (GAME_AREA_LEFT, GAME_AREA_TOP + 20* CELL_WIDTH))
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT + 10 * CELL_WIDTH, GAME_AREA_TOP),
                     (GAME_AREA_LEFT + 10 * CELL_WIDTH, GAME_AREA_TOP + 20 * CELL_WIDTH))
    for i in range(1, 20):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT, GAME_AREA_TOP + i* CELL_WIDTH),
                     (GAME_AREA_LEFT + GAME_AREA_WIDTH,GAME_AREA_TOP + i* CELL_WIDTH))
    for i in range(1, 10):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT+i*CELL_WIDTH, GAME_AREA_TOP),
                     (GAME_AREA_LEFT+i*CELL_WIDTH ,GAME_AREA_TOP + 20* CELL_WIDTH))

def check_event (piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               # print ('按下向下键')
                Piece.mov_down(piece)
            elif event.key == pygame.K_UP:
                print('按下向上键')
            elif event.key == pygame.K_LEFT:
              #  print ('按下向左键')
                Piece.mov_left(piece)
            elif event.key == pygame.K_RIGHT:
              #  print ('按下向右键')
                Piece.mov_right(piece)

if __name__ == '__main__':
     main()
