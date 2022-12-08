import pygame
import random
import sys
from pygame.locals import *

# initialize pygame
pygame.init()

# create game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# create game clock
clock = pygame.time.Clock()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# define snake properties
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# define food properties
food_position = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
food_spawn = True

# define direction variables
direction = "RIGHT"
change_to = direction

# game over function
def game_over():
  my_font = pygame.font.SysFont('times new roman', 20)
  game_over_surface = my_font.render('Game Over!', True, WHITE)
  game_over_rect = game_over_surface.get_rect()
  game_over_rect.midtop = (window_width/2, window_height/2)
  window.blit(game_over_surface, game_over_rect)
  pygame.display.flip()
  pygame.time.wait(1000)  # use pygame.time.wait() to pause the game
  pygame.quit() # quit pygame
  sys.exit() # exit program

# main game loop
while True:
  # get events from the event queue
  for event in pygame.event.get():
    # quit the game if the quit button is pressed
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    # change the direction of the snake when an arrow key is pressed
    elif event.type == KEYDOWN:
      if event.key == K_UP:
        change_to = "UP"
      if event.key == K_DOWN:
        change_to = "DOWN"
      if event.key == K_LEFT:
        change_to = "LEFT"
      if event.key == K_RIGHT:
        change_to = "RIGHT"

  # validate direction change
  if change_to == "UP" and direction != "DOWN":
    direction = "UP"
  if change_to == "DOWN" and direction != "UP":
    direction = "DOWN"
  if change_to == "LEFT" and direction != "RIGHT":
    direction = "LEFT"
  if change_to == "RIGHT" and direction != "LEFT":
    direction = "RIGHT"

  # move the snake
  if direction == "UP":
    snake_position[1] -= 10
  if direction == "DOWN":
    snake_position[1] += 10
  if direction == "LEFT":
    snake_position[0] -= 10
  if direction == "RIGHT":
    snake_position[0] += 10

# snake body growing
    snake_body.insert(0, list(snake_position))  # add closing parenthesis

# check if snake has collided with boundaries
    if snake_position[0] == -1 or snake_position[0] == window_width or snake_position[1] == -1 or snake_position[1] == window_height:
        game_over()  # indent code within the if block

# check if snake has collided with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()  # indent code within the if block

# check if snake has eaten food
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
    else:
        nake_body.pop()

# spawn food
    if not food_spawn:
        food_position = [random.randrange(1, (window_width//10)) * 10, random.randrange(1, (window_height//10)) * 10]
    food_spawn = True

# draw snake
    window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(window, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))

# draw food
    pygame.draw.rect(window, WHITE, pygame.Rect(food_position[0], food_position[1], 10, 10))

# update display
    pygame.display.update()

# set game speed
    clock.tick(10)
