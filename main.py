# main.py
import pygame
import sys
from settings import *
from game import SnakeGame

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    game = SnakeGame()

    print("Game Started")  # Debug message

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game state
        game_over = game.update(events)

        # Render game objects
        game.draw_elements(window)

        pygame.display.update()

        # Check if game is over
        if game_over:
            print(f"Game Over! Your Score: {game.score}")  # Debug message
            running = False

        # Increase the speed based on the score
        speed = 10 + game.score // 5  # Increase speed every 5 points
        clock.tick(speed)  # Adjust the frame rate based on the speed

    print("Game Ended")  # Debug message

if __name__ == "__main__":
    main()
