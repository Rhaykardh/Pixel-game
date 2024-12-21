from config import *
class AMBIENTE(pygame.sprite.Sprite):
    def __init__(self, name = 'sprite/ambiente.png'):
        super(). __init__()
        self.imagem_entrada= pygame.image.load(name)
        self.image= pygame.transform.scale(self.imagem_entrada, (800, 600))
        self.rect= self.image.get_rect()
        self.fundox= 0
        self.velocidade= 7
    def desenhar(self, tela):
        tela.blit(self.image,(self.fundox, 0))
        tela.blit(self.image,(self.fundox + self.rect.width, 0))
    def mover(self):
        self.fundox -= self.velocidade
        if self.fundox <= -self.rect.width: 
            self.fundox = 1
    
