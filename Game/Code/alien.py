import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAME_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

class Alien(pygame.sprite.Sprite):
	def __init__(self,color,x,y,Display_mode,value):
		super().__init__()
		file_name = color + '.png'

		self.image = pygame.image.load(
			os.path.join(GAME_DIR, "graphics", file_name)
		)
		if Display_mode:
			self.image=self.image.convert_alpha()

		self.rect = self.image.get_rect(topleft = (x,y))

		# if color == 'red': self.value = 2
		# elif color == 'green': self.value = 4
		# else: self.value = 6
		self.value=value

	def update(self,direction):
		self.rect.x += direction

class Extra(pygame.sprite.Sprite):
	def __init__(self,side,screen_width,Display_mode):
		super().__init__()

		self.image = pygame.image.load(os.path.join(GAME_DIR, "graphics", "extra.png"))
		if Display_mode:
			self.image=self.image.convert_alpha()
		
		if side == 'right':
			x = screen_width + 50
			self.speed = - 3
		else:
			x = -50
			self.speed = 3

		self.rect = self.image.get_rect(topleft = (x,80))

	def update(self):
		self.rect.x += self.speed