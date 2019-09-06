import pygame

pygame.display.init()
pygame.mixer.init()
pygame.font.init()

pygame.mixer.music.load('pong_sound.mp3')
font = pygame.font.SysFont('optimattc', 25, 0, 0) 

class Game:
    width = 640
    height = 400
    running = True
    movementY = 6
    movementX = 6

    white = (255, 255, 255, 255)
    playerWidth = 10
    playerHeight = 60
    y = 0
    ballX, ballY = 0, 0
    movementY = 6
    movementX = 6
    scoreP1, scoreP2 = 0, 0
    ballRadius = 4
    playerMove = 10

    def __init__(self, pygame, font):
        self.pygame = pygame
        self.font = font


    def init(self):
        screen = pygame.display.set_mode((self.width, self.height))
        self.run(self.pygame, screen)


    def reset(self):
        self.startPositions()
        self.movementY = 6
        self.movementX = 6


    def startPositions(self):
        self.y = int((self.height - self.playerHeight) / 2)
        self.ballX, self.ballY = int(self.width / 2), int(self.height / 2)
    

    def changeMovement(self, playerY, ballY):
        hit = playerY - ballY
        
        if hit < 0 and hit > -25:
            self.movementY = int(self.movementY * 1.5) 
            if self.movementY > 0:
                self.movementY *= -1  
        elif hit < -35 and hit > -60:
            self.movementY = int(self.movementY * 1.5) 
            if self.movementY < 0:
                self.movementY *= -1
        else:
            if self.movementY > 0:
                self.movementY = 6
            else:
                self.movementY = -6
    

    def checkCollision(self, ballX, ballY): 
        if ballY + self.ballRadius >= self.height:
            self.movementY *= -1
            pygame.mixer.music.play()
            return True
        elif ballY - self.ballRadius <= 0:
            self.movementY *= -1
            pygame.mixer.music.play()
            return True
        elif ballX < 20 and (ballY <= self.y + self.playerHeight and ballY >= self.y):
            self.changeMovement(self.y, ballY)

            self.movementX *= -1
            pygame.mixer.music.play()
            return True
        elif ballX > self.width - 20 and (ballY <= ballY + self.playerHeight and ballY >= ballY):
            self.changeMovement(ballY, ballY)

            self.movementX *= -1
            pygame.mixer.music.play()
            return True
        elif ballX < 10:
            self.scoreP2 += 1
            self.reset() # player2 won
            return False
        elif ballX > self.width - 10:
            self.scoreP1 += 1
            self.reset() # player1 won
            return False
        else:
            return True

    def run(self, pygame, screen):
        self.startPositions()

        while self.running:
            screen.fill((0, 0, 0, 255))    
            textP1 = self.font.render(f'{self.scoreP1}', True, self.white)
            textP2 = self.font.render(f'{self.scoreP2}', True, self.white)
            screen.blit(textP1, (self.width / 2 - 40, 10))
            screen.blit(textP2, (self.width / 2 + 30, 10))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # movement
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.y += self.playerMove
                
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.y -= self.playerMove

            if self.movementX > 0 and self.movementY > 0:
                if self.checkCollision(self.ballX + self.movementX + self.ballRadius, self.ballY + self.movementY + self.ballRadius):
                    pass
            elif self.movementX > 0 and self.movementY < 0:
                if self.checkCollision(self.ballX + self.movementX + self.ballRadius, self.ballY + self.movementY - self.ballRadius):
                    pass
            elif self.movementX < 0 and self.movementY > 0:
                if self.checkCollision(self.ballX + self.movementX - self.ballRadius, self.ballY + self.movementY + self.ballRadius):
                    pass
            else:
                if self.checkCollision(self.ballX + self.movementX - self.ballRadius, self.ballY + self.movementY - self.ballRadius):
                    pass
            self.ballX += self.movementX
            self.ballY += self.movementY

            #player1
            pygame.draw.rect(screen, self.white, (10, self.y, self.playerWidth, self.playerHeight))
            #player2
            pygame.draw.rect(screen, self.white, (self.width - self.playerWidth - 10, self.ballY - 30, self.playerWidth, self.playerHeight))
            #ball
            pygame.draw.circle(screen, self.white, (self.ballX, self.ballY), 8)
            #line
            pygame.draw.line(screen, self.white, (self.width / 2, 0), (self.width / 2, self.height), 1)

            pygame.display.flip()

        pygame.display.quit()

game = Game(pygame, font)
game.init()
