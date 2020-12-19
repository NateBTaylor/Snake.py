import random
import pygame
import time
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")
in_game = True

clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Comic Sans MS', 25)

size = 20
headx = 200
heady = 200
xvel = 0
yvel = 0
length = 1
snake = [[headx, heady, size, xvel, yvel]] 

applex, appley = random.randrange(0, 20), random.randrange(0, 20)

timer = 60
click_time = 4
check_time = False

playable = True

def draw(part):
  pygame.draw.rect(screen, (100, 235, 52), [part[0], part[1], part[2], part[2]])

def update():
  global headx, heady, size, xvel, yvel, appley, applex
  if xvel != 0 or yvel != 0:
    snake.append([headx + xvel * size, heady + yvel * size, size, xvel, yvel])
    headx += xvel * size
    heady += yvel * size
    snake.remove(snake[0])
  rect = pygame.Rect(headx, heady, size, size)

def display_text(text, color):
  text = my_font.render(text, False, color)
  screen.blit(text, text.get_rect(center = screen.get_rect().center))

while in_game:
  screen.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      in_game = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and click_time == 4 and playable:
        if yvel != 1:
          yvel = -1
          xvel = 0
          check_time = True
      elif event.key == pygame.K_DOWN and click_time == 4 and playable:
        if yvel != -1:
          yvel = 1
          xvel = 0
          check_time = True
      elif event.key == pygame.K_RIGHT and click_time == 4 and playable:
        if xvel != -1:
          yvel = 0
          xvel = 1
          check_time = True
      elif event.key == pygame.K_LEFT and click_time == 4 and playable:
        if xvel != 1:
          yvel = 0
          xvel = -1
          check_time = True
      elif event.key == pygame.K_r:
        snake.clear()
        snake = [[200, 200, 20, 0, 0]]
        headx = 200
        heady = 200
        length = 1
        playable = True
        appley, applex = random.randrange(0, 20), random.randrange(0, 20)

  pygame.draw.rect(screen, (235, 70, 52), [applex * size, appley * size, size, size])

  if check_time:
    click_time -= 1
  if click_time <= 0:
    check_time = False
    click_time = 4

  timer -= 1
  if timer <= 0:
    timer = 60

  for part in snake:
    draw(part)
  if timer % 5 == 0:
    update()
    
  if headx == applex * size and heady == appley * size:
    snake.insert(0, [snake[0][0] + (snake[0][3] * size), snake[0][1] + (snake[0][4] * size), size, xvel, yvel])    
    appley, applex = random.randrange(0, 20), random.randrange(0, 20)
    length += 1
  
  if headx >= 400 or headx <= -1 * size:
    xvel = 0
    yvel = 0
    playable = False
  elif heady >= 400 or heady <= -1 * size:
    xvel = 0
    yvel = 0
    playable = False
  
  if len(snake) > 4:
    for part in range(len(snake) - 1):
      if snake[part][0] == snake[-1][0] and snake[part][1] == snake[-1][1]:
        playable = False
        xvel = 0
        yvel = 0
  
  if playable == False:
    display_text("Your final length was: " + str(length) + "! press r to restart", (255, 255, 255))
  
  clock.tick(60)
  pygame.display.update()

pygame.quit()
quit()