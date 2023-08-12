import pygame
import sys
import random

def main():
  # Initialize Pygame
  pygame.init()

  # Create the screen
  screen = pygame.display.set_mode((289, 397))

  # Load the images
  background_image = pygame.image.load("assets/background.jpg")
  bird_image = pygame.image.load("assets/flappy_bird.png")
  pipe_image = pygame.image.load("assets/pipe.png")

  # Create the bird
  bird = pygame.Rect(100, 200, 50, 50)

  # Create the pipes
  pipes = []
  for i in range(0, 100000):
    pipe_height = random.randint(0, 300)
    pipes.append(pygame.Rect(200 + i * 100, pipe_height, 100, 200))

  # Game loop
  while True:
    # Check for events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        bird.y -= 30 

    # Update the bird
    bird.y += 5  

    # Check if the bird hits the ground
    if bird.y > 397:
      pygame.quit()
      sys.exit()

    # Check if the bird hits a pipe
    collision_rect = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
    if collision_rect.colliderect(pipe) or collision_rect.colliderect(pipe.topleft) or collision_rect.colliderect(pipe.bottomright):
      pygame.quit()
      sys.exit()


    # Update the pipes
    for i in range(0, len(pipes) - 1):
      pipes[i].x -= 5
      pipes[-1] = pipes[0].copy()
      pipes[0].x = 500

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the bird
    screen.blit(bird_image, bird)

    # Draw the pipes
    for pipe in pipes:
      if pipe.y < 397:
        screen.blit(pipe_image, pipe)
      else:
        pipe_height = random.randint(0, 300)
        pipe = pygame.Rect(500, pipe_height, 100, 200)
        pipes.append(pipe)

    # Update the display
    pygame.display.flip()

    # Delay for 10 milliseconds
    pygame.time.delay(10)

if __name__ == "__main__":
  main()
