from config import *
class BLAST(pygame.sprite.Sprite):
    def __init__(self, x, y, name= 'sprite/especial.png' ):
        super().__init__()
        self.x= x
        self.y= y
        self.imagem_entrada= pygame.image.load(name)
        self.image= pygame.transform.scale(self.imagem_entrada, (150, 150))
        self.rect= self.image.get_rect()
        self.rect.topleft= (x,y)
        self.velocidade= 7
    def mover(self):
        self.rect.x += self.velocidade
        if self.rect.left > 800 or self.rect.right < 0:
            self.kill()
    def desenhar(self, tela):
        tela.blit(self.image, self.rect.topleft)