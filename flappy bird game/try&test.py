# import pygame as p
# import sys as s
# import random as r

# # Global variables
# FPS = 32
# Screen_Width = 289
# Screen_Height = 511
# Screen = p.display.set_mode((Screen_Width, Screen_Height))
# Game_Sprites = {}
# Game_sounds = {}

# # Assets
# Flappy_Bird = "assets/flappy bird.png"
# Background = "assets/background.jfif"
# Pipe = "assets/pipe.jfif"

# # Sounds
# point = "sounds/point.mp3"
# swosh = "sounds/swosh.mp3"
# hit = "sounds/hit.mp3"
# flap = "sounds/flap.mp3"
# out = "sounds/out.mp3"

# while True:
#   # Function for welcoming the user
#   def Welcome_Screen():
#     p.display.get_surface( Game_Sprites["Background"],(0, 0))

#   # Main game loop
#   def main_game():
#     Flappy_Birdy = Screen_Height / 2
  
#       #  if user has to quit the game
#     for event in p.event.get():
#       if event.type == quit or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
#         p.quit()
#         s.exit()

#       elif event.type == p.KEYDOWN and (event.key == p.k_SPACE or event.key == p.K_UP):
#         Game_sounds['flap'].play()
#         Flappy_Birdy -= 20

#       # Update the game state
#       Flappy_Birdy += 2
#       if Flappy_Birdy >= Screen_Height or Flappy_Birdy <= 0:
#         break

#       # Render the game state
#       p.screen.blit(Game_Sprites["Background"], (0, 0))
#       p.screen.blit(Game_Sprites["Flappy_Bird"], (int(Screen_Width / 5), Flappy_Birdy))

#       # Update the display
#       p.display.flip()
      
#       # Check for collisions
#       pipes = Game_Sprites["pipe"]
#       for pipe in pipes:
#         if pipe.colliderect((0, Flappy_Birdy, 289, 511)):
#           Game_sounds['hit'].play()
#           break

#   # Initialize Pygame
#   if __name__ == "__main__":
#     p.init()
#     FPS_Clock = p.time.Clock()
#     p.display.set_caption("Flappy Bird Game")
#     Game_Sprites["numbers"]= (
#       p.image.load("assets/2.png.png").convert_alpha(),
#       p.image.load("assets/3.png.png").convert_alpha(),
#       p.image.load("assets/1.png.png").convert_alpha(),
#       p.image.load("assets/4.png.jfif").convert_alpha(),
#       p.image.load("assets/5.png.png").convert_alpha(),
#       p.image.load("assets/6.png.jfif").convert_alpha(),
#       p.image.load("assets/7.png.png").convert_alpha(),
#       p.image.load("assets/8.png.png").convert_alpha(),
#       p.image.load("assets/9.png.png").convert_alpha(),
#       p.image.load("assets/0.png.png").convert_alpha(),
#     )


#   Game_Sprites["Background"] = p.image.load("assets/background.jfif").convert_alpha(),
#   Game_Sprites["pipe"] = (
#     p.image.load("assets/pipe.jfif").convert_alpha(),
#     p.transform.rotate (p.image.load("assets/pipe.jfif").convert_alpha(),180)
#   )

#   Game_Sprites['Flappy_Bird'] = p.image.load("assets/flappy bird.png")
#   Welcome_Screen()
#   main_game()
#   p.display.flip()
#   p.display.update()
  