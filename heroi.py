from config import *
from bala import *
from blast import *
class HEROI (pygame.sprite.Sprite):
    def __init__(self, x, y, name='sprite/heroi.png'):
        super().__init__()
        self.balas= pygame.sprite.Group()
        self.blasts= pygame.sprite.Group()
        self.x= x
        self.y= y
        self.imagem_entrada= pygame.image.load(name)
        self.image= pygame.transform.scale(self.imagem_entrada, (150, 150))
        self.rect= self.image.get_rect()
        self.rect.topleft= (x,y)
        self.carga= 100
        self.velocidade= 10
    def desenhar(self, tela):
        tela.blit(self.image, self.rect.topleft)
    def mover(self, botao):
        if botao[pygame.K_w] or botao[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidade 
        if botao[pygame.K_d] or botao[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.velocidade
        if botao[pygame.K_s] or botao[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.velocidade
        if botao[pygame.K_a] or botao[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
    def disparo(self): 
        bala= BALA(self.rect.right, self.rect.centery)
        self.balas.add(bala)
    def blast(self):
        if self.carga >= 100:
            blast= BLAST(self.rect.right, self.rect.top)
            self.blasts.add(blast)
            self.carga-=100
            return True
        return False
    
    
    
          
           

