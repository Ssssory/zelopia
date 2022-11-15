import pygame, sys
from settings import *
from levels.level import Level
from state import State
from levels.arena import Arena

PLAYER = pygame.USEREVENT + 1 
class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption(NAME)
		self.clock = pygame.time.Clock()

		state = State()

		# self.level = Level()
		self.level = Arena(state)

		# sound 
		# main_sound = pygame.mixer.Sound('../audio/main.ogg')
		# main_sound.set_volume(0.5)
		# main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				# if event.type == pygame.KEYDOWN:
				# 	if event.key == pygame.K_m:
				# 		self.level.toggle_menu()

				if event.type == PLAYER:
					self.font = pygame.font.Font(UI_FONT,80)
					text = self.font.render("Game Over", 1, 'Red')
					self.screen.blit(text,(300,300))
					pygame.display.update()
					pygame.time.delay(1000)
					pygame.quit()
					break

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()