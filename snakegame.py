import pygame
import random

# Initialize game display
pygame.init()
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.change_direction_to = self.direction

    def change_direction(self, direction):
        if direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if direction == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, food_pos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0, list(self.position))
        if self.position == food_pos:
            return 1
        else:
            self.body.pop()
            return 0

# Game over function
def game_over(score, play_again):
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render("Game Over", True, red)
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (display_width/2, display_height/4)
    game_display.blit(game_over_screen, game_over_rect)
    score_font = pygame.font.Font('freesansbold.ttf', 50)
    score_screen = score_font.render

