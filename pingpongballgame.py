import pygame
import random
import sys

class PongBall:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_speed = random.randint(1, 5)
        self.y_speed = random.randint(1, 5)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def bounce(self, paddle):
        if (
            self.x - self.radius < paddle.x + paddle.width / 2
            and self.x + self.radius > paddle.x - paddle.width / 2
            and self.y - self.radius < paddle.y + paddle.height / 2
            and self.y + self.radius > paddle.y - paddle.height / 2
        ):
            self.x_speed *= -1

    def reset_position(self):
        self.x = 0
        self.y = 0
        self.x_speed = random.randint(1, 5)
        self.y_speed = random.randint(1, 5)

class PongPaddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def move_up(self):
        self.y += 20

    def move_down(self):
        self.y -= 20

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong Game")

    ball = PongBall(0, 0, 10, (255, 255, 255))
    left_paddle = PongPaddle(0, 0, 10, 50, (255, 0, 0))
    right_paddle = PongPaddle(750, 0, 10, 50, (0, 0, 255))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the left paddle towards the ball
        left_paddle.y = ball.y - left_paddle.height / 2

        # Move the right paddle with the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            right_paddle.move_down()
        if keys[pygame.K_DOWN]:
            right_paddle.move_up()

        # Move the ball
        ball.move()

        # Bounce the ball off the paddles
        ball.bounce(left_paddle)
        ball.bounce(right_paddle)

        # Check if the ball has gone off the screen
        if int(ball.x) > 400 or int(ball.x) < -400:
            ball.reset_position()

        # Draw the screen
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, ball.color, (int(ball.x), int(ball.y)), ball.radius)
        pygame.draw.rect(screen, left_paddle.color, (left_paddle.x, left_paddle.y, left_paddle.width, left_paddle.height))
        pygame.draw.rect(screen, right_paddle.color, (right_paddle.x, right_paddle.y, right_paddle.width, right_paddle.height))

        # Update the display
        pygame.display.flip()

        # Limit the framerate
        clock.tick(60)

if __name__ == "__main__":
    main()
