from config import *
from inimigo import *
from desenhar import *
from musica import *
from bala import*
class BOSS(DESENHAR):
    def __init__(self, pontos, vida, x, y, name= 'sprite/boss.png', tamanhox= 200, tamanhoy= 200):
        super().__init__(x,y, name, tamanhox, tamanhoy)
        self.pontos= pontos
        self.vida= vida
        self.balas= pygame.sprite.Group()
        self.velocidade= 5
        self.direcao = random.choice([-1, 1])
        self.mudar_direcao= pygame.time.get_ticks()
        self.risada= pygame.time.get_ticks()
    def mover(self):
        self.rect.y += self.velocidade*self.direcao
        if self.rect.top < 0: 
            self.direcao = 1
            self.rect.top = 0
        elif self.rect.bottom > 600: 
            self.direcao = -1
            self.rect.bottom = 600

            
      

        if pygame.time.get_ticks()> self.mudar_direcao:
            self.direcao = random.choice([-1, 1])
            self.mudar_direcao= pygame.time.get_ticks() + random.randint(1000, 3000)
        if random.randint(1,100) <=2:
            self.disparo()

            

            
    
    def disparo(self):
        bala= BALA(self.rect.left, self.rect.centery, -1, 'sprite/evilblast.png', 90, 90)
        self.balas.add(bala)
        if pygame.time.get_ticks()> self.risada:
            self.risada= pygame.time.get_ticks() + random.randint(1000, 7000)
            tocar_som('risada.mp3')
    
       

    