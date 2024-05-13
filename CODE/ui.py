import pygame

class UI:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("UI")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.font.render("Hello, World!", True, (255, 255, 255)), (100, 100))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        
if __name__ == "__main__":
    ui = UI()
    ui.run()