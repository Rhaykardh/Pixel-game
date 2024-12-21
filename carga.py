from bala import *
class CARGA(BALA):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.velocidade= 5
        self.imagem_entrada= pygame.image.load('sprite/carga.png')
        self.image= pygame.transform.scale(self.imagem_entrada, (100, 100))
        self.rect= self.image.get_rect()
        self.rect.topleft= (x,y)
    def mover(self):
        self.rect.x -= self.velocidade
        if self.rect.left > 800 or self.rect.right < 0:
            self.kill()
    def desenhar(self, tela):
        tela.blit(self.image, self.rect.topleft)
    
    