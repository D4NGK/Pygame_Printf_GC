import pygame
import os
pygame.init()

screen_width = 700
screen_height = 500
WIN = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption ("aha man ka gatan-aw ug maayu. title ra gani ako gi change. HAHAHAAHAHHA")

#! x, y,isJUMP, Player_y_ Momentum, and jumpCount is for the jump
x = 50
y = 50
BG_COLOR = (128, 128, 128)
FPS = 60
VEL = 5
PLAYER_y_MOMENTUM = 0
isJump = False
jumpCount = 2
SPRITE_WIDTH, SPRITE_HIEGHT = (55, 55)


Player_image = pygame.image.load(os.path.join('Assets', 'Player.png'))
Player = pygame.transform.scale(Player_image, (SPRITE_WIDTH, SPRITE_HIEGHT))
 
def draw_window(Player_rect):
    WIN.fill(BG_COLOR)
    WIN.blit(Player, (Player_rect.x, Player_rect.y))
    pygame.display.update()

 #TODO Add a JUMP FEATURE

def player_movement(keys_pressed, Player_rect):
    if keys_pressed[pygame.K_a] and Player_rect.x - VEL > 0: #LEFT
        Player_rect.x -= VEL
    if keys_pressed[pygame.K_d] and Player_rect.x - VEL < screen_width: #LEFT
        Player_rect.x += VEL

  #TODO FIX CLOCK for jump

def main ():
    Player_rect = pygame.Rect(100, 300, SPRITE_WIDTH, SPRITE_HIEGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, Player_rect)
        draw_window(Player_rect)

    pygame.quit()


if __name__ == "__main__":
  main()

  