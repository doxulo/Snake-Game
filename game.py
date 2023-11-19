# game.py
import pygame
import random
from settings import *


class SnakeGame:
    def __init__(self):
        # Start with a snake of three segments
        self.snake_pos = [[100, 50], [90, 50], [80, 50]]
        self.food_pos = [random.randrange(1, (SCREEN_WIDTH // FOOD_SIZE)) * FOOD_SIZE,
                         random.randrange(1, (SCREEN_HEIGHT // FOOD_SIZE)) * FOOD_SIZE]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0

        pygame.font.init()  # Initialize the font module
        self.font = pygame.font.SysFont('Arial', 20)  # Choose a font and size

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.change_to = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.change_to = 'RIGHT'

        # Update the direction
        self.direction = self.change_to

        # Determine the new head position
        new_head_pos = self.snake_pos[0].copy()
        if self.direction == 'UP':
            new_head_pos[1] -= SNAKE_SIZE
        elif self.direction == 'DOWN':
            new_head_pos[1] += SNAKE_SIZE
        elif self.direction == 'LEFT':
            new_head_pos[0] -= SNAKE_SIZE
        elif self.direction == 'RIGHT':
            new_head_pos[0] += SNAKE_SIZE

        # Insert the new head position at the beginning of the snake list
        self.snake_pos.insert(0, new_head_pos)

        # Check if the snake has eaten the food
        if self.snake_pos[0] == self.food_pos:
            self.score += 1
            # Generate new food position
            # Generate new food position
            self.food_pos = [random.randrange(0, SCREEN_WIDTH // FOOD_SIZE) * FOOD_SIZE,
                             random.randrange(0, (
                                         SCREEN_HEIGHT - SCORE_PANEL_HEIGHT) // FOOD_SIZE) * FOOD_SIZE + SCORE_PANEL_HEIGHT]

            # The snake grows, so do not remove the last segment
        else:
            # If the snake has not eaten the food, remove the last segment to maintain its length
            self.snake_pos.pop()

        # Check for collision with boundaries
        if self.snake_pos[0][0] < 0 or self.snake_pos[0][0] >= SCREEN_WIDTH:
            return True  # Game over
        if self.snake_pos[0][1] < 0 or self.snake_pos[0][1] >= SCREEN_HEIGHT:
            return True  # Game over

        # Check for collision with itself
        for block in self.snake_pos[1:]:
            if block == self.snake_pos[0]:
                return True  # Game over

        return False  # Game continues

    def draw_elements(self, window):
        # Clear the screen (or the game area) by filling it with a background color
        window.fill(BACKGROUND_COLOR)  # Fill the entire window
        pygame.draw.rect(window, (30, 30, 30), [0, 0, SCREEN_WIDTH, SCORE_PANEL_HEIGHT])  # Score panel

        # Render and display the score
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))  # White color
        window.blit(score_text, [10, 10])  # Position the score within the panel

        # Draw the snake and food
        for pos in self.snake_pos:
            pygame.draw.rect(window, SNAKE_COLOR,
                             pygame.Rect(pos[0], pos[1] + SCORE_PANEL_HEIGHT, SNAKE_SIZE, SNAKE_SIZE))
        # Draw the food
        pygame.draw.rect(window, FOOD_COLOR, pygame.Rect(self.food_pos[0], self.food_pos[1] + SCORE_PANEL_HEIGHT, FOOD_SIZE, FOOD_SIZE))



