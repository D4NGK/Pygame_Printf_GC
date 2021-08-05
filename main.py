import pygame
import os
pygame.init()

screen_width = 700
screen_height = 500
WIN = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Pygame")

#! x, y,isJUMP, Player_y_ Momentum, and jumpCount is for the jump
BG_COLOR = (128, 128, 128)
FPS = 60
VEL = 5

SPRITE_WIDTH, SPRITE_HIEGHT = (55, 55)


Player_image = pygame.image.load(os.path.join('Assets', 'Player.png'))
Player = pygame.transform.scale(Player_image, (SPRITE_WIDTH, SPRITE_HIEGHT))


def draw_window(Player_rect):
    WIN.fill(BG_COLOR)
    WIN.blit(Player, (Player_rect.x, Player_rect.y))
    pygame.display.update()

 #TODO Add a JUMP FEATURE


def player_movement(keys_pressed, Player_rect):
    isJump = False
    velocity = 5 #velocity and mass for jump: https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
    mass = 1

    if keys_pressed[pygame.K_a] and Player_rect.x - VEL > 0:  # LEFT
        Player_rect.x -= VEL
    if keys_pressed[pygame.K_d] and Player_rect.x - VEL < screen_width:  # LEFT
        Player_rect.x += VEL
    if isJump==False:
        if keys_pressed[pygame.K_SPACE]:
            isJump = True
    if isJump:
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F =(1 / 2)*mass*(velocity**2)
           
            # change in the y co-ordinate
        Player_rect.y-= F
            
            # decreasing velocity while going up and become negative while coming down
        velocity -= 1
            
            # object reached its maximum height
        if velocity<0:
                
                # negative sign is added to counter negative velocity
            mass -= 1
    
            # objected reaches its original state
        if velocity ==-6:
    
                # making isjump equal to false 
            isJump = False
    
        
                # setting original values to v and m
            velocity = 5
            mass = 1
  #TODO FIX CLOCK for jump


def main():
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
