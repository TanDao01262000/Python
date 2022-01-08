import pygame
import sys
from pygame.math import Vector2
import random


class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(3, 0)
        self.is_adding = False
        self.is_over = False

        self.head_up = pygame.image.load('head_up.png')
        self.head_down = pygame.image.load('head_down.png')
        self.head_right = pygame.image.load('head_right.png')
        self.head_left = pygame.image.load('head_left.png')

        self.tail_up = pygame.image.load('tail_up.png')
        self.tail_down = pygame.image.load('tail_down.png')
        self.tail_right = pygame.image.load('tail_right.png')
        self.tail_left = pygame.image.load('tail_left.png')

        self.body_horizontal = pygame.image.load('body_horizontal.png')
        self.body_vertical = pygame.image.load('body_vertical.png')
        self.body_up_right = pygame.image.load('body_tr.png')
        self.body_up_left = pygame.image.load('body_tl.png')
        self.body_down_right = pygame.image.load('body_br.png')
        self.body_down_left = pygame.image.load('body_bl.png')

    def draw_snake(self):
        for index, square in enumerate(self.body):
            x_pos = int(square.x * cell_size)
            y_pos = int(square.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                if self.direction == (1, 0):
                    screen.blit(self.head_right, snake_rect)
                elif self.direction == (-1, 0):
                    screen.blit(self.head_left, snake_rect)
                elif self.direction == (0, 1):
                    screen.blit(self.head_down, snake_rect)
                else:
                    screen.blit(self.head_up, snake_rect)

            elif index == len(self.body) - 1:
                if self.body[len(self.body) - 1] - self.body[len(self.body) - 2] == Vector2(-1, 0):
                    screen.blit(self.tail_left, snake_rect)
                elif self.body[len(self.body) - 1] - self.body[len(self.body) - 2] == Vector2(1, 0):
                    screen.blit(self.tail_right, snake_rect)
                elif self.body[len(self.body) - 1] - self.body[len(self.body) - 2] == Vector2(0, 1):
                    screen.blit(self.tail_down, snake_rect)
                elif self.body[len(self.body) - 1] - self.body[len(self.body) - 2] == Vector2(0, -1):
                    screen.blit(self.tail_up, snake_rect)
            else:
                if self.body[index - 1].y == self.body[index].y == self.body[index + 1].y:
                    screen.blit(self.body_horizontal, snake_rect)
                elif self.body[index - 1].x == self.body[index].x == self.body[index + 1].x:
                    screen.blit(self.body_vertical, snake_rect)

                elif self.body[index - 1] - self.body[index] == Vector2(0, -1) and self.body[index + 1] - self.body[
                    index] == Vector2(-1, 0):
                    screen.blit(self.body_up_left, snake_rect)
                elif self.body[index + 1] - self.body[index] == Vector2(0, -1) and self.body[index - 1] - self.body[
                    index] == Vector2(-1, 0):
                    screen.blit(self.body_up_left, snake_rect)

                elif self.body[index - 1] - self.body[index] == Vector2(0, -1) and self.body[index + 1] - self.body[
                    index] == Vector2(1, 0):
                    screen.blit(self.body_up_right, snake_rect)
                elif self.body[index + 1] - self.body[index] == Vector2(0, -1) and self.body[index - 1] - self.body[
                    index] == Vector2(1, 0):
                    screen.blit(self.body_up_right, snake_rect)

                elif self.body[index - 1] - self.body[index] == Vector2(-1, 0) and self.body[index + 1] - self.body[
                    index] == Vector2(0, 1):
                    screen.blit(self.body_down_left, snake_rect)
                elif self.body[index + 1] - self.body[index] == Vector2(-1, 0) and self.body[index - 1] - self.body[
                    index] == Vector2(0, 1):
                    screen.blit(self.body_down_left, snake_rect)

                elif self.body[index - 1] - self.body[index] == Vector2(1, 0) and self.body[index + 1] - self.body[
                    index] == Vector2(0, 1):
                    screen.blit(self.body_down_right, snake_rect)
                elif self.body[index + 1] - self.body[index] == Vector2(1, 0) and self.body[index - 1] - self.body[
                    index] == Vector2(0, 1):
                    screen.blit(self.body_down_right, snake_rect)

    def move_snake(self):

        if self.is_adding:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.is_adding = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def growth(self):
        self.is_adding = True


class FRUIT:
    def __init__(self):
        self.create()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size,
                                 cell_size)
        # pygame.draw.rect(screen, (226, 166, 104), fruit_rect)
        screen.blit(cherry, fruit_rect)

    def create(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = 0

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def update(self):
        self.snake.move_snake()
        self.is_eating()
        self.is_over()
        self.same_position()

    def is_eating(self):
        if self.snake.body[0] == self.fruit.position:
            print('hit fruit')
            self.fruit.create()
            self.snake.growth()
            self.score += 1

    def is_over(self):
        headless_body = self.snake.body[1:]
        for body_parts in headless_body:
            if self.snake.body[0] == body_parts:
                print('HIT, OVER')

    def same_position(self):
        for body_parts in self.snake.body:
            if self.fruit.position == body_parts:
                self.fruit.create()


pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

# Image for objects
cherry = pygame.image.load('cherry.png').convert_alpha()

# FPS
clock = pygame.time.Clock()

# objects
main = MAIN()


# fruit = FRUIT()
# snake = SNAKE()

def display_score(x, y):
    score_value = main.score
    font = pygame.font.Font("freesansbold.ttf", 32)
    score_text = font.render(str(score_value), True, (255, 0, 0))
    screen.blit(score_text, (x * cell_size, y * cell_size))
    screen.blit(cherry, ((x - 1) * cell_size, y * cell_size))


# Timer for the animation
speed = 100
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# game loop
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            sys.exit()
        if event.type == pygame.USEREVENT:
            # snake.move_snake()
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.snake.direction.y != 1:
                    main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main.snake.direction.y != -1:
                    main.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x != -1:
                    main.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main.snake.direction.x != 1:
                    main.snake.direction = Vector2(-1, 0)

    screen.fill(pygame.Color("green"))
    display_score(1, 1)
    main.draw_elements()


    pygame.display.update()
    clock.tick(1000)
