import pygame, random

class Apple:
    def __init__(self):
        pass

class Game:
    running = True
    body = [ ]
    length = 0
    white = (255, 255, 255, 255)
    red = (255, 0, 0, 255)
    move = {
        'x': 20,
        'y': 0,
    }
    applePosition = {
        'x': 0,
        'y': 0,
    }

    def __init__(self, pygame):
        self.pygame = pygame


    def init(self):
        screen = self.pygame.display.set_mode((400, 400))
        self.start(self.pygame, screen)
    

    def randomPosition(self):
        x = random.randrange(21) * 20
        y = random.randrange(21) * 20
        self.applePosition['x'] = x
        self.applePosition['y'] = y

    
    def eateApple(self, position):
        if position['x'] == self.applePosition['x'] and position['y'] == self.applePosition['y']:
            self.body.append({'x': self.applePosition['x'], 'y': self.applePosition['y']})
            self.length += 1
            return True
        return False


    def checkColision(self, position):
        if position['x'] > 400 or position['x'] < 0 or position['y'] > 400 or position['y'] < 0:
            pygame.display.quit()


    def start(self, pygame, screen):
        position = {
            'x': 200,
            'y': 200,
        }
        loop = 0
        self.randomPosition()
        pygame.draw.rect(screen, self.red, (self.applePosition['x'], self.applePosition['y'], 20, 20))

        while self.running:
            screen.fill((0, 0, 0, 255)) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        self.move['x'] = -20
                        self.move['y'] = 0
                    if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        self.move['x'] = 20
                        self.move['y'] = 0
                    if pygame.key.get_pressed()[pygame.K_UP]:
                        self.move['x'] = 0
                        self.move['y'] = -20
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        self.move['x'] = 0
                        self.move['y'] = 20

            pygame.draw.rect(screen, self.red, (self.applePosition['x'], self.applePosition['y'], 20, 20))
            pygame.draw.rect(screen, self.white, (position.get('x'), position.get('y'), 20, 20))
        
            if self.length > 0:                    
                for i in range(0, self.length):                
                    pygame.draw.rect(screen, self.white, (self.body[i]['x'], self.body[i]['y'], 20, 20))                    
            
            
            if loop % 10 == 0:
                
                if self.length > 0: 
                    for i in range(0, self.length):
                        if i + 1 < self.length:
                            self.body[i] = self.body[i + 1]
                        else:
                            self.body[i] = position
                        
                position['x'] += self.move['x']
                position['y'] += self.move['y']
                self.checkColision(position)

                if self.eateApple(position):
                    self.randomPosition() 
                
            loop += 1
            pygame.display.flip()
        else:
            pygame.display.quit()

g = Game(pygame)
g.init()