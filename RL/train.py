import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Game", "Code")))
from Game import Game, CRT 
import pygame
import numpy as np
from Deep_Q_learning import Agent_DQN,ReplayBuffer
from env import SpaceInvadersEnv


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

# clock = pygame.time.Clock()
# ALIENLASER = pygame.USEREVENT + 1
# pygame.time.set_timer(ALIENLASER,800)
period_event_ALIENLASER=75

##### MAIN ######





n_episodes=600
start_eps=1.0
batch_size=64
update_weights_period=1000


display_train=10


# game = Game(screen_width,screen_height,screen,Display_mode)
# env=SpaceInvadersEnv(game)


# agent=Agent_DQN(
#     env=game,

#     start_learning_rate=0.002,
#     start_factor_lr=1.0,
#     end_factor_lr=0.2,
#     total_iters_lr=int(n_episodes/2),
    
#     start_epsilon=start_eps,
#     epsilon_decay = start_eps / (n_episodes/2),
#     final_epsilon=0.1,
#     gamma=0.99
#     )

buffer = ReplayBuffer(capacity=100_000)




max_steps_per_episode=10_000


for episode in range(15): # One episode = one game
    # state=game.reset()
    game = Game(screen_width,screen_height,screen,Display_mode)
    total_reward = 0

    step=0
    terminated=False
    while (step<max_steps_per_episode and terminated==False):
            step+=1

            ### Specifique au jeu ####
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if (step%period_event_ALIENLASER == 0):
                game.alien_shoot()
            
            if Display_mode:
                screen.fill((30,30,30))
            ### Specifique au jeu ####
    

            # action=np.random.randint(4)
            action=1
            new_state,reward,terminated=game.step(action)

            # print("\nnew_state",new_state)
            # print("reward,terminated",reward,terminated)

            if (step>max_steps_per_episode):
                print("sortie épisode, time exceeded")

            # if (step%display_train==0):
            #     print(step)

            ### Specifique au jeu ####
            if Display_mode:
                pygame.display.flip()
                # #ATTentiion la clock détermine la cadence des tirs de lasers
                # clock.tick(60)
            ### Specifique au jeu ####



if (Display_mode):
    pygame.quit()
    sys.exit()

print("entrainement done")