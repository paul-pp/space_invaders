import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Game", "Code")))
from Game import Game, CRT 
import pygame
import numpy as np



##### MAIN ######
pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
crt = CRT(screen_width,screen_height,screen)

ALIENLASER = pygame.USEREVENT + 1
pygame.time.set_timer(ALIENLASER,800)
##### MAIN ######

step=0
max_steps_per_episode=10_000

for episode in range(2): # One episode = one game
    game = Game(screen_width,screen_height,screen)
    state=game.get_state()
    total_reward = 0


    while (step<max_steps_per_episode or terminated==False):
            step+=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ALIENLASER:
                    game.alien_shoot()
    
            screen.fill((30,30,30))
    
            action=np.random.randint(4)
            new_state,reward,terminated=game.step(action)
            print("\nnew_state",new_state)
            print("reward,terminated",reward,terminated)
            #crt.draw()
                
            pygame.display.flip()
            clock.tick(60)

            if (step>max_steps_per_episode):
                 print("sortie épisode, time exceeded")

