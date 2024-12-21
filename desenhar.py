from config import *
class DESENHAR(pygame.sprite.Sprite):
    def __init__(self, x, y, name= 'sprite/titulo.png', tamanhox= 350, tamanhoy= 350):
        super().__init__()
        self.x= x
        self.y= y
        self.imagem_entrada= pygame.image.load(name)
        self.image= pygame.transform.scale(self.imagem_entrada, (tamanhox, tamanhoy))
        self.rect= self.image.get_rect()
        self.rect.topleft= (x,y)
    def desenhar(self, tela):
        tela.blit(self.image, self.rect.topleft)