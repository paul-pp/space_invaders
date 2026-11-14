import numpy as np
import pygame
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Game", "Code")))
from Game import Game, CRT 


class SpaceInvadersEnv:
    def __init__(self, screen_width,screen_height,Display_mode,max_steps_per_episode,period_step,
                value_alien_red,
                value_alien_green,
                value_alien_else,
                value_extra,
                value_life):
        
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.Display_mode=Display_mode
        self.max_steps_per_episode=max_steps_per_episode
        self.period_event_ALIENLASER=75
        self.period_step=period_step


        self.value_alien_red=value_alien_red
        self.value_alien_green=value_alien_green
        self.value_alien_else=value_alien_else
        self.value_extra=value_extra
        self.value_life=value_life



        pygame.init()
        if Display_mode:
            self.screen = pygame.display.set_mode((screen_width,screen_height))
            # crt = CRT(screen_width,screen_height,self.screen)

        else:
            self.screen = pygame.Surface((screen_width, screen_height))


        self.return_queue=[]
        self.length_queue=[]


        self.tot_reward=0
        self.game = Game(self.screen_width,self.screen_height,self.screen,self.Display_mode,
                        value_alien_red=value_alien_red,
                        value_alien_green=value_alien_green,
                        value_alien_else=value_alien_else,
                        value_extra=value_extra,
                        value_life=value_life)
        self.ep_step=0

        self.observation_space=np.array(self.get_state())
        self.action_space=Action_space(nb_actions=4)

    def reset(self):
        self.return_queue.append(self.tot_reward)
        self.length_queue.append(self.ep_step)

        self.tot_reward=0
        self.game = Game(self.screen_width,self.screen_height,self.screen,self.Display_mode,
                         value_alien_red=self.value_alien_red,
                        value_alien_green=self.value_alien_green,
                        value_alien_else=self.value_alien_else,
                        value_extra=self.value_extra,
                        value_life=self.value_life)
        self.ep_step=0
        return self.get_state()

    def get_state(self):
        return self.game.get_state()

    def step(self, action):
        """
        Given current environment and agent's action, it updates the game and returns new state, reward for the agent and indicates if game is finished or not
        """
        ### Specifique au jeu ####
        self.ep_step+=1

        for _ in range(self.period_step):
            reward=0
            done=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if (self.ep_step%self.period_event_ALIENLASER == 0):
                self.game.alien_shoot()
            
            if self.Display_mode:
                self.screen.fill((30,30,30))
            ### Specifique au jeu ####

            state, r, d=self.game.step(action)
            # print('r',r)

            reward+=r
            if d : 
                done=True

        # if (self.ep_step>self.max_steps_per_episode):
        #     print("sortie épisode, time exceeded")

        if self.Display_mode:
            pygame.display.flip()

        self.tot_reward+=reward
        # print(' ')

        return state, reward, done
    
    def close(self):
        pygame.quit()
        sys.exit()
        return 0
    

class Action_space:
	def __init__(self,nb_actions):
		self.n=nb_actions

	def sample(self):
		return np.random.randint(self.n)