import pygame
import random

pygame.display.init()

class Piece:
    p0 = [
        [1],
        [1],
        [1],
        [1],
    ]

    p1 = [
        [2, 2],
        [2, 2],
    ]

    p2 = [
        [0, 3, 0],
        [3, 3, 3],
    ]

    p3 = [
        [4, 0],
        [4, 0],
        [4, 4],
    ]

    p4 = [
        [0, 5],
        [0, 5],
        [5, 5],
    ]

    p5 = [
        [6, 6, 0],
        [0, 6, 6],
    ]

    p6 = [
        [0, 7, 7],
        [7, 7, 0],
    ]

    pieces = [p0, p1, p2, p3, p4, p5, p6]

    def __init__(self):
        pass

    def getPiece(self):
        return self.pieces[random.randint(0, 6)]

# todo rotation

class Game:
    running = True
    position = [0, 3]
    score = 0
    white = (255, 255, 255, 255)
    yellow = (255, 255, 0, 255)
    red = (255, 0, 0, 255)
    blue = (0, 0, 255, 255)
    green = (0, 255, 0, 255)
    purple = (255, 0, 255, 255)
    cyan = (0, 255, 255, 255)
    p = Piece()

    field = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def __init__(self, pygame):
        self.pygame = pygame


    def init(self):
        screen = self.pygame.display.set_mode((200, 480))
        self.start(self.pygame, screen)


    def drawRect(self, screen, x, y, color):
        if color == 1:
            color = self.white
        elif color == 2:
            color = self.yellow
        elif color == 3:
            color = self.red
        elif color == 4:
            color = self.blue
        elif color == 5:
            color = self.green
        elif color == 6:
            color = self.purple
        else:
            color = self.cyan

        self.pygame.draw.rect(screen, color, (x, y, 20, 20))


    def rotate(self, piece): # todo
        row = len(piece)
        col = len(piece[0])
        rotatedPiece = [[]]

        for r in reversed(piece):
            for val in reversed(piece[r]):
                pass # list.append(elem)
        
        return rotatedPiece

    def newPiece(self):
        self.position = [0, 3]
        return self.p.getPiece()


    def clearRow(self):
        for row in range(0, 24):
            all = True
            for val in range(0, 10):
                if self.field[row][val] > 0:
                    pass
                else:
                    all = False
            if all:
                self.score += 10
                for i in range(0, 10):
                    self.field[row][i] = 0
                for j in range(row, -1):
                    if j > 0:
                        self.field[j] = self.field[j - 1]
                    


    def checkColision(self, piece, direction):
        if direction == 0:
            if self.position[0] + len(piece) == 25:
                return True
            else:
                j = 0
                for row in range(0, len(piece)):
                    for cell in range(0, len(piece[0])):
                        if row < len(piece) - 1:                            
                            if piece[row][cell] > 0 and piece[row + 1][cell] > 0:
                                pass
                            elif piece[row][cell] > 0 and self.field[self.position[0] + row][self.position[1] + cell] > 0:
                                return True
                        else:
                            if piece[row][cell] > 0 and self.field[self.position[0] + row][self.position[1] + cell] > 0:
                                return True
                        j += 1
                    j = 0
            return False
        elif direction == 1 and self.position[1] == 0: # todo
            return True
        elif direction == 2 and self.position[1] + len(piece[0]) == 10: # todo
            return True
        else:
            return False

    def clearActivePiece(self, piece):
        i = 0
        j = 0
        for row in range(self.position[0] - 1, self.position[0] + len(piece) - 1):
            for cell in range(self.position[1], self.position[1] + len(piece[0])):
                if piece[i][j] > 0:
                    self.field[row][cell] = 0
                j += 1
            j = 0
            i += 1


    def pieceMove(self, piece, direction):
        print(len(piece))

        if self.checkColision(piece, direction):
            return

        self.clearActivePiece(piece)
        
        if direction == 1: # left
            self.position[1] -= 1
        elif direction == 2: # right
            self.position[1] += 1

        for pieceR in range(len(piece)):
            for pieceC in range(len(piece[pieceR])):
                if piece[pieceR][pieceC] > 0:
                    if direction == 0: # down
                        self.field[self.position[0] + pieceR][self.position[1] + pieceC] = piece[pieceR][pieceC]
                    elif direction == 1: # left
                        self.field[self.position[0] - 1 + pieceR][self.position[1] + pieceC] = piece[pieceR][pieceC]
                    else: # right
                        self.field[self.position[0] - 1 + pieceR][self.position[1] + pieceC] = piece[pieceR][pieceC]


    def start(self, pygame, screen): 
        time = 0
        piece = self.p.getPiece()
        
        # game cycle
        while self.running:
            screen.fill((0, 0, 0, 255))    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        self.pieceMove(piece, 1)
                    if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        self.pieceMove(piece, 2)
                    if pygame.key.get_pressed()[pygame.K_UP]:
                        piece = self.rotate(piece)
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        self.pieceMove(piece, 0)
                        self.position[0] += 1 
            
            
            if self.checkColision(piece, 0):
                self.clearRow()
                piece = self.newPiece()

            if time % 20 == 0: 
                self.pieceMove(piece, 0)
                self.position[0] += 1 
            
            for row in range(len(self.field)):
                for cell in range(len(self.field[row])):
                    
                    if self.field[row][cell] > 0:
                        y = row * 20
                        x = cell * 20                        
                        self.drawRect(screen, x, y, self.field[row][cell])
            
            time += 1
            pygame.display.flip()
        else:
            pygame.display.quit()

g = Game(pygame)
g.init()