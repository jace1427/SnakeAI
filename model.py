import pygame
import time
from food import Food
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
        self.score = 0
        self.direction = 'RIGHT'
        self.change_to = 'RIGHT'
        self.score = 0
        self.snake = Snake()
        self.food = Food(self.win_x, self.win_y)

    def showScore(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def gameOver(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(self.score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.win_x / 2, self.win_y / 4)
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        quit()

    def drawFood(self):
        pygame.draw.rect(self.game_window, white, pygame.Rect(self.food.pos[0], self.food.pos[1], 10, 10))

    def drawSnake(self):
        for pos in self.snake.tailpos:
            pygame.draw.rect(self.game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    def gameLoop(self):
        while True:

            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            # Moving the snake
            if self.snake.move(self.food.pos):
                while [self.food.pos[0], self.food.pos[1]] in self.snake.tailpos:
                    self.Food.new()

            if self.snake.alive is False:
                self.gameOver()

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
            self.drawFood()
            self.drawSnake()
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
            self.showScore(1, white, 'times new roman', 20)

            # Refresh game screen
            pygame.display.update()

            # Frame Per Second /Refresh Rate
            self.fps.tick(self.speed)


if __name__ == '__main__':
    m = Model()
    m.gameLoop()