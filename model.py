import pygame
import time
import random
from snake import Snake

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


class Model():
    def __init__(self):
        self.speed = 15
        self.win_x = 500
        self.win_y = 500
        pygame.init()
        pygame.display.set_caption('Snake AI')
        self.game_window = pygame.display.set_mode((self.win_x, self.win_y))
        self.fps = pygame.time.Clock()
        # WILL DELETE
        # self.snake_position = [250, 250]
        # self.snake_body = [[250, 250], [240, 250], [230, 250]]
        self.score = 0
        self.direction = 'RIGHT'
        self.change_to = 'RIGHT'
        self.score = 0
        self.snake = Snake(self.game_window, self.win_x, self.win_y)

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(self.score), True, self.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.win_x / 2, self.win_y / 4)
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        quit()

    def gameLoop(self):
        while True:

            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_UP:
                #         self.change_to = 'UP'
                #     if event.key == pygame.K_DOWN:
                #         self.change_to = 'DOWN'
                #     if event.key == pygame.K_LEFT:
                #         self.change_to = 'LEFT'
                #     if event.key == pygame.K_RIGHT:
                #         self.change_to = 'RIGHT'
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            # If two keys pressed simultaneously
            # we don't want snake to move into two
            # directions simultaneously
            # if self.change_to == 'UP' and self.direction != 'DOWN':
            #     self.direction = 'UP'
            # if self.change_to == 'DOWN' and self.direction != 'UP':
            #     self.direction = 'DOWN'
            # if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            #     self.direction = 'LEFT'
            # if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            #     self.direction = 'RIGHT'

            # Moving the snake
            self.snake.move()
            # if self.direction == 'UP':
            #     self.snake_position[1] -= 10
            # if self.direction == 'DOWN':
            #     self.snake_position[1] += 10
            # if self.direction == 'LEFT':
            #     self.snake_position[0] -= 10
            # if self.direction == 'RIGHT':
            #     self.snake_position[0] += 10

            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            # self.snake_body.insert(0, list(self.snake_position))
            # if self.snake_position[0] == self.food[0] and self.snake.pos[1] == self.food[1]:
            #     self.score += 10
            #     self.food.spawn = False
            # else:
            #     self.snake_body.pop()

            # if not self.food.spawn:
            #     self.food.new()

            # self.food.spawn = True
            self.game_window.fill(black)

            self.snake.show()
            # for pos in self.snake_body:
            #     pygame.draw.rect(self.game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
            #self.food.draw(self.game_window)

            # Game Over conditions
            # if self.snake_position[0] < 0 or self.snake_position[0] > self.win_x - 10:
            #     self.game_over()
            # if self.snake_position[1] < 0 or self.snake_position[1] > self.win_y - 10:
            #     self.game_over()

            # Touching the snake body
            # for block in self.snake_body[1:]:
            #     if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
            #         self.game_over()

            # displaying score countinuously
            self.show_score(1, white, 'times new roman', 20)

            # Refresh game screen
            pygame.display.update()

            # Frame Per Second /Refresh Rate
            self.fps.tick(self.speed)


class Food():
    def __init__(self, win_x, win_y):
        self.win_x = win_x
        self.win_y = win_y
        self.pos = [random.randrange(1, (self.win_x // 10)) * 10,
                    random.randrange(1, (self.win_y // 10)) * 10]
        self.spawn = True

    def __getitem__(self, key):
        return self.pos[key]

    def new(self):
        self.pos = [random.randrange(1, (self.win_x // 10)) * 10,
                    random.randrange(1, (self.win_y // 10)) * 10]

    def draw(self, game_window):
        pygame.draw.rect(game_window, white, pygame.Rect(self.pos[0], self.pos[1], 10, 10))


if __name__ == '__main__':
    m = Model()
    m.gameLoop()