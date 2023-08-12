import pygame as p
import sys as s

def main():
  # Initialize Pygame
  p.init()

  # Global Variables 
  background = p.image.load("assets/background.jpg")
  player = p.image.load("assets/flappy_bird.png ")
  player_X = 0
  player_y = 397/2
  pipe = p.image.load("assets/pipe.png")
  numbers_2 = p.image.load("assets/2.png.png")
  numbers_3 = p.image.load("assets/3.png.png")
  numbers_1 = p.image.load("assets/1.png.png")
  numbers_4 = p.image.load("assets/4.png.png")
  numbers_5 = p.image.load("assets/5.png.png")
  numbers_6 = p.image.load("assets/6.png.png")
  numbers_7 = p.image.load("assets/7.png.png")
  numbers_8 = p.image.load("assets/8.png.png")
  numbers_0 = p.image.load("assets/0.png.png")
  numbers_9 = p.image.load("assets/9.png.png")



  

  # Create a display surface
  screen = p.display.set_mode((289, 397))

  # Blit the background image to the screen
  screen.blit(background, (0, 0))
  screen.blit(player,(player_X,player_y))
  screen.blit(numbers_0,(287/3,0))
  screen.blit(numbers_1,(287/3,0))
  screen.blit(numbers_2,(287/3,0))
  screen.blit(numbers_3,(287/3,0))
  screen.blit(numbers_4,(287/3,0))
  screen.blit(numbers_5,(287/3,0))
  screen.blit(numbers_6,(287/3,0))
  screen.blit(numbers_7,(287/3,0))
  screen.blit(numbers_8,(287/3,0))
  screen.blit(numbers_9,(289/3,0))
  
  # let's add pipes
  screen.blit(pipe,(0 ,289))
  # .rotate (p.image.load("assets/pipe.jfif").convert_alpha(),180)


  # Update the display
  p.display.flip()

  # Keep the game running
  while True:
    for event in p.event.get():
      if event.type == p.QUIT or(event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
        p.quit()
        s.exit()
      elif (event.type == p.KEYDOWN and event.key == p.K_SPACE):
          player_y -= 20
          player_y += 2

    
  
  

    # Update the display
      p.display.update()

    # Delay for 100 milliseconds
      p.time.delay(100)

        

# Run the main function
if __name__ == "__main__":
  main()

