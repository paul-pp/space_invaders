import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Game", "Code")))
from Game import Game, CRT 
import pygame
import numpy as np

Display_mode=True

##### MAIN ######
pygame.init()
screen_width = 600
screen_height = 600


if Display_mode:
    screen = pygame.display.set_mode((screen_width,screen_height))
    crt = CRT(screen_width,screen_height,screen)

else:
    screen = pygame.Surface((screen_width, screen_height))

clock = pygame.time.Clock()
ALIENLASER = pygame.USEREVENT + 1
pygame.time.set_timer(ALIENLASER,800)
##### MAIN ######





max_steps_per_episode=10_000


for episode in range(2): # One episode = one game
    game = Game(screen_width,screen_height,screen,Display_mode)
    state=game.get_state()
    total_reward = 0

    step=0
    terminated=False
    while (step<max_steps_per_episode and terminated==False):
            step+=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ALIENLASER:
                    game.alien_shoot()
            
            if Display_mode:
                screen.fill((30,30,30))
    
            action=np.random.randint(4)
            new_state,reward,terminated=game.step(action)
            print("\nnew_state",new_state)
            print("reward,terminated",reward,terminated)
            #crt.draw()
            
            if Display_mode:
                pygame.display.flip()
                clock.tick(60)
            else :
                clock.tick(60)

            if (step>max_steps_per_episode):
                 print("sortie épisode, time exceeded")

