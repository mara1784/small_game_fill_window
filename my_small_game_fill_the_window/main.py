from queue import Queue
import pygame,time,threading
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1400, 600))
        pygame.display.set_caption("Paint your window")
        self.running = True
        self.left, self.right, self.down, self.up = False,False,False,False
        self.y, self.x = 0, 0
        clock = pygame.time.Clock()
        clock.tick(60)
        start = time.time()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.up = True
                    if event.key == pygame.K_RIGHT:
                        self.right = True
                    if event.key == pygame.K_DOWN:
                        self.down = True
                    if event.key == pygame.K_LEFT:
                        self.left = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.up = False
                    if event.key == pygame.K_RIGHT:
                        self.right = False
                    if event.key == pygame.K_DOWN:
                        self.down = False
                    if event.key == pygame.K_LEFT:
                        self.left = False
                    pygame.display.flip()
            if any ([self.left, self.right, self.down, self.up]):
                from adjunct_main import nevim_jak_to_nazvat
                list = nevim_jak_to_nazvat(self.y, self.x,self.up,self.down,self.right,self.left).navrat()
                self.y = list[0]
                self.x = list[1]
                self.square = pygame.Rect(self.x, self.y,200, 200)
                self.square_bool = True
            now = time.time()
            cas1 = (f"Uplynulo: {now - start:.4f} s")
            cas = pygame.font.SysFont('amiriquranregular',26,bold=False, italic=True)
            cas = cas.render(str(cas1), True, (0, 255, 0))
            self.screen.blit(cas,(10,10))
            if hasattr(self, "square_bool"):
                pygame.draw.rect(self.screen, (0, 0, 254), self.square)
            pygame.display.flip()
            square02 = pygame.Rect(0, 10,235,75)
            pygame.draw.rect(self.screen, (0, 0, 0), square02)
            self.q = Queue(maxsize=1)
            width, height =self.screen.get_size()
            snap = pygame.transform.smoothscale(self.screen, (width, height))
            b = pygame.image.tostring(snap, 'RGB')
            self.q.put_nowait((b, width, height))
            t = threading.Thread(target=self.vlakenko(), args=(self.q,), daemon=True)
            t.start()
            if hasattr(self, "boolovka"):
                self.screen.blit(cas, (10, 10))
                pygame.display.flip()
                for i in range(6):
                    i = 5 - i
                    time.sleep(1)
                    x,y = 660,320
                    vypis1 = pygame.font.SysFont('amiriquranregular', 26, bold=False, italic=True)
                    vypis1 = vypis1.render(str("You painted the window."), True, (50, 50, 150))
                    self.screen.blit(vypis1, (660, 300))
                    vypis = pygame.font.SysFont('amiriquranregular', 26, bold=False, italic=True)
                    vypis = vypis.render(str(f"window will close above: {i}"), True, (50, 50, 150))
                    self.screen.blit(vypis, (x,y))
                    pygame.display.flip()
                    pygame.draw.rect(self.screen, (0, 0, 254), (x,y,400,200))
                    print(i)
                self.running = False
    def vlakenko(self):
            import numpy as np
            target = np.array([0, 0, 254],dtype=np.uint8)
            b, w, h = self.q.get()
            arr = np.frombuffer(b, dtype=np.uint8)
            arr = arr.reshape((h, w, 3))
            mask = np.all(arr == target, axis=2)
            matched = mask.sum()
            total = mask.size
            percent = matched / total * 100.0
            if np.any(mask):
                print(f"toto je {percent}")
            hledana = 97.9017857142857
            if hledana <= percent:
                self.boolovka = True

Game()
