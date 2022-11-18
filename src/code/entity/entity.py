import pygame
from math import sin
from state import State

class Entity(pygame.sprite.Sprite):
	def __init__(self,groups):
		super().__init__(groups)
		self.frame_index = 0
		self.animation_speed = 0.15
		self.direction = pygame.math.Vector2()

		self.obstacle_sprites = State().getSpriteGroup('obstacle')

	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					self.sliding(self,sprite, direction)
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):					
					self.sliding(self,sprite, direction)
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def sliding(self, object, subject, direction):
		pass
		# TODO: fix bug with coordinates
		# if direction == 'vertical':
		# 	if subject.hitbox.center[0] > object.hitbox.center[0]:
		# 		object.direction.x = -1
		# 		object.hitbox.x += object.direction.x * 1
		# 	else:
		# 		object.direction.x = 1
		# 		object.hitbox.x += object.direction.x * 1
		# else:
		# 	if subject.hitbox.center[1] > object.hitbox.center[1]:
		# 		object.direction.y = -1
		# 		object.hitbox.y += object.direction.y * 1
		# 	else:
		# 		object.direction.y = 1
		# 		object.hitbox.y += object.direction.y * 1


	def wave_value(self):
		value = sin(pygame.time.get_ticks())
		if value >= 0: 
			return 255
		else: 
			return 0