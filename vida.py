from bala import *
from carga import *
class VIDA(CARGA):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.velocidade= 5
        self.imagem_entrada= pygame.image.load('sprite/vida.png')
        self.image= pygame.transform.scale(self.imagem_entrada, (25, 25))
        self.rect= self.image.get_rect()
        self.rect.topleft= (x,y)
    def desenhar(self, tela):
        tela.blit(self.image, self.rect.topleft)
    def mover(self):
        self.rect.x -= self.velocidade
        if self.rect.left > 800 or self.rect.right < 0:
            self.kill()