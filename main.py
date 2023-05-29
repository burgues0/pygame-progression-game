import pygame, sys
from settings import *

#main game running logic
class Game:
    def __init__(self):
        #basic pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                #checking if the game is being closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()