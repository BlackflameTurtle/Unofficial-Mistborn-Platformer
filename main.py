
import random
import pygame
from pygame.locals import *
pygame.font.init()

class Character:
    def __init__(self,background):
        self.background = background
        self.vin = pygame.image.load("modelsandmusic/vin pixelc.png")
        self.char = self.vin
        self.char_x = 200
        self.char_y = 440
        self.horizontal_momentum = 0
        self.coinz = self.char_y
        self.health = 100
        self.knife_x = self.char_x + 67
        self.knife_y = self.char_y - 10
        self.direction = "right"
    def draw(self):

        self.background.fill((255, 200, 200))
        self.background.blit(self.char, (self.char_x , self.char_y))


    def down (self):
        self.gravity = 0.8
        if self.char_y < 440:
            self.char_y += self.gravity
            self.knife_y -= self.gravity


        else:
            self.char_y -= 0
    def momentum_reset(self):
        county = False
        for k in pygame.key.get_pressed():
            if k == True:
                county = True
        if county == False:
            if self.horizontal_momentum > 0:
                self.horizontal_momentum -= 0.6
            if self.horizontal_momentum < 0:
                self.horizontal_momentum += 0.6
    def knife(self):
        if self.direction == "right":
            self.knife_x = self.char_x + 67
        if self.direction == "left":
            self.knife_x = self.char_x - 67

class Coin:
    def __init__(self, background):
        self.background_screen = background
        self.coin = pygame.image.load("modelsandmusic/coin.png")
        self.coin1 = pygame.image.load("modelsandmusic/coin.png")
        self.coin2 = pygame.image.load("modelsandmusic/coin.png")

        self.character = Character(self.background_screen)
        self.coin_y = -1
        self.coin_x = -1
        self.coin_y1 = -1
        self.coin_x1 = - 1
        self.coin_y2 = -1
        self.coin_x2 = -10
        self.coin_num = 10
        self.difference_x = 0
        self.difference_y = 0
        self.collectible_x = 40
        self.collectible_y = 470
    def coin_move_right(self):
        self.coin_x = 890
        self.coin_y = self.character.char_y + self.difference_y
    def coin_move_left(self):
        self.coin_x1 = -5
        self.coin_y1 = self.character.char_y + self.difference_y
    def coin_move_down(self):
        self.coin_y2 = 490
        self.coin_x2 = self.character.char_x + self.difference_x
    def draw(self):
        self.background_screen.blit(self.coin, (self.coin_x , self.coin_y))
        self.background_screen.blit(self.coin1, (self.coin_x1, self.coin_y1))
        self.background_screen.blit(self.coin2, (self.coin_x2, self.coin_y2))


    def num_coins(self):

        model = pygame.image.load("modelsandmusic/coin2.png")
        self.background_screen.blit(model, (3, 3))
        font1 = pygame.font.SysFont("Britannic", 20, bold=False, italic=False)
        line1 = font1.render(f"X{self.coin_num}", True, (0, 0, 0))
        self.background_screen.blit(line1,(25, 3))
    def coin_collectible(self):
        model = pygame.image.load("modelsandmusic/coin.png")
        self.background_screen.blit(model, (self.collectible_x, self.collectible_y))
    def grav(self):
        if self.character.char_y > 440:
            self.difference_y += self.character.gravity






class Platform:
    def __init__(self, background):
        self.background = background
        self.x = 300
        self.y = 400



    def draw(self):

        pygame.draw.rect(self.background, (0,0,0), [self.x, self.y, 240, 6])
        pygame.draw.rect(self.background, (0,0,0), [540, 240, 120, 6])


class Enemies:
    def __init__(self, surface):
        self.koloss = pygame.image.load("modelsandmusic\koloss.png")
        self.koloss_x = 340
        self.koloss_y = 430
        self.surface = surface
        self.health = 100
    def draw_koloss(self):
        if self.health > 0:
            self.surface.blit(self.koloss, (self.koloss_x, self.koloss_y))
        floor = pygame.transform.rotate(self.koloss, 270)
        if self.health == 0:

            self.surface.blit(floor, (self.koloss_x, self.koloss_y + 50))

class Game:
    def __init__(self):

        self.character = Character(self.surface)
        self.character.draw()
        self.character.down()
        self.coin = Coin(self.surface)
        self.coin.draw()
        self.coin.num_coins()
        self.platform = Platform(self.surface)
        self.platform.draw()
        self.coin.coin_collectible()
        self.platy = False
        self.state = "jump"
        self.enemies = Enemies(self.surface)
        self.enemies.draw_koloss()
        self.attack = True
        self.knock = False
        self.counter = 0

    def right_coin_reset(self):
        self.coin.coin_y = -20
    def left_coin_reset(self):
        self.coin.coin_y1 = -20
    def down_coin_reset(self):
        self.coin.coin_x2 = -20



    def platform_collide(self, x1, y1, x2, y2, width2):
        if x2 + width2 >= x1 >= x2 - 51:
            if y2 + 6 >= y1 + 55 >= y2 - 6:
                return True
        return False

    def collectible_collide(self, x1, y1, x2, y2):
        if x1 -10 <= x2 <= x1 + 57:
            if y1 <= y2 <= y1 + 51:
                return True
        return False
    def koloss_collide(self, x1, y1, x2, y2):
        if x1 <= x2 <= x1 + 57:
            if y1 - 10 <= y2 <= y1:
                return True
            else:
                return False
    def attack_koloss(self, x1, y1, x2, y2):
        if y1+ 70 >= y2 and y1 <= y2 + 57:
            if x1 - 20 <= x2 <= x1 + 57:

                return True
        return False


    def play(self):
        self.character.down()
        self.coin.grav()
        self.character.draw()
        self.coin.num_coins()
        self.platform.draw()
        self.enemies.draw_koloss()
        self.coin.draw()
        self.coin.coin_collectible()
        self.character.momentum_reset()

        if self.platform_collide(self.character.char_x, self.character.char_y, self.platform.x, self.platform.y, 240):
            self.character.char_y -= self.character.gravity
            self.state = "jump"
            self.coin.coin_y1 = self.character.char_y
            self.coin.coin_y = self.character.char_y
        elif self.platform_collide(self.character.char_x, self.character.char_y, 540, 240,120):
            self.character.char_y -= self.character.gravity

            self.state = "jump"
            self.coin.coin_y1 =self.character.char_y
            self.coin.coin_y =self.character.char_y
        elif self.collectible_collide(self.character.char_x, self.character.char_y, self.coin.collectible_x, self.coin.collectible_y):
            self.coin.coin_num += 1
        elif self.koloss_collide(self.character.char_x, self.character.char_y, self.enemies.koloss_x, self.enemies.koloss_y):
            self.character.health -= 35
            print(self.character.health)
            #while self.counter > -30:
             #   self.character.char_x -= 10
              #  self.character.char_y -= 4
                #self.counter -= 2
                #self.coin.difference_x -= 10
        if self.counter <= -30:
            self.counter =0



        if self.attack_koloss(self.enemies.koloss_x, self.character.knife_y, self.character.knife_x, self.enemies.koloss_y):

            if self.attack:
                health = self.enemies.health
                if self.enemies.health > 0:

                    self.enemies.health -= 10


                self.attack = False
                print(self.enemies.health)
        if self.character.health <= 0:
            pass









    def run(self):
        running = True
        down_coin = False
        right_coin = False
        left_coin = False
        self.direction = "right"
        self.state = "jump"
        possible_state = ["jump", "platform", "stand"]
        posture = "stand"
        self.attack = False

        while running:

            if self.character.char_y >= 440:
                self.state = "jump"

            if posture == "stand":
                if self.character.direction == "right":
                    self.character.char = self.character.vin
                if self.character.direction == "left":
                    self.character.char = self.vin2
            if posture == "barreling left":
                self.character.char = pygame.transform.rotate(self.character.vin, 90)
            if posture == "barreling right":
                self.character.char = pygame.transform.rotate(self.character.vin, 270)
            if down_coin:
                if self.character.char_y < 440:
                    self.character.char_y -= self.character.gravity
                    self.coin.difference_y -= self.character.gravity
                    self.character.knife_y -= self.character.gravity


                #else:
                    #self.coin.coin_y -= 1
                    #self.coin.coin_y2 -= 1
                    #self.coin.coin_y1 -= 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                pygame.key.set_repeat(1, 3)
                if event.type == KEYDOWN:
                    if not down_coin :
                        if event.key == K_DOWN:
                            pygame.key.set_repeat(1, 10000000)
                            if self.coin.coin_num > 0:
                                down_coin = True
                                self.coin.coin_move_down()
                                self.coin.coin_num -= 1
                    if down_coin:
                        if event.key == K_SEMICOLON:
                            pygame.key.set_repeat(1, 10000000)
                            self.coin.coin_num += 1
                            down_coin = False
                            self.down_coin_reset()
                    if not left_coin:
                        if event.key == K_LEFT:
                            pygame.key.set_repeat(1, 10000000)
                            if self.coin.coin_num > 0:
                                left_coin = True
                                self.coin.coin_move_left()

                                self.coin.coin_num -= 1
                    if left_coin:
                        if event.key == K_PERIOD:
                            pygame.key.set_repeat(1, 1000000)
                            self.coin.coin_num += 1
                            self.left_coin_reset()
                            pygame.display.flip()
                            left_coin = False
                    if not right_coin:
                        if event.key == K_RIGHT:
                            pygame.key.set_repeat(1, 10000000)
                            if self.coin.coin_num > 0:
                                self.coin.coin_num -= 1
                                right_coin = True
                                self.coin.coin_move_right()


                    if right_coin is True:
                        if event.key == K_SLASH:
                            pygame.key.set_repeat(1, 100000)
                            self.coin.coin_num += 1
                            self.right_coin_reset()
                            pygame.display.flip()
                            right_coin = False


                    if event.key == K_f:
                        pygame.key.set_repeat(1, 10000000)
                        self.attack = "True"
                    if not down_coin:
                        if event.key == K_SPACE:
                            pygame.key.set_repeat(1, 10000000)
                            if self.state == "jump":
                                self.character.char_y -= 120
                                self.coin.coin_y1 = self.character.char_y
                                self.coin.coin_y = self.character.char_y
                                if 840 > self.character.char_x > 10:
                                    self.character.char_x += self.character.horizontal_momentum
                                    #if self.character.char_x + self.character.horizontal_momentum > 790:
                                    #    self.character.horizontal_momentum += (790 -(self.character.char_x + self.character.horizontal_momentum))
                                    #if self.character.char_x + self.character.horizontal_momentum < 10:
                                     #   self.character.horizontal_momentum -= (10 - (self.character.char_x + self.character.horizontal_momentum))
                                    self.coin.difference_x += self.character.horizontal_momentum
                                    if self.character.char_x < 0:
                                        self.coin.difference_x += 5 - self.character.char_x
                                        self.character.char_x = 5
                                    if self.character.char_x > 840:
                                        self.coin.difference_x += 840 - self.character.char_x
                                        self.character.char_x = 840
                                self.state = "stand"




                        if event.key == K_d:
                            if self.character.char_x < 840:
                                self.character.char_x += 2
                                if self.character.direction == "left":
                                    self.character.direction = "right"
                                self.coin.difference_x += 2
                                self.character.knife_x += 2
                                posture = "stand"
                                if self.character.horizontal_momentum < 0:
                                    self.character.horizontal_momentum = 0
                                if self.character.horizontal_momentum < 150:
                                    self.character.horizontal_momentum += 0.6

                        if event.key == K_a:
                            if self.character.char_x > 0:
                                self.character.char_x -= 2
                                if self.character.direction == "right":
                                    self.character.direction = "left"
                                self.coin.difference_x -= 2
                                self.character.knife_x -=2
                                posture = "stand"
                                if self.character.horizontal_momentum > 0:
                                    self.character.horizontal_momentum = 0
                                if self.character.horizontal_momentum > -150:
                                    self.character.horizontal_momentum -= 0.6
                    if self.character.direction == "left":
                        self.vin2 = pygame.transform.flip(self.character.vin, True, False)
                        self.character.char = self.vin2
                    if self.character.direction == "right":
                        self.character.char = self.character.vin


                    if down_coin:

                        if event.key == K_SPACE:
                            self.character.char_y -= 3
                        if event.key == K_a:
                            if self.character.char_x > 0:
                                self.character.char_x -= 1
                            down_coin = False
                            self.down_coin_reset()

                        if event.key == K_s:
                            if self.character.char_y < 440:
                                pygame.key.set_repeat(1, 1000000)
                                self.character.char_y += 20
                        if event.key == K_d:
                            if self.character.char_x < 870:
                                self.character.char_x += 1
                            down_coin = False
                            self.down_coin_reset()
                    if left_coin:

                        if self.character.char_y >=self.coin.coin_y1 + 40:
                            left_coin = False
                            self.left_coin_reset()

                        if self.character.char_y < self.coin.coin_y1:
                            left_coin = False
                            self.left_coin_reset()
                        counter = False
                        for k in pygame.key.get_pressed():
                            if k ==  True:
                                counter = True
                        if counter ==  False:
                            posture = "stand"
                            self.character.char = self.character.vin
                        else:
                            if event.key == K_d:
                                if 840 > self.character.char_x :
                                    self.character.char_x += 15
                                    self.character.char = pygame.transform.rotate(self.character.vin, 270)
                                    self.coin.difference_x += 15
                                    posture = "barreling right"
                                    self.character.direction = "right"
                                    if self.character.horizontal_momentum < 0:
                                        self.character.horizontal_momentum = 0
                                    if self.character.horizontal_momentum < 200:
                                        self.character.horizontal_momentum += 12
                                    if self.character.horizontal_momentum > 200:
                                        self.character.horizontal_momentum = 200
                                if 790 < self.character.char_x < 840:
                                    self.character.char = pygame.transform.rotate(self.character.vin, 315)
                                    posture = "barreling right"
                                    self.character.direction = "right"



                    if right_coin is True:

                        if self.character.char_y >= self.coin.coin_y + 40:
                            right_coin = False
                            self.right_coin_reset()
                        if self.character.char_y < self.coin.coin_y:
                            right_coin = False
                            self.right_coin_reset()

                        counter = False
                        for k in pygame.key.get_pressed():

                            if k == True:
                                counter = True
                        if counter == False:
                            posture = "stand"
                        else:
                            if event.key == K_a:
                                if self.character.char_x > 0:
                                    self.character.char_x -= 15
                                    self.character.char = pygame.transform.rotate(self.character.vin, 90)
                                    self.coin.difference_x -= 15
                                    posture = "barreling left"
                                    self.character.direction = "left"
                                    if self.character.horizontal_momentum > 0:
                                        self.character.horizontal_momentum = 0
                                    if self.character.horizontal_momentum > -200:
                                        self.character.horizontal_momentum -= 12
                                    if self.character.horizontal_momentum < -200:
                                        self.character.horizontal_momentum = -200
                                if self.character.char_x < 50:
                                    self.character.char = pygame.transform.rotate(self.character.vin, 45)
                                    posture = "barreling left"
                                    self.character.direction = "left"









            self.play()
            pygame.display.flip()
















if __name__ == '__main__':
    game = Game()
    game.run()
